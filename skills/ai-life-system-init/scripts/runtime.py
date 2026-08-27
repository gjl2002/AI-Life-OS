#!/usr/bin/env python3
"""Resolve AI Life System targets and preflight Notion writes from the local index."""

from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path
from typing import Any, Optional

from build_config import canonical_notion_id, normalize_text


RUNTIME_VERSION = "1.2.0"


class RuntimeConfigError(ValueError):
    """Raised when the local runtime config is absent or inconsistent."""


def default_config_dir() -> Path:
    configured = os.environ.get("AI_LIFE_SYSTEM_DATA_DIR")
    return Path(configured).expanduser() if configured else Path.home() / ".ai-life-system"


def load_json(path: Path) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise RuntimeConfigError(f"缺少本地配置文件：{path}") from exc
    except json.JSONDecodeError as exc:
        raise RuntimeConfigError(f"本地配置 JSON 无效：{path.name}: {exc}") from exc
    if not isinstance(value, dict):
        raise RuntimeConfigError(f"本地配置顶层必须是对象：{path.name}")
    return value


def referenced_file(config_dir: Path, profile: dict[str, Any], key: str, fallback: str) -> Path:
    raw_name = str(profile.get(key) or fallback)
    if Path(raw_name).name != raw_name:
        raise RuntimeConfigError(f"profile.json 中的 {key} 不是安全文件名")
    return config_dir / raw_name


def load_runtime(config_dir: Path) -> dict[str, Any]:
    root = config_dir.expanduser().resolve()
    profile = load_json(root / "profile.json")
    index = load_json(referenced_file(root, profile, "source_index_file", "notion-index.json"))
    semantic = load_json(referenced_file(root, profile, "semantic_map_file", "semantic-map.json"))
    pages = load_json(referenced_file(root, profile, "dimension_pages_file", "dimension-pages.json"))

    versions = {str(item.get("schema_version") or "") for item in (profile, index, semantic, pages)}
    if len(versions) != 1 or "" in versions:
        raise RuntimeConfigError("profile、事实索引与语义映射的 schema_version 不一致")
    if not isinstance(index.get("sources"), list) or not isinstance(index.get("lookup"), dict):
        raise RuntimeConfigError("notion-index.json 缺少 sources 或 lookup")
    if not isinstance(semantic.get("concepts"), dict):
        raise RuntimeConfigError("semantic-map.json 缺少 concepts")
    if not isinstance(pages.get("pages"), list):
        raise RuntimeConfigError("dimension-pages.json 缺少 pages")
    return {"config_dir": root, "profile": profile, "index": index, "semantic": semantic, "pages": pages}


def runtime_status(bundle: dict[str, Any]) -> dict[str, Any]:
    profile = bundle["profile"]
    index = bundle["index"]
    semantic = bundle["semantic"]
    health = profile.get("health") if isinstance(profile.get("health"), dict) else {}
    health_status = str(health.get("status") or "unknown")
    return {
        "runtime_version": RUNTIME_VERSION,
        "runtime_status": "ready" if health_status == "ready" else "needs_attention",
        "config_valid": True,
        "config_dir": str(bundle["config_dir"]),
        "schema_version": profile.get("schema_version"),
        "health": health,
        "workspace": profile.get("workspace", {}),
        "hub": profile.get("hub", {}),
        "initialized_at": profile.get("initialized_at", ""),
        "index_generated_at": index.get("generated_at", ""),
        "source_count": len(index["sources"]),
        "page_count": len(bundle["pages"]["pages"]),
        "semantic_count": len(semantic["concepts"]),
    }


def unique_targets(targets: list[Any]) -> list[Any]:
    result: list[Any] = []
    seen: set[str] = set()
    for target in targets:
        marker = json.dumps(target, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
        if marker not in seen:
            seen.add(marker)
            result.append(target)
    return result


def resolution(kind: str, value: str, targets: list[Any]) -> dict[str, Any]:
    unique = unique_targets(targets)
    status = "not_found" if not unique else "ready" if len(unique) == 1 else "multiple"
    return {
        "query": {"kind": kind, "value": value, "normalized": normalize_text(value)},
        "status": status,
        "target_count": len(unique),
        "targets": unique,
        "primary_target": unique[0] if len(unique) == 1 else None,
    }


def runtime_page_reference(page: dict[str, Any]) -> dict[str, Any]:
    return {
        "kind": "page",
        "key": page.get("key"),
        "title": page.get("title"),
        "page_id": page.get("page_id"),
        "url": page.get("url", ""),
        "last_edited_time": page.get("last_edited_time", ""),
        "parent_page_id": page.get("parent_page_id", ""),
        "parent_key": page.get("parent_key", ""),
        "depth": page.get("depth", 1),
        "read_ready": bool(page.get("readable", False)),
    }


def resolve(bundle: dict[str, Any], kind: str, value: str) -> dict[str, Any]:
    if kind == "concept":
        rule = bundle["semantic"]["concepts"].get(value)
        if not isinstance(rule, dict):
            return resolution(kind, value, [])
        result = resolution(kind, value, rule.get("targets") if isinstance(rule.get("targets"), list) else [])
        result["concept"] = {key: rule.get(key) for key in ("label", "kind", "status")}
        return result

    lookup = bundle["index"]["lookup"]
    key = normalize_text(value)
    if kind == "source":
        source_targets = lookup.get("source_titles", {}).get(key, [])
        database_targets = lookup.get("database_titles", {}).get(key, [])
        return resolution(kind, value, list(source_targets) + list(database_targets))
    if kind == "page":
        page_targets = [
            runtime_page_reference(page)
            for page in bundle["pages"]["pages"]
            if normalize_text(page.get("title")) == key
        ]
        return resolution(kind, value, page_targets)
    lookup_name = "property_names" if kind == "property" else "option_names"
    return resolution(kind, value, list(lookup.get(lookup_name, {}).get(key, [])))


def find_source(index: dict[str, Any], data_source_id: str) -> Optional[dict[str, Any]]:
    wanted = canonical_notion_id(data_source_id)
    for source in index["sources"]:
        if canonical_notion_id(source.get("data_source_id")) == wanted:
            return source
    return None


def find_page(pages: dict[str, Any], page_id: str) -> Optional[dict[str, Any]]:
    wanted = canonical_notion_id(page_id)
    for page in pages["pages"]:
        if canonical_notion_id(page.get("page_id")) == wanted:
            return page
    return None


def matching_properties(source: dict[str, Any], field_name: str) -> list[dict[str, Any]]:
    wanted = normalize_text(field_name)
    return [prop for prop in source.get("properties", []) if normalize_text(prop.get("name")) == wanted]


def issue(code: str, message: str, **details: Any) -> dict[str, Any]:
    return {"code": code, "message": message, **details}


def parse_option_specs(values: list[str]) -> tuple[list[tuple[str, str]], list[dict[str, Any]]]:
    parsed: list[tuple[str, str]] = []
    errors: list[dict[str, Any]] = []
    for raw in values:
        if "=" not in raw:
            errors.append(issue("invalid_option_syntax", "选项必须使用 字段=值 格式", value=raw))
            continue
        field, value = (part.strip() for part in raw.split("=", 1))
        if not field or not value:
            errors.append(issue("invalid_option_syntax", "选项字段和值都不能为空", value=raw))
            continue
        parsed.append((field, value))
    return parsed, errors


def check_write(
    bundle: dict[str, Any],
    data_source_id: str,
    fields: list[str],
    option_specs: list[str],
    operation: str = "create",
) -> dict[str, Any]:
    index = bundle["index"]
    profile = bundle["profile"]
    errors: list[dict[str, Any]] = []
    warnings: list[dict[str, Any]] = []
    source = find_source(index, data_source_id)
    base: dict[str, Any] = {
        "operation": operation,
        "data_source_id": canonical_notion_id(data_source_id),
        "requires_user_authorization": True,
        "requires_live_schema_check": True,
        "index_generated_at": index.get("generated_at", ""),
        "errors": errors,
        "warnings": warnings,
    }
    if source is None:
        errors.append(issue("data_source_not_found", "事实索引中没有这个 Data Source"))
        return {**base, "write_ready": False, "target": None}

    base["target"] = {
        "database_id": source.get("database_id"),
        "data_source_id": source.get("data_source_id"),
        "title": source.get("title"),
        "schema_fingerprint": source.get("schema_fingerprint"),
    }
    health = profile.get("health") if isinstance(profile.get("health"), dict) else {}
    if health.get("status") == "blocked":
        errors.append(issue("runtime_blocked", "本地配置健康状态为 blocked，请先重新绑定"))

    access = source.get("access") if isinstance(source.get("access"), dict) else {}
    if not access.get("read_ready"):
        errors.append(issue("source_unreadable", "目标 Data Source 当前不可读取"))
    if operation == "create" and not access.get("create_page_ready"):
        errors.append(issue("create_not_ready", "目标 Data Source 不满足创建页面条件", reasons=access.get("blocked_reasons", [])))

    normalized_fields = {normalize_text(name) for name in fields}
    if operation == "create" and access.get("title_field") and normalize_text(access["title_field"]) not in normalized_fields:
        errors.append(issue("title_field_required", "创建页面必须显式包含真实 title 字段", field=access["title_field"]))

    readonly = {normalize_text(item.get("name")) for item in source.get("readonly_fields", [])}
    relations = {normalize_text(item.get("field")): item for item in source.get("relations", [])}
    resolved_fields: dict[str, dict[str, Any]] = {}
    for field in fields:
        matches = matching_properties(source, field)
        if not matches:
            errors.append(issue("field_not_found", "字段不存在于目标 Data Source", field=field))
            continue
        if len(matches) > 1:
            errors.append(issue("field_ambiguous", "规范化后存在多个同名字段", field=field))
            continue
        prop = matches[0]
        key = normalize_text(prop["name"])
        resolved_fields[key] = prop
        if key in readonly:
            errors.append(issue("field_readonly", "字段不可自动写入", field=prop["name"], field_type=prop.get("type")))
        relation = relations.get(key)
        if relation and not relation.get("resolved"):
            errors.append(issue("relation_unresolved", "relation 目标未解析，禁止自动写入", field=prop["name"]))

    parsed_options, option_errors = parse_option_specs(option_specs)
    errors.extend(option_errors)
    for field, value in parsed_options:
        key = normalize_text(field)
        if key not in normalized_fields:
            errors.append(issue("option_field_not_declared", "选项字段必须同时通过 --field 声明", field=field, value=value))
            continue
        prop = resolved_fields.get(key)
        if prop is None:
            continue
        options = prop.get("options") if isinstance(prop.get("options"), list) else []
        if not options:
            errors.append(issue("field_has_no_options", "字段不是带选项的字段", field=prop["name"], value=value))
        elif normalize_text(value) not in {normalize_text(option) for option in options}:
            errors.append(issue("option_not_found", "选项不属于目标字段", field=prop["name"], value=value, allowed_options=options))

    base["write_ready"] = not errors
    return base


def check_page_write(bundle: dict[str, Any], page_id: str) -> dict[str, Any]:
    profile = bundle["profile"]
    page = find_page(bundle["pages"], page_id)
    errors: list[dict[str, Any]] = []
    warnings: list[dict[str, Any]] = []
    base: dict[str, Any] = {
        "operation": "update_page_body",
        "page_id": canonical_notion_id(page_id),
        "requires_user_authorization": True,
        "requires_live_page_check": True,
        "errors": errors,
        "warnings": warnings,
    }
    if page is None:
        errors.append(issue("page_not_found", "普通页面索引中没有这个页面"))
        return {**base, "page_write_ready": False, "target": None}

    base["target"] = {
        "kind": "page",
        "key": page.get("key"),
        "title": page.get("title"),
        "page_id": page.get("page_id"),
        "url": page.get("url"),
        "last_edited_time": page.get("last_edited_time"),
        "parent_page_id": page.get("parent_page_id"),
        "parent_key": page.get("parent_key"),
    }
    health = profile.get("health") if isinstance(profile.get("health"), dict) else {}
    if health.get("status") == "blocked":
        errors.append(issue("runtime_blocked", "本地配置健康状态为 blocked，请先重新绑定"))
    if not page.get("readable"):
        errors.append(issue("page_unreadable", "目标普通页面当前不可读取"))
    if not page.get("last_edited_time"):
        warnings.append(issue("page_edit_time_missing", "索引没有页面最后编辑时间，写入前必须重新读取并核对页面身份"))

    base["page_write_ready"] = not errors
    return base


def print_json(value: dict[str, Any]) -> None:
    print(json.dumps(value, ensure_ascii=False, indent=2))


def parse_args(argv: Optional[list[str]] = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config-dir", type=Path, default=default_config_dir())
    subparsers = parser.add_subparsers(dest="command", required=True)
    subparsers.add_parser("status", help="检查本地运行时状态")

    resolve_parser = subparsers.add_parser("resolve", help="解析语义、普通页面、数据源、字段或选项")
    resolve_group = resolve_parser.add_mutually_exclusive_group(required=True)
    resolve_group.add_argument("--concept")
    resolve_group.add_argument("--source")
    resolve_group.add_argument("--property")
    resolve_group.add_argument("--option")
    resolve_group.add_argument("--page")

    write_parser = subparsers.add_parser("check-write", help="对一次创建或更新动作做本地写入前校验")
    write_parser.add_argument("--data-source-id", required=True)
    write_parser.add_argument("--operation", choices=("create", "update"), default="create")
    write_parser.add_argument("--field", action="append", default=[])
    write_parser.add_argument("--option", action="append", default=[])

    page_write_parser = subparsers.add_parser("check-page-write", help="对一次普通页面正文更新做本地身份预检")
    page_write_parser.add_argument("--page-id", required=True)
    return parser.parse_args(argv)


def main(argv: Optional[list[str]] = None) -> int:
    args = parse_args(argv)
    try:
        bundle = load_runtime(args.config_dir)
        if args.command == "status":
            print_json(runtime_status(bundle))
            return 0
        if args.command == "resolve":
            kind = next(kind for kind in ("concept", "source", "property", "option", "page") if getattr(args, kind) is not None)
            result = resolve(bundle, kind, getattr(args, kind))
            print_json(result)
            return 3 if result["status"] == "not_found" else 0
        if args.command == "check-page-write":
            result = check_page_write(bundle, args.page_id)
            print_json(result)
            return 0 if result["page_write_ready"] else 4
        result = check_write(bundle, args.data_source_id, args.field, args.option, args.operation)
        print_json(result)
        return 0 if result["write_ready"] else 4
    except RuntimeConfigError as exc:
        print_json({
            "runtime_version": RUNTIME_VERSION,
            "runtime_status": "needs_init",
            "config_valid": False,
            "error": str(exc),
            "next_action": "运行 $ai-life-system-init 完成初始化或重新绑定",
        })
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
