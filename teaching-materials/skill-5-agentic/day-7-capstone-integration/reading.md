# Day 7 深链阅读清单

> v5.0升级：从"课程主页"升级为**经验证的深链**（指向具体论文/文档/仓库，非主页）。全部链接已验证存在。Day 7聚焦DSR设计科学研究+可复现研究+端到端Capstone整合。

---

## ① DSR设计科学研究（Capstone方法论框架）

### Hevner et al. (2004) MIS Quarterly 经典（DSR七准则）
- 📄 JSTOR：https://www.jstor.org/stable/25148625
- **用法**：Day 7 DSR框架的理论来源。Hevner提出DSR七准则（artifact为研究贡献/问题相关性/设计评估/研究贡献/研究严谨性/设计即搜索/研究交流），是信息系统的核心研究范式。重点读 §2（Design Science vs Natural Science）和 §3（Seven Guidelines）。本Day的Capstone用DSR定位：你的Agent系统是一个可发表的artifact。

### Peffers et al. (2007) DSR六步方法论
- 📄 paper：https://desrist.org/desrist/files/peffers2007.pdf
- **用法**：把Hevner的七准则操作化为六步流程（问题识别→目标定义→设计开发→演示→评估→传播），是DSR的标准方法论模板。本Day TODO1直接用这六步定义Capstone的研究计划。重点读 §3（Methodology）的六步描述。

### Design Science Research in IS 参考书目
- 🌐 DESRIST社区：https://desrist.org/ （已验证，DSR研究社区，年度会议）
- **用法**：DSR领域的研究社区和年度会议，Capstone论文可投DESRIST会议（CCF-C级别，适合初学者）。

---

## ② 可复现研究（Reproducible Research）

### DoWhy 因果推断库（微软Research）
- 📦 GitHub：https://github.com/py-why/dowhy （已验证，微软Research维护，活跃开发）
- 📄 文档：https://py-why.github.io/dowhy/ （已验证，完整API文档）
- **深链用法**：
  - [CausalModel API](https://py-why.github.io/dowhy/v0.8/api.html)：对标 TODO3，用CausalModel定义因果图+识别+估计
  - [后门调整教程](https://py-why.github.io/dowhy/v0.8/example_notebooks/dowhy_estimation_methods.html)：对标 TODO3 的估计方法选择
  - [反驳检验](https://py-why.github.io/dowhy/v0.8/api.html#dowhy.causal_model.CausalModel.refute_estimate)：对标稳健性检验，是可复现研究的关键

### causaldata 真实数据集
- 📦 GitHub：https://github.com/NickCH-K/causaldata （已验证，NSW/LaLonde等真实数据集）
- 📦 PyPI：https://pypi.org/project/causaldata/ （已验证，MIT License）
- **深链用法**：对标 TODO2，`from causaldata import nsw` 加载真实RCT数据。NSW是LaLonde (1986) 使用的经典数据集，因果推断方法论的benchmark。

---

## ③ Agent层与评估层（端到端流水线）

### LangGraph 官方文档（Agent编排）
- 📦 GitHub：https://github.com/langchain-ai/langgraph （已验证，LangChain团队出品）
- 📄 文档：https://langchain-ai.github.io/langgraph/ （已验证，完整教程）
- **深链用法**：
  - [StateGraph Quickstart](https://langchain-ai.github.io/langgraph/tutorials/introduction/)：对标 TODO4，用StateGraph定义Agent工作流
  - [工具调用](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/)：对标 TODO4 的Agent工具调用

### ReAct 论文（Agent推理模式）
- 📄 arXiv 2210.03629：https://arxiv.org/abs/2210.03629
- **用法**：ReAct（Reasoning+Acting）是Agent的经典推理模式，LangGraph的Agent设计基于此。理解Thought-Action-Observation循环，对标TODO4的Agent轨迹设计。

### deepeval 评估框架（LLM-as-a-judge）
- 📦 GitHub：https://github.com/confident-ai/deepeval （已验证，17k★）
- 📄 文档：https://docs.confident-ai.com/ （已验证，301重定向至deepeval.com/docs/）
- **深链用法**：
  - [GEval（LLM-as-a-judge）](https://deepeval.com/docs/metrics-llm-evals)：对标 TODO5，用criteria模式让LLM自动评分Agent策略质量
  - [自定义BaseMetric](https://deepeval.com/docs/metrics-custom)：对标 TODO5，自定义策略评估指标

### LLM-as-a-judge 原始论文（NeurIPS 2023）
- 📄 arXiv 2306.05685：https://arxiv.org/abs/2306.05685
- **用法**：用LLM自动评估Agent输出质量的理论基础。重点读 §3（评估方法）和 §5（已知偏差）。注意：LLM-as-a-judge是辅助评估，不能替代真实A/B测试。

---

## ④ 学术发表（Capstone传播）

### IMRaD 论文写作指南
- 📄 arXiv AgentBench（论文结构参考）：https://arxiv.org/abs/2308.03688
- **用法**：AgentBench论文是Agent系统评估的标杆论文结构参考。看它如何组织Introduction（动机+贡献）、Methods（系统设计+评估方法）、Results（实验结果）、Discussion（局限+未来）。对标 TODO6 的论文草稿结构。

### Creswell《Research Design》（混合方法研究）
- 📖 书籍：Creswell, J. W., & Plano Clark, V. L. (2018). *Designing and conducting mixed methods research* (3rd ed.). SAGE.
- **用法**：DSR评估阶段采用混合方法（定量A/B测试+定性访谈）。Creswell是混合方法研究的权威参考。对标论文Methods部分的评估方法设计。

---

## 阅读路径建议

| 顺序 | 材料 | 用途 | 时长 |
|:----:|------|------|:----:|
| 1 | 本Day `notes.md` 理论回顾 + 独立教材 §3.7.1-3.7.4 | DSR框架+Capstone整合 | 1h |
| 2 | Hevner 2004 §2-3（选读） | DSR七准则 | 0.5h |
| 3 | Peffers 2007 §3（选读） | DSR六步方法论 | 0.5h |
| 4 | `starter.ipynb` 上机（配DoWhy+LangGraph+deepeval文档） | 端到端Capstone实操 | 2h |
| 5 | ReAct论文 §3（选读） | Agent推理模式 | 0.5h |
| 6 | LLM-as-a-judge论文 §3, §5（选读） | 评估方法论 | 0.5h |

---

*全部深链已于 2026-07-24 验证存在。如发现失效，请在 Issues 报告。*
