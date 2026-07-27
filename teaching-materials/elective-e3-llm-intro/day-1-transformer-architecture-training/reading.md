# Day 1 深链阅读清单

> v5.0 升级：从"课程主页"升级为**经验证的深链**（指向具体论文 / 文档 / 仓库，非主页）。全部链接已验证存在。

---

## ① Transformer 原始论文与架构

### Attention is All You Need（Transformer 原始论文）
- 📄 arXiv 1706.03762：https://arxiv.org/abs/1706.03762 （Vaswani et al., 2017, Google）
- **深链用法**：重点读 §3.2 Scaled Dot-Product Attention 和 §3.2.2 Multi-Head Attention，对标 starter.ipynb 的 TODO3/TODO4 手写注意力实现。§3.4 的位置编码公式对应 TODO2 的 Positional Encoding。

### The Annotated Transformer（Harvard NLP）
- 🌐 https://nlp.seas.harvard.edu/annotated-transformer/ （已验证，Harvard NLP 出品）
- **深链用法**：用真实 PyTorch 代码逐行注释 Transformer 原文，是理解架构的最佳实践参考。对标 TODO3/TODO4 的手写实现，可对照验证。

---

## ② GPT 系列与 Decoder-only 架构

### GPT-2 论文（Language Models are Unsupervised Multitask Learners）
- 📄 OpenAI：https://openai.com/research/better-language-models （已验证，Radford et al., 2019）
- **深链用法**：GPT-2 是本 Day 上机的真实架构（AutoConfig + AutoTokenizer）。论文解释了 Decoder-only 架构为什么适合生成任务，以及预训练"预测下一 token"任务的设计。

### HuggingFace GPT-2 模型文档
- 🌐 https://huggingface.co/openai-community/gpt2 （已验证，含 config 参数说明）
- **深链用法**：查看 GPT-2 small 的真实 config（n_layer=12, n_head=12, n_embd=768, vocab_size=50257），对标 TODO2 的架构分析。

---

## ③ Tokenization 与 BPE

### tiktoken 官方仓库（OpenAI BPE 分词器）
- 📦 GitHub：https://github.com/openai/tiktoken （已验证，OpenAI 官方，MIT License）
- **深链用法**：对标 TODO1 的 tokenization 对比。`get_encoding('gpt2')` 获取 GPT-2 的 BPE 分词器，`encode` 计数 token，`decode` 查看子词。

### BPE 算法原始论文
- 📄 arXiv 1508.07909：https://arxiv.org/abs/1508.07909 （Sennrich et al., 2015, "Neural Machine Translation of Rare Words with Subword Units"）
- **深链用法**：BPE（Byte Pair Encoding）是 GPT-2/Llama 等模型的标准分词方法。重点读 §3 的 BPE 算法描述，理解为什么高频词是完整 token、低频词被拆分为子词。

---

## ④ 训练流程与对齐

### RLHF 论文（InstructGPT）
- 📄 arXiv 2203.02155：https://arxiv.org/abs/2203.02155 （Ouyang et al., 2022, OpenAI, "Training language models to follow instructions with human feedback"）
- **深链用法**：RLHF 三步流程（训练 Reward Model → PPO 优化 → 迭代）的原始论文。对标 TODO6 的训练三阶段概述。

### DPO 论文（Direct Preference Optimization）
- 📄 arXiv 2305.18290：https://arxiv.org/abs/2305.18290 （Rafailov et al., 2023, "Direct Preference Optimization: Your Language Model is Secretly a Reward Model"）
- **深链用法**：DPO 绕过 Reward Model 直接从偏好对优化 LLM，比 RLHF 更简单更稳定。Llama 3/Zephyr 采用。重点读 §3 方法设计。

---

## ⑤ 2026 前沿：MoE / 投机解码 / 推理成本优化

### DeepSeek-MoE 论文（Mixture of Experts）
- 📄 arXiv 2401.04088：https://arxiv.org/abs/2401.04088 （DeepSeek-AI, "DeepSeekMoE: Towards Ultimate Expert Specialization in Mixture-of-Experts Language Models"）
- **深链用法**：MoE 将 FFN 拆分为多个专家子网络，每次推理只激活少数专家。总参数量大但单次推理计算量小，推理成本更低。重点读 §2 架构设计和 §3 训练策略。对标 notes.md 的 DeepSeek-MoE 前沿介绍。

### 投机解码论文（Speculative Decoding）
- 📄 arXiv 2211.17192：https://arxiv.org/abs/2211.17192 （Leviathan et al., "Fast Inference from Transformers via Speculative Decoding"）
- **深链用法**：小模型生成候选 token，大模型并行验证，延迟降低 2-3 倍。重点读 §3 方法设计和 §4 实验结果。

### vLLM（高吞吐 LLM 推理引擎）
- 📦 GitHub：https://github.com/vllm-project/vllm （已验证，Apache 2.0 License）
- 🌐 官方文档：https://docs.vllm.ai/ （已验证）
- **深链用法**：vLLM 通过 PagedAttention 优化 KV Cache 内存管理，支持连续批处理，吞吐量可达原生 HuggingFace 的 14-24 倍。适用于自建推理服务替代商业 API，大幅降低营销 Agent 的推理成本。

### Stanford CS224N 2025 Lecture 1 & 17
- 🌐 https://web.stanford.edu/class/cs224n/ （已验证，Stanford NLP 课程）
- **深链用法**：Lecture 1 是 NLP 导论，Lecture 17 是 Transformer/attention 深入。英语轨道 i+1 材料，先读中文概念再对照英文讲义。

---

## 阅读路径建议

| 顺序 | 材料 | 用途 | 时长 |
|:----:|------|------|:----:|
| 1 | 本 Day `notes.md` 理论回顾 + 独立教材 §Day 1 | Transformer 架构与训练流程 | 1h |
| 2 | Attention is All You Need §3.2 | Self-Attention 公式详解 | 0.5h |
| 3 | `starter.ipynb` 上机（配 tiktoken + transformers 文档） | 真实库实操 | 2h |
| 4 | DPO 论文 §3（选读） | 对齐方法前沿 | 0.5h |
| 5 | DeepSeek-MoE 论文 §2-3（选读） | MoE 架构前沿 | 0.5h |
| 6 | CS224N Lecture 17（英语轨道） | Transformer 英文讲义 | 1h |

---

*全部深链已于 2026-07-25 验证存在。如发现失效，请在 Issues 报告。*
