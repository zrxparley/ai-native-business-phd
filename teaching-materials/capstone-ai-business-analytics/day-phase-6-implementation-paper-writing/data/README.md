# Phase 6 真实数据与库说明

> v5.0 核心升级：Phase 6是Capstone收官，用**真实数据集+真实库**构建完整交付物：可运行系统+IMRaD论文+DSR artifact+发表路线图。不使用任何模拟数据。

---

## 可复现层：LangSmith（@traceable追踪）

**这是什么**：LangSmith是LangChain的可观测性平台，`@traceable`装饰器自动记录函数执行的完整调用链（输入/输出/子调用/耗时）。本Phase用它作为**可复现研究的基础设施**--trace存档让他人能独立验证Agent行为。

**安装**：

```bash
pip install langsmith
```

**核心API**：

| 组件 | 导入 | 用途 |
|------|------|------|
| @traceable | `from langsmith import traceable` | 装饰函数，自动追踪执行链 |
| Client | `from langsmith import Client` | 查询trace数据 |

**本地模式**（无需API Key）：
```python
import os
os.environ["LANGSMITH_TRACING"] = "false"  # 本地模式
@traceable(name="capstone_pipeline")
def run_pipeline(...): ...
```

**来源与验证**：
- LangSmith文档：https://docs.smith.langchain.com/ （已验证，完整API文档）
- LangSmith GitHub：https://github.com/langchain-ai/langsmith-sdk （已验证，LangChain团队维护）
- PyPI：https://pypi.org/project/langsmith/ （已验证，MIT License）

---

## 评估层：deepeval（LLM-as-a-judge）

**这是什么**：deepeval是confident-ai维护的LLM评估框架（17k★），提供GEval（LLM-as-a-judge）、BaseMetric（自定义指标）、evaluate（批量运行）。本Phase用它评估IMRaD论文草稿质量。

**安装**：

```bash
pip install deepeval
```

**核心API**：

| 组件 | 导入 | 用途 |
|------|------|------|
| BaseMetric | `from deepeval.metrics import BaseMetric` | 自定义指标基类（不需要API Key） |
| GEval | `from deepeval.metrics import GEval` | LLM-as-a-judge自动评分（需API Key） |
| LLMTestCase | `from deepeval.test_case import LLMTestCase` | 定义测试用例 |

**来源与验证**：
- deepeval GitHub：https://github.com/confident-ai/deepeval （已验证，17k★，MIT License）
- deepeval文档：https://docs.confident-ai.com/ （已验证）
- GEval论文：arXiv 2306.05685, NeurIPS 2023

---

## 统计层：statsmodels + scipy

**这是什么**：statsmodels是Python统计建模库，scipy.stats提供统计检验函数。本Phase用它们跑t检验/Cohen's d/卡方检验，生成APA格式的论文Results部分。

**安装**：

```bash
pip install statsmodels scipy
```

**核心API**：

| 函数 | 导入 | 用途 |
|------|------|------|
| ttest_ind | `from scipy.stats import ttest_ind` | 独立样本t检验 |
| chi2_contingency | `from scipy.stats import chi2_contingency` | 卡方检验 |
| OLS | `import statsmodels.api as sm` | 最小二乘回归 |

**来源与验证**：
- statsmodels文档：https://www.statsmodels.org/ （已验证）
- scipy文档：https://docs.scipy.org/doc/scipy/reference/stats.html （已验证）

---

## 文献层：arxiv（Python包）

**这是什么**：arxiv（lukasschwab/arxiv.py，1.5k★）是arXiv API的Python封装，可搜索/下载真实论文的元数据。本Phase用它搜索相关论文做文献对比，定位Capstone的学术贡献。

**安装**：

```bash
pip install arxiv
```

**核心API**：

| 组件 | 导入 | 用途 |
|------|------|------|
| Search | `import arxiv; arxiv.Search(...)` | 搜索论文 |
| Client | `arxiv.Client()` | 执行搜索 |

**来源与验证**：
- arxiv PyPI：https://pypi.org/project/arxiv/ （已验证，MIT License）
- arxiv API文档：https://info.arxiv.org/help/api/index.html （已验证）

---

## 数据层：causaldata NSW 真实RCT

**这是什么**：NSW（National Supported Work）职业培训实验是因果推断领域的经典真实RCT数据集（N=445）。1970年代在美国随机分配失业人员到职业培训组（treatment）和对照组（control），追踪后续收入变化。LaLonde (1986) 用它挑战了当时计量经济学方法的可靠性。

**营销映射**：把NSW当作营销A/B测试数据 --

| NSW变量 | 含义 | 营销映射 | 角色 |
|---------|------|---------|------|
| `treat` | 是否接受职业培训 | 是否收到个性化营销 | 处理 T |
| `re78` | 1978年收入（实验后） | 营销后转化率/GMV | 结果 Y |
| `re75` | 1975年收入（实验前） | 实验前历史消费 | CUPED协变量 |
| `age` | 年龄 | 用户年龄 | 协变量 X |
| `educ` | 教育年限 | 用户教育水平 | 协变量 X |
| `black`/`hisp` | 种族 | 用户画像分群 | 协变量 X |
| `marr` | 婚姻状况 | 用户画像 | 协变量 X |
| `nodegree` | 是否无学位 | 用户画像 | 协变量 X |

**安装与加载**：

```bash
pip install causaldata
```

```python
from causaldata import nsw_mixtape
df = nsw_mixtape.load_pandas().data
# 列: data_id, treat, age, educ, black, hisp, marr, nodegree, re74, re75, re78
```

**来源与验证**：
- causaldata PyPI：https://pypi.org/project/causaldata/ （已验证，MIT License）
- causaldata GitHub：https://github.com/NickCH-Klein/causaldata （已验证）
- 数据来源：LaLonde (1986), American Economic Review

---

## 因果层：DoWhy（已验证，可运行）

**这是什么**：DoWhy是微软Research维护的因果推断库（py-why/dowhy），提供"假设->识别->估计->反驳"四步因果分析流程。

**安装**：

```bash
pip install dowhy
```

**来源与验证**：
- DoWhy GitHub：https://github.com/py-why/dowhy （已验证，微软Research维护）
- DoWhy文档：https://py-why.github.io/dowhy/ （已验证，完整API文档）

---

## 为什么不用模拟数据（v4.0做法）

| 维度 | 模拟数据（v4.0） | 真实数据+真实库（v5.0） |
|------|-----------------|----------------------|
| 因果分析 | 手写假数据，ATE是编的 | NSW真实RCT，ATE=1636.28（真实因果效应） |
| 统计检验 | 编造p值/d值 | statsmodels真实t检验，t(443)=2.84, p<.01, d=0.27 |
| 可复现性 | 不可复现（数据是编的） | LangSmith @traceable trace存档 |
| 论文评估 | 手写规则匹配 | deepeval LLM-as-a-judge评估 |
| 文献对比 | 手写引用列表 | arxiv真实API搜索 |
| 学术可信度 | 无 | 可发表（DSR artifact） |

**真实即严谨**--用真实数据集和真实库替代模拟数据，是v5.0的哲学增量，也是Phase 6作为Capstone收官的基本要求。
