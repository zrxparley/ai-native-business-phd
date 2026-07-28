# from_scratch.md · AI工程从零构建层 (v11.0)

> **单元**：技能5 Agentic系统工程 · Day 3 Agent评估与Benchmarking
> **scratch 哲学**：不调 deepeval，手写 Agent eval harness，从任务通过率到 Wilson 置信区间到轨迹评分直译到裸 Python。

## scratch_topic

本单元 from-scratch 主题：**手写 Agent eval harness（任务 fixture + 通过率 + 轨迹评分 + Wilson CI）**。对应 rohitg00 P14/19 Benchmarks SWE-bench GAIA + P14/30 Eval Driven Agent Development。notes.md 用 deepeval 的 GEval/FaithfulnessMetric/BaseMetric 三件套搭建评测套件，本层把"评估"拆到裸 Python：TestCase 数据类 + 指标函数 + Wilson 置信区间 + 批量 evaluate 聚合，让"通过率 85% 意味着什么"不再是 deepeval 的黑箱数字，而是带置信区间的统计陈述。

## core_algorithm

Agent 评估的核心是把"Agent 好不好"量化为可统计的指标。给定测试集 $D = \{(q_i, a_i^*, \tau_i^*)\}_{i=1}^N$（问题、期望答案、期望轨迹），Agent 产生轨迹 $\hat{\tau}_i$ 与输出 $\hat{a}_i$。三类指标：

**任务通过率**（End-to-End）：二值判定 $y_i = \mathbb{1}[\text{match}(\hat{a}_i, a_i^*)]$，点估计 $\hat{p} = \frac{1}{N}\sum y_i$。但点估计隐藏了样本量信息--$N=20$ 时 85% 与 $N=2000$ 时 85% 可信度天差地别。Wilson 95% 置信区间修正这一点：

$$\text{CI}_{95} = \frac{\hat{p} + \frac{z^2}{2N} \pm z\sqrt{\frac{\hat{p}(1-\hat{p})}{N} + \frac{z^2}{4N^2}}}{1 + \frac{z^2}{N}}, \quad z = 1.96$$

**轨迹评分**（Trajectory）：每步打分 $s_{i,t} \in [0,1]$，轨迹分 $\bar{s}_i = \sum_t w_t s_{i,t}$（加权）。关键维度：工具选择正确性（是否选对工具）、参数正确性（参数是否匹配）、推理合理性（thought 是否逻辑连贯）。

**LLM-as-Judge 可靠性**：用 Cohen's $\kappa$ 衡量 judge 与人工标注的一致性：

$$\kappa = \frac{p_o - p_e}{1 - p_e}$$

$p_o$ 为观察一致率，$p_e$ 为随机一致率。$\kappa > 0.8$ 才可信，$\kappa < 0.4$ 不可接受。这是 notes.md "LLM-as-judge 有自身偏差"的数学度量--不报告 $\kappa$ 的自动评分不可发表。

## code_artifact

```python
import math
from dataclasses import dataclass, field

@dataclass
class TestCase:
    query: str
    expected: str
    expected_tools: tuple = ()
    actual_output: str = ""
    trajectory: list = field(default_factory=list)

@dataclass
class MetricResult:
    name: str
    score: float
    reason: str = ""

def exact_match(tc):
    s = 1.0 if tc.actual_output.strip() == tc.expected.strip() else 0.0
    return MetricResult("exact_match", s)

def tool_accuracy(tc):
    if not tc.expected_tools:
        return MetricResult("tool_acc", 1.0, "no_expected")
    called = tuple(a.get("tool") for a in tc.trajectory
                   if isinstance(a, dict) and "tool" in a)
    correct = sum(1 for e, c in zip(tc.expected_tools, called) if e == c)
    return MetricResult("tool_acc", correct / len(tc.expected_tools))

def wilson_ci(p, n, z=1.96):
    if n == 0:
        return (0.0, 0.0)
    denom = 1 + z * z / n
    center = (p + z * z / (2 * n)) / denom
    spread = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / denom
    return (max(0.0, center - spread), min(1.0, center + spread))

def evaluate(test_cases, metrics=None):
    metrics = metrics or [exact_match, tool_accuracy]
    rows = [{m(tc).name: m(tc).score for m in metrics} for tc in test_cases]
    passed = sum(1 for r in rows if r.get("exact_match", 0) >= 0.5)
    pr = passed / len(rows) if rows else 0.0
    lo, hi = wilson_ci(pr, len(rows))
    ta = sum(r.get("tool_acc", 0) for r in rows) / len(rows) if rows else 0.0
    return {"pass_rate": pr, "ci95": (lo, hi), "tool_acc_mean": ta, "per_case": rows}

if __name__ == "__main__":
    cases = [
        TestCase("q1", "final", ("calc",), "final",
                 [{"tool": "calc"}, {"tool": "search"}]),
        TestCase("q2", "final", ("calc",), "wrong", [{"tool": "search"}]),
    ]
    rep = evaluate(cases)
    assert 0.0 <= rep["pass_rate"] <= 1.0
    assert rep["ci95"][0] <= rep["pass_rate"] <= rep["ci95"][1]
    assert 0.0 <= rep["tool_acc_mean"] <= 1.0
```

**verification_property**: pass_rate ∈ [0,1]；Wilson CI 下界 ≤ pass_rate ≤ 上界（覆盖率保证）；tool_acc_mean ∈ [0,1]；per_case 行数 = 测试用例数（无遗漏）。

## connection_to_unit

1. **库指标 vs 手写指标**：notes.md 用 deepeval 的 `GEval`/`FaithfulnessMetric`/`BaseMetric` 三件套，from-scratch 版把 `BaseMetric` 直译为 `Callable[[TestCase], MetricResult]`，把 `evaluate()` 直译为遍历+聚合。库隐藏了"指标本质是函数 TestCase->score"这一事实--from-scratch 让你看到 evaluate 就是 `for tc in cases: for m in metrics: score += m(tc)`。
2. **点估计 vs 置信区间**：notes.md 的"任务完成率 ≥ 85%"是点估计，from-scratch 版加 Wilson CI 揭示"N=20 时 85% 的 CI 是 [62%, 97%]"--这是 notes.md 没说的统计真相，小样本通过率不可信。deepeval 默认不报告 CI，这是 from-scratch 补的工程盲点。
3. **确定性指标 vs 语义指标**：notes.md 的 LLM-as-judge 用 GEval criteria 打分（语义指标），from-scratch 版的 `tool_accuracy` 用 `expected_tools` 轨迹对比（确定性指标）--两者互补：确定性指标可复现但覆盖窄，语义指标覆盖宽但不可复现。暴露了"哪些维度可确定性评估，哪些必须靠 judge"。
4. **幻觉率对比**：notes.md 的"幻觉率 ≤ 5%"用 `FaithfulnessMetric` 对比 `actual_output` 与 `retrieval_context`，from-scratch 版的 `tool_accuracy` 用 `expected_tools` 对比轨迹--两者都是"轨迹级确定性指标"，区别在对比对象（声明 vs 工具调用）。from-scratch 让你看到幻觉检测的内核就是"声明是否在证据中"。

## deep_dive_links

- [P14/19 Benchmarks SWE-bench GAIA - rohitg00](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/14-agent-engineering/19-benchmarks-swebench-gaia/README.md) - Agent 基准测试设计，本单元评估方法论的理论锚点
- [P14/30 Eval Driven Agent Development - rohitg00](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/14-agent-engineering/30-eval-driven-agent-development/README.md) - 评估驱动开发，从 eval 到迭代改进的闭环

## exercises

1. 在本单元 `starter.ipynb` TODO6（`evaluate()` 批量运行）完成后，用 from-scratch `evaluate()` 跑同一批 LLMTestCase，对比 deepeval 的 GEval 分数与 from-scratch 的 `exact_match`/`tool_acc`。提示：用 mock Agent 轨迹（预设脚本）替代真实 LLM，聚焦指标计算验证。
2. 实现 Cohen's kappa：给定两个 judge（如 deepeval GEval vs 人工标注）对同一批 case 的分数，计算 $\kappa$。这是 notes.md "LLM-as-judge 有偏差"的量化度量，对应 core_algorithm 的公式。
3. 为 from-scratch `evaluate()` 添加 P50/P95 延迟指标：在 `TestCase` 加 `latency` 字段，`evaluate` 计算分位数（排序取第 $\lceil 0.5N \rceil$ 位）。对应 notes.md "延迟 P50<30s, P95<60s" 的 SLI。
4. TODO: 在 `practice.md` 的 D2-Trajectory drill 中，把 from-scratch `tool_accuracy` 替换为加权版（按工具重要性赋权），观察与等权版本的排名差异。这是 notes.md "工具调用准确率 ≥ 90%" 的精细化拆解。
