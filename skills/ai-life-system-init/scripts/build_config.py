#!/usr/bin/env python3
"""Build deterministic AI Life System config from read-only Notion discovery metadata."""

from __future__ import annotations

import argparse
import copy
import datetime as dt
import hashlib
import json
import os
import re
import shutil
import sys
import tempfile
import unicodedata
from pathlib import Path
from typing import Any, Optional


SCHEMA_VERSION = "0.4"
ACCEPTED_DISCOVERY_VERSIONS = {"0.2", "0.3", SCHEMA_VERSION}
OUTPUT_FILES = (
    "profile.json",
    "discovery.json",
    "notion-index.json",
    "notion-schema.json",
    "semantic-map.json",
    "routing-rules.json",
    "dimension-pages.json",
    "initialization-report.md",
)
READ_ONLY_TYPES = {
    "formula",
    "rollup",
    "button",
    "unique_id",
    "created_time",
    "created_by",
    "last_edited_time",
    "last_edited_by",
}


class ConfigError(ValueError):
    """Raised when discovery or manifest input is invalid."""


def utc_now() -> str:
    return dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat()


def load_json(path: Path) -> dict[str, Any]:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise ConfigError(f"文件不存在：{path}") from exc
    except json.JSONDecodeError as exc:
        raise ConfigError(f"JSON 无效：{path}: {exc}") from exc
    if not isinstance(data, dict):
        raise ConfigError(f"JSON 顶层必须是对象：{path}")
    return data


def normalize_text(value: Any) -> str:
    text = unicodedata.normalize("NFKC", str(value or "")).lower()
    return re.sub(r"[\s|｜·・\-_/\\\[\]【】()（）:：]+", "", text)


def canonical_notion_id(value: Any) -> str:
    raw = str(value or "").strip()
    compact = raw.replace("-", "")
    if re.fullmatch(r"[0-9a-fA-F]{32}", compact):
        compact = compact.lower()
        return "-".join((compact[:8], compact[8:12], compact[12:16], compact[16:20], compact[20:]))
    return raw


def json_digest(value: Any) -> str:
    payload = json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def option_names(config: dict[str, Any], property_type: str) -> list[str]:
    direct = config.get("options")
    nested = config.get(property_type, {}).get("options") if isinstance(config.get(property_type), dict) else None
    values = direct if isinstance(direct, list) else nested if isinstance(nested, list) else []
    result = []
    for value in values:
        name = value.get("name") if isinstance(value, dict) else value
        if name not in (None, ""):
            result.append(str(name))
    return result


def normalize_property(name: str, config: Any) -> dict[str, Any]:
    source = config if isinstance(config, dict) else {}
    property_type = str(source.get("type") or "unknown")
    item: dict[str, Any] = {"name": str(name), "type": property_type}
    options = option_names(source, property_type)
    if options:
        item["options"] = options

    relation = source.get("relation") if isinstance(source.get("relation"), dict) else {}
    related_database_id = source.get("related_database_id") or relation.get("database_id")
    related_data_source_id = source.get("related_data_source_id") or relation.get("data_source_id")
    if related_database_id:
        item["related_database_id"] = canonical_notion_id(related_database_id)
    if related_data_source_id:
        item["related_data_source_id"] = canonical_notion_id(related_data_source_id)

    if property_type == "rollup":
        rollup = source.get("rollup") if isinstance(source.get("rollup"), dict) else {}
        function = source.get("function") or rollup.get("function")
        if function:
            item["function"] = str(function)
    return item


def normalize_properties(value: Any) -> list[dict[str, Any]]:
    properties: list[dict[str, Any]] = []
    if isinstance(value, dict):
        for name, config in value.items():
            properties.append(normalize_property(str(name), config))
    elif isinstance(value, list):
        for config in value:
            if not isinstance(config, dict):
                continue
            name = config.get("name")
            if name in (None, ""):
                continue
            properties.append(normalize_property(str(name), config))
    return sorted(properties, key=lambda item: normalize_text(item["name"]))


def normalize_data_source(source: dict[str, Any], candidate: dict[str, Any]) -> dict[str, Any]:
    source_id = canonical_notion_id(source.get("id") or source.get("data_source_id") or candidate["database_id"])
    return {
        "id": source_id,
        "title": str(source.get("title") or source.get("name") or candidate.get("title") or "未命名数据源"),
        "url": str(source.get("url") or candidate.get("url") or ""),
        "last_edited_time": str(source.get("last_edited_time") or candidate.get("last_edited_time") or ""),
        "retrieve_failed": bool(source.get("retrieve_failed", candidate.get("retrieve_failed", False))),
        "error": str(source.get("error") or candidate.get("error") or ""),
        "properties": normalize_properties(source.get("properties", candidate.get("properties", []))),
        "user_override": copy.deepcopy(source.get("user_override", {})) if isinstance(source.get("user_override"), dict) else {},
    }


def normalize_candidate(raw: dict[str, Any]) -> dict[str, Any]:
    database_id = canonical_notion_id(raw.get("database_id") or raw.get("id"))
    if not database_id:
        raise ConfigError("候选数据库缺少 database_id")
    candidate: dict[str, Any] = {
        "database_id": database_id,
        "title": str(raw.get("title") or "未命名数据库"),
        "url": str(raw.get("url") or ""),
        "archived": bool(raw.get("archived", False)),
        "last_edited_time": str(raw.get("last_edited_time") or ""),
        "source": str(raw.get("source") or "unknown"),
        "source_page_id": canonical_notion_id(raw.get("source_page_id")),
        "source_section": str(raw.get("source_section") or raw.get("module") or ""),
        "detection_reason": str(raw.get("detection_reason") or ""),
        "selected": bool(raw.get("selected", not bool(raw.get("archived", False)))),
        "retrieve_failed": bool(raw.get("retrieve_failed", False)),
        "error": str(raw.get("error") or ""),
        "user_override": copy.deepcopy(raw.get("user_override", {})) if isinstance(raw.get("user_override"), dict) else {},
    }
    raw_sources = raw.get("data_sources") if isinstance(raw.get("data_sources"), list) else []
    if raw_sources:
        candidate["data_sources"] = [normalize_data_source(item, candidate) for item in raw_sources if isinstance(item, dict)]
    else:
        candidate["data_sources"] = [normalize_data_source({}, {**candidate, "properties": raw.get("properties", [])})]
    return candidate


def merge_candidate(existing: dict[str, Any], incoming: dict[str, Any]) -> dict[str, Any]:
    merged = copy.deepcopy(existing)
    for key in ("title", "url", "last_edited_time", "source_page_id", "source_section", "error"):
        if (not merged.get(key) or merged.get(key) == "unknown") and incoming.get(key):
            merged[key] = incoming[key]
    merged["selected"] = bool(existing.get("selected") or incoming.get("selected"))
    merged["retrieve_failed"] = bool(existing.get("retrieve_failed") and incoming.get("retrieve_failed"))
    merged["archived"] = bool(existing.get("archived") and incoming.get("archived"))
    if incoming.get("user_override"):
        merged["user_override"] = incoming["user_override"]

    sources = []
    for value in (existing.get("source"), incoming.get("source")):
        if value and value not in sources:
            sources.append(value)
    merged["source"] = sources[0] if len(sources) == 1 else "+".join(sources)

    reasons = []
    for value in (existing.get("detection_reason"), incoming.get("detection_reason")):
        if value and value not in reasons:
            reasons.append(value)
    merged["detection_reason"] = "；".join(reasons)

    by_id = {source["id"]: source for source in existing.get("data_sources", [])}
    for source in incoming.get("data_sources", []):
        current = by_id.get(source["id"])
        if not current or (current.get("retrieve_failed") and not source.get("retrieve_failed")):
            by_id[source["id"]] = source
    merged["data_sources"] = sorted(by_id.values(), key=lambda item: (normalize_text(item["title"]), item["id"]))
    return merged


def normalize_dimension_page(raw: dict[str, Any]) -> dict[str, Any]:
    page_id = canonical_notion_id(raw.get("page_id") or raw.get("id"))
    if not page_id:
        raise ConfigError("非数据库页面缺少 page_id")
    depth_raw = raw.get("depth", 1)
    try:
        depth = int(depth_raw)
    except (TypeError, ValueError) as exc:
        raise ConfigError(f"非数据库页面 depth 无效：{depth_raw}") from exc
    if depth < 0 or depth > 2:
        raise ConfigError(f"非数据库页面 depth 必须在 0 到 2 之间：{depth}")
    title = str(raw.get("title") or "未命名页面")
    return {
        "key": str(raw.get("key") or normalize_text(title) or "page"),
        "title": title,
        "page_id": page_id,
        "url": str(raw.get("url") or ""),
        "last_edited_time": str(raw.get("last_edited_time") or ""),
        "source": str(raw.get("source") or "hub_direct"),
        "parent_page_id": canonical_notion_id(raw.get("parent_page_id")),
        "parent_key": str(raw.get("parent_key") or ""),
        "depth": depth,
        "detection_reason": str(raw.get("detection_reason") or ""),
        "readable": bool(raw.get("readable", True)),
        "user_override": copy.deepcopy(raw.get("user_override", {})) if isinstance(raw.get("user_override"), dict) else {},
    }


def merge_dimension_page(existing: dict[str, Any], incoming: dict[str, Any]) -> dict[str, Any]:
    merged = copy.deepcopy(existing)
    existing_depth = int(existing.get("depth", 2))
    incoming_depth = int(incoming.get("depth", 2))
    if incoming_depth < existing_depth:
        for key in ("key", "parent_page_id", "parent_key", "detection_reason"):
            if incoming.get(key):
                merged[key] = incoming[key]
    for key in ("title", "url", "last_edited_time", "parent_page_id", "parent_key", "detection_reason"):
        if not merged.get(key) and incoming.get(key):
            merged[key] = incoming[key]
    merged["depth"] = min(existing_depth, incoming_depth)
    merged["readable"] = bool(existing.get("readable") or incoming.get("readable"))
    if incoming.get("user_override"):
        merged["user_override"] = incoming["user_override"]
    sources = []
    for value in (existing.get("source"), incoming.get("source")):
        if value and value not in sources:
            sources.append(value)
    merged["source"] = sources[0] if len(sources) == 1 else "+".join(sources)
    return merged


def normalize_discovery(raw: dict[str, Any]) -> dict[str, Any]:
    input_version = str(raw.get("schema_version") or "")
    if input_version and input_version not in ACCEPTED_DISCOVERY_VERSIONS:
        raise ConfigError(f"discovery schema_version 不受支持：{input_version}")
    hub = raw.get("hub")
    if not isinstance(hub, dict):
        raise ConfigError("discovery.hub 必须是对象")
    if "readable" not in hub:
        raise ConfigError("discovery.hub.readable 必须来自真实读取结果")
    if not hub.get("page_id"):
        raise ConfigError("discovery.hub.page_id 不能为空")

    raw_candidates = raw.get("candidates")
    if not isinstance(raw_candidates, list):
        raise ConfigError("discovery.candidates 必须是数组")
    by_id: dict[str, dict[str, Any]] = {}
    for item in raw_candidates:
        if not isinstance(item, dict):
            continue
        candidate = normalize_candidate(item)
        current = by_id.get(candidate["database_id"])
        by_id[candidate["database_id"]] = merge_candidate(current, candidate) if current else candidate

    pages_by_id: dict[str, dict[str, Any]] = {}
    for page in raw.get("dimension_pages", []):
        if not isinstance(page, dict) or not page.get("page_id"):
            continue
        normalized_page = normalize_dimension_page(page)
        current = pages_by_id.get(normalized_page["page_id"])
        pages_by_id[normalized_page["page_id"]] = merge_dimension_page(current, normalized_page) if current else normalized_page

    smoke_tests = []
    for test in raw.get("smoke_tests", []):
        if not isinstance(test, dict):
            continue
        status = str(test.get("status") or "not_run")
        if status not in {"passed", "failed", "not_run"}:
            raise ConfigError(f"未知 smoke test 状态：{status}")
        smoke_tests.append({
            "data_source_id": canonical_notion_id(test.get("data_source_id")),
            "status": status,
            "empty": bool(test.get("empty", False)),
            "checked_at": str(test.get("checked_at") or ""),
            "error": str(test.get("error") or ""),
        })

    workspace = raw.get("workspace") if isinstance(raw.get("workspace"), dict) else {}
    return {
        "schema_version": SCHEMA_VERSION,
        "discovered_at": str(raw.get("discovered_at") or utc_now()),
        "workspace": {"id": str(workspace.get("id") or ""), "name": str(workspace.get("name") or "未知工作区")},
        "hub": {
            "page_id": canonical_notion_id(hub.get("page_id")),
            "title": str(hub.get("title") or "未命名 Hub"),
            "url": str(hub.get("url") or ""),
            "last_edited_time": str(hub.get("last_edited_time") or ""),
            "readable": bool(hub.get("readable")),
        },
        "candidates": sorted(by_id.values(), key=lambda item: (normalize_text(item["source_section"]), normalize_text(item["title"]), item["database_id"])),
        "dimension_pages": sorted(pages_by_id.values(), key=lambda item: (item["depth"], normalize_text(item["title"]), item["page_id"])),
        "smoke_tests": smoke_tests,
    }


def normalize_semantics(semantics: dict[str, Any]) -> list[dict[str, Any]]:
    if semantics.get("schema_version") != SCHEMA_VERSION:
        raise ConfigError(f"语义映射 schema_version 必须为 {SCHEMA_VERSION}")
    raw_concepts = semantics.get("concepts")
    if not isinstance(raw_concepts, list):
        raise ConfigError("语义映射 concepts 必须是数组")

    concepts = []
    seen = set()
    for raw in raw_concepts:
        if not isinstance(raw, dict) or not raw.get("key"):
            continue
        key = str(raw["key"])
        if key in seen:
            raise ConfigError(f"语义概念 key 重复：{key}")
        seen.add(key)
        kind = str(raw.get("kind") or "source")
        if kind not in {"source", "property", "option", "page"}:
            raise ConfigError(f"语义概念 {key} kind 无效：{kind}")
        aliases = [str(value) for value in raw.get("aliases", []) if normalize_text(value)]
        if not aliases:
            raise ConfigError(f"语义概念 {key} 缺少 aliases")
        concepts.append({
            "key": key,
            "label": str(raw.get("label") or key),
            "kind": kind,
            "aliases": aliases,
            "source_aliases": [str(value) for value in raw.get("source_aliases", []) if normalize_text(value)],
            "property_aliases": [str(value) for value in raw.get("property_aliases", []) if normalize_text(value)],
        })
    return concepts


def schema_sources(discovery: dict[str, Any], generated_at: str) -> list[dict[str, Any]]:
    result = []
    for candidate in discovery["candidates"]:
        if not candidate["selected"]:
            continue
        for source in candidate["data_sources"]:
            properties = source["properties"]
            relations = []
            for prop in properties:
                if prop["type"] != "relation":
                    continue
                relations.append({
                    "field": prop["name"],
                    "related_database_id": prop.get("related_database_id", ""),
                    "related_data_source_id": prop.get("related_data_source_id", ""),
                })
            fingerprint_payload = {
                "database_id": candidate["database_id"],
                "data_source_id": source["id"],
                "title": source["title"],
                "properties": properties,
            }
            result.append({
                "database_id": candidate["database_id"],
                "database_title": candidate["title"],
                "data_source_id": source["id"],
                "title": source["title"],
                "url": source["url"] or candidate["url"],
                "source": candidate["source"],
                "source_page_id": candidate["source_page_id"],
                "source_section": candidate["source_section"],
                "detection_reason": candidate["detection_reason"],
                "last_edited_time": source["last_edited_time"] or candidate["last_edited_time"],
                "last_fetched_at": discovery["discovered_at"] or generated_at,
                "retrieve_failed": bool(candidate["retrieve_failed"] or source["retrieve_failed"]),
                "error": source["error"] or candidate["error"],
                "properties": properties,
                "relations": relations,
                "schema_fingerprint": json_digest(fingerprint_payload),
                "user_override": source.get("user_override") or candidate.get("user_override") or {},
            })
    return sorted(result, key=lambda item: (normalize_text(item["title"]), item["data_source_id"]))


def enrich_field_access(sources: list[dict[str, Any]]) -> None:
    database_ids = {item["database_id"] for item in sources}
    data_source_ids = {item["data_source_id"] for item in sources}
    for source in sources:
        writable = []
        readonly = []
        relations = []
        for prop in source["properties"]:
            is_readonly = prop["type"] in READ_ONLY_TYPES
            relation = None
            if prop["type"] == "relation":
                database_target = prop.get("related_database_id", "")
                source_target = prop.get("related_data_source_id", "")
                resolved = bool((database_target and database_target in database_ids) or (source_target and source_target in data_source_ids))
                relation = {
                    "field": prop["name"],
                    "related_database_id": database_target,
                    "related_data_source_id": source_target,
                    "resolved": resolved,
                }
                is_readonly = not resolved
                relations.append(relation)
            field = {"name": prop["name"], "type": prop["type"]}
            if prop.get("options"):
                field["options"] = prop["options"]
            (readonly if is_readonly else writable).append(field)
        source["writable_fields"] = writable
        source["readonly_fields"] = readonly
        source["relations"] = relations
        title_fields = [field["name"] for field in writable if field["type"] == "title"]
        blocked_reasons = []
        if source["retrieve_failed"]:
            blocked_reasons.append("schema_unreadable")
        if not title_fields:
            blocked_reasons.append("title_field_missing")
        source["access"] = {
            "read_ready": not source["retrieve_failed"],
            "create_page_ready": not source["retrieve_failed"] and bool(title_fields),
            "title_field": title_fields[0] if title_fields else None,
            "write_requires_runtime_validation": True,
            "blocked_reasons": blocked_reasons,
        }


def add_lookup(lookup: dict[str, list[Any]], name: Any, value: Any) -> None:
    key = normalize_text(name)
    if not key:
        return
    lookup.setdefault(key, [])
    if value not in lookup[key]:
        lookup[key].append(value)


def page_reference(page: dict[str, Any]) -> dict[str, Any]:
    return {
        "kind": "page",
        "key": page["key"],
        "title": page["title"],
        "page_id": page["page_id"],
        "url": page["url"],
        "last_edited_time": page["last_edited_time"],
        "parent_page_id": page["parent_page_id"],
        "parent_key": page["parent_key"],
        "depth": page["depth"],
        "read_ready": page["readable"],
    }


def build_lookup(sources: list[dict[str, Any]], pages: list[dict[str, Any]]) -> dict[str, Any]:
    source_titles: dict[str, list[Any]] = {}
    database_titles: dict[str, list[Any]] = {}
    property_names: dict[str, list[Any]] = {}
    option_names_index: dict[str, list[Any]] = {}
    page_titles: dict[str, list[Any]] = {}
    for source in sources:
        source_ref = {
            "database_id": source["database_id"],
            "data_source_id": source["data_source_id"],
            "title": source["title"],
        }
        add_lookup(source_titles, source["title"], source_ref)
        add_lookup(database_titles, source["database_title"], source_ref)
        for prop in source["properties"]:
            field_ref = {**source_ref, "property": prop["name"], "property_type": prop["type"]}
            add_lookup(property_names, prop["name"], field_ref)
            for option in prop.get("options", []):
                add_lookup(option_names_index, option, {**field_ref, "option": option})
    for page in pages:
        add_lookup(page_titles, page["title"], page_reference(page))
    return {
        "normalization": "NFKC + lowercase + remove separators",
        "source_titles": source_titles,
        "database_titles": database_titles,
        "property_names": property_names,
        "option_names": option_names_index,
        "page_titles": page_titles,
    }


def source_matches_context(source: dict[str, Any], aliases: list[str]) -> bool:
    if not aliases:
        return True
    names = {normalize_text(source["title"]), normalize_text(source["database_title"])}
    return any(normalize_text(alias) in names for alias in aliases)


def semantic_targets(concept: dict[str, Any], sources: list[dict[str, Any]], pages: list[dict[str, Any]]) -> list[dict[str, Any]]:
    aliases = {normalize_text(value) for value in concept["aliases"]}
    property_aliases = {normalize_text(value) for value in concept["property_aliases"]}
    targets = []
    if concept["kind"] == "page":
        for page in pages:
            override = page.get("user_override") if isinstance(page.get("user_override"), dict) else {}
            explicit = str(override.get("capability") or "") == concept["key"]
            exact = normalize_text(page["title"]) in aliases
            if explicit or exact:
                targets.append({
                    **page_reference(page),
                    "confidence": 1.0 if explicit else 0.99,
                    "evidence": "user_override" if explicit else "exact_page_title",
                })
        return sorted(targets, key=lambda item: (item["depth"], normalize_text(item["title"]), item["page_id"]))

    for source in sources:
        source_ref = {
            "database_id": source["database_id"],
            "data_source_id": source["data_source_id"],
            "title": source["title"],
            "read_ready": source["access"]["read_ready"],
            "create_page_ready": source["access"]["create_page_ready"],
        }
        override = source.get("user_override") if isinstance(source.get("user_override"), dict) else {}
        if concept["kind"] == "source":
            explicit = str(override.get("capability") or "") == concept["key"]
            exact = normalize_text(source["title"]) in aliases or normalize_text(source["database_title"]) in aliases
            if explicit or exact:
                targets.append({
                    "kind": "source",
                    **source_ref,
                    "confidence": 1.0 if explicit else 0.99,
                    "evidence": "user_override" if explicit else "exact_source_title",
                })
            continue

        if not source_matches_context(source, concept["source_aliases"]):
            continue
        for prop in source["properties"]:
            if concept["kind"] == "property" and normalize_text(prop["name"]) in aliases:
                targets.append({
                    "kind": "property",
                    **source_ref,
                    "property": prop["name"],
                    "property_type": prop["type"],
                    "confidence": 0.99,
                    "evidence": "exact_property_name",
                })
            elif concept["kind"] == "option":
                if property_aliases and normalize_text(prop["name"]) not in property_aliases:
                    continue
                for option in prop.get("options", []):
                    if normalize_text(option) in aliases:
                        targets.append({
                            "kind": "option",
                            **source_ref,
                            "property": prop["name"],
                            "property_type": prop["type"],
                            "option": option,
                            "confidence": 0.99,
                            "evidence": "exact_option_name",
                        })
    return sorted(targets, key=lambda item: (normalize_text(item["title"]), item["data_source_id"], item.get("property", ""), item.get("option", "")))


def build_semantic_map(concepts: list[dict[str, Any]], sources: list[dict[str, Any]], pages: list[dict[str, Any]]) -> dict[str, Any]:
    mapped = {}
    for concept in concepts:
        targets = semantic_targets(concept, sources, pages)
        if not targets:
            continue
        mapped[concept["key"]] = {
            "label": concept["label"],
            "kind": concept["kind"],
            "status": "ready" if len(targets) == 1 else "multiple",
            "targets": targets,
            "primary_target": targets[0] if len(targets) == 1 else None,
        }
    return mapped


def overall_health(discovery: dict[str, Any], sources: list[dict[str, Any]], pages: list[dict[str, Any]]) -> tuple[str, list[str]]:
    warnings = []
    if not discovery["hub"]["readable"]:
        return "blocked", ["Hub 无法读取"]
    usable = [source for source in sources if not source["retrieve_failed"]]
    if not usable:
        return "blocked", ["没有任何可用 Data Source Schema"]

    failed_sources = [source for source in sources if source["retrieve_failed"]]
    if failed_sources:
        warnings.append(f"{len(failed_sources)} 个 Data Source 读取失败")
    unresolved = sum(1 for source in sources for relation in source["relations"] if not relation["resolved"])
    if unresolved:
        warnings.append(f"{unresolved} 个 relation 目标未解析")
    failed_smoke = [test for test in discovery["smoke_tests"] if test["status"] == "failed"]
    if failed_smoke:
        warnings.append(f"{len(failed_smoke)} 个只读冒烟测试失败")
    unreadable_pages = [page for page in pages if not page["readable"]]
    if unreadable_pages:
        warnings.append(f"{len(unreadable_pages)} 个普通页面不可读取")
    return ("needs_attention" if failed_sources or failed_smoke or unreadable_pages else "ready"), warnings


def render_report(
    discovery: dict[str, Any],
    semantics: dict[str, Any],
    semantic_map: dict[str, Any],
    sources: list[dict[str, Any]],
    pages: list[dict[str, Any]],
    health: str,
    warnings: list[str],
    generated_at: str,
) -> str:
    selected_count = sum(1 for candidate in discovery["candidates"] if candidate["selected"])
    readable_count = sum(1 for source in sources if not source["retrieve_failed"])
    lines = [
        "# AI 人生系统初始化报告",
        "",
        f"- 生成时间：`{generated_at}`",
        f"- 索引格式：`{SCHEMA_VERSION}`",
        f"- 工作区：`{discovery['workspace']['name']}`",
        f"- Hub：{discovery['hub']['title']} (`{discovery['hub']['page_id']}`)",
        f"- 整体状态：`{health}`",
        f"- 候选数据库：`{len(discovery['candidates'])}`，已选择：`{selected_count}`",
        f"- Data Source：`{len(sources)}`，可读取：`{readable_count}`",
        f"- 普通页面：`{len(pages)}`，可读取：`{sum(1 for page in pages if page['readable'])}`",
        "",
        "## 实际数据源索引",
        "",
        "| 数据源 | 属性数 | 可读取 | 可创建页面 |",
        "| --- | ---: | --- | --- |",
    ]
    for source in sources:
        lines.append(f"| {source['title']} | `{len(source['properties'])}` | `{'true' if source['access']['read_ready'] else 'false'}` | `{'true' if source['access']['create_page_ready'] else 'false'}` |")

    lines.extend([
        "",
        "## 已识别语义",
        "",
        "这里只显示实际找到的概念；未找到的概念不会被报告为缺失。",
        "",
        "| 概念 | 类型 | 状态 | 目标 |",
        "| --- | --- | --- | --- |",
    ])
    for rule in semantic_map.values():
        target_labels = []
        for target in rule["targets"]:
            detail = target["title"]
            if target["kind"] in {"property", "option"}:
                detail += f".{target['property']}"
            if target["kind"] == "option":
                detail += f"={target['option']}"
            target_labels.append(detail)
        lines.append(f"| {rule['label']} | `{rule['kind']}` | `{rule['status']}` | {'；'.join(target_labels)} |")

    lines.extend(["", "## 警告与阻塞", ""])
    if warnings:
        lines.extend(f"- {warning}" for warning in warnings)
    else:
        lines.append("- 无")

    failures = [source for source in sources if source["retrieve_failed"]]
    if failures:
        lines.extend(["", "## 读取失败", ""])
        for source in failures:
            lines.append(f"- {source['title']} (`{source['data_source_id']}`)：{source['error'] or '未知错误'}")

    lines.extend(["", "## 只读冒烟测试", ""])
    if discovery["smoke_tests"]:
        for test in discovery["smoke_tests"]:
            suffix = "（空数据库）" if test["status"] == "passed" and test["empty"] else ""
            detail = f"：{test['error']}" if test["error"] else ""
            lines.append(f"- `{test['data_source_id']}`：`{test['status']}`{suffix}{detail}")
    else:
        lines.append("- 未记录冒烟测试；初始化结果仅证明 Schema 发现与配置生成成功。")
    return "\n".join(lines).rstrip() + "\n"


def build_outputs(discovery: dict[str, Any], semantics: dict[str, Any]) -> dict[str, str]:
    generated_at = utc_now()
    concepts = normalize_semantics(semantics)
    sources = schema_sources(discovery, generated_at)
    pages = discovery["dimension_pages"]
    enrich_field_access(sources)
    lookup = build_lookup(sources, pages)
    mapped = build_semantic_map(concepts, sources, pages)
    health, warnings = overall_health(discovery, sources, pages)

    profile_concepts = {
        key: {
            "label": rule["label"],
            "kind": rule["kind"],
            "status": rule["status"],
            "target_count": len(rule["targets"]),
        }
        for key, rule in mapped.items()
    }
    profile = {
        "schema_version": SCHEMA_VERSION,
        "system_name": str(semantics.get("system_name") or "AI人生系统"),
        "mapping_version": str(semantics.get("mapping_version") or ""),
        "initialized_at": generated_at,
        "workspace": discovery["workspace"],
        "hub": discovery["hub"],
        "semantic_concepts": profile_concepts,
        "source_index_file": "notion-index.json",
        "schema_compat_file": "notion-schema.json",
        "discovery_file": "discovery.json",
        "semantic_map_file": "semantic-map.json",
        "routing_rules_file": "routing-rules.json",
        "dimension_pages_file": "dimension-pages.json",
        "health": {
            "status": health,
            "hub_readable": discovery["hub"]["readable"],
            "schema_readable": any(not source["retrieve_failed"] for source in sources),
            "smoke_test": "failed" if any(test["status"] == "failed" for test in discovery["smoke_tests"]) else "passed" if any(test["status"] == "passed" for test in discovery["smoke_tests"]) else "not_run",
            "warnings": warnings,
        },
    }
    notion_index = {
        "schema_version": SCHEMA_VERSION,
        "generated_at": generated_at,
        "workspace": discovery["workspace"],
        "hub": discovery["hub"],
        "sources": sources,
        "lookup": lookup,
    }
    notion_schema = {
        "schema_version": SCHEMA_VERSION,
        "generated_at": generated_at,
        "compatibility_note": "兼容旧版；新 Skill 应读取 notion-index.json",
        "sources": sources,
    }
    semantic_map = {
        "schema_version": SCHEMA_VERSION,
        "mapping_version": str(semantics.get("mapping_version") or ""),
        "generated_at": generated_at,
        "policy": "only_present_concepts",
        "concepts": mapped,
    }
    routing_rules = {
        "schema_version": SCHEMA_VERSION,
        "mapping_version": str(semantics.get("mapping_version") or ""),
        "generated_at": generated_at,
        "compatibility_note": "兼容旧版文件名；仅包含实际匹配概念，不表示模板必需能力",
        "capabilities": mapped,
    }
    dimension_pages = {"schema_version": SCHEMA_VERSION, "generated_at": generated_at, "pages": discovery["dimension_pages"]}
    report = render_report(discovery, semantics, mapped, sources, pages, health, warnings, generated_at)

    json_values = {
        "profile.json": profile,
        "discovery.json": discovery,
        "notion-index.json": notion_index,
        "notion-schema.json": notion_schema,
        "semantic-map.json": semantic_map,
        "routing-rules.json": routing_rules,
        "dimension-pages.json": dimension_pages,
    }
    outputs = {name: json.dumps(value, ensure_ascii=False, indent=2) + "\n" for name, value in json_values.items()}
    outputs["initialization-report.md"] = report
    return outputs


def validate_output_payloads(outputs: dict[str, str]) -> None:
    missing = set(OUTPUT_FILES) - set(outputs)
    if missing:
        raise ConfigError(f"生成结果缺少文件：{', '.join(sorted(missing))}")
    for name, payload in outputs.items():
        if name.endswith(".json"):
            parsed = json.loads(payload)
            if parsed.get("schema_version") != SCHEMA_VERSION:
                raise ConfigError(f"{name} schema_version 无效")


def transactional_write(output_dir: Path, outputs: dict[str, str]) -> Optional[Path]:
    output_dir.mkdir(parents=True, exist_ok=True)
    staging = Path(tempfile.mkdtemp(prefix=".ai-life-init-", dir=output_dir))
    backup_dir: Optional[Path] = None
    replaced: list[str] = []
    existed: dict[str, bool] = {}
    try:
        for name, payload in outputs.items():
            target = staging / name
            target.write_text(payload, encoding="utf-8")
            if name.endswith(".json"):
                json.loads(target.read_text(encoding="utf-8"))

        timestamp = dt.datetime.now(dt.timezone.utc).strftime("%Y%m%dT%H%M%S%fZ")
        existing_names = [name for name in outputs if (output_dir / name).exists()]
        if existing_names:
            backup_dir = output_dir / "backups" / timestamp
            backup_dir.mkdir(parents=True, exist_ok=True)
            for name in existing_names:
                shutil.copy2(output_dir / name, backup_dir / name)

        for name in outputs:
            target = output_dir / name
            existed[name] = target.exists()
            os.replace(staging / name, target)
            replaced.append(name)
    except Exception:
        for name in reversed(replaced):
            target = output_dir / name
            backup = backup_dir / name if backup_dir else None
            if backup and backup.exists():
                shutil.copy2(backup, target)
            elif not existed.get(name, False) and target.exists():
                target.unlink()
        raise
    finally:
        shutil.rmtree(staging, ignore_errors=True)
    return backup_dir


def default_output_dir() -> Path:
    configured = os.environ.get("AI_LIFE_SYSTEM_DATA_DIR")
    return Path(configured).expanduser() if configured else Path.home() / ".ai-life-system"


def parse_args(argv: Optional[list[str]] = None) -> argparse.Namespace:
    skill_root = Path(__file__).resolve().parent.parent
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--discovery", required=True, type=Path, help="标准化 Notion 发现 JSON")
    parser.add_argument("--semantics", type=Path, default=skill_root / "references" / "semantic-aliases.json")
    parser.add_argument("--output-dir", type=Path, default=default_output_dir())
    parser.add_argument("--check-only", action="store_true", help="只校验并生成内存结果，不写文件")
    return parser.parse_args(argv)


def main(argv: Optional[list[str]] = None) -> int:
    args = parse_args(argv)
    try:
        discovery = normalize_discovery(load_json(args.discovery.expanduser().resolve()))
        semantics = load_json(args.semantics.expanduser().resolve())
        outputs = build_outputs(discovery, semantics)
        validate_output_payloads(outputs)
        profile = json.loads(outputs["profile.json"])
        if args.check_only:
            print(json.dumps({"valid": True, "health": profile["health"]["status"], "files": list(OUTPUT_FILES)}, ensure_ascii=False))
            return 0
        backup = transactional_write(args.output_dir.expanduser().resolve(), outputs)
        print(json.dumps({
            "valid": True,
            "health": profile["health"]["status"],
            "output_dir": str(args.output_dir.expanduser().resolve()),
            "backup_dir": str(backup) if backup else "",
            "files": list(OUTPUT_FILES),
        }, ensure_ascii=False))
        return 0
    except (ConfigError, OSError, json.JSONDecodeError) as exc:
        print(f"初始化配置生成失败：{exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
