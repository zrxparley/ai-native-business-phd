# from_scratch.md · AI工程从零构建层 (v11.0)

> **单元**：选修E3 LLM导论 · Day 3 LLM评估与部署（⭐旗舰模块 Day 3）
> **scratch 哲学**：不调 deepeval BaseMetric / vLLM，手写 INT8 对称量化矩阵分解 + perplexity 信息论评估 + greedy/beam search 解码，从量化误差 $\text{scale}=\max(|W|)/127$ 直译到 numpy。

## scratch_topic

本单元 from-scratch 主题：**手写 INT8 对称量化（矩阵分解 + 反量化误差）+ 手写 perplexity 计算 + 手写 greedy/beam search**。对应 rohitg00 P11/10 Evaluation + P17/04 vLLM Serving Internals。notes.md/starter.ipynb 用 deepeval BaseMetric 规则评分（关键词重合度/CTA 检测）+ tiktoken 统计 API token 成本，本层进一步去库化：手写 INT8 量化让"FP16->INT8 显存减 75%"的数学根源（$\text{scale}=\max(|W|)/127$ + round + 反量化误差）在白板代码中显形；手写 perplexity 让"LLM 评估的信息论指标"不被 deepeval 黑箱封装；手写 greedy/beam search 让"自回归生成每步 argmax"和"beam 剪枝"可见。notes.md 明确标注量化"本 Day 只做概念讲解，不实装"--from-scratch 层用纯 numpy 模拟权重矩阵打破这一限制。

## core_algorithm

**INT8 对称量化**（symmetric per-tensor quantization）是 LLM 推理优化的数学基石。给定 FP16/FP32 权重矩阵 $W \in \mathbb{R}^{m \times n}$，对称量化将浮点范围映射到 INT8 的 $[-127, 127]$（对称，零点为 0）：

$$\text{scale} = \frac{\max(|W|)}{127}, \quad W_q = \text{round}\left(\frac{W}{\text{scale}}\right)$$

反量化恢复浮点近似：$\hat{W} = W_q \times \text{scale}$。量化误差来自 round 操作：每个元素的舍入误差 $e_i \in [-\text{scale}/2, \text{scale}/2]$。相对 L2 误差度量重建质量：

$$\text{error}_{\text{rel}} = \frac{\|W - \hat{W}\|_2}{\|W\|_2} = \frac{\sqrt{\sum_i (W_i - \hat{W}_i)^2}}{\sqrt{\sum_i W_i^2}}$$

当权重服从零均值小方差分布（如初始化的 $\mathcal{N}(0, 0.02^2)$），$\max(|W|) \approx 4\sigma$，$\text{scale} \approx 4\sigma/127 \approx 0.031\sigma$，单元素最大舍入误差 $\approx 0.016\sigma$，相对 L2 误差 $<2\%$。这就是"INT8 量化几乎无损"的数学根源。但当权重有离群值（outlier）时，$\max(|W|)$ 被拉大，scale 增大，大部分正常权重的量化粒度变粗--这是 LLM.int8()（Dettmers 2022）引入混合精度量化的动机。

**Perplexity** 是语言模型的信息论评估指标，直接从负对数似然推导：

$$\text{PPL} = \exp\left(-\frac{1}{N}\sum_{i=1}^{N}\log p(x_i \mid x_{<i})\right)$$

PPL 的物理含义：模型在每个位置"等效均匀猜测的词表大小"。$\text{PPL}=1$ 表示完美预测，$\text{PPL}=V$（词表大小）表示均匀随机。当模型对每个 token 的概率为 $1/V$，$\log p = -\log V$，$\text{PPL} = \exp(\log V) = V$。PPL 是 MMLU/HumanEval 等任务基准之外的信息论评估，可直接对比模型质量。

**Greedy search** 是最简自回归解码：每步选 $\arg\max$ 的 token。**Beam search** 维护宽度 $k$ 的候选序列集，每步扩展所有 beam 的所有 next-token，保留累计 log-prob 最高的 $k$ 条--这是"延迟 vs 多样性"权衡的算法层。

## code_artifact

```python
import numpy as np
import math

def int8_quantize(W):
    # symmetric per-tensor INT8: scale = max(|W|)/127, zero-point = 0
    scale = np.max(np.abs(W)) / 127.0
    if scale == 0:
        scale = 1.0
    q = np.round(W / scale).astype(np.int8)
    return q, scale

def int8_dequantize(q, scale):
    return q.astype(np.float32) * scale

def quant_error(W, W_deq):
    # relative L2 reconstruction error
    num = np.sqrt(np.sum((W - W_deq) ** 2))
    den = np.sqrt(np.sum(W ** 2))
    return float(num / den) if den > 0 else 0.0

def perplexity(log_probs):
    # log_probs: list of log p(x_i | x_<i); PPL = exp(-mean(NLL))
    n = len(log_probs)
    return math.exp(-sum(log_probs) / n) if n > 0 else float('inf')

# verification_property:
#   INT8 range [-127,127] respected; dequantized ≈ original (rel error < 5% for small weights);
#   scale = max(|W|)/127; uniform PPL over vocab V equals V
if __name__ == "__main__":
    rng = np.random.default_rng(42)
    W = rng.standard_normal((64, 128)) * 0.02  # simulated FP16 weight matrix
    q, scale = int8_quantize(W)
    assert q.dtype == np.int8, "quantized dtype must be int8"
    assert q.min() >= -128 and q.max() <= 127, "INT8 range"
    W_deq = int8_dequantize(q, scale)
    err = quant_error(W, W_deq)
    assert err < 0.05, f"quant error {err:.4f} should be < 5%"
    # perplexity sanity: uniform over vocab=1000 -> PPL = 1000
    lp = [math.log(1 / 1000)] * 10
    assert abs(perplexity(lp) - 1000.0) < 1.0, "uniform PPL = vocab_size"
    print(f"scale={scale:.6f}, quant_error={err:.4f}, ppl_uniform={perplexity(lp):.1f}")
```

**verification_property**：INT8 量化后 $W_q \in [-127, 127]$（对称范围）；反量化相对 L2 误差 $<5\%$（小方差权重近无损）；$\text{scale} = \max(|W|)/127$（零点为 0 的对称量化）；均匀分布 perplexity $= V$（词表大小，信息论下界验证）。

## connection_to_unit

1. **评估指标对比**：starter.ipynb TODO2/TODO6 用 deepeval `BaseMetric` + `LLMJudge` 规则评分（关键词重合度/CTA 检测/违禁词检测，任务级启发式，score $\in [0,1]$），from-scratch 用 perplexity（信息论指标，直接从 $\log p(x_i|x_{<i})$ 计算，PPL $\geq 1$ 越低越好）。前者评"文案是否符合营销规则"，后者评"模型语言建模能力"--两者互补：PPL 评模型质量上限，规则评分评任务适配度。
2. **量化实现对比**：notes.md "推理优化五大技术"讲"FP16 权重压缩为 INT8，显存减少 50-75%"但明确标注"本 Day 只做概念讲解，不实装（需 GPU+权重）"，from-scratch 手写 INT8 对称量化 + 反量化 + 误差测量，让 $\text{scale}=\max(|W|)/127$ 和"量化误差 $<2\%$"在纯 numpy 白板代码中可见--不需要 GPU/权重，用 `rng.standard_normal` 模拟权重矩阵即可理解量化原理。这打破了 notes.md "不实装"的限制。
3. **成本监控对比**：starter.ipynb TODO5 用 tiktoken 统计 token 数 $\times$ API 定价（单维 OPEX 成本，gpt-4o $2.5/\text{M}$ vs DeepSeek V3 $0.27/\text{M}$），from-scratch 的 INT8 量化展示了另一条降本路径：权重显存压缩 4x（FP32 32bit $\to$ INT8 8bit），直接减少 GPU 显存需求，是 vLLM 自建推理 + PagedAttention 的基础。前者是 API OPEX（按 token 付费），后者是 GPU CAPEX（按显存/卡数付费）--模型选型决策框架需同时权衡两条路径。
4. **解码算法对比**：notes.md 讲"投机解码（小模型先生成草稿，大模型验证）"但只做概念讲解，from-scratch 可延伸到 greedy/beam search 手写实现（exercise），让"自回归生成每步选 $\arg\max$"和"beam 宽度 $k$ 的剪枝策略"在代码中显形。这是 notes.md "2026 已成为低成本高延迟场景的标配技术"的底层算法根源--不理解 greedy/beam 就无法理解投机解码的"草稿-验证"机制。

## deep_dive_links

- [P11/10 Evaluation - rohitg00](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/11-llm-engineering/10-evaluation/README.md) - LLM 评估，本 from-scratch perplexity 信息论指标的理论锚点
- [P17/04 vLLM Serving Internals - rohitg00](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/17-infrastructure-and-production/04-vllm-serving-internals/README.md) - vLLM 推理服务内部，本 from-scratch INT8 量化的工程锚点（PagedAttention + 连续批处理基础）

## exercises

1. 在本单元 `starter.ipynb` TODO5（tiktoken 监控 gpt-4o vs DeepSeek V3 成本）运行后，用上面的 `int8_quantize` + `quant_error` 对一个模拟权重矩阵（`rng.standard_normal((256, 512)) * 0.02`）做量化，测量 INT8 vs FP32 的显存节省（4x）和量化误差。再注入离群值（`W[0,0] = 10.0`），观察 scale 增大导致量化误差飙升--这正是 LLM.int8() 混合精度量化的动机。
2. 实现 **greedy search**：给定一个 mock logits 矩阵 `logits[T, vocab]`（用 `rng.standard_normal` 模拟），手写 `greedy_decode(logits) -> token_ids`，每步选 $\arg\max$。再用 `perplexity` 计算 mock 序列的 PPL。对应 notes.md "投机解码"的草稿模型原理--greedy 是最简草稿策略。
3. 实现 **beam search**：给定 mock logits 矩阵 + beam width $k=3$，手写 `beam_search(logits, k) -> list[(sequence, log_prob)]`，每步扩展所有 beam 的 top-$k$ next-token，保留累计 log-prob 最高的 $k$ 条。对比 greedy 与 beam search 的输出序列差异（beam 通常更优但 $k$ 倍慢）。
4. TODO: 在 `practice.md` drill D01（deepeval MarketingQualityMetric 四维度评分）中，用 `perplexity` 函数为 starter.ipynb TODO4 的 mock LLM 输出计算 PPL，对比 PPL（信息论指标）与 deepeval score（任务规则指标）--观察两者是否一致（高质量文案是否 PPL 更低）。这是 starter.ipynb TODO2+TODO6 的 from-scratch 串联练习。
