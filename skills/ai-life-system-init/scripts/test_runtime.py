#!/usr/bin/env python3

import tempfile
import unittest
from pathlib import Path


SCRIPT_DIR = Path(__file__).resolve().parent

import build_config  # noqa: E402
import runtime  # noqa: E402


class RuntimeTest(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.config_dir = Path(self.temp.name)
        discovery = {
            "schema_version": "0.3",
            "workspace": {"id": "workspace-1", "name": "测试工作区"},
            "hub": {"page_id": "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "title": "AI 人生系统", "readable": True},
            "candidates": [
                {
                    "database_id": "11111111111111111111111111111111",
                    "title": "任务",
                    "source": "child_database",
                    "selected": True,
                    "properties": [
                        {"name": "任务", "type": "title"},
                        {"name": "状态", "type": "status", "options": ["未开始", "进行中", "已完成"]},
                        {"name": "专注", "type": "number"},
                        {"name": "自动摘要", "type": "formula"},
                        {
                            "name": "关联目标",
                            "type": "relation",
                            "related_database_id": "99999999999999999999999999999999",
                        },
                    ],
                },
                {
                    "database_id": "22222222222222222222222222222222",
                    "title": "计时",
                    "source": "child_database",
                    "selected": True,
                    "properties": [
                        {"name": "名称", "type": "title"},
                        {"name": "专注", "type": "checkbox"},
                    ],
                },
            ],
            "dimension_pages": [],
            "smoke_tests": [],
        }
        semantics = build_config.load_json(SCRIPT_DIR.parent / "references" / "semantic-aliases.json")
        outputs = build_config.build_outputs(build_config.normalize_discovery(discovery), semantics)
        build_config.transactional_write(self.config_dir, outputs)
        self.bundle = runtime.load_runtime(self.config_dir)

    def test_status_reports_ready_runtime(self):
        status = runtime.runtime_status(self.bundle)
        self.assertEqual("ready", status["runtime_status"])
        self.assertEqual(2, status["source_count"])
        self.assertGreater(status["semantic_count"], 0)

    def test_resolve_concept_source_and_multiple_property(self):
        concept = runtime.resolve(self.bundle, "concept", "task")
        self.assertEqual("ready", concept["status"])
        self.assertEqual("任务", concept["primary_target"]["title"])

        source = runtime.resolve(self.bundle, "source", "任务")
        self.assertEqual("ready", source["status"])
        self.assertEqual("任务", source["primary_target"]["title"])

        focus = runtime.resolve(self.bundle, "property", "专注")
        self.assertEqual("multiple", focus["status"])
        self.assertEqual(2, focus["target_count"])

        missing = runtime.resolve(self.bundle, "source", "不存在")
        self.assertEqual("not_found", missing["status"])

    def test_check_write_accepts_real_fields_and_option(self):
        result = runtime.check_write(
            self.bundle,
            "11111111111111111111111111111111",
            ["任务", "状态"],
            ["状态=进行中"],
        )
        self.assertTrue(result["write_ready"])
        self.assertTrue(result["requires_user_authorization"])
        self.assertTrue(result["requires_live_schema_check"])

    def test_check_write_blocks_unsafe_fields_and_options(self):
        result = runtime.check_write(
            self.bundle,
            "11111111111111111111111111111111",
            ["任务", "自动摘要", "关联目标", "状态"],
            ["状态=随便写"],
        )
        self.assertFalse(result["write_ready"])
        codes = {item["code"] for item in result["errors"]}
        self.assertIn("field_readonly", codes)
        self.assertIn("relation_unresolved", codes)
        self.assertIn("option_not_found", codes)

    def test_create_requires_real_title_field(self):
        result = runtime.check_write(
            self.bundle,
            "11111111111111111111111111111111",
            ["状态"],
            ["状态=未开始"],
        )
        self.assertFalse(result["write_ready"])
        self.assertIn("title_field_required", {item["code"] for item in result["errors"]})


if __name__ == "__main__":
    unittest.main()
