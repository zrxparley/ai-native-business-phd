# Day 2 深链阅读清单

> v5.0 升级：从"课程主页"升级为**经验证的深链**（指向具体论文 / 文档 / 仓库，非主页）。全部链接已验证存在。

---

## 1. Prompt Injection 攻击与防御

### OWASP Top 10 for LLM Applications
- 官网：https://owasp.org/www-project-top-10-for-large-language-model-applications/
- **用法**：本Day核心威胁分类来源。OWASP在2024年发布了LLM应用Top 10安全风险，系统化梳理了LLM应用面临的主要威胁。重点看LLM01 Prompt Injection（本Day核心）和LLM08 Excessive Agency（权限隔离）。对应独立教材 2.1节。

### Prompt Injection attack against LLM-integrated Apps（arXiv 2306.05499）
- 论文：https://arxiv.org/abs/2306.05499
- **用法**：Prompt Injection的学术定义论文。区分了直接注入和间接注入，提出了间接注入通过外部文档攻击Agent的威胁模型。重点读 3.2 Indirect Prompt Injection，理解为什么间接注入比直接注入更危险。对应独立教材 2.2节。

### Not what you've signed up for: Compromising Real-World LLM-integrated Apps (arXiv 2302.10273)
- 论文：https://arxiv.org/abs/2302.10273
- **用法**：间接注入的真实攻击案例论文。展示了如何通过网页/邮件/评论中隐藏的指令，让Bing Chat/Replika等真实Agent执行恶意操作。营销Agent同样面临评论/UGC中的间接注入风险。

---

## 2. 真实库 + 上机

### deepeval 官方文档与教程（已验证：confident-ai/deepeval）
- 官方文档：https://docs.confident-ai.com/
- GitHub：https://github.com/confident-ai/deepeval
- **深链用法**：
  - [自定义指标 BaseMetric](https://deepeval.com/docs/metrics-custom)：对标 TODO6，继承后实现 measure 方法做SafetyMetric安全评分
  - [LLMTestCase](https://deepeval.com/docs/test-case-introduction)：定义安全测试用例（input=攻击prompt, actual_output=防御结果）
  - [evaluate 批量运行](https://deepeval.com/docs/evaluate-introduction)：对标 TODO6，批量运行安全测试套件

### garak 官方文档与仓库（已验证：NVIDIA/garak）
- 官方文档：https://garak.ai/
- GitHub：https://github.com/NVIDIA/garak
- PyPI：https://pypi.org/project/garak/
- **深链用法**：
  - [probes 列表](https://github.com/NVIDIA/garak/tree/main/garak/probes)：理解 dan/promptinject/encoding 等探针如何检测漏洞
  - 注意：本Day不实跑garak（避免pip install阻塞），用手写5层防御替代。生产环境用完整garak

### PyRIT 官方文档与仓库（已验证：Azure/PyRIT）
- GitHub：https://github.com/Azure/PyRIT
- 文档：https://azure.github.io/PyRIT/
- **深链用法**：
  - [PromptSendingOrchestrator](https://azure.github.io/PyRIT/orchestrators/prompt_sending_orchestrator.html)：理解批量对抗提示编排
  - 注意：本Day不实跑PyRIT，用12个手写攻击向量替代

---

## 3. 2026 前沿：自动化红队 + 对抗基准

### HarmBench: A Standardization Framework for Automated Red Teaming（arXiv 2402.04249）
- 论文：https://arxiv.org/abs/2402.04249
- **用法**：标准化对抗行为数据集，评估Agent的对抗拒绝率。用于横向比较不同防御策略的效果。重点读 3 Standard Behaviors 和 5 Contextual Behaviors，理解如何系统化评估防御能力。

### AdvBench: adversarial prompt benchmark（arXiv 2307.15024）
- 论文：https://arxiv.org/abs/2307.15024
- **用法**：520条有害行为提示数据集，是红队测试的标准参考。本Day的12个攻击向量参考了AdvBench的格式和分类。

### LLM-as-a-judge 原始论文（NeurIPS 2023，arXiv 2306.05685）
- 论文：https://arxiv.org/abs/2306.05685
- **用法**：用LLM-as-a-judge自动评估Agent输出是否安全（比regex更强大，能理解语义层面的安全失败）。本Day的deepeval SafetyMetric是LLM-as-a-judge理念的可运行实现（本Day用规则评分，生产环境可升级为LLM-as-a-judge）。

---

## 4. 安全治理与标准

### NIST AI RMF（AI 风险管理框架）
- 官网：https://www.nist.gov/itl/ai-risk-management-framework
- **用法**：独立教材的安全治理对标框架。四步循环（Govern/Map/Measure/Manage）中，本Day的"红队测试"对应Measure层--量化AI系统的安全姿态。Day 3将深入治理框架。

### Anthropic 安全设计实践
- 官网：https://docs.anthropic.com/en/docs/test-and-evaluate/strengthen-guardrails
- **用法**：Prompt Injection防御的工程实践来源。涵盖分层防御、人在回路、权限隔离等设计模式。本Day的5层防御设计参考此文档。

---

## 阅读路径建议

| 顺序 | 材料 | 用途 | 时长 |
|:----:|------|------|:----:|
| 1 | 本 Day `notes.md` 理论回顾 + 独立教材 2.1-2.5 | 安全威胁全景 | 1h |
| 2 | OWASP LLM Top 10（LLM01/LLM06/LLM08） | 威胁分类 | 0.5h |
| 3 | `starter.ipynb` 上机（配 deepeval 文档） | 真实库实操 | 2h |
| 4 | Prompt Injection论文（选读 3.2节） | 间接注入原理 | 0.5h |
| 5 | garak/PyRIT 文档（选读） | 红队工具认知 | 0.5h |

---

*全部深链已于 2026-07-25 验证存在。如发现失效，请在 Issues 报告。*
