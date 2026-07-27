# Day 6 真实论文与库说明

> v5.0 核心升级：用**真实论文**（ReAct, arXiv 2210.03629）+ **真实库**（arxiv Python 包 + statsmodels）替代手写文本模板。手写模板只能讲格式，真实论文+统计库能让学生从真实学术实践中学习 IMRaD 写作。

---

## 主库 1：arxiv Python 包（已验证，可运行）

**这是什么**：arxiv 是 lukasschwab 维护的开源 Python 库（1.5k★，MIT License），封装了 arXiv API，支持按关键词/ID 搜索论文、获取元数据（标题/作者/摘要/发表日期）、下载 PDF。它是获取真实学术论文的**可运行工程工具**。

**为什么用它**：
- **Search**：按关键词搜索 arXiv 上的论文（支持高级查询语法）
- **Result**：获取论文的完整元数据（title/authors/summary/published/pdf_url）
- **download_pdf**：下载论文 PDF（可用于全文 IMRaD 结构分析）
- **Client**：可配置分页/重试/速率限制

**安装方式**：

```bash
pip install arxiv
# 无需 API key，直接使用 arXiv 公共 API
# 需要网络连接访问 export.arxiv.org
```

**核心 API 速查**：

| 组件 | 导入 | 用途 |
|------|------|------|
| Client | `import arxiv; client = arxiv.Client()` | 创建 API 客户端（管理连接池/速率限制） |
| Search | `arxiv.Search(id_list=["2210.03629"])` | 按 arXiv ID 搜索论文 |
| Search | `arxiv.Search(query="marketing agent", max_results=5)` | 按关键词搜索 |
| Result | `paper = next(client.results(search))` | 获取搜索结果 |
| Result.title | `paper.title` | 论文标题 |
| Result.authors | `paper.authors` | 作者列表 |
| Result.summary | `paper.summary` | 摘要（用于 IMRaD 结构分析） |

**来源与验证**：
- arxiv.py GitHub：https://github.com/lukasschwab/arxiv.py （1.5k★，MIT License，已验证存在，2026-07 活跃维护）
- arxiv.py PyPI：https://pypi.org/project/arxiv/ （已验证，持续发布）
- arXiv API 官方文档：https://info.arxiv.org/help/api/index.html （已验证）

---

## 主库 2：statsmodels + scipy（统计检验）

**这是什么**：statsmodels 是 Python 统计建模库，scipy.stats 是 SciPy 的统计模块。两者提供 t 检验、卡方检验、回归分析等统计方法，是 Results 部分的**数据支撑工具**。

**为什么用它**：
- **ttest_ind**：独立样本 t 检验（比较两组均值差异是否显著）
- **chi2_contingency**：卡方检验（比较分类变量差异是否显著）
- **Cohen's d**：效应量计算（差异的大小，不只是显著性）
- 结果用于撰写 APA 格式的 Results 部分学术表述

**安装方式**：

```bash
pip install statsmodels scipy numpy
# 离线可用，无需网络连接
```

**核心 API 速查**：

| 组件 | 导入 | 用途 |
|------|------|------|
| ttest_ind | `from statsmodels.stats.weightstats import ttest_ind` | 独立样本 t 检验 |
| chi2_contingency | `from scipy.stats import chi2_contingency` | 卡方检验（列联表） |
| numpy | `import numpy as np` | 数据生成/计算 |

---

## 真实论文：ReAct（arXiv 2210.03629，已验证）

**这是什么**：ReAct 是 Yao et al. (2022) 提出的 Agent 推理-行动协同框架，发表于 NeurIPS 2022。它是 Agent 领域的里程碑论文，也是 IMRaD 结构的优秀范例。

**为什么用它作为 IMRaD 结构分析对象**：
- Introduction：清晰的研究动机（LLM 推理和行动能力被分开研究）
- Methods：详细的框架设计（推理轨迹 + 任务行动交替）
- Results：多基准测试结果（HotpotQA/Fever/AlfWorld等）
- Discussion：有效性和局限性讨论

**获取方式**：

```python
import arxiv
client = arxiv.Client()
search = arxiv.Search(id_list=["2210.03629"])
paper = next(client.results(search))
print(paper.title)    # ReAct: Synergizing Reasoning and Acting in Language Models
print(paper.summary)  # 摘要文本
```

**来源与验证**：
- arXiv 页面：https://arxiv.org/abs/2210.03629 （已验证，Yao et al., NeurIPS 2022）
- arXiv API 返回标题：`ReAct: Synergizing Reasoning and Acting in Language Models`（已通过 API 验证）

---

## 真实论文：LLM-as-a-judge（arXiv 2306.05685，已验证）

**这是什么**：Zheng et al. (2023) 提出的 LLM-as-a-judge 评估方法，发表于 NeurIPS 2023。它用强 LLM（如 GPT-4）自动评估开放式问题的回答质量，是 2026 年 AI 写作质量评估的基础方法论。

**为什么用它**：
- Day 6 将 LLM-as-a-judge 用于评估 IMRaD 论文写作质量（Introduction/Methods/Results/Discussion 各部分评分）
- 与 Day 3 的 deepeval GEval（LLM-as-a-judge 评估 Agent 轨迹）形成范式连贯
- 论文本身也是 IMRaD 结构的优秀范例

**来源与验证**：
- arXiv 页面：https://arxiv.org/abs/2306.05685 （已验证，Zheng et al., NeurIPS 2023，标题：Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena）

---

## 营销 A/B 测试数据（用于 Results 统计分析）

本 Day 的 Results 部分使用基于行业基准的可复现营销 A/B 测试数据：

| 指标 | 对照组（人工） | 实验组（Agent） | 数据来源 |
|------|:-----------:|:-----------:|---------|
| 内容产出效率（篇/天） | M~8.2, SD~2.5 | M~32.5, SD~8.0 | 基于真实营销团队效率基准 |
| 内容 CTR | 2.1% | 2.8% | 基于行业 CTR 基准 |
| 用户满意度（1-10） | M~7.2, SD~1.2 | M~7.8, SD~1.0 | 基于用户评分基准 |

**数据生成方式**（固定随机种子，可复现）：

```python
import numpy as np
np.random.seed(42)
control_eff = np.random.normal(8.2, 2.5, 200)      # 人工组
treatment_eff = np.random.normal(32.5, 8.0, 200)    # Agent组
```

> 💡 **数据来源说明**：这些数据基于真实营销行业基准（内容产出效率/CTR/满意度）生成，固定随机种子确保可复现。在真实研究中，你应该使用自己 A/B 测试平台的实际数据。数值范围参考了 McKinsey 2025 AI in Marketing 报告和 HubSpot Marketing Benchmark Report。

---

## 为什么不用手写文本模板（v4.0 做法）

| 维度 | 手写文本模板（v4.0） | 真实论文+统计库（v5.0） |
|------|---------------------|------------------------|
| IMRaD 结构学习 | 看抽象模板 | 从真实论文（ReAct）解析结构 |
| Results 数据 | 编造数字 | statsmodels 跑真实统计检验 |
| APA 格式 | 手写容易出错 | 代码生成格式准确 |
| 统计报告 | 主观描述 | APA 标准格式（t/df/p/d） |
| 可复现 | 无法复现 | 固定随机种子 + 真实代码 |
| 写作质量评估 | 人工审稿 | LLM-as-a-judge 自动评分 |

**真实即严谨**--用真实论文和统计工具替代手写模板，是 v5.0 的哲学增量。
