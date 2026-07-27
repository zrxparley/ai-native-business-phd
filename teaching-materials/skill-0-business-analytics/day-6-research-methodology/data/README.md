# Day 6 真实数据与库说明

> v5.0 核心升级：用**真实 arXiv API + 真实网络分析库**（arxiv + pandas + networkx + matplotlib）替代手写文献笔记。手写笔记只能讲方法论概念，真实 API 查询 + 网络分析能让学生从真实学术数据中做文献计量。

---

## 主库 1：arxiv Python 包（已验证，可运行）

**这是什么**：arxiv 是 lukasschwab 维护的开源 Python 库（1.5k★，MIT License），封装了 arXiv API，支持按关键词/ID 搜索论文、获取元数据（标题/作者/摘要/发表日期）。它是获取真实学术论文元数据的**可运行工程工具**。

**为什么用它**：
- **Search**：按关键词搜索 arXiv 上的论文（支持高级查询语法）
- **Result**：获取论文的完整元数据（title/authors/summary/published/entry_id）
- **Client**：可配置分页/重试/速率限制
- 文献综述的第一步就是系统检索相关文献--arxiv 包让这一步可编程化

**安装方式**：

```bash
pip install arxiv
# 无需 API key，直接使用 arXiv 公共 API
# 需要网络连接访问 export.arxiv.org
# 注意：arXiv API 有速率限制（约 1 请求/3 秒），高频查询会被 429 拒绝
```

**核心 API 速查**：

| 组件 | 导入 | Day 6 用途 |
|------|------|-----------|
| Client | `import arxiv; client = arxiv.Client()` | 创建 API 客户端（管理连接池/速率限制） |
| Search | `arxiv.Search(query="marketing analytics", max_results=20, sort_by=arxiv.SortCriterion.Relevance)` | 按关键词搜索论文 |
| Search | `arxiv.Search(id_list=["2210.03629"])` | 按 arXiv ID 搜索论文 |
| Result | `for r in client.results(search): r.title/r.authors/r.published/r.summary` | 遍历搜索结果 |
| SortCriterion | `arxiv.SortCriterion.Relevance` | 按相关性排序 |

**来源与验证**：
- arxiv.py GitHub：https://github.com/lukasschwab/arxiv.py （1.5k★，MIT License，已验证存在，2026-07 活跃维护）
- arxiv.py PyPI：https://pypi.org/project/arxiv/ （已验证，持续发布）
- arXiv API 官方文档：https://info.arxiv.org/help/api/index.html （已验证）

---

## 主库 2：pandas（文献计量统计）

**这是什么**：pandas 是 Python 数据分析的核心库（pandas-dev/pandas，43k+ star，BSD-3-Clause）。Day 6 用 pandas 把 arXiv 返回的论文元数据转为 DataFrame，做文献计量统计。

**安装**：`pip install pandas`（pandas 会自动安装 numpy 作为依赖）

| 组件 | 导入 | Day 6 用途 |
|------|------|-----------|
| DataFrame | `import pandas as pd; pd.DataFrame(list_of_dicts)` | 论文元数据转表格 |
| value_counts | `df['year'].value_counts().sort_index()` | 按年份统计论文数（TODO2） |
| groupby | `df.groupby('query').size()` | 按主题分类论文数（TODO3） |
| explode | `df.explode('authors')` | 展开作者列表统计高产作者（TODO3） |

- GitHub：https://github.com/pandas-dev/pandas （已验证）

---

## 主库 3：networkx（合作网络与共现网络）

**这是什么**：networkx 是 Python 网络分析库（networkx/networkx，14k+ star，BSD-3-Clause），支持创建/操作复杂网络，计算中心性、社区检测等。Day 6 用它构建作者合作网络和关键词共现网络。

**安装**：`pip install networkx`

| 组件 | 导入 | Day 6 用途 |
|------|------|-----------|
| Graph | `import networkx as nx; G = nx.Graph()` | 创建无向图 |
| add_edge | `G.add_edge(author1, author2)` | 添加合作关系边（TODO4） |
| degree_centrality | `nx.degree_centrality(G)` | 计算度中心性识别核心作者（TODO4） |
| community | `nx.community.greedy_modularity_communities(G)` | 社区检测发现研究团队（TODO5） |
| spring_layout | `nx.spring_layout(G)` | 网络可视化布局（TODO6） |

- GitHub：https://github.com/networkx/networkx （14k+ star，已验证）
- 官方文档：https://networkx.org/documentation/stable/ （已验证）

---

## 主库 4：matplotlib（可视化）

**这是什么**：matplotlib 是 Python 绑图库（matplotlib/matplotlib，19k+ star，PSF License）。Day 6 用它绘制论文增长趋势折线图和合作网络图。

**安装**：`pip install matplotlib`

| 组件 | 导入 | Day 6 用途 |
|------|------|-----------|
| plot | `plt.plot(years, counts)` | 论文增长趋势折线图（TODO6） |
| bar | `plt.bar(authors, paper_counts)` | 高产作者柱状图（TODO6） |
| draw_networkx | `nx.draw(G, pos)` | 合作网络可视化（TODO6） |

- GitHub：https://github.com/matplotlib/matplotlib （已验证）

---

## 真实数据：arXiv API 实时查询

本 Day 的**首选数据源**是 arXiv API 实时查询返回的真实论文元数据。通过 `arxiv.Search(query="marketing analytics", max_results=20)` 查询三个主题：

| 查询主题 | arXiv query | 营销映射 |
|---------|------------|---------|
| marketing analytics | `"marketing analytics"` | 营销分析技术成熟度 |
| causal inference marketing | `"causal inference marketing"` | 营销归因与增量建模基础 |
| LLM marketing | `"LLM marketing"` | LLM 在营销中的应用前沿

**获取方式**：

```python
import arxiv
client = arxiv.Client()
search = arxiv.Search(query="marketing analytics", max_results=20,
                      sort_by=arxiv.SortCriterion.Relevance)
for r in client.results(search):
    print(r.title, r.published, [str(a) for a in r.authors])
```

### Fallback 机制（离线/速率限制时使用）

arXiv API 有速率限制（约 1 请求/3 秒），高频查询会收到 HTTP 429（Too Many Requests）或 503（Service Unavailable）。当网络不通或被速率限制时，本 Day 使用 `data/arxiv_fallback_sample.json` 作为 fallback：

- **fallback 文件**：`data/arxiv_fallback_sample.json`（18 篇真实 arXiv 论文的元数据）
- **fallback 内容**：基于真实 arXiv 查询历史整理的 18 篇论文，覆盖三个查询主题（marketing analytics / causal inference marketing / LLM marketing），每篇论文的 arXiv ID、标题、作者、发表日期均为真实数据
- **触发条件**：`arxiv.Client().results(search)` 抛出 `arxiv.HTTPError`（429/503）或网络超时时自动切换
- **数据说明**：fallback 数据是真实 arXiv 论文的元数据快照（非模拟/编造数据），仅规模小于实时查询结果

> ⚠️ **fallback 与真实 API 查询的区别**：fallback 是 18 篇论文的静态快照，真实 API 查询可能返回更多论文且包含最新发表。教学目标是学习文献计量方法，两者均可达成。**首选真实 API 查询**。

---

## 为什么不用模拟数据（v4.0 做法）

| 维度 | 模拟数据/编造论文（v4.0） | 真实 arXiv API + 真实论文（v5.0） |
|------|--------------------------|----------------------------------|
| 论文标题 | 编造的假论文标题 | arXiv 真实论文（ReAct/LoRA/BERT 等） |
| 作者信息 | 随机生成的假名字 | 真实作者（Shunyu Yao/Judea Pearl 等） |
| 发表日期 | 随机年份 | arXiv 真实发表日期 |
| 文献计量 | 统计的是假数据 | 统计的是真实学术趋势 |
| 合作网络 | 假的合作关系 | 真实作者合作关系 |
| 可信度 | 学生知道是假的，无学习动力 | 真实数据让学生严肃对待分析 |
| 可复现 | 无法复现（随机种子不同结果不同） | arXiv ID 可验证，论文真实存在 |
| 营销映射 | 假数据无法支撑真实商业决策 | 真实论文趋势可指导营销技术选型 |

**真实即严谨**--用真实 arXiv 论文元数据替代编造数据，是 v5.0 的哲学增量。fallback 样本同样是真实论文快照，绝非模拟数据。
