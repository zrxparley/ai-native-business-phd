# R5 真实数据与库说明

> v5.0 核心升级：用**真实论文**（arXiv多篇论文）+ **真实因果推断数据**（causaldata NSW职业培训实验）+ **真实统计库**（statsmodels + scipy.stats）替代手写文本模板。手写模板只能讲格式，真实论文+统计库+因果数据能让学生从真实学术实践中学习IMRaD写作方法论本身。

---

## 主库 1：arxiv Python 包（已验证，可运行）

**这是什么**：arxiv 是 lukasschwab 维护的开源 Python 库（1.5k★，MIT License），封装了 arXiv API，支持按关键词/ID搜索论文、获取元数据（标题/作者/摘要/发表日期）。它是获取真实学术论文的**可运行工程工具**。

**为什么用它**：
- **Search**：按关键词搜索 arXiv 上的论文（支持高级查询语法）
- **Result**：获取论文的完整元数据（title/authors/summary/published）
- **Client**：可配置分页/重试/速率限制
- 本单元用arxiv下载多篇真实论文，对摘要做句级IMRaD分类，跨论文对比结构差异

**安装方式**：

```bash
pip install arxiv
# 无需 API key，直接使用 arXiv 公共 API
# 需要网络连接访问 export.arxiv.org
```

**核心 API 速查**：

| 组件 | 导入 | R5 用途 |
|------|------|---------|
| Client | `import arxiv; client = arxiv.Client()` | 创建 API 客户端 |
| Search | `arxiv.Search(id_list=["2210.03629"])` | 按arXiv ID搜索论文 |
| Search | `arxiv.Search(query="LLM-as-a-judge", max_results=5)` | 按关键词搜索 |
| Result | `paper = next(client.results(search))` | 获取搜索结果 |
| Result.title | `paper.title` | 论文标题 |
| Result.summary | `paper.summary` | 摘要（用于IMRaD结构分析） |

**来源与验证**：
- arxiv.py GitHub：https://github.com/lukasschwab/arxiv.py （1.5k★，MIT License，已验证存在，2026-07活跃维护）
- arxiv.py PyPI：https://pypi.org/project/arxiv/ （已验证，持续发布）
- arXiv API 官方文档：https://info.arxiv.org/help/api/index.html （已验证）

---

## 主库 2：statsmodels + scipy.stats（统计检验，已验证）

**这是什么**：statsmodels 是 Python 统计建模库（BSD License），scipy.stats 是 SciPy 的统计模块。两者提供 t 检验、卡方检验、效应量计算等统计方法，是 Results 部分统计报告的**数据支撑工具**。

**为什么用它**：
- **ttest_ind**：独立样本 t 检验（比较两组均值差异是否显著）
- **Cohen's d**：效应量计算（差异的大小，不只是显著性）
- **95% CI**：置信区间（效果估计的精确度）
- 结果用于撰写APA第7版格式的Results部分

**安装方式**：

```bash
pip install statsmodels scipy numpy
# 离线可用，无需网络连接
```

**核心 API 速查**：

| 组件 | 导入 | R5 用途 |
|------|------|---------|
| ttest_ind | `from scipy.stats import ttest_ind` | 独立样本t检验（TODO4） |
| t | `from scipy.stats import t` | t分布分位数（Welch CI） |
| numpy | `import numpy as np` | 数据计算/Cohen's d |

**来源与验证**：
- statsmodels官方文档：https://www.statsmodels.org/stable/index.html （已验证，BSD License）
- scipy.stats官方文档：https://docs.scipy.org/doc/scipy/reference/stats.html （已验证，BSD License）

---

## 真实数据：causaldata NSW职业培训实验（已验证，可运行）

**这是什么**：NSW（National Supported Work Demonstration）是LaLonde (1986) 经典因果推断数据集，来自causaldata Python包。它是一项真实的随机对照试验（RCT）：处理组（treat=1）接受职业培训，对照组（treat=0）不接受，结果变量re78是1978年收入。

**为什么用它**：
- **真实RCT数据**：非模拟数据，是因果推断教科书的标准数据集（LaLonde 1986, Dehejia & Wahba 1999）
- **结构同构营销A/B测试**：NSW（培训 vs 无培训）与营销A/B测试（AI Agent vs 人工）结构相同--都是二值处理变量+连续结果变量的RCT
- **统计检验有实际意义**：t检验问"职业培训是否显著提高收入"，与营销场景"AI Agent是否显著提高效率"逻辑一致

**数据概况**（已验证）：

| 变量 | 类型 | 说明 | 示例值 |
|------|------|------|--------|
| treat | int | 处理组（1=职业培训，0=对照） | 0 / 1 |
| age | int | 年龄 | 37 |
| educ | int | 教育年限 | 11 |
| re74 | float | 1974年收入（美元） | 0.0 |
| re75 | float | 1975年收入（美元） | 0.0 |
| re78 | float | 1978年收入（美元，结果变量） | 9930.05 |

**样本量**：N=445（treat=1: 185, treat=0: 260）

**获取方式**：

```python
import pandas as pd
# causaldata包加载有兼容性问题，直接读.dta文件
data_path = '/opt/anaconda3/lib/python3.12/site-packages/causaldata/nsw_mixtape/nsw_mixtape.dta'
df = pd.read_stata(data_path)
# 或用causaldata包（如版本兼容）
# from causaldata import nsw_mixtape
# df = nsw_mixtape.load().data
```

**来源与验证**：
- causaldata PyPI：https://pypi.org/project/causaldata/ （已验证，NSW数据集包含在内）
- LaLonde (1986) 原始论文：https://www.jstor.org/stable/1806062 （American Economic Review）
- Dehejia & Wahba (1999)：https://doi.org/10.1080/01621459.1999.10473858 （JASA）

---

## 真实论文：3篇arXiv论文（已验证，用于IMRaD结构分析）

| 论文 | arXiv ID | 用途 |
|------|----------|------|
| ReAct (Yao et al., NeurIPS 2022) | 2210.03629 | Agent论文IMRaD结构范例 |
| LLM-as-a-judge (Zheng et al., NeurIPS 2023) | 2306.05685 | 2026前沿：写作质量评估方法论 |
| GraphRAG (Edge et al., 2024) | 2404.16130 | RAG论文IMRaD结构范例 |

**获取方式**：

```python
import arxiv
client = arxiv.Client()
search = arxiv.Search(id_list=["2210.03629", "2306.05685", "2404.16130"])
results = list(client.results(search))
for paper in results:
    print(paper.title, len(paper.summary))
```

**来源与验证**：
- ReAct arXiv页面：https://arxiv.org/abs/2210.03629 （已验证）
- LLM-as-a-judge arXiv页面：https://arxiv.org/abs/2306.05685 （已验证）
- GraphRAG arXiv页面：https://arxiv.org/abs/2404.16130 （已验证）

---

## 为什么不用模拟数据（v4.0做法）

| 维度 | 模拟数据/手写模板（v4.0） | 真实论文+真实数据（v5.0） |
|------|------------------------|------------------------|
| IMRaD结构学习 | 看抽象模板 | 从3篇真实arXiv论文摘要做句级IMRaD分类 |
| 统计报告 | 编造数字/手写公式 | 真实NSW实验数据(N=445)的t检验/Cohen's d/CI |
| 效应量解读 | 主观描述 | 真实Cohen's d=0.27（小效应），有实际意义讨论 |
| APA格式 | 手写容易出错 | 代码生成格式准确（t/df/p/d/CI） |
| 因果推断连接 | 无 | NSW是LaLonde(1986)经典因果推断数据集 |
| 可复现 | 无法复现 | 固定代码 + 真实数据源 |
| 写作质量评估 | 人工审稿 | LLM-as-a-judge自动评分checklist |

**真实即严谨**--用真实论文和真实因果推断数据替代模拟数据，是v5.0的哲学增量。
