# Day 7 真实数据与库说明

> v5.0 核心升级：Day 7是整合性Capstone，用**真实数据集+真实库**串起端到端流水线：数据层(causaldata)→因果层(DoWhy)→Agent层(LangGraph)→评估层(deepeval)→论文层(IMRaD)。不使用任何模拟数据。

---

## 数据层：causaldata NSW 职业培训实验（真实RCT）

**这是什么**：NSW（National Supported Work）职业培训实验是因果推断领域的经典真实RCT数据集。1970年代在美国随机分配失业人员到职业培训组（treatment）和对照组（control），追踪后续收入变化。LaLonde (1986) 用它挑战了当时计量经济学方法的可靠性，此后成为因果推断方法论的benchmark数据集。

**为什么用它**：NSW是真实随机对照实验（RCT），数据质量高、变量清晰、有明确的treatment/outcome/covariates结构，适合做端到端因果分析。在本Day的Capstone中，我们把NSW映射为营销场景：treat=营销干预，re78=转化率/收入，re75=基线消费。

**安装与加载**：

```bash
pip install causaldata
```

```python
from causaldata import nsw
df = nsw.load_pandas().data
# 列: treat, age, education, black, hispanic, married, nodegree, re74, re75, re78
```

**NSW变量与营销映射**：

| NSW变量 | 含义 | 营销映射 | 角色 |
|---------|------|---------|------|
| `treat` | 是否接受职业培训 | 是否收到个性化营销/优惠券 | 处理 T |
| `re78` | 1978年收入（实验后） | 营销后的转化率/GMV/客单价 | 结果 Y |
| `re75` | 1975年收入（实验前） | 实验前的历史消费/活跃度 | CUPED协变量/后门协变量 |
| `age` | 年龄 | 用户年龄 | 协变量 X |
| `education` | 教育年限 | 用户教育水平 | 协变量 X |
| `black`/`hispanic` | 种族 | 用户画像分群 | 协变量 X |
| `married` | 婚姻状况 | 用户画像 | 协变量 X |
| `nodegree` | 是否无学位 | 用户画像 | 协变量 X |

**来源与验证**：
- causaldata PyPI：https://pypi.org/project/causaldata/ （已验证，MIT License，Nick Huntington-Klein维护）
- causaldata GitHub：https://github.com/NickCH-K/causaldata （已验证，含NSW/LaLonde等数据集）
- 数据来源：LaLonde (1986), "Evaluating the Econometric Evaluations of Training Programs", American Economic Review. NSW原始实验数据。

> 💡 本Day复用技能3（因果推断）的真实数据集，但视角不同：技能3做纯因果分析，今天把因果分析作为Agent流水线的一环（Agent调用因果分析工具）。

---

## 因果层：DoWhy（已验证，可运行）

**这是什么**：DoWhy是微软Research维护的因果推断库（py-why/dowhy），提供"假设→识别→估计→反驳"四步因果分析流程。它支持后门调整、前门调整、工具变量等多种识别策略，并能调用econml/sklearn做估计。

**安装**：

```bash
pip install dowhy econml
```

**核心API速查**：

| 组件 | 导入 | 用途 |
|------|------|------|
| CausalModel | `from dowhy import CausalModel` | 定义因果模型（数据+图+treatment/outcome） |
| identify_estimand | `model.identify_effect()` | 因果识别（找后门调整集） |
| estimate_effect | `model.estimate_effect()` | 因果估计（ATE/ATT/ATC） |
| refute_estimate | `model.refute_estimate()` | 稳健性检验（安慰剂/子集） |

**来源与验证**：
- DoWhy GitHub：https://github.com/py-why/dowhy （已验证，微软Research维护，活跃开发）
- DoWhy文档：https://py-why.github.io/dowhy/ （已验证，完整API文档）

---

## Agent层：LangGraph（已验证，可运行）

**这是什么**：LangGraph是LangChain团队出品的Agent编排框架（langchain-ai/langgraph），基于图结构的有状态Agent工作流。它用StateGraph定义节点和边，支持循环、条件分支、持久化状态。Day 2已深入使用，今天作为Capstone流水线的一环。

**安装**：

```bash
pip install langgraph langchain-core
```

**核心API速查**：

| 组件 | 导入 | 用途 |
|------|------|------|
| StateGraph | `from langgraph.graph import StateGraph` | 定义有状态图 |
| START/END | `from langgraph.graph import START, END` | 图的起点/终点 |
| add_node | `graph.add_node(name, fn)` | 添加节点（Agent/工具） |
| add_edge | `graph.add_edge(a, b)` | 添加边（顺序执行） |
| add_conditional_edges | `graph.add_conditional_edges(a, fn)` | 条件分支 |
| compile | `graph.compile()` | 编译为可执行图 |

**来源与验证**：
- LangGraph GitHub：https://github.com/langchain-ai/langgraph （已验证，LangChain团队出品）
- LangGraph文档：https://langchain-ai.github.io/langgraph/ （已验证，完整教程）

---

## 评估层：deepeval（已验证，可运行）

**这是什么**：deepeval是confident-ai维护的LLM评估框架（17k★），提供GEval（LLM-as-a-judge）、FaithfulnessMetric（幻觉检测）、BaseMetric（自定义指标）、evaluate（批量运行）。Day 3已深入使用，今天评估Capstone Agent的策略输出质量。

**安装**：

```bash
pip install deepeval
# GEval默认使用OpenAI作为judge模型，需设置：
# export OPENAI_API_KEY=sk-...
```

**核心API速查**：

| 组件 | 导入 | 用途 |
|------|------|------|
| LLMTestCase | `from deepeval.test_case import LLMTestCase` | 定义测试用例 |
| GEval | `from deepeval.metrics import GEval` | LLM-as-a-judge自动评分 |
| BaseMetric | `from deepeval.metrics import BaseMetric` | 自定义指标基类 |
| evaluate | `from deepeval import evaluate` | 批量运行测试套件 |

**来源与验证**：
- deepeval GitHub：https://github.com/confident-ai/deepeval （已验证，17k★，MIT License）
- deepeval文档：https://docs.confident-ai.com/ （已验证，301重定向至deepeval.com/docs/）

---

## 部署/追踪层：LangSmith（可观测性）

**这是什么**：LangSmith是LangChain的可观测性平台，自动记录Agent执行的完整调用链（trace/eval/score）。Day 5已介绍，今天作为可复现研究的基础设施--trace存档让他人能独立验证你的Agent行为。

**来源与验证**：
- LangSmith文档：https://docs.smith.langchain.com/ （已验证）
- LangGraph（含LangSmith集成）：https://github.com/langchain-ai/langgraph （已验证）

---

## DSR框架参考

**DSR（设计科学研究）**是Capstone的研究方法论框架：

- **Hevner et al. (2004)** "Design Science in Information Systems Research", MIS Quarterly 28(1), 75-105. JSTOR: https://www.jstor.org/stable/25148625 （DSR七准则经典论文）
- **Peffers et al. (2007)** "A Design Science Research Methodology for Information Systems Research", Journal of Management Information Systems 24(3), 45-78. https://desrist.org/desrist/files/peffers2007.pdf （DSR六步方法论）

---

## 为什么不用模拟数据（v4.0做法）

| 维度 | 模拟数据（v4.0） | 真实数据+真实库（v5.0） |
|------|-----------------|----------------------|
| 因果分析 | 手写假数据，ATE是编的 | NSW真实RCT，ATE是真实因果效应 |
| Agent | 手写if-else假装Agent | LangGraph真实图编排 |
| 评估 | 手写规则匹配 | deepeval LLM-as-a-judge |
| 可复现 | 不可复现（数据是编的） | 可复现（真实数据+开源代码） |
| 学术可信度 | 无 | 可发表（DSR artifact） |

**真实即严谨**--用真实数据集和真实库替代模拟数据，是v5.0的哲学增量，也是Day 7作为Capstone收官的基本要求。
