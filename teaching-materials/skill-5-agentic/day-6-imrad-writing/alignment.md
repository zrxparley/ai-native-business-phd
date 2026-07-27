---
unit: U5D6
title: IMRaD 论文写作 建构对齐 (Biggs ILO ↔ TLA ↔ AT)
version: v6.0
based_on: Biggs (1996) constructive alignment + Bloom mastery learning + Hattie (2007) feed up/back/forward
---

# U5D6 建构对齐矩阵 (Constructive Alignment)

> **Biggs 原理**: 预期学习产出 (ILO, Intended Learning Outcomes) 决定教学学习活动 (TLA, Teaching/Learning Activities), TLA 决定评估任务 (AT, Assessment Tasks)。三者必须对齐, 否则学生"学会了无关的东西"。本矩阵把本单元 5 条 ILO (来自 notes.md 学习目标) 映射到 starter/practice/tutorial/solution 的具体活动与评估。

---

## ILO ↔ TLA ↔ AT 矩阵 (5 行, 覆盖 notes.md 全部 5 条学习目标)

| ILO (预期学习产出, 学完能做到) | TLA (教学学习活动, 引用本单元文件) | AT (评估任务, 引用本单元文件) | mastery_threshold |
|------------------------------|------------------------------------|------------------------------|------|
| **ILO1**: 能解释 IMRaD 四部分结构, 说明为什么它是科学交流效率最优解 (回答读者四问) | ① 读 `notes.md` 关键回顾 1 + `reading.md` 深链; ② 做 `practice.md` diagnostic Q1 (结构识别); ③ 跑 `starter.ipynb` TODO1 (用 arxiv 抽取 ReAct 论文 IMRaD); ④ `tutorial.ipynb` cell5 苏格拉底追问"Methods 和 Results 的边界在哪" | `solution.ipynb` TODO1 输出的 IMRaD 四段边界对照表 + `practice.md` D1 独立解 (抽 2306.05685) | 四段边界偏差 < 200 字符, 且能口述"读者四问"映射 |
| **ILO2**: 能用 arxiv 包下载/解析真实论文 (ReAct, 2210.03629), 自动提取 IMRaD 各部分结构 | ① `notes.md` 上机任务 1; ② `data/README.md` arxiv 包文档; ③ `practice.md` D1 三阶段 worked-faded (完整示范 ReAct -> 部分填空 `extract_imrad_sections()` -> 独立解 2306.05685); ④ `tutorial.ipynb` cell3 苏格拉底追问"若论文没有标准 section heading 怎么办" | `solution.ipynb` TODO1 + `practice.md` D1 reps_required=3 (3 篇不同论文) | 3 篇论文抽取成功率 >= 2/3, 代码无 scaffold |
| **ILO3**: 能撰写 Introduction (漏斗结构: 背景->问题->空白->贡献->结构), 基于营销研究问题 | ① `notes.md` 关键回顾 2; ② `starter.ipynb` TODO2 Introduction 写作; ③ `practice.md` D4 综合拔高; ④ `tutorial.ipynb` cell2 pre-tutorial task (强制提交一段 Introduction 草稿); ⑤ `schedule.json` C2 漏斗卡片间隔重复 | `solution.ipynb` TODO2 输出的 Introduction (200-400 字) + `practice.md` progressive_project Milestone (Day 6 第 90 分钟提交 Intro+Methods) | 漏斗 5 层齐全, 每层段落数符合 notes.md 规定, LLM-as-a-judge 评分 >= 3.5/5 |
| **ILO4**: 能用 statsmodels 跑统计检验 (t 检验 / Cohen's d / 卡方), 写 APA 格式 Results | ① `notes.md` 关键回顾 4; ② `starter.ipynb` TODO4 statsmodels 调用; ③ `practice.md` D2 三阶段 worked-faded (完整示范 ttest_ind + APA 函数 -> 部分填空 `format_t_apa()` -> 独立解 chi2_contingency); ④ `schedule.json` C4 APA 格式卡片; ⑤ `tutorial.ipynb` cell3 苏格拉底追问"为什么 p < .001 而非 p = 0.001" | `solution.ipynb` TODO4 输出的 APA 字符串 + `practice.md` D2 reps_required=4 (t/d/χ²/CI 四子集) | APA 格式 4 项检查全过 (两位小数 / 点前缀 p / d 阈值解读 / χ² N 大写), statsmodels 调用无错 |
| **ILO5**: 能撰写 Methods (可复现性) + Discussion (6 要素) + APA 第 7 版参考文献 | ① `notes.md` 关键回顾 3+5; ② `starter.ipynb` TODO3+5+6; ③ `practice.md` D3 三阶段 worked-faded (完整示范范文+LLM-judge JSON -> 部分填空 6 要素骨架 -> 独立解+自评); ④ `schedule.json` C5 Discussion 六要素卡片; ⑤ `tutorial.ipynb` cell5 Hattie 四级反馈含 [FEED-FORWARD] 下篇先写哪部分 | `solution.ipynb` TODO3+5+6 输出的 Methods+Discussion+References + `practice.md` progressive_project Final (1500-2500 字, 6 条 APA 引用) | Methods 五要素齐全 / Discussion 六要素齐全 (关键词扫描通过) / APA 引用 3 种格式 (单/双/三作者) 无误 |

---

## 3 自检问题 (Biggs Feed Up / Feed Back / Feed Forward)

### Q1 Feed Up (TLA 是否训练 ILO?)

> "教学活动是否让学生练习了预期产出?"

- **ILO1->TLA**: `notes.md` 关键回顾 1 + `starter.ipynb` TODO1 (arxiv 抽取 IMRaD) 是否训练了"解释 IMRaD 结构"? **是**。学生不是被动读定义, 而是用代码从真实论文 (ReAct 2210.03629) 中识别结构边界, 这是 active retrieval 而非重读。
- **ILO4->TLA**: `practice.md` D2 完整示范->部分填空->独立解 三阶段 worked-faded, 是否训练了"用 statsmodels 写 APA 格式"? **是**。学生从抄写到填空到独立生成, 渐进释放脚手架。
- **潜在缺口**: ILO5 的"APA 第 7 版参考文献"只在 `starter.ipynb` TODO6 训练, `practice.md` 无对应 drill。**补救**: D3 独立解阶段要求附带 6 条 APA 引用, 作为隐性训练。

### Q2 Feed Back (AT 是否测量 ILO?)

> "评估任务是否真实测量了预期产出, 还是测了别的?"

- **ILO2 的 AT**: `solution.ipynb` TODO1 输出的 IMRaD 四段边界对照表, 是否测量了"用 arxiv 解析真实论文"? **是**。判别依据明确 (偏差 < 200 字符), 不是主观打分。
- **ILO4 的 AT**: `practice.md` D2 的 4 项自动检查 (两位小数/点前缀 p/d 阈值解读/χ² N 大写), 是否测量了"APA 格式"? **是**, 但只测了**格式**而非**统计判断**。**补救**: D2 独立解阶段增加"为什么选 t 检验而非卡方"的口述题。
- **ILO3 的 AT**: LLM-as-a-judge 评分 >= 3.5/5, 是否测量了"漏斗结构"? **部分**。LLM-judge 有长度偏差, 可能给冗长 Introduction 高分。**补救**: 必须附加人工抽查 5%, 校准 LLM-judge 偏差。

### Q3 Feed Forward (不经 TLA 能过 AT 吗? 若能 = 对齐失败)

> "学生能否绕过教学活动, 直接通过评估? 若能, 对齐失败。"

- **ILO4 AT 能否绕过 D2?** 不能。D2 独立解要求从零用 `scipy.stats.chi2_contingency` 生成 `χ²(2, N = 400) = 9.84, p = .007, φ = 0.16`, 不调用 statsmodels/scipy 不可能完成。`solution.ipynb` 是 gated (做完才看), 抄答案不构成 TLA。
- **ILO3 AT 能否绕过 starter.ipynb TODO2?** **风险点**: 学生可能让 LLM 直接生成 Introduction 草稿, 跳过漏斗结构思考。**补救**: `tutorial.ipynb` cell2 强制 pre-tutorial retrieval (学生必须先手写一段 200 字 Introduction 草稿, 不许用 LLM), 作为 TLA 闸门。
- **ILO5 AT 能否绕过 D3?** **风险点**: Discussion 6 要素可被关键词堆砌骗过 (扫描"局限""未来""伦理"即可)。**补救**: D3 独立解要求每要素 50-100 字, 且 LLM-as-a-judge 给出 per-section 评分 (而非总分), 防关键词堆砌。
- **结论**: 经补救后, 无 ILO 可绕过 TLA 直通 AT, 对齐成立。

---

## mastery_threshold 说明 (Bloom mastery learning)

- 每条 ILO 设独立 mastery 阈值 (见矩阵第 4 列), 不用综合分摊
- **未达 mastery** 的 ILO 触发 `practice.md` weak_loop: 连续 2 次失败回退上一 drill + 重读 worked example
- **已达 mastery** 的 ILO 进入 `schedule.json` 间隔重复 (FSRS-6 due 序列), 长期保持
- 整单元 mastery 定义: 5 条 ILO 全部达标 + `practice.md` progressive_project Final 提交 + `tutorial.ipynb` exit artifact (2-3 盲点 + 推荐复习单元)

---

## 与 v5.0 文件的关系 (不破坏, 只补充)

| v5.0 文件 | v6.0 新增层 | 对齐作用 |
|----------|------------|---------|
| `notes.md` (理论) | 末尾追加"学习科学层"节 | 声明本单元采用刻意练习/FSRS/建构对齐/牛津 tutorial |
| `data/README.md` (数据) | 无新增 | 数据集不变, TLA 引用 |
| `starter.ipynb` (TODO 脚手架) | 无修改 | TLA 的主体 (6 个 TODO 对应 5 条 ILO) |
| `solution.ipynb` (gated 答案) | 无修改 | AT 的参照标准 |
| `reading.md` (深链) | 无新增 | TLA 的扩展阅读 |
| `practice.md` (新) | 刻意练习 drills | TLA 的强化训练 + AT 的诊断 |
| `schedule.json` (新) | FSRS-6 间隔重复 | mastery 后的长期保持 |
| `alignment.md` (本文件, 新) | Biggs 对齐矩阵 | ILO↔TLA↔AT 自检 |
| `tutorial.ipynb` (新) | 牛津 tutorial LLM 仿真 | TLA 的苏格拉底追问 + Hattie 四级反馈 |

---

*本 alignment.md 基于 Biggs (1996) constructive alignment + Bloom (1968) mastery learning + Hattie (2007) formative feedback feed up/back/forward。所有 ILO/TLA/AT 引用本单元真实文件 (notes.md/starter.ipynb/solution.ipynb/practice.md/tutorial.ipynb/schedule.json), 非通用模板。*
