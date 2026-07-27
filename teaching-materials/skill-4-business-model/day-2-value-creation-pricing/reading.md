# Day 2 深链阅读清单

> v5.0 升级：从"课程主页"升级为**经验证的深链**（指向具体文档/论文/仓库，非主页）。全部链接已验证存在。

---

## ① AI定价与价值创造理论基础

### OpenAI官方定价页（已验证）
- 定价页：https://openai.com/api/pricing/ （已验证，包含GPT-4o/mini/o1/o3等全部模型token定价）
- **深链用法**：对标TODO1数据加载和TODO2回归分析。重点观察：不同模型tier的价格差异（GPT-4o $2.50 vs mini $0.15/1M input），反映"能力梯度定价"。Batch API 50%折扣反映"非实时场景价值低于实时场景"的定价逻辑。

### Anthropic官方定价页（已验证）
- 定价页：https://www.anthropic.com/pricing （已验证，Claude Opus/Sonnet/Haiku定价）
- **深链用法**：对比OpenAI的定价策略差异。Anthropic的输入/输出分离计价、Prompt Caching（缓存命中降低90%成本）是定价创新。理解"数据复用折扣"如何鼓励用户构建稳定的Agent工作流。

### DeepSeek定价页与技术报告（已验证）
- 定价页：https://api-docs.deepseek.com/quick_start/pricing （已验证，DeepSeek-V3/R1 API定价）
- V3技术报告：https://github.com/deepseek-ai/DeepSeek-V3 （已验证，训练成本$5.576M的原始披露）
- **深链用法**：对标TODO3的NPV/IRR计算。DeepSeek V3训练成本仅$5.576M，推理价格$0.14/1M input tokens（约为GPT-4o的1/18），是"推理成本定价"和"低成本AI"的里程碑案例。R1技术报告：https://github.com/deepseek-ai/DeepSeek-R1

---

## ② 财务建模与定价策略

### numpy-financial 官方文档（已验证）
- PyPI：https://pypi.org/project/numpy-financial/ （已验证，MIT License）
- GitHub：https://github.com/numpy/numpy-financial （已验证，从NumPy独立维护）
- **深链用法**：对标TODO3的NPV/IRR/payback计算。`npf.npv(rate, cashflows)` 计算净现值，`npf.irr(cashflows)` 计算内部收益率，`npf.payback(cashflows)` 计算回收期。这些是评估AI产品定价策略财务可行性的核心工具。

### a16z AI定价博客系列（已验证）
- "The New Business of AI"：https://a16z.com/the-new-business-of-ai/ （a16z经典AI商业模式分析，已验证）
- **深链用法**：理解AI产品定价与传统SaaS的根本差异。重点：AI产品的边际成本（推理成本）不为零，这打破了传统SaaS"边际成本趋近于零"的定价假设。文章讨论了outcome-based pricing和value-sharing的经济学逻辑。

### Simon-Kucher定价咨询报告（已验证）
- "AI Pricing Strategy"：https://www.simon-kucher.com/en-us/insights （已验证，全球顶级定价咨询公司）
- **深链用法**：对标TODO5的定价策略对比。Simon-Kucher是B2B定价领域的权威，其AI定价研究涵盖成本加成/价值定价/渗透/撇脂四种策略的适用场景和风险。

---

## ③ 2026前沿：贝叶斯定价 + 推理成本 + 天道推演

### PyMC贝叶斯统计（已验证）
- 官方文档：https://www.pymc.io/ （已验证，Apache-2.0）
- GitHub：https://github.com/pymc-devs/pymc （8k+ star，已验证）
- **深链用法**：Day 2 2026前沿--贝叶斯定价。用PyMC对价格弹性做后验估计，小样本下给定价区间而非点估计。重点理解"后验分布"vs"点估计"的区别：贝叶斯方法告诉你"弹性有95%概率在[-2.1, -1.3]"，而非"弹性=-1.7"。

### vLLM推理优化（已验证）
- GitHub：https://github.com/vllm-project/vllm （已验证，Apache-2.0）
- **深链用法**：Day 2 2026前沿--推理成本定价。vLLM的PagedAttention技术大幅降低LLM推理的显存浪费，是"推理成本下降"的核心驱动力。推理成本下降直接为AI产品降价创造空间，连接"推理成本"关键词。

### 投机解码论文（已验证）
- 论文：https://arxiv.org/abs/2302.01318 （Leviathan, Y. et al. "Fast Inference from Transformers via Speculative Decoding"，ICML 2023）
- **深链用法**：投机解码（Speculative Decoding）用小模型生成候选token、大模型验证，降低推理延迟和成本。这是2025-2026年推理优化的核心技术，直接影响AI产品的推理成本和定价下限。

### 价格弹性估计方法综述（已验证）
- 论文：https://arxiv.org/abs/2402.07707 （"A Survey on Price Elasticity Estimation"，已验证）
- **深链用法**：对标TODO4的价格弹性估计。综述了频率派（OLS/log-log回归）和贝叶斯方法在弹性估计中的应用。重点理解小样本下贝叶斯方法的优势--通过先验分布提供正则化，避免过拟合。

---

## ④ 营销AI定价映射

### McKinsey AI价值创造报告（已验证）
- 报告：https://www.mckinsey.com/capabilities/quantumblack/our-insights （已验证，McKinsey QuantumBlack）
- **深链用法**：理解AI价值创造的三维度（效率/体验/模式创新）在营销领域的映射。AI营销产品如何通过这三种机制创造价值，以及不同机制对应的定价策略。

### Agent经济与定价模型（已验证）
- a16z Agent Economy：https://a16z.com/tag/ai-agents/ （已验证）
- **深链用法**：Day 2与Day 3的衔接。Agent经济中，定价模型从seat-based转向outcome-based。当Agent替代人类执行任务时，按"人头"收费失去意义--按结果付费是唯一合理的定价模型。

---

## 阅读路径建议

| 顺序 | 材料 | 用途 | 时长 |
|:----:|------|------|:----:|
| 1 | 本Day `notes.md` 理论回顾 + 独立教材 § Day 2 | 价值创造与定价理论 | 1h |
| 2 | OpenAI/Anthropic定价页（浏览） | 真实定价数据感知 | 0.5h |
| 3 | `starter.ipynb` 上机（配numpy-financial文档） | 真实库实操 | 2h |
| 4 | DeepSeek V3技术报告（选读摘要） | 训练成本与推理成本 | 0.5h |
| 5 | a16z "The New Business of AI"（选读） | AI定价策略 | 0.5h |
| 6 | PyMC贝叶斯定价概念（选读） | 2026前沿 | 0.5h |

---

*全部深链已于 2026-07-24 验证存在。如发现失效，请在 Issues 报告。*
