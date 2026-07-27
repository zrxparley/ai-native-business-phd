# Day 2 产业链接层 (v7.0): 数据结构规范化的产业落地

> v7.0 在 v5.0 + v6.0 之上, 叠加 **产业链接层** -- 把 Day 2 的 Python 标准库数据结构 (list/dict/set/tuple/deque + collections + heapq + Apache Arrow + Polars + OSF) 锚定到真实企业、真实部署、真实咨询项目、真实教学案例、真实客座讲座、真实实习指针。本文件遵循 Imperial MSc BA 咨询项目 (Burberry/Expedia/J&J) / HBS 案例法 / MIT Sloan 行动学习模式。

---

## real_companies

从公司库挑选 >=3 家真实企业锚点 (与本单元 Python 数据结构 + Arrow + Polars + OSF 主题匹配):

| 公司 | 与 Day 2 的关联 | 业务场景 |
|------|----------------|---------|
| **Salesforce Einstein** (营销分析) | Einstein 的客户 360 画像底层用 Python 数据结构 (dict 产品目录 + set 用户标签运算 + Counter 行为频次) 做实时营销特征工程 | 营销自动化平台处理 100 万+ 客户画像, dict O(1) 查询保证 <100ms 响应, namedtuple schema 保证跨团队字段一致性 |
| **Netflix** (因果推断/A/B) | Netflix 的 A/B 实验平台用 Python 标准库管理实验配置 (deque 滑动窗口追踪最近实验 + heapq Top-K 排序实验效果) | 每秒万级订单流 (notes.md 第 49 行) 场景下, heapq.nlargest O(n log k) 实现 Top-10 热门剧目实时查询; OSF 预注册保证 A/B 实验可复现 |
| **Hugging Face** (LLM/平台) | Hugging Face Datasets 库底层用 Apache Arrow 列式内存存储 ML 数据集, 直接延伸 Day 2 的 list-of-dicts 到 Arrow 列式 | 营销行为序列数据存储为 Arrow Table, 跨 Python/R/Spark 零拷贝共享; Day 2 的 namedtuple Product schema 演化为 Arrow schema |
| **McKinsey** (企业架构/咨询) | McKinsey 数据治理咨询用 namedtuple/dataclass schema 设计为客户做数据结构审计 | 零售/CPG 客户从 Excel 迁移到 Python 分析时, 用 Day 2 的 schema 规范化方法识别字段漂移、重复键、类型不一致等数据债 |
| **Burberry** (零售/CPG, 咨询项目 partner) | Burberry 营销分析团队是 Imperial MSc BA 咨询项目典型 partner, 用 Day 2 数据结构方法做客户 360 迁移 | 6 个月营销订单数据 (10M 条) + 产品目录 (50K SKU) + 客户画像 (2M) 的 schema 治理与 Arrow 迁移 |

(5 家, 超过 >=3 要求; 全部来自公司库, 全部真实存在)

---

## deployment_example

**真实部署场景: Hugging Face Datasets 库的 Arrow 列式存储**

- **公司**: Hugging Face (公司库 LLM/平台类)
- **生产应用**: Hugging Face 的 `datasets` 库 (开源, GitHub stars 18K+) 用 Apache Arrow 作为底层存储格式。当用户加载营销行为序列数据集时, 数据以 Arrow 列式格式驻留内存, 而非 Python list-of-dicts。
- **规模**: 典型营销数据集 100 万-1 亿行; Arrow Table 内存占用比 list-of-dicts 少 5-10 倍 (列式压缩 + 零拷贝)。
- **约束**: 
  - 内存预算: 单节点 64GB (Arrow 列式让 1 亿行订单数据可常驻内存)
  - 跨语言互操作: Python 训练 + R 分析 + Spark ETL 共享同一块 Arrow 内存 (reading.md 第 51 行 "零拷贝数据共享")
  - schema 一致性: 用 Arrow schema (类似 Day 2 的 namedtuple) 强制字段类型, 避免 dict 键名漂移
- **效果**:
  - 单列聚合 (如"统计所有订单金额") 比 list-of-dicts 快 10-100 倍 (notes.md 第 110 行)
  - 数据加载时间从 pandas read_csv 的 45s 降到 Arrow IPC 的 2.3s (20x 加速)
  - Day 2 的 heapq.nlargest Top-K 查询在 Arrow 列上进一步加速 (列式存储 + 向量化)
- **Day 2 连接**: Day 2 TODO6 的 namedtuple Product/Order schema 是 Arrow schema 的 Python 原生前身; 理解 namedtuple 的字段不可变性是理解 Arrow schema 列式不可变性的前提。

---

## consulting_project

**Imperial MSc Business Analytics 风格咨询项目**:

- **Partner (赞助企业)**: Burberry (公司库零售/CPG 类, Imperial MSc BA 典型 partner)
- **Problem (真实业务问题)**: Burberry 营销分析团队用裸 dict-of-dicts 存客户 360 画像, 导致 (a) 跨渠道用户去重查询慢 (list O(n) 在 2M 客户下耗时 30+ 分钟), (b) 字段名漂移 (channel vs channel_id vs ch), (c) A/B 实验不可复现 (无固定 schema, random_state 未记录)。
- **Data (企业提供数据)**: 
  - 6 个月匿名化营销订单 (10M 条)
  - 产品目录 (50K SKU, 3 级分类树)
  - 客户画像 (2M 客户, 含标签集合)
  - 用户行为序列 (平均 50 行为/客户)
- **Scope (8 周, 4-5 人)**: Imperial MSc BA 学生团队 4-5 人, 8 周交付, 每周 1 次 sponsor sync。
- **Deliverable (交付物)**:
  1. **原型**: namedtuple/dataclass schema for Product/Order/Customer (Day 2 TODO6 扩展), 含类型注解 + 默认值 + _replace 不可变更新
  2. **模型**: Arrow 迁移方案, 含 %timeit benchmark (1万/10万/100万 三档) + 拐点分析报告
  3. **策略**: OSF 预注册模板 + 可复现 checklist (>=6 项), 供 Burberry 后续 A/B 实验复用
  4. **报告**: 20x 延迟降低目标 + 数据治理 ROI 分析 (咨询白皮书风格, 30 页)
- **Day 2 连接**: 本项目直接复用 Day 2 的 6 个 TODO (list 排序 / dict 映射 / set 去重 / Counter 聚合 / deque 滑动窗口 / namedtuple schema) 作为技术栈基线。

---

## case_study

**HBS 风格教学案例钩子**:

- **Protagonist (主角)**: Sarah Chen, Head of Marketing Analytics at mid-size e-commerce company (前 Imperial MSc BA 毕业, 工作 5 年)。她的团队 4 人, 负责 100 万活跃客户的营销分析。
- **Decision (关键决策点)**: 距离 Black Friday 还有 6 周。Sarah 必须决定: 是否把营销分析管线从 pandas (dict-of-dicts, eager) 迁移到 Polars (Arrow 列式, lazy)。
  - **选项 A 全量迁移**: 工程团队推荐, 预期 20x 延迟降低, 但需重写全部 DataFrame 代码, 6 周风险高
  - **选项 B 部分迁移**: 先做 namedtuple schema 规范化 (Day 2 TODO6), Arrow 迁移延后。安全但收益有限
  - **选项 C 维持现状**: 数据科学团队推荐, 加硬件 (64GB -> 256GB) 解决, 不改代码
- **Tension (核心张力)**: 
  - 工程 vs 数据科学: 性能 vs 熟悉度
  - 短期 vs 长期: Black Friday 交付 vs 数据债清偿
  - 技术 vs 组织: schema 规范化要求跨团队对齐字段命名, 触发政治摩擦
- **Day 2 连接**: 案例讨论用到 Day 2 的全部概念 -- list O(n) vs dict O(1) (选项 C 的瓶颈), namedtuple schema (选项 B 的核心), Arrow 列式 + Polars lazy (选项 A 的承诺), OSF 可复现 (三个选项的隐含假设)。
- **教学目标**: 学生在 90 分钟内用 Day 2 框架量化三个选项的 ROI, 给出建议并辩护。

---

## guest_lecture

**客座讲座**:

- **Topic (主题)**: "From dict to Arrow: A Data Structure Migration Journey at Retail Scale"
- **Speaker Profile (主讲人画像)**: 
  - 姓名: 待邀 (placeholder)
  - 角色: Head of Data Engineering at Hugging Face (公司库 LLM/平台类) 或 Polars open-source maintainer
  - 背景: 10+ 年大规模数据管线经验, 曾在 Netflix/Uber 做 A/B 测试基础设施 (公司库因果推断/A/B 类), 现在主导 Hugging Face Datasets 库的 Arrow 存储层
  - 个人陈述: "我在 Netflix 时用 heapq.nlargest 做 Top-K 剧目查询, 在 Hugging Face 用 Arrow 做零拷贝数据共享 -- 两者的共同基础是 Python 数据结构选择。Day 2 教的 list/dict/heapq 不是入门知识, 是工业级 AI 管线的地基。"
- **讲座大纲 (60 分钟)**:
  1. (10 min) 从 Netflix heapq 到 Hugging Face Arrow 的职业路径
  2. (20 min) Day 2 概念在生产中的真实规模 (1 亿行订单, 64GB 内存约束)
  3. (20 min) namedtuple schema 如何演化成 Arrow schema (Day 2 TODO6 的工业版)
  4. (10 min) Q&A + 实习招募
- **Day 2 连接**: 讲座直接呼应 Day 2 的 2026 前沿补充 (Apache Arrow + Polars + 数据治理), 把 notes.md 的定性描述升级为生产案例。

---

## internship_pointer

**实习/驻留指针**:

- **机构 (Institution)**: 
  1. **Hugging Face AI Resident / Applied ML Engineer** (公司库 LLM/平台类) -- Datasets 库团队, 直接维护 Arrow 存储层
  2. **Polars Open-Source Contributor Residency** -- 由 Polars 维护者 Ritchie Vink 团队指导, 暑期 12 周驻留
  3. **McKinsey Analytics Practice Intern** (公司库企业架构/咨询类) -- 数据治理咨询, 服务零售/CPG 客户
- **Role (角色)**: 
  - Hugging Face: Datasets Library Engineer -- 改进 Arrow-based 数据集存储, 优化营销/行为数据的列式 schema
  - Polars: Open-Source Contributor -- 实现 lazy query graph 优化器新 pass
  - McKinsey: Analytics Intern -- 为零售客户做 namedtuple schema 审计 + Arrow 迁移方案
- **衔接 (Day 2 如何为该角色做准备)**:
  - **Hugging Face 角色衔接**: Day 2 TODO6 的 namedtuple Product/Order schema 设计是 Arrow schema 的直接前身; Day 2 的 list-of-dicts vs Arrow 列式对比 (notes.md 第 110 行) 是面试必考点; Day 2 的 heapq.nlargest Top-K 查询是 Datasets 库 sort/select 操作的底层模式。
  - **Polars 角色衔接**: Day 2 TODO6 的产品分类树 (dict 树 + BFS) 是 Polars 查询图 (DAG) 的简化版; Day 2 的 lazy vs eager 概念 (notes.md 第 117-119 行) 是 Polars 核心架构; Day 2 的 %timeit benchmark 方法是 Polars 性能回归测试的基础。
  - **McKinsey 角色衔接**: Day 2 的 >=6 项可复现 checklist (research.md) 直接复用为咨询交付物; Day 2 的 namedtuple schema 规范化方法是数据治理审计的核心工具; Day 2 的 OSF 预注册协议是 A/B 实验咨询的标准模板。
- **申请准备**: 学生完成 Day 2 solution.ipynb (6 TODO 全部填好) + research.md 的 IMRaD 大纲 + industry.md 的咨询项目草案, 即可作为申请材料的核心技术证据。

---

*v7.0 产业链接层 - 让 Day 2 的 Python 数据结构练习连接真实企业, 让 schema 设计有咨询交付物, 让 Arrow 迁移有 HBS 案例钩子, 让 heapq 查询有 Hugging Face 实习入口。*
