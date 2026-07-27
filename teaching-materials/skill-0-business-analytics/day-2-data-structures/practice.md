# 刻意练习 - Day 2 数据结构与应用 (v6.0 学习科学层)

> Ericsson 刻意练习 5 要素 + MIT 提取练习/交叉/Worked-Faded + Biggs 建构对齐
> 真实库锚点: Python 标准库 (list/dict/set/tuple/deque) + collections (Counter/defaultdict/namedtuple) + heapq

---

## skill_target

能在营销订单/产品/客户/行为数据场景下, **自主选择并实现** Python 标准库数据结构 (list/dict/set/tuple/deque + collections + heapq), 用 `%timeit` 实测 O(1) vs O(n) 差距, 并用 namedtuple 设计可治理的数据 schema -- 在 10 万级数据规模下达到正确 + 可解释 + 可复现三重门槛。

---

## subskills

- **S1 结构选择**: 能根据查询模式 (按值/按键/按序/去重/两端) 在 list/dict/set/tuple/deque 中做时间复杂度论证, 阐述"为什么选 A 不选 B"
- **S2 collections 聚合**: 能用 Counter.most_common 做销量排行、defaultdict(list) 做渠道分组、namedtuple 设计 Product/Order 不可变 schema
- **S3 高级结构与前沿**: 能用 heapq.nlargest 实现 O(n log k) Top-K、用 deque(maxlen=) 实现滑动窗口, 并阐述 Apache Arrow 列式内存与 Polars 懒求值如何延续这些工程权衡

---

## diagnostic (pset0 式先测, 不通过则回退 worked example)

> 提交 starter.ipynb 前先做这 3 题, 每题 90 秒, 不查文档。这是 Biggs "Feed Up" 的基线锚点。

**Q1 (诊断 S1)**: 给定 `orders = [{"product_id": "P{}".format(i), "amount": i*10} for i in range(100000)]`, 实现"查询 product_id == "P50000" 的 amount", 你会用哪种结构 + 为什么? 写出时间复杂度。

**Q2 (诊断 S2)**: 用 `collections.____` 一行代码统计 `["apple","banana","apple","cherry","apple","banana"]` 中各水果出现次数并取 Top 2。

**Q3 (诊断 S3)**: 实时流式订单, 每秒万级, 要维护"最近 100 个订单" + "当前 Top 10 热销商品"。用哪两个 Python 标准库结构?

---

## drills (>=3, 每个含 drill_id/difficulty/reps_required/feedback_rule/worked_faded)

### drill_id: D1
- **difficulty**: 2
- **reps_required**: 3
- **feedback_rule**: 若学生用 list 做产品目录查询 (O(n)) 或答不出 O(1) vs O(n) 差距倍数, 反馈: "用 `%timeit` 在 10 万级 list 和 dict 上各跑 `product_id in container`, 对比 ns 量级; 重读 Python 官方 dict 实现原理 (hash table)。" 失败 2 次触发 weak_loop: 回退到 worked example (见下), 用 `collections.ChainMap` 做多源 dict 合并的演示再重做。
- **worked_faded** (三阶段):
  - **Worked (完整示范)**: 教师演示 `product_catalog = {"P001": {...}, "P002": {...}}; product_catalog.get("P001", None)` -- 解释 hash table O(1)
  - **Faded (部分填空)**: 给出 `product_catalog = ____` 和 `product_catalog.____("P999", default=____)`, 学生填空
  - **Independent (独立解)**: 学生独立实现"给定 10 万产品 list of dicts, 构建产品目录 dict 并查询 P50000, 用 %timeit 对比 list.index() 与 dict[]"

### drill_id: D2
- **difficulty**: 3
- **reps_required**: 3
- **feedback_rule**: 若学生手写 for 循环计数 (而非 Counter) 或用 dict.setdefault 而非 defaultdict(list), 反馈: "查看 `collections.Counter` 源码模式 -- 它继承 dict, `__missing__` 自动初始化为 0; `defaultdict(list)` 的 `__missing__` 调用 `list()` 自动建空 list。这是 Pythonic 的'告知宽恕非许可'。重做时禁止用 `if key not in d`。" 失败 2 次触发 weak_loop: 回退 D1 + 补充 worked example (`Counter("abracadabra").most_common(3)` 演示)。
- **worked_faded**:
  - **Worked**: `sales = Counter(order["product_id"] for order in orders); sales.most_common(10)` -- 教师口述 Counter 继承 dict 的设计
  - **Faded**: `sales = ____.____(o["product_id"] for o in orders); sales.____(10)` -- 学生填空
  - **Independent**: 学生独立实现"按渠道分组订单 (defaultdict(list)) + 商品销量 Top 10 (Counter.most_common)", 并对比手写循环的代码行数

### drill_id: D3
- **difficulty**: 4
- **reps_required**: 3
- **feedback_rule**: 若学生用 `sorted(orders, key=lambda x: -x["amount"])[:10]` 而非 `heapq.nlargest(10, orders, key=...)`, 或答不出 O(n log k) vs O(n log n) 差异, 反馈: "看 `heapq.nlargest` 文档: 当 k << n 时, 用大小为 k 的最小堆维护候选, 每个元素 O(log k) 进出堆, 总 O(n log k)。用 `%timeit` 对比 `sorted()[:10]` 与 `heapq.nlargest(10, ...)` 在 n=10^6, k=10 下的耗时差。" 失败 2 次触发 weak_loop: 回退 D2 + worked example (`heapq.nlargest(3, [1,5,2,8,3])` 逐步推演堆状态)。
- **worked_faded**:
  - **Worked**: 教师演示 `heapq.nlargest(10, orders, key=lambda o: o["amount"])` + `deque(maxlen=100)` 滑动窗口, 用图示推演最小堆的 sift-up/sift-down
  - **Faded**: `import heapq, collections; top10 = heapq.____(10, orders, key=____); recent = collections.____(maxlen=100)` -- 学生填空
  - **Independent**: 学生独立实现"流式订单: deque 维护最近 100 单 + heapq 维护 Top 10 热销, 用 namedtuple 设计 Order schema, 阐述 Arrow 列式内存如何在此基础上进一步提速"

---

## progressive_project (脚手架渐退, MIT/Stanford 模式)

> 贯穿本 Day + 衔接 Day 3-5, 4 阶段交付, 每阶段独立评分。

- **proposal** (Day 2 第 1h): 选 1 个营销场景 (订单排序/产品查询/标签运算/行为聚合/路径模拟), 写 200 字方案: 选哪些数据结构? 为什么? 预期 O(?) 复杂度? (评分: 论证合理性 50% + 复杂度正确 50%)
- **milestone** (Day 2 第 3h): 实现核心聚合 -- Counter 销量排行 + defaultdict 渠道分组, 用 %timeit 实测, 提交 .ipynb + 200 字反思 (评分: 代码正确 60% + 实测数据 20% + 反思深度 20%)
- **final** (Day 2 作业周): 完整版 -- Top-K (heapq) + 滑动窗口 (deque) + namedtuple schema + 产品分类树 (dict + BFS), 跑通 10 万级数据, 提交 .ipynb + 500 字架构说明 (评分: 完整性 40% + 性能论证 30% + 可治理性 30%)
- **poster** (Day 5 衔接): 1 页 PDF 海报 -- 对比 list-of-dicts (行式) vs Apache Arrow (列式) vs Polars (lazy) 在你的营销场景下的性能, 用真实 %timeit 数据 (评分: 对比清晰 40% + 数据真实 30% + 可视化 30%)

---

## interleaving (A1B1C1...B2C2A2...C3A3B3, 禁块状)

> MIT Open Learning 明文原则: 交叉练习 (interleaving) 比块状练习 (blocking) 提升长期保留 40%+。本 Day 不按 "list → dict → set → ..." 顺序练, 而按下列螺旋交叉:

- **A = 结构选择 (S1)**, **B = collections 聚合 (S2)**, **C = 高级/前沿 (S3)**

| 轮次 | 序列 | 任务 |
|:---:|:---:|---|
| 1 | A1 | 给 1k 订单 list, 选结构做"按金额排序 Top 5" |
| 1 | B1 | 用 Counter 统计 1k 订单的商品频次 Top 3 |
| 1 | C1 | 用 deque(maxlen=10) 维护最近 10 次浏览 |
| 2 | B2 | 用 defaultdict(list) 按 channel 分组 1k 订单 |
| 2 | C2 | 用 heapq.nlargest(5, ...) 取 1k 订单金额 Top 5 |
| 2 | A2 | 给 10k 产品, 选结构做"按 product_id 查询" (dict vs list 对比) |
| 3 | C3 | 用 namedtuple 定义 Order schema + 阐述 Arrow 列式如何提速 |
| 3 | A3 | 给 10k 用户标签 set, 做跨渠道交集/差集 |
| 3 | B3 | 用 Counter + defaultdict 组合: 按渠道分组后取每渠道 Top 3 商品的销量 |

**禁止**: 一次连续做 3 个 A 再做 3 个 B (块状) -- 块状短期分数高但 1 周后遗忘率 60%, 交叉短期分数低 10% 但 1 周后保留率高 40% (Butler 2010, RER)。

---

## retry_policy

- 每次 drill 提交后, 反馈在 24h 内返回 (NUS Autograder 模式)
- **late penalty**: 借鉴 Stanford CS230 -- 每迟 1 天扣 20%, 最多迟 5 天 (5 late days free, 之后 0 分)
- **retry window**: 一个 drill 最多重做 3 次, 第 2 次起必须附 200 字反思 (哪里错了 + 为什么 + 怎么改)
- **重做条件**: 单次得分 < 70% 触发重做; 连续 2 次 < 70% 触发 weak_loop

---

## weak_loop (弱项循环, 连续 2 次失败触发)

```
触发条件: drill D_n 连续 2 次得分 < 70%
      ↓
回退:  回到 D_{n-1} (或 D1 若 n=1)
      ↓
补充:  看该 drill 的 Worked 示例 (教师完整推演)
      ↓
重做:  Faded 阶段 (填空版) 1 次
      ↓
升级:  再回到 D_n Independent 阶段
      ↓
记录:  在 student_model.json 标记 D_n 为 "weak", 下次 schedule.json 复习间隔减半
```

**真实库锚点**: weak_loop 触发时, 反馈必须引用本单元真实库的具体函数/源码模式 (如 `collections.Counter.__missing__`、`heapq._siftdown`、`dict.__getitem__` 的 hash table 实现), 而非泛泛说"再练一次"。

---

## mastery 自检 (Biggs Feed Forward)

- [ ] 我能在不查文档的情况下, 说出 list/dict/set/tuple/deque 各自的查询复杂度
- [ ] 我能用 Counter 一行代码完成销量排行, 用 defaultdict 一行代码完成渠道分组
- [ ] 我能用 heapq.nlargest 实现 Top-K 并说出 O(n log k) 的来历
- [ ] 我能用 namedtuple 设计 Product/Order schema, 并从数据治理角度论证 vs 裸 dict
- [ ] 我能阐述 Apache Arrow 列式内存如何延续 list-of-dicts 的工程权衡

*5 项全勾 = mastery 达成, 可进入 Day 3 SQL; < 4 项 = 回 weak_loop。*
