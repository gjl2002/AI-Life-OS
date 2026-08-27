#!/usr/bin/env python3
"""Validate generated AI Life System config and cross-file references."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any, Optional


SCHEMA_VERSION = "0.4"
REQUIRED_JSON = (
    "profile.json",
    "discovery.json",
    "notion-index.json",
    "notion-schema.json",
    "semantic-map.json",
    "routing-rules.json",
    "dimension-pages.json",
)


def load_json(path: Path) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise ValueError(f"缺少文件：{path.name}") from exc
    except json.JSONDecodeError as exc:
        raise ValueError(f"JSON 无效：{path.name}: {exc}") from exc
    if not isinstance(value, dict):
        raise ValueError(f"{path.name} 顶层必须是对象")
    if value.get("schema_version") != SCHEMA_VERSION:
        raise ValueError(f"{path.name} schema_version 必须为 {SCHEMA_VERSION}")
    return value


def validate(config_dir: Path) -> list[str]:
    errors: list[str] = []
    loaded: dict[str, dict[str, Any]] = {}
    for name in REQUIRED_JSON:
        try:
            loaded[name] = load_json(config_dir / name)
        except ValueError as exc:
            errors.append(str(exc))
    report = config_dir / "initialization-report.md"
    if not report.is_file() or not report.read_text(encoding="utf-8").strip():
        errors.append("缺少或空文件：initialization-report.md")
    if errors:
        return errors

    index = loaded["notion-index.json"]
    sources = index.get("sources")
    if not isinstance(sources, list):
        errors.append("notion-index.json sources 必须是数组")
        return errors

    source_ids = []
    database_ids = set()
    for source in sources:
        if not isinstance(source, dict):
            errors.append("notion-index.json 包含非对象 source")
            continue
        source_id = source.get("data_source_id")
        if not source_id:
            errors.append("Schema source 缺少 data_source_id")
        else:
            source_ids.append(str(source_id))
        if source.get("database_id"):
            database_ids.add(str(source["database_id"]))
        fingerprint = str(source.get("schema_fingerprint") or "")
        if not re.fullmatch(r"[0-9a-f]{64}", fingerprint):
            errors.append(f"Schema 指纹无效：{source_id or 'unknown'}")
        properties = source.get("properties")
        if not isinstance(properties, list):
            errors.append(f"properties 必须是数组：{source_id or 'unknown'}")
        access = source.get("access")
        if not isinstance(access, dict):
            errors.append(f"source 缺少 access：{source_id or 'unknown'}")
        elif access.get("create_page_ready") and not access.get("title_field"):
            errors.append(f"create_page_ready=true 但缺少 title_field：{source_id or 'unknown'}")

    if len(source_ids) != len(set(source_ids)):
        errors.append("notion-index.json 存在重复 data_source_id")

    valid_source_ids = set(source_ids)
    pages = loaded["dimension-pages.json"].get("pages")
    valid_page_ids: set[str] = set()
    if not isinstance(pages, list):
        errors.append("dimension-pages.json pages 必须是数组")
        pages = []
    for page in pages:
        if not isinstance(page, dict):
            errors.append("dimension-pages.json 包含非对象 page")
            continue
        page_id = str(page.get("page_id") or "")
        if not page_id:
            errors.append("普通页面缺少 page_id")
            continue
        if page_id in valid_page_ids:
            errors.append(f"dimension-pages.json 存在重复 page_id：{page_id}")
        valid_page_ids.add(page_id)
        if not page.get("key") or not page.get("title"):
            errors.append(f"普通页面缺少 key 或 title：{page_id}")
        if not isinstance(page.get("readable"), bool):
            errors.append(f"普通页面 readable 必须是布尔值：{page_id}")
        depth = page.get("depth")
        if not isinstance(depth, int) or depth < 0 or depth > 2:
            errors.append(f"普通页面 depth 必须是 0 到 2 的整数：{page_id}")

    lookup = index.get("lookup")
    if not isinstance(lookup, dict):
        errors.append("notion-index.json lookup 必须是对象")
    elif not isinstance(lookup.get("page_titles"), dict):
        errors.append("notion-index.json lookup.page_titles 必须是对象")

    semantic_map = loaded["semantic-map.json"].get("concepts")
    if not isinstance(semantic_map, dict):
        errors.append("semantic-map.json concepts 必须是对象")
    else:
        for key, rule in semantic_map.items():
            if not isinstance(rule, dict):
                errors.append(f"语义规则不是对象：{key}")
                continue
            targets = rule.get("targets")
            if not isinstance(targets, list) or not targets:
                errors.append(f"语义规则没有目标：{key}")
                continue
            expected_status = "ready" if len(targets) == 1 else "multiple"
            if rule.get("status") != expected_status:
                errors.append(f"语义规则状态与目标数量不一致：{key}")
            for target in targets:
                if target.get("kind") == "page":
                    page_id = str(target.get("page_id") or "")
                    if page_id not in valid_page_ids:
                        errors.append(f"语义 {key} 引用了不存在的 page_id：{page_id}")
                    continue
                source_id = str(target.get("data_source_id") or "")
                if source_id not in valid_source_ids:
                    errors.append(f"语义 {key} 引用了不存在的 data_source_id：{source_id}")

    compatibility = loaded["routing-rules.json"].get("capabilities")
    if compatibility != semantic_map:
        errors.append("routing-rules.json 与 semantic-map.json 不一致")

    profile = loaded["profile.json"]
    if not isinstance(profile.get("hub"), dict) or not profile["hub"].get("page_id"):
        errors.append("profile.json 缺少 Hub page_id")
    health = profile.get("health") if isinstance(profile.get("health"), dict) else {}
    if health.get("status") not in {"ready", "needs_attention", "blocked"}:
        errors.append("profile.json health.status 无效")
    for key in ("source_index_file", "schema_compat_file", "discovery_file", "semantic_map_file", "routing_rules_file", "dimension_pages_file"):
        value = profile.get(key)
        if not value or not (config_dir / str(value)).is_file():
            errors.append(f"profile.json 引用文件不存在：{key}")

    discovery = loaded["discovery.json"]
    if not isinstance(discovery.get("candidates"), list):
        errors.append("discovery.json candidates 必须是数组")
    return errors


def parse_args(argv: Optional[list[str]] = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config-dir", required=True, type=Path)
    return parser.parse_args(argv)


def main(argv: Optional[list[str]] = None) -> int:
    args = parse_args(argv)
    errors = validate(args.config_dir.expanduser().resolve())
    if errors:
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 2
    print(json.dumps({"valid": True, "config_dir": str(args.config_dir.expanduser().resolve())}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
