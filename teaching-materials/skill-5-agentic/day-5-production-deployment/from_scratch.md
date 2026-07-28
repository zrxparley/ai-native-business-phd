# from_scratch.md · AI工程从零构建层 (v11.0)

> **单元**：技能5 Agentic系统工程 · Day 5 生产部署与运维
> **scratch 哲学**：不调 vLLM，手写连续批处理调度骨架，从 Little's Law 到 KV cache 页分配到 admit/decode/evict 循环直译到裸 Python。

## scratch_topic

本单元 from-scratch 主题：**手写简易 vLLM 连续批处理调度骨架**。对应 rohitg00 P17/04 vLLM Serving Internals + P17/13 LLM Observability。notes.md 用 LangSmith `@traceable` + tiktoken 做应用层可观测性与成本统计，本层把推理引擎内部拆到裸 Python：请求队列 + KV cache 页池 + admit/decode/evict 三阶段循环 + 页回收，让"连续批处理为什么比静态批处理快"不再是 vLLM 的黑箱魔法，而是可逐行审计的 35 行调度器。

## core_algorithm

vLLM 的核心创新是 **PagedAttention + 连续批处理**。传统静态批处理：等凑齐 batch_size 个请求或超时才一起前向，请求间长短不齐时短请求等长请求，GPU 空闲。连续批处理：每步动态重组 batch，已完成请求退出、新请求加入，KV cache 按页分配复用。

**Little's Law**（吞吐上界）：稳态系统 $L = \lambda W$，$L$ 为系统中平均请求数，$\lambda$ 为到达率，$W$ 为平均逗留时间。连续批处理降低 $W$（短请求不等长请求），故同 $\lambda$ 下 $L$ 更小（内存压力低），或同 $L$ 下 $\lambda$ 更大（吞吐高）。

**KV cache 内存模型**：单请求 KV cache 占用 $M = 2 \cdot n_{\text{layer}} \cdot s \cdot d \cdot b$（K+V 两份，$b$ 为 dtype 字节数）。批处理 $B$ 个请求、序列长 $s$：$M_{\text{batch}} = B \cdot M$。PagedAttention 把 KV cache 分成固定大小 page（如 16 token/page），按需分配，避免为短请求预分配全长 $s$ 的浪费。碎片率：

$$\text{frag} = 1 - \frac{\sum_i s_i}{\text{pages\_allocated} \cdot \text{page\_size}}$$

**调度目标**：每步选 subset $S_t \subseteq \text{queue}$ 最大化 $\sum_{i \in S_t} s_i$（吞吐）subject to $\sum_{i \in S_t} M_i \leq M_{\text{total}}$（内存约束）。这是背包问题的在线版。

**Prefill vs Decode**：LLM 推理分两阶段--prefill（处理 prompt，compute-bound）和 decode（逐 token 生成，memory-bound）。连续批处理在 decode 步插入新请求的 prefill，打散 compute/memory 峰值，提升 GPU 利用率。

## code_artifact

```python
import math
from dataclasses import dataclass, field

@dataclass
class Request:
    rid: int
    prompt_len: int
    max_new: int
    generated: int = 0
    done: bool = False
    kv_pages: list = field(default_factory=list)

class ContinuousBatchScheduler:
    def __init__(self, total_pages, page_size=16, max_batch=8):
        self.page_size = page_size
        self.max_batch = max_batch
        self.free_pages = list(range(total_pages))
        self.running = []
        self.queue = []

    def add(self, req):
        self.queue.append(req)

    def step(self):
        # admit: prefill new requests if pages and batch slots available
        while self.queue and len(self.running) < self.max_batch:
            r = self.queue[0]
            need = math.ceil(r.prompt_len / self.page_size)
            if len(self.free_pages) < need:
                break
            self.queue.pop(0)
            r.kv_pages = [self.free_pages.pop() for _ in range(need)]
            self.running.append(r)
        # decode: advance each running request one token
        for r in self.running:
            r.generated += 1
            if r.generated >= r.max_new:
                r.done = True
            elif self.free_pages:
                r.kv_pages.append(self.free_pages.pop())
        # evict finished, reclaim pages
        finished = [r for r in self.running if r.done]
        for r in finished:
            self.free_pages.extend(r.kv_pages)
            r.kv_pages = []
        self.running = [r for r in self.running if not r.done]
        return finished

if __name__ == "__main__":
    sched = ContinuousBatchScheduler(64, page_size=16, max_batch=4)
    for i in range(6):
        sched.add(Request(i, prompt_len=32, max_new=5))
    done = 0
    for _ in range(30):
        done += len(sched.step())
        if done == 6:
            break
    assert done == 6, "all complete"
    assert len(sched.running) == 0
    assert len(sched.free_pages) == 64, "all pages reclaimed"
```

**verification_property**: 所有请求在有限步内完成；free_pages 完全回收（无内存泄漏）；running 不超过 max_batch；每步 admit 受 KV cache 页约束（内存不足时排队等待）。

## connection_to_unit

1. **可观测对象 vs 可观测工具**：notes.md 用 LangSmith `@traceable` 追踪 Agent 调用链（应用层可观测性），from-scratch 版的 scheduler 是 vLLM 内部（推理引擎层）--两者是不同层。notes.md 讲"怎么看"，from-scratch 讲"被看的对象"（KV cache 页池、batch 组成、admit/decode 状态）。
2. **成本优化层次对比**：notes.md 的"成本优化三大策略"（token 管理 / 语义缓存 / 模型路由）是应用层减请求，from-scratch 的连续批处理是引擎层增吞吐--两者互补：应用层减 $\lambda$（到达率），引擎层减 $W$（逗留时间），Little's Law $L=\lambda W$ 把两者统一。
3. **token 计数对比**：notes.md 的 tiktoken 数 token 算成本（应用层），from-scratch 的 `prompt_len` 字段就是 token 数--scheduler 用它算 KV cache 页数 `need = ceil(prompt_len / page_size)`。这是"token 数如何影响内存"的代码体现：prompt 越长，prefill 需要的页越多，admit 越难。
4. **灾备降级对比**：notes.md 的"灾备降级"是应用层多级 fallback（主模型 -> 备用 -> 缓存），from-scratch 的 `if len(self.free_pages) < need: break` 是引擎层内存压力降级（请求排队等待页释放）--OOM 时真实 vLLM 会抢占低优先级请求，from-scratch 简化为等页可用。

## deep_dive_links

- [P17/04 vLLM Serving Internals - rohitg00](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/17-infrastructure-and-production/04-vllm-serving-internals/README.md) - vLLM 内部机制，PagedAttention + 连续批处理，本单元核心理论锚点
- [P17/13 LLM Observability - rohitg00](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/17-infrastructure-and-production/13-llm-observability/README.md) - LLM 可观测性设计，从 trace 到 SLO

## exercises

1. 在本单元 `starter.ipynb` TODO3（延迟监控分步计时）完成后，用 from-scratch scheduler 模拟"静态批处理 vs 连续批处理"两种策略，对比完成 6 请求的总步数。提示：静态批处理等凑齐 max_batch 才开始，连续批处理有请求即开始。
2. 实现 PagedAttention 的精确页管理：每 page 容纳 `page_size` 个 token，仅在 last_page 满时分配新页。对比与"每 token 一页"简化版的内存占用。对应 core_algorithm 的碎片率公式。
3. 实现抢占：当 `free_pages` 不足且新请求优先级更高时，evict 低优先级 running 请求（回滚其 KV cache 页）。对应 vLLM 的 preemption 机制。
4. TODO: 在 `practice.md` 的成本优化 drill 中，用 from-scratch scheduler 量化"prompt_len 对吞吐的影响"--固定 `total_pages`，变化 `prompt_len`，观察最大并发数。这是 notes.md "token 管理降本"的引擎层验证。
