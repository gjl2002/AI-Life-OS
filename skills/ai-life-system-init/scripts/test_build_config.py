#!/usr/bin/env python3

import json
import sys
import tempfile
import unittest
from pathlib import Path


SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))

import build_config  # noqa: E402
import validate_config  # noqa: E402


def candidate(database_id, title, section, properties=None, **extra):
    value = {
        "database_id": database_id,
        "title": title,
        "source": "child_database",
        "source_page_id": "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
        "source_section": section,
        "detection_reason": f"来自 {section} 区块",
        "selected": True,
        "properties": properties or [{"name": "名称", "type": "title"}],
    }
    value.update(extra)
    return value


class BuildConfigTest(unittest.TestCase):
    def setUp(self):
        self.semantics = build_config.load_json(SCRIPT_DIR.parent / "references" / "semantic-aliases.json")

    def discovery(self):
        return {
            "schema_version": "0.2",
            "discovered_at": "2026-08-22T10:00:00+08:00",
            "workspace": {"id": "workspace-1", "name": "测试工作区"},
            "hub": {
                "page_id": "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "title": "数据管理",
                "url": "https://www.notion.so/test",
                "readable": True,
            },
            "candidates": [
                candidate("11111111111111111111111111111111", "目标", "12周行动"),
                candidate("22222222222222222222222222222222", "项目", "12周行动"),
                candidate(
                    "33333333333333333333333333333333",
                    "任务",
                    "12周行动",
                    [
                        {"name": "任务", "type": "title"},
                        {"name": "情景", "type": "multi_select", "options": ["☑️ 待办", "深度工作"]},
                        {"name": "专注", "type": "number"},
                        {
                            "name": "项目",
                            "type": "relation",
                            "related_database_id": "22222222222222222222222222222222",
                        },
                        {"name": "自动摘要", "type": "formula"},
                    ],
                ),
                candidate("44444444444444444444444444444444", "每日记录", "周期复盘"),
                candidate("55555555555555555555555555555555", "每周复盘", "周期复盘"),
                candidate(
                    "66666666666666666666666666666666",
                    "计时",
                    "目标与行动",
                    [{"name": "名称", "type": "title"}, {"name": "专注", "type": "checkbox"}],
                ),
                candidate(
                    "77777777777777777777777777777777",
                    "梦境日记",
                    "身心健康",
                    retrieve_failed=True,
                    error="permission denied",
                    properties=[],
                ),
                candidate("99999999999999999999999999999999", "忽略数据库", "其他", selected=False),
            ],
            "dimension_pages": [
                {
                    "key": "commercial_system",
                    "title": "商业系统",
                    "page_id": "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb",
                    "source": "hub_direct",
                    "depth": 1,
                    "readable": True,
                },
                {
                    "key": "commercial_positioning",
                    "title": "商业定位",
                    "page_id": "cccccccccccccccccccccccccccccccc",
                    "source": "system_child",
                    "parent_page_id": "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb",
                    "parent_key": "commercial_system",
                    "depth": 2,
                    "last_edited_time": "2026-08-22T11:00:00+08:00",
                    "readable": True,
                },
            ],
            "smoke_tests": [
                {"data_source_id": "11111111111111111111111111111111", "status": "passed", "empty": True}
            ],
        }

    def outputs(self, raw=None):
        discovery = build_config.normalize_discovery(raw or self.discovery())
        return build_config.build_outputs(discovery, self.semantics)

    def test_builds_fact_index_and_field_option_semantics(self):
        outputs = self.outputs()
        build_config.validate_output_payloads(outputs)

        index = json.loads(outputs["notion-index.json"])
        self.assertEqual(7, len(index["sources"]))
        self.assertNotIn("忽略数据库", [source["title"] for source in index["sources"]])
        task = next(source for source in index["sources"] if source["title"] == "任务")
        self.assertTrue(task["access"]["create_page_ready"])
        self.assertEqual("任务", task["access"]["title_field"])
        self.assertTrue(task["relations"][0]["resolved"])
        self.assertIn("自动摘要", [field["name"] for field in task["readonly_fields"]])

        semantic = json.loads(outputs["semantic-map.json"])["concepts"]
        self.assertEqual("source", semantic["daily_record"]["kind"])
        self.assertEqual("每日记录", semantic["daily_record"]["primary_target"]["title"])
        self.assertEqual("option", semantic["todo"]["kind"])
        self.assertEqual("☑️ 待办", semantic["todo"]["primary_target"]["option"])
        self.assertEqual("multiple", semantic["focus"]["status"])
        self.assertEqual("page", semantic["commercial_positioning"]["kind"])
        self.assertEqual("商业定位", semantic["commercial_positioning"]["primary_target"]["title"])

        self.assertIn("商业定位", outputs["initialization-report.md"])
        page_lookup = index["lookup"]["page_titles"][build_config.normalize_text("商业定位")]
        self.assertEqual("cccccccc-cccc-cccc-cccc-cccccccccccc", page_lookup[0]["page_id"])

    def test_absent_semantics_do_not_create_missing_or_degrade_health(self):
        raw = self.discovery()
        raw["candidates"] = raw["candidates"][:5]
        raw["candidates"][2]["properties"] = [
            prop for prop in raw["candidates"][2]["properties"] if prop["name"] != "专注"
        ]
        outputs = self.outputs(raw)
        semantic = json.loads(outputs["semantic-map.json"])["concepts"]
        self.assertNotIn("focus", semantic)
        profile = json.loads(outputs["profile.json"])
        self.assertEqual("ready", profile["health"]["status"])
        self.assertNotIn("`missing`", outputs["initialization-report.md"])

    def test_duplicate_exact_sources_are_multiple_not_missing(self):
        raw = self.discovery()
        raw["candidates"].append(candidate("abababababababababababababababab", "目标", "12周行动"))
        outputs = self.outputs(raw)
        goal = json.loads(outputs["semantic-map.json"])["concepts"]["goal"]
        self.assertEqual("multiple", goal["status"])
        self.assertIsNone(goal["primary_target"])

    def test_multi_data_source_container_preserves_source_titles_and_semantics(self):
        raw = self.discovery()
        raw["candidates"].append(candidate(
            "88888888888888888888888888888888",
            "AI 学习库",
            "AI与系统工具",
            data_sources=[
                {
                    "id": "88888888888888888888888888880001",
                    "title": "去AI味库",
                    "properties": [
                        {"name": "句式名称", "type": "title"},
                        {"name": "禁用等级", "type": "select", "options": ["必删", "慎用", "可保留"]},
                    ],
                },
                {
                    "id": "88888888888888888888888888880002",
                    "title": "文风语料库",
                    "properties": [{"name": "文章标题", "type": "title"}],
                },
            ],
        ))
        outputs = self.outputs(raw)
        index = json.loads(outputs["notion-index.json"])
        source_titles = {
            source["title"]: source["data_source_id"]
            for source in index["sources"]
            if source["database_title"] == "AI 学习库"
        }
        self.assertEqual({"去AI味库", "文风语料库"}, set(source_titles))

        semantic = json.loads(outputs["semantic-map.json"])["concepts"]
        self.assertEqual("去AI味库", semantic["ai_flavor_library"]["primary_target"]["title"])
        self.assertEqual("文风语料库", semantic["style_corpus"]["primary_target"]["title"])

    def test_duplicate_exact_pages_are_multiple_and_page_ids_are_deduplicated(self):
        raw = self.discovery()
        raw["dimension_pages"].append({
            "key": "commercial_positioning_copy",
            "title": "商业定位",
            "page_id": "dddddddddddddddddddddddddddddddd",
            "source": "system_child",
            "parent_page_id": "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb",
            "parent_key": "commercial_system",
            "depth": 2,
            "readable": True,
        })
        raw["dimension_pages"].append(dict(raw["dimension_pages"][1]))
        outputs = self.outputs(raw)
        concept = json.loads(outputs["semantic-map.json"])["concepts"]["commercial_positioning"]
        pages = json.loads(outputs["dimension-pages.json"])["pages"]
        self.assertEqual("multiple", concept["status"])
        self.assertEqual(2, len([page for page in pages if page["title"] == "商业定位"]))

    def test_rejects_page_discovery_beyond_bounded_depth(self):
        raw = self.discovery()
        raw["dimension_pages"].append({
            "key": "too_deep",
            "title": "不应继续扫描的页面",
            "page_id": "eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee",
            "depth": 3,
            "readable": True,
        })
        with self.assertRaises(build_config.ConfigError):
            build_config.normalize_discovery(raw)

    def test_transaction_and_cross_file_validation(self):
        outputs = self.outputs()
        with tempfile.TemporaryDirectory() as temp:
            config_dir = Path(temp)
            self.assertIsNone(build_config.transactional_write(config_dir, outputs))
            self.assertEqual([], validate_config.validate(config_dir))
            backup = build_config.transactional_write(config_dir, outputs)
            self.assertIsNotNone(backup)
            self.assertTrue((backup / "profile.json").is_file())


if __name__ == "__main__":
    unittest.main()
