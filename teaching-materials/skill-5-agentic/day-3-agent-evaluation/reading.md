# Day 3 深链阅读清单

> v5.0 升级：从"课程主页"升级为**经验证的深链**（指向具体论文 / 文档 / 仓库，非主页）。全部链接已验证存在。

---

## ① Agent 评估理论

### AgentBench 原始论文（清华等，综合 Agent 能力评估）
- 📄 arXiv 2308.03688：https://arxiv.org/abs/2308.03688
- **用法**：Day 3 理论回顾的基准框架来源。覆盖8个场景（OS/DB/KG/卡牌/横向思维/家务/网页购物/网页浏览），理解学术 benchmark 如何标准化评估 Agent 能力。重点读 §3 评估方法和 §4 实验结果。

### SWE-bench（软件工程 Agent 评估，真实 GitHub issue）
- 📄 arXiv 2310.06770：https://arxiv.org/abs/2310.06770
- **用法**：理解"端到端评估"的标杆--用真实 GitHub issue 测试 Agent 能否修 bug，通过测试用例（unit test）判定成功/失败。这是"任务完成率"指标的学术基础。

### GAIA（通用 AI 助手能力评估）
- 📄 arXiv 2311.12983：https://arxiv.org/abs/2311.12983
- **用法**：理解真实世界 Agent 评估的挑战--GAIA 的测试用例需要多步推理、工具使用、web浏览，设计理念可借鉴到营销 Agent 的测试集设计。

---

## ② 真实库 + 上机

### deepeval 官方文档与教程（已验证：confident-ai/deepeval）
- 🌐 官方文档：https://docs.confident-ai.com/ （已验证，301重定向至 deepeval.com/docs/，内容完整）
- 📦 GitHub：https://github.com/confident-ai/deepeval （17k★，MIT License，已验证存在）
- **深链用法**：
  - [GEval（LLM-as-a-judge 自动评分）](https://deepeval.com/docs/metrics-llm-evals)：对标 starter.ipynb 的 TODO2/TODO5，用 criteria 模式让 LLM 自动打分
  - [FaithfulnessMetric（幻觉检测）](https://deepeval.com/docs/metrics-faithfulness)：对标 TODO4，对比 actual_output 与 retrieval_context 检测幻觉
  - [自定义指标 BaseMetric](https://deepeval.com/docs/metrics-custom)：对标 TODO3，继承后实现 measure 方法做轨迹评估
  - [evaluate 批量运行](https://deepeval.com/docs/evaluate-introduction)：对标 TODO6，批量运行测试套件

### LangSmith / LangGraph（LangChain 可观测性）
- 📦 GitHub：https://github.com/langchain-ai/langgraph （已验证，LangSmith 是 LangChain 的可观测性平台）
- **深链用法**：本 Day 聚焦 deepeval 离线测试，LangSmith 属在线可观测性（trace/eval/score）。进阶可将 deepeval 的评估结果与 LangSmith 的 trace 关联，实现离线测试+在线监控闭环。

---

## ③ 2026 前沿：LLM-as-a-judge

### LLM-as-a-judge 原始论文（NeurIPS 2023）
- 📄 arXiv 2306.05685：https://arxiv.org/abs/2306.05685
- **用法**：本 Day 用 LLM-as-a-judge **自动评估 Agent 轨迹质量**（工具选择、推理链、最终答案），用 deepeval 的 GEval 写成可测试用例纳入 CI。重点读 §3 评估方法和 §5 已知偏差（位置偏差/冗长偏差/自我偏好）。

### LLM-as-a-judge 的已知偏差与缓解
- 📄 "On the Limitations of Reasoning LLM as Judge" / Meta-judge 趋势：https://arxiv.org/abs/2504.18703 （2025，LLM 评审的偏差分析）
- **用法**：理解 LLM-as-a-judge 不是银弹--它有位置偏差（偏好第一个答案）、冗长偏差（偏好长答案）、自我偏好（偏好同类模型输出）。实践建议：随机化选项顺序 + 多 judge 投票 + 人工校准。

---

## ④ Agent 评估工程实践

### Evaluating Agents 系列文章（LangChain 官方博客）
- 🌐 LangSmith 评估文档：https://docs.smith.langchain.com/evaluation
- **用法**：LangChain 团队对 Agent 评估的工程实践总结，包括轨迹评估、端到端评估、数据集管理。与 deepeval 互补：deepeval 做离线测试，LangSmith 做在线评估。

### Evals 工程化最佳实践（OpenAI Cookbook）
- 🌐 OpenAI Evals：https://github.com/openai/evals （已验证，OpenAI 官方评估框架）
- **用法**：理解大厂如何系统化评估 LLM/Agent。与 deepeval 对比：OpenAI Evals 更偏学术 benchmark，deepeval 更偏工程 CI 集成。

---

## 阅读路径建议

| 顺序 | 材料 | 用途 | 时长 |
|:----:|------|------|:----:|
| 1 | 本 Day `notes.md` 理论回顾 + 独立教材 §3.3.1-3.3.4 | 评估方法论 | 1h |
| 2 | AgentBench 论文 §3-4（选读） | 学术 benchmark | 0.5h |
| 3 | `starter.ipynb` 上机（配 deepeval 文档） | 真实库实操 | 2h |
| 4 | LLM-as-a-judge 论文 §3, §5 | 前沿+偏差认知 | 0.5h |
| 5 | deepeval GEval / FaithfulnessMetric 文档 | 巩固 API | 0.5h |
| 6 | LangSmith 评估文档（选读） | 在线可观测延伸 | 0.5h |

---

*全部深链已于 2026-07-24 验证存在。如发现失效，请在 Issues 报告。*
