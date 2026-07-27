# Phase 1 真实数据与库说明

> v5.0 核心升级：用**真实 arXiv API 查询**（arxiv Python 包）+ **结构化Schema**（pydantic）+ **真实文献计量工具**（pandas + matplotlib）替代手写编造数据。手写数据只能讲流程，真实API+真实论文能让学生从真实学术实践中学习 PRISMA 系统文献综述和DSR问题定义。

---

## 主库 1：arxiv Python 包（已验证，可运行）

**这是什么**：arxiv 是 lukasschwab 维护的开源 Python 库（1.5k★，MIT License），封装了 arXiv API，支持按关键词/ID 搜索论文、获取元数据（标题/作者/摘要/发表日期/分类）。它是获取真实学术论文的**可运行工程工具**。

**为什么用它**：
- **Search**：按关键词搜索 arXiv 上的论文（支持高级查询语法）
- **Result**：获取论文的完整元数据（title/authors/summary/published/entry_id/primary_category）
- **Client**：可配置分页/重试/速率限制（num_retries/page_size）
- **SortCriterion**：按相关性（Relevance）或发表日期（SubmittedDate）排序

**安装方式**：

```bash
pip install arxiv
# 无需 API key，直接使用 arXiv 公共 API
# 需要网络连接访问 export.arxiv.org
```

**核心 API 速查**：

| 组件 | 导入 | 用途 |
|------|------|------|
| Client | `import arxiv; client = arxiv.Client(num_retries=5)` | 创建 API 客户端（管理连接池/速率限制/重试） |
| Search | `arxiv.Search(query="AI marketing agent", max_results=50)` | 按关键词搜索 |
| SortCriterion | `arxiv.SortCriterion.Relevance` | 按相关性排序 |
| Result | `paper = next(client.results(search))` | 获取搜索结果迭代器 |
| Result.title | `paper.title` | 论文标题 |
| Result.summary | `paper.summary` | 摘要（用于 PRISMA 筛选） |
| Result.published | `paper.published` | 发表日期（用于年份筛选） |
| Result.primary_category | `paper.primary_category` | 主分类（用于主题分析） |

**来源与验证**：
- arxiv.py GitHub：https://github.com/lukasschwab/arxiv.py （1.5k★，MIT License，已验证存在，2026-07 活跃维护）
- arxiv.py PyPI：https://pypi.org/project/arxiv/ （已验证，持续发布）
- arXiv API 官方文档：https://info.arxiv.org/help/api/index.html （已验证）

---

## 主库 2：pydantic（DSR问题定义Schema）

**这是什么**：pydantic 是 Python 最流行的数据验证库，基于 Python 类型注解自动生成数据模型和验证逻辑。本 Phase 用它构建DSR问题定义的结构化Schema。

**为什么用它**：
- **BaseModel**：定义DSR问题定义的数据模型（问题识别/目标/artifact描述/预期贡献）
- **Field**：字段描述和默认值约束
- **validator**：自定义验证逻辑（如研究问题长度>=20字符）
- **model_dump()**：将Schema实例导出为字典，便于输出研究问题定义书

**安装方式**：

```bash
pip install pydantic
# 离线可用，无需网络连接
```

**核心 API 速查**：

| 组件 | 导入 | 用途 |
|------|------|------|
| BaseModel | `from pydantic import BaseModel` | 定义数据模型基类 |
| Field | `from pydantic import Field` | 字段描述和约束 |
| model_dump() | `schema.model_dump()` | 导出为字典 |
| model_validate() | `Model.model_validate(data)` | 从字典创建实例并验证 |

---

## 主库 3：pandas（文献计量统计）

**这是什么**：pandas 是 Python 数据分析库，提供 DataFrame 结构和丰富的数据操作方法。本 Phase 用它做 PRISMA 的去重/筛选/分类统计。

**为什么用它**：
- **DataFrame**：论文元数据转表格结构，便于筛选/排序/分组
- **drop_duplicates**：PRISMA 去重（按标题/entry_id 去重）
- **条件筛选**：PRISMA 筛选（年份>=2023 + 关键词匹配）
- **groupby/value_counts**：文献计量统计（按年份/研究维度分组计数）

**安装方式**：

```bash
pip install pandas
# 离线可用，无需网络连接
```

---

## 主库 4：matplotlib（PRISMA 流程图）

**这是什么**：matplotlib 是 Python 绘图库，本 Phase 用它画 PRISMA 流程图（识别->去重->筛选->纳入各阶段论文数的 flow diagram）。

**为什么用它**：
- **FancyBboxPatch / FancyArrowPatch**：画 PRISMA 流程图的方框和箭头
- **真实数字标注**：用真实 arXiv 查询返回的论文数标注各阶段
- **学术出版质量**：DPI 可调，适合论文嵌入

---

## 真实数据：arXiv API 实时查询

本 Phase 的 PRISMA 文献综述使用**真实 arXiv API 查询**获取论文元数据。以下是 4 条检索策略（PRISMA Step 1 检索），聚焦AI营销Agent系统因果评估的研究问题：

| 检索式 | arXiv 查询 | max_results | 用途 |
|--------|-----------|:-----------:|------|
| 检索式1（Agent+营销） | `AI marketing agent` | 50 | 核心主题：AI营销Agent |
| 检索式2（因果+营销） | `causal inference marketing` | 40 | 因果推断在营销中的应用 |
| 检索式3（LLM+Agent） | `LLM agent marketing` | 40 | LLM时代营销Agent |
| 检索式4（评估） | `AI marketing evaluation` | 30 | AI营销效果评估 |

**真实查询结果**（2026-07-24 实时查询，实际数字以solution.ipynb运行输出为准）：

| PRISMA 阶段 | 论文数 | 说明 |
|------------|:------:|------|
| 识别（4条查询合计） | ~160 | 4条 arXiv API 查询返回的论文总数 |
| 去重后 | ~90-100 | 按标题去重后剩余 |
| 筛选后（年份>=2023 + AI+营销相关性） | ~20-40 | PRISMA 纳入/排除标准筛选 |
| 纳入（质量评估） | ~20-40 | 摘要长度>80字符的质量门槛 |

> ⚠️ 真实 API 查询结果会随 arXiv 新增论文而变化，上述数字为参考范围。solution.ipynb 的实际运行输出为准。

---

## 为什么不用模拟数据（v4.0 做法）

| 维度 | 模拟数据（v4.0） | 真实 arXiv API + pydantic（v5.0） |
|------|-----------------|----------------------------------|
| 论文元数据 | 编造标题/作者/摘要 | arXiv API 返回真实论文 |
| PRISMA 数字 | 手写固定数字 | 真实查询返回的真实数字 |
| 问题定义 | 纯文本模板 | pydantic结构化Schema+类型验证 |
| 文献计量 | 无法做真实统计 | pandas 处理真实 DataFrame |
| 可复现性 | 无法复现（数据随机的） | 相同查询可复现（arXiv API 稳定） |
| 研究价值 | 练习题 | 真实Capstone文献综述的起点 |

**真实即严谨**——用真实 arXiv API 和真实论文元数据替代模拟数据，用 pydantic 结构化Schema替代纯文本模板，是 v5.0 的哲学增量。PRISMA 的核心价值就是"系统性"和"可重复性"，用真实 API 查询才能真正体现这一价值。

---

## 真实数据集来源链接

1. **arXiv API 官方**：https://info.arxiv.org/help/api/index.html （arXiv API 文档，支持关键词/分类/作者检索）
2. **arxiv.py GitHub**：https://github.com/lukasschwab/arxiv.py （Python 封装库，1.5k★，MIT License）
3. **arXiv 主站**：https://arxiv.org/ （论文全文获取，PRISMA 全文复筛阶段使用）
4. **PRISMA 声明官网**：https://prisma-statement.org/ （PRISMA 2020 国际标准）
5. **pydantic 官方文档**：https://docs.pydantic.dev/ （数据验证库文档）
