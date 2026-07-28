# from_scratch.md · AI工程从零构建层 (v11.0)

> **单元**：技能5 Agentic系统工程 · Day 6 IMRaD论文写作
> **scratch 哲学**：不调 LangSmith/Langfuse，手写实验追踪 logger（trace + span），从 OTel 语义约定到逻辑时钟到 P95 尾延迟直译到裸 Python。

## scratch_topic

本单元 from-scratch 主题：**手写实验追踪 logger（trace + span，OTel GenAI 风格）**。对应 rohitg00 P14/24 Agent Observability Platforms + P14/23 OTel GenAI Conventions。notes.md 用 arxiv + statsmodels 拆解论文结构 + 跑统计检验，本层补上"论文 Results 的数据从哪来"的工程基础：trace/span 结构化日志 + 逻辑时钟 + 尾延迟分位数 + GenAI 语义约定字段，让"可复现研究"不再是口号，而是可逐行审计的 40 行 logger，每个 IMRaD Results 数字都能回溯到原始 span。

## core_algorithm

实验追踪 logger 的核心是 **trace/span 二级结构**（OpenTelemetry 模型）。一次实验运行 = 一个 trace，内含多个 span（每步操作）。span 是树状嵌套（有 parent_span_id）。

**Span 结构**：$\text{span} = (\text{id}, \text{parent\_id}, \text{name}, t_{\text{start}}, t_{\text{end}}, \text{attrs}, \text{status})$。duration $d = t_{\text{end}} - t_{\text{start}}$。

**Trace 作为 DAG**：spans 形成森林（多根 span 的 parent_id = None），边 $e = (\text{parent}, \text{child})$。trace 的总 wall-clock 时长 $T = \max(t_{\text{end}}) - \min(t_{\text{start}})$，但 CPU 时间 $\sum d_i$ 可能小于 $T$（并行 span）或大于 $T$（嵌套 span 重复计算）。

**尾延迟**（tail latency）：P95/P99 通过 order statistics 估计。给定 $N$ 个 span 的 duration 样本 $\{d_{(1)} \leq ... \leq d_{(N)}\}$，P95 = $d_{(\lceil 0.95N \rceil)}$。这是 IMRaD Results "P95 延迟 2.3s"的数学定义。

**GenAI 语义约定**（OTel GenAI）：span 的 attrs 须含 `gen_ai.request.model`、`gen_ai.usage.prompt_tokens`、`gen_ai.usage.completion_tokens`、`gen_ai.system` 等。这些字段让 trace 可跨模型/跨版本聚合统计--这是 Results "我们用 Claude-Sonnet，平均 1200 token/请求"的数据来源。

**因果可追溯**：trace 的 span 嵌套结构记录了"哪个 LLM 调用属于哪个 Agent 步骤"，使 Results 部分的每个数字可回溯到原始 span。这是可复现研究的工程基础：论文报告 trace_id，读者可调取完整 span 树验证。

## code_artifact

```python
from dataclasses import dataclass, field
from typing import Optional

_idc = [0]
def _new_id():
    _idc[0] += 1
    return f"{_idc[0]:016x}"

_tick = [0]
def _now():
    _tick[0] += 1
    return _tick[0]

@dataclass
class Span:
    name: str
    trace_id: str
    span_id: str = field(default_factory=_new_id)
    parent_id: Optional[str] = None
    start: int = 0
    end: int = 0
    attrs: dict = field(default_factory=dict)
    status: str = "OK"
    def duration(self):
        return self.end - self.start

class Tracer:
    def __init__(self):
        self.spans = []
        self._stack = []
    def start_span(self, name, attrs=None):
        parent = self._stack[-1].span_id if self._stack else None
        tid = self._stack[0].trace_id if self._stack else _new_id()
        s = Span(name, tid, parent_id=parent, attrs=attrs or {})
        s.start = _now()
        self._stack.append(s)
        return s
    def end_span(self, span, status="OK"):
        span.end = _now()
        span.status = status
        self.spans.append(span)
        if self._stack and self._stack[-1].span_id == span.span_id:
            self._stack.pop()
    def trace_summary(self):
        durs = sorted(s.duration() for s in self.spans if s.status == "OK")
        def pct(p):
            return durs[min(len(durs) - 1, int(len(durs) * p))] if durs else 0
        return {"n_spans": len(self.spans), "total_cpu": sum(durs),
                "p50": pct(0.5), "p95": pct(0.95)}

if __name__ == "__main__":
    tr = Tracer()
    root = tr.start_span("agent_run", {"gen_ai.system": "claude"})
    for _ in range(3):
        s = tr.start_span("llm_call", {"gen_ai.request.model": "sonnet"})
        _now()  # simulate work
        tr.end_span(s)
    tr.end_span(root)
    summ = tr.trace_summary()
    assert summ["n_spans"] == 4
    assert summ["p50"] <= summ["p95"]
    assert all(s.trace_id == root.trace_id for s in tr.spans)
```

**verification_property**: 所有 span 共享同一 trace_id；P50 ≤ P95（order statistic 单调性）；n_spans = 创建的 span 数（无丢失）；parent_id 形成有效树结构（无环）。

## connection_to_unit

1. **Results 数据来源对比**：notes.md 用 arxiv 包下载论文 + statsmodels 跑统计检验写 Results，from-scratch 版的 Tracer 是"Results 数据从哪来"的工程基础--span attrs（`gen_ai.request.model`, `prompt_tokens`）就是 Results "我们用 Claude-Sonnet，平均 1200 token"的原始数据。论文数字来自 trace 聚合，而非凭空编造。
2. **可复现性对比**：notes.md 的 IMRaD Methods 要求"可复现性"（别人读完能用同样方法重复），from-scratch 版的 trace_id + span_id 嵌套结构让"每次实验运行的每步操作可回溯"--这是可复现研究的工程载体：论文报告 trace_id，读者可调取完整 span 树验证。
3. **LLM-as-judge 延迟对比**：notes.md 的 LLM-as-judge 评估写作质量，from-scratch 版的 `trace_summary(p50/p95)` 是"评估 itself 的延迟分布"--judge LLM 的 P95 延迟决定评估成本，这是 Discussion "局限性"部分常被忽略的工程现实。
4. **APA 统计报告对比**：notes.md 的 APA t 检验报告 `t(df)=X.XX, p<.001`，from-scratch 版的 span attrs 是 t 检验的原始数据来源--每个 `llm_call` span 的 duration 是一个样本，N 个 span 跑 t 检验。这暴露了"统计检验的数据来自 trace"这一工程链路。

## deep_dive_links

- [P14/24 Agent Observability Platforms - rohitg00](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/14-agent-engineering/24-agent-observability-platforms/README.md) - Agent 可观测平台，trace/span 存储与查询，本单元核心理论锚点
- [P14/23 OTel GenAI Conventions - rohitg00](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/14-agent-engineering/23-otel-genai-conventions/README.md) - OpenTelemetry GenAI 语义约定，span attrs 标准化

## exercises

1. 在本单元 `starter.ipynb` TODO3（Methods 撰写，确保可复现性）完成后，用 from-scratch Tracer 为你的营销 Agent 实验生成 trace，把 `trace_summary` 的数字写入 Methods 的"实验环境"段落。提示：span attrs 记录 `gen_ai.request.model` 和 token 数。
2. 实现跨 trace 聚合：给定多个 trace，按 `span.name` 分组计算 P50/P95。对应 IMRaD Results "表1：各步骤延迟分布"的数据生成。
3. 实现 span 事件（events）：在 span 上记录离散事件（如"工具调用失败"），对应 OTel span events 语义。这是 Discussion "局限性"中"X% 的请求因工具失败重试"的数据来源。
4. TODO: 在 `practice.md` 的统计写作 drill 中，用 from-scratch Tracer 采集 30 个 `llm_call` span 的 duration，跑 t 检验对比两个模型的延迟差异，写 APA 格式结果。这是 notes.md "Results 数据说话"的端到端实现。
