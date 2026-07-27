# Constructive Alignment - Python 编程基础 (pandas / numpy / Apache Arrow / Polars)

> v6.0 学习科学层 · Biggs 建构对齐 (ILO ↔ TLA ↔ AT) + mastery threshold
> 适用单元: skill-0-business-analytics / day-1-python-fundamentals
> 哲学: 不经 TLA 能过 AT = 对齐失败 (Biggs 1996)

---

## ILO ↔ TLA ↔ AT 矩阵

| ILO (预期学习产出) | TLA (教学学习活动) | AT (评估任务) | mastery_threshold |
|---|---|---|---|
| ILO1: 能用 pandas 加载营销数据 (产品/客户/订单) 为 DataFrame, 用 dtypes/head/describe/info 识别前导零丢失/日期解析错误/缺失值等数据质量问题 | starter.ipynb TODO1-2 (填空脚手架) + practice.md D1 三阶段 worked-faded + tutorial.ipynb Socratic 第 1-2 轮追问 + schedule.json C1 间隔复习 | solution.ipynb TODO1-2 完整解 + tutorial.ipynb 后测口述 "customer_id 00123 读成 int 会发生什么不可逆损失" | >=80% (D1 reps 3 次全过) |
| ILO2: 能用 Python 控制流 (if-elif-else) + df.apply() 实现 RFM 客户分类, 并解释 apply 比 for 循环快 10-100x 的向量化原理, 能用 np.select 重写 | starter.ipynb TODO3 (填空) + practice.md D2 三阶段 worked-faded + tutorial.ipynb Socratic 第 3 轮 "凭什么 apply 比 for 快" + schedule.json C2 间隔复习 + interleaving A1B1C1 交叉 | solution.ipynb TODO3 完整 RFM 解 + tutorial.ipynb 后测 "向量化 vs Python 解释器开销, 哪一行触发" | >=80% (D2 reps 3 次全过, 含 np.select 重写版) |
| ILO3: 能用 pandas + numpy 计算 ROI/转化率/客单价 AOV/复购率, 用 to_csv/read_json 读写, 固定 random_state=42, 能口述 pandas 2.x Arrow 后端 vs Polars LazyFrame 取舍 | starter.ipynb TODO5-6 (填空) + practice.md D3 三阶段 worked-faded + tutorial.ipynb Socratic 第 4 轮 "Arrow 凭什么零拷贝" + schedule.json C3-C4 间隔复习 + progressive_project final 阶段 | solution.ipynb TODO5-6 完整解 + progressive_project final + poster 同伴互评 + tutorial.ipynb 后测 "除零时 np.divide where 与 replace(0,nan) 区别" | >=80% (D3 reps 3 次全过 + 300 字分析报告合格) |

---

## 3 自检问题 (Biggs Feed Up / Feed Back / Feed Forward)

### 1. Feed Up - TLA 是否训练 ILO? (学生知道在练什么吗)
- D1 的 worked-faded 三阶段是否让学生明确知道"我现在在练 dtype 治理"而非"在写 read_csv"?
- starter.ipynb 的 6 个 TODO 是否每个都映射到 ILO1/ILO2/ILO3 之一? (本单元: TODO1-2→ILO1, TODO3-4→ILO2, TODO5-6→ILO3)
- tutorial.ipynb 的 Socratic 追问是否覆盖三个 ILO 各至少 1 次? (本单元: 第 1-2 轮→ILO1, 第 3 轮→ILO2, 第 4 轮→ILO3)

### 2. Feed Back - AT 是否测量 ILO? (学生知道哪里没过关吗)
- solution.ipynb 对照后, 学生能否指出自己卡在 D1/D2/D3 哪一阶段?
- mastery_threshold >=80% 是否对应 ILO 的可观察行为 (能跑通 + 能口述 + 能复用), 而非"代码能跑"?
- progressive_project final 阶段的 300 字分析报告是否测量了 ILO3 的"口述取舍依据", 还是只测了代码?

### 3. Feed Forward - 不经 TLA 能过 AT 吗? 若能 = 对齐失败
- 学生若不练 D1 的 worked-faded, 能直接通过 solution.ipynb 的对照吗? 若能, 说明 AT 太浅, 应加"口述前导零为何不可逆"。
- 学生若不参加 tutorial.ipynb 的 Socratic, 能通过后测吗? 若能, 说明后测仅测代码不测理解, 应加"用 np.select 重写并对比 %timeit"。
- 学生若不做 interleaving A1B1C1 交叉, 仅块状练 D1×3 再 D2×3 再 D3×3, 1 周后保留率是否 <50%? (Butler 2010: 交叉 vs 块状保留率差 43%。若 AT 不测延迟保留, 则对齐失败, 应在 Day 5 后测中加 D1/D2/D3 复用题。)

---

## 与本单元 v5.0/v6.0 文件的交叉引用
- ILO1-3 直接引自 notes.md 学习目标 1-5 (v5.0)
- TLA 引用 starter.ipynb (v5.0) + practice.md D1-D3 (v6.0) + tutorial.ipynb Socratic (v6.0) + schedule.json (v6.0)
- AT 引用 solution.ipynb (v5.0) + tutorial.ipynb 后测 (v6.0) + progressive_project (v6.0)
- mastery_threshold 引用 practice.md weak_loop (连 2 次失败回退)
