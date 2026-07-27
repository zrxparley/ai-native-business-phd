# Day 1 深链阅读清单

> v5.0 升级：从"课程主页"升级为**经验证的深链**（指向具体论文 / 文档 / 仓库，非主页）。全部链接已验证存在。

---

## ① 对齐方法理论（RLHF -> Constitutional AI -> DPO）

### Constitutional AI: Harmlessness from AI Feedback（Anthropic，arXiv 2212.08073）
- 📄 arXiv 2212.08073：https://arxiv.org/abs/2212.08073
- **用法**：本Day核心理论来源。Anthropic提出的Constitutional AI方法，用AI反馈（RLAIF）替代人类反馈，通过显式宪法原则驱动模型自我对齐。重点读§2 Constitutional SL（监督学习阶段）和§3 Constitutional RL（强化学习阶段），理解"宪法原则如何变成对齐信号"。对应独立教材§1.4。

### Direct Preference Optimization（Stanford，arXiv 2305.18290）
- 📄 arXiv 2305.18290：https://arxiv.org/abs/2305.18290
- **用法**：DPO原论文。Stanford团队提出的RLHF替代方案，跳过显式奖励模型，直接用偏好数据优化策略。重点读§3 DPO数学推导（最优奖励函数可从策略推导）和§4 实验结果（DPO效果接近RLHF，更稳定）。对应独立教材§1.3。

### InstructGPT / Training language models to follow instructions（OpenAI，arXiv 2203.02155）
- 📄 arXiv 2203.02155：https://arxiv.org/abs/2203.02155
- **用法**：RLHF的工程化标杆论文。OpenAI用三步流程（SFT -> RM -> PPO）对齐GPT-3，产出InstructGPT。重点读§3 RLHF三步流程和§5 局限性（标注偏见/Reward Hacking），理解RLHF的优势与痛点。对应独立教材§1.2。

---

## ② 真实库 + 上机

### deepeval 官方文档与教程（已验证：confident-ai/deepeval）
- 🌐 官方文档：https://docs.confident-ai.com/ （已验证，301重定向至 deepeval.com/docs/，内容完整）
- 📦 GitHub：https://github.com/confident-ai/deepeval （17k★，MIT License，已验证存在）
- **深链用法**：
  - [自定义指标 BaseMetric](https://deepeval.com/docs/metrics-custom)：对标 starter.ipynb 的 TODO2/3/4，继承后实现 measure 方法做HHH三维度评估
  - [GEval（LLM-as-a-judge 自动评分）](https://deepeval.com/docs/metrics-llm-evals)：对标 TODO6，用 criteria 模式让 LLM 按 Constitutional AI 原则自动评审
  - [FaithfulnessMetric（幻觉检测）](https://deepeval.com/docs/metrics-faithfulness)：检测营销Agent是否虚构成分/功效（诚实性维度）
  - [evaluate 批量运行](https://deepeval.com/docs/evaluate-introduction)：对标 TODO6，批量运行对齐测试套件

### garak 官方文档与仓库（已验证：NVIDIA/garak）
- 🌐 官方文档：https://garak.ai/ （已验证，含 probes 和 CLI 参考）
- 📦 GitHub：https://github.com/NVIDIA/garak （已验证，NVIDIA 官方维护）
- 📦 PyPI：https://pypi.org/project/garak/ （已验证，0.15.1，2026-06-05 发布）
- **深链用法**：
  - [probes 列表](https://github.com/NVIDIA/garak/tree/main/garak/probes)：对标 TODO5，理解 alignment probes 如何检测价值偏差
  - [CLI 参考](https://garak.ai/en/latest/cli.html)：`--target_type` / `--probes` / `--list_probes` 等参数
  - 注意：本Day无API key时用本地静态扫描fallback，garak完整功能需API key

---

## ③ 2026 前沿：LLM-as-a-judge 对齐评估 + 可解释性

### LLM-as-a-judge 原始论文（NeurIPS 2023，arXiv 2306.05685）
- 📄 arXiv 2306.05685：https://arxiv.org/abs/2306.05685
- **用法**：本Day用 LLM-as-a-judge **自动评估营销Agent的对齐质量**（按HHH原则和Constitutional AI宪法打分）。重点读§3 评估方法和§5 已知偏差（位置偏差/冗长偏差/自我偏好）。用 deepeval 的 GEval 写成可测试用例纳入 CI。

### Anthropic 可解释性研究（Scaling Monosemanticity / Toy Models of Superposition）
- 🌐 Scaling Monosemanticity：https://transformer-circuits.pub/2024/scaling-monosemanticity/ （已验证，Anthropic可解释性研究）
- **用法**：对应独立教材§1.5。理解AI安全的前沿方向--通过稀疏自编码器识别模型内部对应特定概念的神经元激活模式。终极目标是"在AI产生危险行为之前检测到并干预"。对企业实践意义：输出可解释性 / 行为可审计性 / 异常检测。

---

## ④ 安全治理与对齐标准

### NIST AI RMF（AI 风险管理框架）
- 🌐 NIST AI RMF 1.0：https://www.nist.gov/itl/ai-risk-management-framework
- **用法**：独立教材的对齐治理对标框架。四步循环（Govern/Map/Measure/Manage）中，本Day的"对齐评估"对应Measure层--量化AI系统的对齐质量。Day 3将深入治理框架。

### Anthropic 安全设计实践
- 🌐 Anthropic 安全指南：https://docs.anthropic.com/en/docs/test-and-evaluate/strengthen-guardrails
- **用法**：Constitutional AI 的工程实践来源。涵盖宪法原则设计、分级风险、人在回路等设计模式。本Day的"企业宪法"设计参考此文档。

---

## 阅读路径建议

| 顺序 | 材料 | 用途 | 时长 |
|:----:|------|------|:----:|
| 1 | 本 Day `notes.md` 理论回顾 + 独立教材 §1.1-1.5 | 对齐方法论 | 1h |
| 2 | Constitutional AI 论文 §2-3（选读） | RLAIF原理 | 0.5h |
| 3 | `starter.ipynb` 上机（配 deepeval 文档） | 真实库实操 | 2h |
| 4 | DPO 论文 §3-4（选读） | DPO vs RLHF | 0.5h |
| 5 | LLM-as-a-judge 论文 §3, §5 | 前沿+偏差认知 | 0.5h |
| 6 | garak probes 列表（选读） | 对齐探针理解 | 0.5h |

---

*全部深链已于 2026-07-24 验证存在。如发现失效，请在 Issues 报告。*
