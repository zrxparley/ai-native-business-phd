# 建构对齐表 (Constructive Alignment, Biggs 1996) -- 选修E10 · Day 2

> **方法论**：Biggs 建构对齐--预期学习产出 (ILO) ↔ 教学学习活动 (TLA) ↔ 评估任务 (AT) 三者必须对齐，否则学生"猜题"通过而未真正掌握。每行附 mastery 阈值。底部三自检问题 (Feed Up / Feed Back / Feed Forward) 用于学期中持续校准。
> **与各文件的引用关系**：TLA 列引用 `starter.ipynb` / `practice.md` 的 drill / `tutorial.ipynb`；AT 列引用 `solution.ipynb` / `tutorial.ipynb` 的后测。

---

## ILO ↔ TLA ↔ AT 矩阵

| ILO (预期学习产出) | TLA (教学学习活动) | AT (评估任务) | mastery_threshold |
|---|---|---|---|
| **ILO-1** 能用 pydantic 定义四种定价契约 (AaaS订阅 / 按调用计费 / outcome-based / 收益分润) 的 schema，并实现 API Economy 2.0 的 Agent 可发现能力声明 | ① 听讲 `notes.md` §真实库1 pydantic 小节 + 关键回顾1/4<br>② 做 `practice.md` drill-1 (Worked-Faded 三阶段)<br>③ 在 `starter.ipynb` 完成 TODO1 (四种 schema 定义)<br>④ `tutorial.ipynb` Socratic 第2-3轮追问 schema 设计 | ① `solution.ipynb` TODO1 输出四种 pydantic 模型 + `model_validate_json` 通过<br>② `tutorial.ipynb` 后测：给定 Sierra JSON 能否正确 dispatch 到 OutcomeBasedPricing | schema 通过 `model_validate_json` 全字段非负 + Union dispatch 正确率 >=80% |
| **ILO-2** 能用 numpy-financial 对三种定价模式做 12 月 NPV/IRR 对比，量化推理成本 (GPT-4o $5/1M vs DeepSeek V3 $0.27/1M) 对 Agent 利润率的影响，找盈亏平衡推理成本阈值 | ① 听讲 `notes.md` §推理成本 + §真实库2 numpy-financial<br>② 做 `practice.md` drill-2 (Worked Cursor -> Faded Intercom Fin -> Independent Devin+DeepSeek)<br>③ 在 `starter.ipynb` 完成 TODO3+TODO5 (三模式 NPV/IRR + 推理成本敏感度) | ① `solution.ipynb` TODO3 输出三模式 12月 NPV/IRR 表<br>② TODO5 输出推理成本敏感度图，标注盈亏平衡阈值<br>③ `tutorial.ipynb` 后测：推理成本从 GPT-4o 降到 DeepSeek V3，outcome-based NPV 变化多少 | NPV/IRR 计算误差 <5% (与 `solution.ipynb` 参考值对比) + 敏感度结论方向正确 |
| **ILO-3** 能用 statsmodels 拟合定价弹性回归 (log-log OLS: log(采纳率) ~ log(价格))，解释弹性系数与 95% CI，找利润最大化定价点 | ① 听讲 `notes.md` §真实库3 statsmodels + §营销场景映射<br>② 做 `practice.md` drill-3 (Worked OLS -> Faded Lerner -> Independent 9真实案例)<br>③ 在 `starter.ipynb` 完成 TODO4 (弹性回归+最优定价) | ① `solution.ipynb` TODO4 输出 OLS summary (coef / std err / 95% CI / p-value)<br>② 输出 Lerner 最优定价点 + 与真实定价对比<br>③ `tutorial.ipynb` 后测：弹性 -1.4 + p=0.03，该涨价还是降价？ | 弹性方向正确 + p-value<0.05 + Lerner 公式应用正确 + 能解释 95% CI 是否含 -1 |
| **ILO-4** 能解释定价模式演进五阶段 (按席位->按用量->按任务->按结果->按价值分成)，并在营销 Agent 场景设计混合定价方案 (基础费+绩效费+分润) | ① 听讲 `notes.md` §关键回顾2 五阶段表 + §营销场景映射<br>② 读 `reading.md` a16z Agent Economy 深链<br>③ `tutorial.ipynb` Socratic 第1轮追问五阶段归属<br>④ 写 `practice.md` progressive_project proposal (选营销 Agent + 定价假设) | ① `solution.ipynb` 末尾 300 字分析：三种定价模式在学生选定营销场景下哪种最优<br>② `tutorial.ipynb` exit artifact：2-3 盲点 + 推荐复习单元 | 五阶段归属 >=4/5 正确 + 混合定价方案含基础+绩效+分润三要素且逻辑自洽 |
| **ILO-5** 能建立天道推演×商业模式沙盘的同构认知，用三时间线推演 (immediate月/near年/far 3年) 分析推理成本下降/A2A经济/MCP标准化三股力量下的定价演化 | ① 听讲 `notes.md` §天道推演×商业模式沙盘 (特色章节)<br>② 在 `practice.md` progressive_project poster 阶段画三时间线<br>③ `tutorial.ipynb` Socratic 第4轮反例追问"若推理成本不降反升会怎样" | ① progressive_project poster 一页 A3：三栏(schema / 数值 / 三时间线推演)<br>② `tutorial.ipynb` 后测：写出 2026-2028 outcome-based 在三股力量下的演化走向 | 三时间线每条至少 1 个因果节点 + 至少 1 个反事实假设 + 结论与弹性/推理成本数据一致 |

---

## mastery 阈值汇总

| ILO | mastery_threshold | 评估来源 |
|---|---|---|
| ILO-1 | schema `model_validate_json` 全过 + Union dispatch >=80% | solution.ipynb TODO1 + tutorial 后测 |
| ILO-2 | NPV/IRR 误差 <5% + 敏感度方向正确 | solution.ipynb TODO3+5 + tutorial 后测 |
| ILO-3 | 弹性方向正确 + p<0.05 + Lerner 正确 | solution.ipynb TODO4 + tutorial 后测 |
| ILO-4 | 五阶段 >=4/5 + 混合定价三要素自洽 | solution.ipynb 300字分析 + tutorial exit |
| ILO-5 | 三时间线每条 >=1 因果节点 + >=1 反事实 | progressive_project poster + tutorial 后测 |

**单元整体 mastery**：5 个 ILO 全部达标 = 通过；任意 1 个未达标 -> 触发 `practice.md` weak_loop；连续 2 个未达标 -> 触发 `tutorial.ipynb` 牛津 tutorial 仿真。

---

## 三自检问题 (Feed Up / Feed Back / Feed Forward)

> Hattie & Timperley (2007) 三层反馈：Feed Up (我要去哪) / Feed Back (我怎么到那) / Feed Forward (下一步去哪)。每个学期中点答一次。

### 自检1: Feed Up -- TLA 是否训练 ILO？(目标清晰度)

- **问题**：ILO-2 要求"量化推理成本对利润率的影响"，但 TLA 中 `practice.md` drill-2 的 Faded 阶段只让学生填"每月解决数"和"推理成本"两个空，是否足够训练"量化影响"这一能力？还是只是"代数代入"？
- **自检方法**：抽 3 份学生 drill-2 阶段C (Independent) 作业，看学生是否主动写了"推理成本下降 X% -> 利润率提升 Y%"的因果陈述，而非只交 NPV 数字。
- **不通过信号**：>=2 份作业只有数字无因果陈述 -> TLA 需增补"写一句因果结论"硬要求。

### 自检2: Feed Back -- AT 是否测量 ILO？(测量效度)

- **问题**：ILO-3 的 AT 是 `solution.ipynb` TODO4 输出 OLS summary，但 OLS summary 只是 statsmodels 的打印输出，学生能否 copy-paste 通过而未真正理解弹性？
- **自检方法**：在 `tutorial.ipynb` 后测加一题"用大白话解释 -1.4 这个系数对产品经理意味着什么"，看学生能否脱离代码说出"降价 1% 需求涨 1.4%，弹性需求下降价增收"。
- **不通过信号**：>=30% 学生后测无法用大白话解释 -> AT 需增补口述/文字解释题，不能只看代码输出。

### 自检3: Feed Forward -- 不经 TLA 能过 AT 吗？(对齐失败检测)

- **问题**：`solution.ipynb` 是公开的参考答案，学生能否不刷 `practice.md` 的 drill、不听讲、直接 copy `solution.ipynb` 通过 `starter.ipynb` 的 TODO？
- **自检方法**：在 `tutorial.ipynb` 设计 1 道变式题（如把 Intercom Fin $0.99/解决 换成 11x.ai 按预约会议收费，数据未在 starter/solution 出现），看学生能否独立迁移。
- **对齐失败信号**：学生在 starter.ipynb TODO 全对但 tutorial 变式题正确率 <50% -> 说明 AT 测的是"复制能力"而非 ILO 要求的"迁移能力"，AT 需升级为含变式题的口头答辩或限时闭卷变式。
- **当前状态**：本单元已用 `practice.md` interleaving (A1B1C1-B2C2A2-C3A3B3) 强制上下文切换，降低 copy-paste 通过率；tutorial.ipynb 的 Socratic 追问进一步防止"刷题通过"。

---

## 与 v5.0 评估的对齐

v5.0 的 `notes.md` §作业与评估 列了三项交付物（starter.ipynb / 300字分析 / 推理成本重算可选项）。本表把这三项重新组织到 ILO-2/4/5 的 AT 列，并补 mastery 阈值。v5.0 交付物未删改，本表为 v6.0 增量对齐层。
