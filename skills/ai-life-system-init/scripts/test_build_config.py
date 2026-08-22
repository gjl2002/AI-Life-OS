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
                {"key": "life_dashboard", "title": "人生仪表盘", "page_id": "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb", "readable": True}
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
