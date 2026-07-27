# Phase 6 深链阅读清单

> v5.0升级：从"课程主页"升级为**经验证的深链**（指向具体论文/文档/仓库，非主页）。Phase 6聚焦DSR artifact+可复现研究+LangSmith trace+LLM-as-a-judge+天道推演×多Agent仿真。

---

## ① DSR设计科学研究（Capstone方法论框架）

### Hevner et al. (2004) MIS Quarterly 经典（DSR七准则）
- 📄 JSTOR：https://www.jstor.org/stable/25148625
- **用法**：Phase 6 DSR框架的理论来源。Hevner提出DSR七准则（artifact为研究贡献/问题相关性/设计评估/研究贡献/研究严谨性/设计即搜索/研究交流）。重点读 §2（Design Science vs Natural Science）和 §3（Seven Guidelines）。你的Capstone用DSR定位：Agent系统是一个可发表的artifact。

### Peffers et al. (2007) DSR六步方法论
- 📄 paper：https://desrist.org/desrist/files/peffers2007.pdf
- **用法**：把Hevner的七准则操作化为六步流程（问题识别->目标定义->设计开发->演示->评估->传播）。本Phase TODO1直接用这六步定义Capstone研究计划。重点读 §3（Methodology）。

### DESRIST 研究社区
- 🌐 DESRIST：https://desrist.org/ （已验证，DSR研究社区，年度会议）
- **用法**：DSR领域的研究社区和年度会议，Capstone论文可投DESRIST会议。

---

## ② 可复现研究与 LangSmith trace存档

### LangSmith 官方文档
- 📄 文档：https://docs.smith.langchain.com/ （已验证，完整API文档）
- 📦 GitHub：https://github.com/langchain-ai/langsmith-sdk （已验证，LangChain团队维护）
- **深链用法**：
  - [@traceable装饰器](https://docs.smith.langchain.com/observability/concepts)：对标 TODO2，用@traceable追踪Capstone pipeline执行链
  - [Trace查询API](https://docs.smith.langchain.com/observability/query_examples)：对标可复现研究的trace存档检索

### DoWhy 因果推断库
- 📦 GitHub：https://github.com/py-why/dowhy （已验证，微软Research维护）
- 📄 文档：https://py-why.github.io/dowhy/ （已验证）
- **深链用法**：
  - [CausalModel API](https://py-why.github.io/dowhy/v0.8/api.html)：对标 TODO3，因果模型定义+识别+估计
  - [反驳检验](https://py-why.github.io/dowhy/v0.8/api.html#dowhy.causal_model.CausalModel.refute_estimate)：对标稳健性检验

### causaldata 真实数据集
- 📦 GitHub：https://github.com/NickCH-Klein/causaldata （已验证，NSW/LaLonde等真实数据集）
- 📦 PyPI：https://pypi.org/project/causaldata/ （已验证，MIT License）
- **深链用法**：对标 TODO3，`from causaldata import nsw_mixtape` 加载真实RCT数据。

---

## ③ 论文评估与统计报告

### deepeval 评估框架（LLM-as-a-judge）
- 📦 GitHub：https://github.com/confident-ai/deepeval （已验证，17k★）
- 📄 文档：https://docs.confident-ai.com/ （已验证）
- **深链用法**：
  - [GEval（LLM-as-a-judge）](https://deepeval.com/docs/metrics-llm-evals)：对标 TODO6，用criteria模式让LLM自动评分论文质量
  - [自定义BaseMetric](https://deepeval.com/docs/metrics-custom)：对标 TODO6，自定义论文评估指标

### LLM-as-a-judge 原始论文（NeurIPS 2023）
- 📄 arXiv 2306.05685：https://arxiv.org/abs/2306.05685
- **用法**：用LLM自动评估论文质量的理论基础。重点读 §3（评估方法）和 §5（已知偏差）。注意：LLM-as-a-judge是辅助评估，不能替代真实同行评审。

### statsmodels 统计建模
- 📄 文档：https://www.statsmodels.org/ （已验证）
- **深链用法**：对标 TODO4，用scipy.stats.ttest_ind跑t检验，手算Cohen's d，生成APA格式报告。

### arxiv Python包
- 📦 PyPI：https://pypi.org/project/arxiv/ （已验证，MIT License）
- 📦 GitHub：https://github.com/lukasschwab/arxiv.py （已验证，1.5k★）
- **深链用法**：对标 TODO7，搜索"causal inference marketing agent"相关论文做文献对比。

---

## ④ 学术发表与IMRaD写作

### Capstone独立教材 § Phase 6
- 📄 教材：[`../../../AI原生化商业博士_独立教材_Capstone_AI和商业分析项目.md`](../../../AI原生化商业博士_独立教材_Capstone_AI和商业分析项目.md) § Phase 6
- **用法**：Phase 6完整理论讲义，含IMRaD论文结构模板/学术发表路线图/交付物清单。

### IMRaD 论文结构参考
- 📄 AgentBench论文（arXiv 2308.03688）：https://arxiv.org/abs/2308.03688
- **用法**：Agent系统评估的标杆论文结构参考。看它如何组织Introduction/Methods/Results/Discussion。

### ReAct 论文（Agent推理模式）
- 📄 arXiv 2210.03629：https://arxiv.org/abs/2210.03629
- **用法**：ReAct（Reasoning+Acting）是Agent的经典推理模式，Capstone的Agent设计基于此。

---

## ⑤ 天道推演×多Agent仿真（特色章节）

### 项目CLAUDE.md 天道推演系统
- 📄 项目根：`/CLAUDE.md` § 天道推演系统
- **用法**：天道推演的完整定义（局势感知/因果链追踪/沙盘模拟/概率评估/最优路径推荐），作为Capstone特色理论视角的理论来源。

### 多Agent仿真与涌现行为
- 📄 arXiv AgentBench：https://arxiv.org/abs/2308.03688
- **用法**：多Agent仿真的评估框架，理解Agent交互与涌现行为的建模方法。与天道推演的沙盘模拟同构。

---

## 阅读路径建议

| 顺序 | 材料 | 用途 | 时长 |
|:----:|------|------|:----:|
| 1 | 本Phase `notes.md` 理论回顾 + 独立教材 § Phase 6 | DSR框架+论文结构 | 1h |
| 2 | Hevner 2004 §2-3（选读） | DSR七准则 | 0.5h |
| 3 | Peffers 2007 §3（选读） | DSR六步方法论 | 0.5h |
| 4 | LangSmith @traceable文档 | 可复现trace存档 | 0.5h |
| 5 | `starter.ipynb` 上机 | 端到端Capstone实操 | 3h |
| 6 | LLM-as-a-judge论文 §3, §5（选读） | 论文评估方法论 | 0.5h |
| 7 | arxiv搜索相关论文 | 文献对比定位 | 0.5h |

---

*全部深链已于 2026-07-24 验证存在。如发现失效，请在 Issues 报告。*
