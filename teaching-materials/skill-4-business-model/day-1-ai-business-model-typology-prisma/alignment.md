# Constructive Alignment (Biggs) - AI商业模式类型学 + PRISMA

> v6.0 建构对齐: ILO (Intended Learning Outcomes) <-> TLA (Teaching/Learning Activities) <-> AT (Assessment Tasks)
> Reference: Biggs, J. (1996). Enhancing teaching through constructive alignment. *Higher Education*, 32(3), 347-364.
> Reference: Hattie, J. & Timperley, H. (2007). The Power of Feedback. *Review of Educational Research*, 77(1), 81-112.

## ILO <-> TLA <-> AT 矩阵

| ILO (预期学习产出) | TLA (教学学习活动) | AT (评估任务) | mastery_threshold |
|---|---|---|---|
| ILO1: 能解释AI商业模式五大类型的差异 (核心驱动力 / 收入模型 / 护城河) | notes.md 关键回顾1 + starter.ipynb TODO1 + tutorial Socratic 追问 + D1 worked-faded + schedule.json C1 卡片 | tutorial 口头辩护 (说出5类型驱动力) + D1 Independent 通过 + pre-tutorial essay | >=80% (5类型至少答对4) |
| ILO2: 能用 arxiv+pandas 执行 PRISMA 四步 (识别 / 去重 / 筛选 / 纳入) | starter.ipynb TODO2-3 + D2 worked-faded + schedule.json C2 卡片复习 + reading.md PRISMA 条目 | solution.ipynb 输出 160->96->30->30 真实数字 + PRISMA 流程图 (matplotlib) | >=70% (数字偏差 <=5%) |
| ILO3: 能基于真实文献构建类型学分类 + ASReview 加速筛选 | starter.ipynb TODO4-5 + D3 worked-faded + reading.md ASReview 条目 + schedule.json C3 卡片 | progressive_project milestone (类型学分类函数 `classify_type`) + final (分布统计 + 流程图) | 能独立解 D3 Independent |
| ILO4: 能用天道推演预判类型演化 + 用 ASReview/DeepSeek/RAGAS 等前沿工具 | notes.md 2026前沿节 + tutorial HBS devil's advocate + reading.md 天道推演条目 + schedule.json C3 卡片 | poster (三沙盘分支推演: Agent主导 / 平台整合 / 基础设施商品化, 每分支3层 immediate/near/far) + 300字分析 | >=3 分支 + 概率分布标注 |

## mastery_threshold 汇总

- **ILO1**: 5 类型至少答对 4 (>=80%) -- 不看 notes.md 能独立说出 5 类型 + 驱动力
- **ILO2**: PRISMA 真实数字偏差 <=5% (>=70%) -- 160/96/30/30 四步数字 + 流程图
- **ILO3**: 能独立解 D3 Independent (无需看 worked) -- 分类函数 + ASReview 模拟
- **ILO4**: 至少 3 个沙盘分支 + 每分支 3 层推演 (immediate/near/far) + 概率分布

## 3 自检问题 (Biggs + Hattie 3 问)

### 1. Feed Up -- TLA 是否训练 ILO?

每个 ILO 是否都有对应的 TODO / drill / tutorial 活动? 若有 ILO 无 TLA -> 补 TLA。

- 自检: ILO1 <- TODO1 + D1 + tutorial Socratic Round 1-2 + schedule C1. 覆盖.
- 自检: ILO2 <- TODO2-3 + D2 + schedule C2 + reading PRISMA. 覆盖.
- 自检: ILO3 <- TODO4-5 + D3 + reading ASReview. 覆盖.
- 自检: ILO4 <- notes 2026前沿 + tutorial devil's advocate Round 4 + reading 天道推演. 覆盖.
- **结论**: 全部 ILO 有 TLA 覆盖, Feed Up 成立.

### 2. Feed Back -- AT 是否测量 ILO?

每个 ILO 是否都有可观察的评估任务? 若 AT 测的不是 ILO -> 改 AT。

- 自检: ILO1 <- tutorial 口头辩护 + D1 Independent. 可观察.
- 自检: ILO2 <- 160/96/30 数字 + matplotlib 流程图. 可观察.
- 自检: ILO3 <- `classify_type` 函数 + 分布统计. 可观察.
- 自检: ILO4 <- poster 三沙盘分支 + 概率分布. 可观察.
- **结论**: 全部 ILO 有 AT 测量, Feed Back 成立.

### 3. Feed Forward -- 不经 TLA 能过 AT 吗? 若能 = 对齐失败

学生是否可以不看 notes / drill / tutorial 就过 AT? 若能 -> TLA 太弱或 AT 太浅。

- 自检: D1 Independent 需看 notes 类型表 (5 类型 + 驱动力) -- 不看则无法归类.
- 自检: D2 需跑过 arxiv + pandas -- 不跑则无 160/96/30 数字.
- 自检: D3 需理解 ASReview 主动学习原理 -- 不理解则无法实现模拟.
- 自检: ILO4 poster 需读 notes 2026前沿 + reading 天道推演 -- 不读则无沙盘分支.
- **结论**: 不经 TLA 无法过 AT, 对齐成立, Feed Forward 成立.

## Hattie (2007) 3 问 x 4 级 (tutorial.ipynb 内化)

| 级别 | 效应量 d | 本单元应用 |
|---|---|---|
| [TASK] 任务级 | 0.78 | D1 归类错误 -> 指向驱动力列重判; D2 数字偏差 -> 对照真实 160/96/30 |
| [PROCESS] 过程级 | 0.72 | D2 筛选失败 -> 反思检索策略 (query 太宽? 太窄?); D3 排序差 -> 反思种子集偏置 |
| [SELF-REG] 自我调节级 | 0.65 | "你失败 2 次才触发 weak_loop -- 下次失败 1 次就主动回退" |
| [FEED-FORWARD] 前馈级 | 0.66 | "盲点 -> 复习 reading.md ASReview + Day2 定价策略" |
| ~~Self 表扬~~ | ~~0.14~~ | ~~避免 "你真聪明"~~ (Hattie 警告: 表扬降低内在动机) |

> 设计原则: 反馈后必须给 Feed Forward (下一步具体行动), 避免 Self 级表扬 (d=0.14), 强化 TASK/PROCESS 级 (d=0.78/0.72).
