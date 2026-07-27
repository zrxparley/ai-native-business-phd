# Constructive Alignment - Day 2 数据结构与应用 (v6.0)

> Biggs (1996) 建构对齐 (Constructive Alignment): ILO (Intended Learning Outcomes) ↔ TLA (Teaching/Learning Activities) ↔ AT (Assessment Tasks) 三者必须对齐, 否则学生可通过"不经 TLA"路径过 AT = 对齐失败。
> 本单元 v5.0 上机任务 (starter.ipynb 6 个 TODO) + v6.0 学习科学层 (practice.md / schedule.json / tutorial.ipynb) 共同构成 TLA。

---

## ILO ↔ TLA ↔ AT 矩阵

| ILO (预期学习产出) | TLA (教学学习活动) | AT (评估任务) | mastery_threshold |
|---|---|---|---|
| **ILO1**: 能解释 list/dict/set/tuple/deque 五种 Python 内置结构的时间复杂度 (O(1) vs O(n)), 并在营销订单/产品/客户场景下论证"为什么选 A 不选 B" | starter.ipynb TODO1-3 (list/dict/set 上机) + practice.md drill D1 (worked-faded) + tutorial.ipynb Socratic loop 第 1-2 轮 + schedule.json C1 间隔复习 | solution.ipynb TODO1-3 解题 + practice.md diagnostic Q1 + tutorial 后测: 口头辩护"10 万级产品查询为何用 dict" | >=80% (复杂度论证全对 + %timeit 实测正确) |
| **ILO2**: 能用 collections.Counter 做销量计数、defaultdict 做渠道分组、namedtuple 设计 Product/Order 不可变 schema | starter.ipynb TODO4 + TODO6 (Counter/defaultdict/namedtuple 上机) + practice.md drill D2 (worked-faded) + schedule.json C2 间隔复习 + interleaving B1/B2/B3 交叉练习 | solution.ipynb TODO4 + TODO6 + progressive_project milestone (Counter+defaultdict 实测) + tutorial Socratic 第 3 轮"为什么 defaultdict 而非 setdefault" | >=70% (代码正确 + Pythonic 模式 + 反思 200 字) |
| **ILO3**: 能用 heapq.nlargest 实现 O(n log k) Top-K、用 deque(maxlen=) 实现滑动窗口, 并阐述 Apache Arrow 列式内存 + Polars 懒求值如何延续这些工程权衡, 理解 OSF 可复现研究对数据结构规范化的要求 | starter.ipynb TODO5 (deque) + practice.md drill D3 (worked-faded) + schedule.json C3+C4 间隔复习 + interleaving C1/C2/C3 + reading.md Apache Arrow/Polars 深链 | solution.ipynb TODO5 + progressive_project final (Top-K+滑动窗口+namedtuple+分类树) + poster (Arrow vs list-of-dicts 对比) | 能独立解 (无脚手架, 10 万级数据跑通, 500 字架构说明) |

---

## mastery_threshold (整体)

- **本 Day mastery 达成线**: ILO1 >=80% AND ILO2 >=70% AND ILO3 能独立解
- **触发 weak_loop**: 任一 ILO 连续 2 次低于阈值
- **进入 Day 3 SQL 前提**: 本 Day mastery 达成 + 5 项自检全勾 (见 practice.md 末尾)
- **不达标后果**: 回 weak_loop, schedule.json 复习间隔减半 (FSRS request_retention 临时降至 0.85 加权)

---

## 3 自检问题 (Biggs + Hattie 形成性反馈三问)

> Hattie (2007 RER 77(1):81-112) 形成性反馈三问: Feed Up (去哪) / Feed Back (现在哪) / Feed Forward (下一步去哪)。本单元每条 ILO 必须能回答这三问, 否则对齐失败。

### 1. Feed Up - TLA 是否训练 ILO? (目标校准)

- ILO1 要求"解释复杂度差异", TLA 中的 drill D1 worked-faded 是否真的让学生推演 hash table? -- **是**: D1 Worked 阶段教师口述 dict hash table 实现, Faded 阶段学生填 `product_catalog.get(...)` 并 %timeit 对比, Independent 阶段独立实现 10 万级对比。
- ILO2 要求"用 Counter/defaultdict/namedtuple", TLA 中的 TODO4 + drill D2 是否覆盖? -- **是**: TODO4 上机 + D2 三阶段 worked-faded, feedback_rule 明确禁 `if key not in d` 手写模式。
- ILO3 要求"heapq + deque + Arrow 论证", TLA 中的 TODO5 + drill D3 + reading.md 是否覆盖? -- **是**: D3 worked 推演 sift-up/sift-down, reading.md 含 Apache Arrow / Polars 深链。

**自检结论**: TLA 全覆盖 ILO, 无遗漏。

### 2. Feed Back - AT 是否测量 ILO? (现状校准)

- AT1 (solution.ipynb TODO1-3 + diagnostic Q1) 是否真能测出 ILO1? -- **是**: diagnostic Q1 要求写出时间复杂度, 不是只跑代码; solution.ipynb 要求 %timeit 实测, 不是只交答案。
- AT2 (TODO4/TODO6 + milestone) 是否真能测出 ILO2? -- **是**: milestone 要求 200 字反思 + Pythonic 模式评分, 不只看代码跑通。
- AT3 (final + poster) 是否真能测出 ILO3? -- **部分**: final 测代码, poster 测 Arrow 论证 -- 但"OSF 可复现研究对 schema 规范化的要求"在 AT 中权重偏低, 下次迭代需在 final 加 100 字 OSF 论证。

**自检结论**: AT 基本测量 ILO, ILO3 的 OSF 维度待补强。

### 3. Feed Forward - 不经 TLA 能过 AT 吗? (对齐失败检测)

> Biggs 警告: 如果学生不经 TLA (不上机、不练 drill、不读 reading) 也能过 AT (solution 跑通), 则对齐失败 -- 学生用了"应试路径"而非"建构路径"。

- **风险点 1**: 学生抄 solution.ipynb 过 TODO -- **缓解**: solution gated (做完才看), diagnostic Q1 在 starter 前做, tutorial Socratic 口头辩护查过程理解。
- **风险点 2**: 学生用 pandas DataFrame 绕过 list/dict 直接做聚合 -- **缓解**: AT 明确要求"用 Python 标准库 + collections + heapq", pandas 路径在 milestone 评分扣 50%。
- **风险点 3**: 学生背"dict 是 O(1)"而不理解 hash table -- **缓解**: tutorial Socratic 第 1 轮必问"hash 冲突时 dict 还是 O(1) 吗", 答不出触发 weak_loop。

**自检结论**: 3 个风险点均有缓解, 对齐基本成立。但 tutorial 限频 1 次/天 (见 tutorial.ipynb cell 6) 防止学生把 Socratic 当答案机, 保留"建构"而非"获取"路径。

---

## 跨单元衔接 (Feed Forward 纵向)

- **前接 Day 1**: Day 1 Python 基础 -> Day 2 数据结构 (本 Day 是 Day 1 的工程化)
- **后接 Day 3 SQL**: 本 Day ILO1 的 dict 映射 -> Day 3 SQL JOIN/GROUP BY, schedule.json C1 在 Day 3 复习
- **后接 Day 4 数据清洗**: 本 Day ILO2 的 collections 聚合 -> Day 4 pandas 向量化, schedule.json C2 在 Day 4 复习
- **后接 Day 5 数据管理**: 本 Day ILO3 的 namedtuple schema + Arrow -> Day 5 DVC + 数据血缘, schedule.json C3/C4 在 Day 5 复习
- **后接技能1 表示工程**: 本 Day 的"list->dict->schema"是 embedding 表示的原始数据层

*本对齐表是 v6.0 学习科学层的建构对齐锚点, 与 v5.0 上机任务互补不冲突。*
