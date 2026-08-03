import ast
import json
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]


GOLDEN_UNITS = {
    "CQ-S3-1": REPO_ROOT / "teaching-materials/skill-3-causal/day-1-causal-basics",
    "CQ-S5-1": REPO_ROOT / "teaching-materials/skill-5-agentic/day-3-agent-evaluation",
    "CQ-R4-1": REPO_ROOT / "teaching-materials/module-r-research-methodology/day-r4-systematic-review-prisma",
    "CQ-C4-1": REPO_ROOT / "teaching-materials/capstone-ai-business-analytics/day-phase-4-causal-experiment-design",
}


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def assert_terms(testcase: unittest.TestCase, text: str, terms: tuple[str, ...]) -> None:
    missing = [term for term in terms if term not in text]
    testcase.assertEqual([], missing, f"missing required quality terms: {missing}")


class GoldenContentQualityTests(unittest.TestCase):
    """Quality contracts for the first four high-impact curriculum revisions."""

    def test_quality_outcome_is_traceable_across_learning_artifacts(self) -> None:
        for outcome_id, unit_dir in GOLDEN_UNITS.items():
            with self.subTest(outcome_id=outcome_id):
                for filename in ("notes.md", "practice.md", "alignment.md", "research.md"):
                    self.assertIn(outcome_id, read_text(unit_dir / filename), filename)

    def test_skill3_teaches_identification_assumptions_and_falsification(self) -> None:
        notes = read_text(GOLDEN_UNITS["CQ-S3-1"] / "notes.md")
        assert_terms(
            self,
            notes,
            (
                "## 识别假设与可证伪诊断",
                "一致性（consistency）",
                "可交换性（exchangeability）",
                "正值性（positivity）",
                "负对照",
                "敏感性分析",
                "https://www.pywhy.org/dowhy/v0.14/user_guide/refuting_causal_estimates/",
                "证据复核日期：2026-08-03",
            ),
        )

    def test_agent_evaluation_distinguishes_data_provenance_and_calibrates_judges(self) -> None:
        notes = read_text(GOLDEN_UNITS["CQ-S5-1"] / "notes.md")
        data_readme = read_text(GOLDEN_UNITS["CQ-S5-1"] / "data/README.md")
        assert_terms(
            self,
            notes,
            (
                "## 评估可靠性协议",
                "人工黄金集",
                "位置偏差",
                "长度偏差",
                "重复评估",
                "置信区间",
                "成本",
                "延迟",
                "安全失败率",
                "arXiv:2306.05685",
                "arXiv:2606.13685",
            ),
        )
        assert_terms(
            self,
            data_readme,
            (
                "## 数据真实性分级与泄漏控制",
                "教学合成（synthetic）",
                "人工策展（curated）",
                "生产记录（recorded）",
                "训练集泄漏",
                "证据复核日期：2026-08-03",
            ),
        )
        self.assertNotIn("本 Day 不使用模拟数据", data_readme)

    def test_r4_covers_protocol_bias_certainty_and_automation_disclosure(self) -> None:
        notes = read_text(GOLDEN_UNITS["CQ-R4-1"] / "notes.md")
        assert_terms(
            self,
            notes,
            (
                "## 预注册、偏倚与证据确定性",
                "protocol amendment",
                "双人独立筛选",
                "研究内偏倚",
                "报告偏倚",
                "证据确定性",
                "自动化工具披露",
                "PRISMA 2020 Item 11",
                "PRISMA 2020 Item 24",
                "https://www.prisma-statement.org/prisma-2020",
            ),
        )

    def test_capstone_requires_a_publishable_causal_evidence_pack(self) -> None:
        notes = read_text(GOLDEN_UNITS["CQ-C4-1"] / "notes.md")
        assert_terms(
            self,
            notes,
            (
                "## 最小可发表因果报告规范",
                "estimand",
                "重叠性/正值性",
                "协变量平衡",
                "置信区间",
                "多重检验",
                "缺失数据",
                "敏感性分析",
                "业务决策阈值",
                "环境锁文件",
                "CQ-C4-1",
            ),
        )

    def test_golden_solution_notebook_code_is_syntactically_valid(self) -> None:
        for outcome_id, unit_dir in GOLDEN_UNITS.items():
            notebook = json.loads(read_text(unit_dir / "solution.ipynb"))
            for index, cell in enumerate(notebook.get("cells", [])):
                if cell.get("cell_type") != "code":
                    continue
                source = cell.get("source", "")
                if isinstance(source, list):
                    source = "".join(source)
                source = "\n".join(
                    line for line in source.splitlines() if not line.lstrip().startswith(("%", "!"))
                )
                with self.subTest(outcome_id=outcome_id, cell=index):
                    ast.parse(source)


if __name__ == "__main__":
    unittest.main()
