---
unit: U5D6
title: IMRaD 论文写作 刻意练习
skill_target: 能独立用 arxiv+statsmodels 拆解一篇真实论文的 IMRaD 结构, 并撰写一篇符合 APA 第 7 版规范的营销研究 IMRaD 短文 (4 部分齐全, t/χ² 检验报告无误, 可复现性自检通过)
version: v6.0
based_on: Ericsson deliberate practice + MIT CS229 pset0 diagnostic + CS230 progressive project + Hattie feedback
---

# U5D6 刻意练习 (Deliberate Practice)

## skill_target (一句话可评估)

学完本单元, 学生能**独立完成**以下任务 (无脚手架, 90 分钟内): 用 `arxiv` 包下载 ReAct 论文 (arXiv 2210.03629) 并自动抽取其 IMRaD 四部分结构, 用 `statsmodels.ttest_ind` + `scipy.stats.chi2_contingency` 跑统计检验, 按漏斗结构撰写 Introduction, 按 5 要素撰写 Methods, 按 APA 第 7 版格式撰写 Results, 按 6 要素撰写 Discussion, 最后用 LLM-as-a-judge (arXiv 2306.05685) 评分并解释偏差。

---

## diagnostic (CS229 pset0 式先测, 探测先验缺口)

> 规则: 30 分钟内闭卷作答, 不查 arxiv/statsmodels 文档。每题先写答案, 再勾选置信度 (1-5)。目的不是评分, 是定位盲点。

**Q1 (结构识别)**: 下面哪一段属于 Methods 而非 Results? 请说明判别依据。
- A. "t(398) = 4.27, p < .001, d = 0.43, 营销Agent 组转化率显著高于人工组"
- B. "本研究采用双臂 A/B 测试 (N=400), 实验组接入营销Agent, 对照组由 8 位营销人员操作, 数据收集周期 14 天, 使用独立样本 t 检验和卡方检验"
- C. "实验组转化率提升 12.3% (95% CI [8.1%, 16.5%]), 但质量评分仅提升 2.1% (p = .08)"

置信度: □1 □2 □3 □4 □5

**Q2 (APA 格式)**: 写出下面结果的 APA 第 7 版格式表述:
"卡方检验显示渠道偏好与组别相关, χ² = 9.84, 自由度 2, N = 400, p = 0.007, φ系数 = 0.157"

置信度: □1 □2 □3 □4 □5

**Q3 (可复现性)**: 一位读者想复现你的 statsmodels 分析。列出 Methods 部分必须包含的**至少 5 个**可复现性要素 (本单元 Methods 五要素)。

置信度: □1 □2 □3 □4 □5

> 评分规则: 每题 0/1/2 分。Q1=B 且能说明"Methods 描述怎么做, Results 描述发现什么"得 2 分。Q2 格式完全正确得 2 分 (`χ²(2, N = 400) = 9.84, p = .007, φ = 0.16`, 注意 APA 用 `.007` 而非 `0.007`)。Q3 列出 5 要素 (研究设计/系统架构/数据收集/评估指标/数据分析方法) 得 2 分。>=4 分免修 subskill A, <4 分需走完所有 drills。

---

## subskills (3 个子技能拆解)

- **A. 结构识别与提取 (Structure Parsing)**: 用 `arxiv` 包下载 ReAct 论文, 用正则/section 标题自动抽取 Introduction/Methods/Results/Discussion, 识别漏斗结构。判别依据: 能在 20 分钟内输出一张 IMRaD 四段长度+边界对照表。
- **B. 统计写作 (Statistical Writing)**: 用 `statsmodels.ttest_ind` 跑独立样本 t 检验, 用 `scipy.stats.chi2_contingency` 跑卡方, 计算 Cohen's d, 按 APA 第 7 版写出 `t(df) = X.XX, p < .001, d = X.XX` 与 `χ²(df, N = XXX) = X.XX, p < .01, φ = 0.XX` 格式。
- **C. 批判性 Discussion + 自评 (Critical Discussion)**: 按 Discussion 六要素 (发现解读/理论贡献/实践启示/局限性/未来方向/伦理声明) 撰写, 用 LLM-as-a-judge 评分, 解释偏差来源 (位置偏差/长度偏差/自我偏好), 并给出"投稿前自检"建议。

---

## drills (>=3, 每个 drill 含 difficulty/reps_required/feedback_rule/worked-faded)

### drill_id: D1
**子技能**: A 结构识别
**difficulty**: 2
**reps_required**: 3 (3 篇不同论文重复)
**feedback_rule**: 领域特定--学生提交 IMRaD 四段边界 (start_char, end_char)。若任一段落边界与 `arxiv` 解析的 ReAct 论文 (2210.03629) 真实 section heading 偏差 > 200 字符, 触发反馈: "重新阅读论文 Introduction 末尾的论文结构段, 你的 Introduction 边界停早了。" 引用具体论文 ID, 不泛泛而谈。
**worked_faded (三阶段)**:
- 完整示范 (Worked): 给出 ReAct 论文 IMRaD 抽取的完整代码 + 四段边界表, 学生跑一遍能复现
- 部分填空 (Faded): 给出代码框架, 仅 `extract_imrad_sections()` 函数体留空, 学生填 4 行正则
- 独立解 (Independent): 学生自行下载 arXiv 2306.05685 (LLM-as-a-judge 论文), 独立完成抽取

### drill_id: D2
**子技能**: B 统计写作
**difficulty**: 3
**reps_required**: 4 (4 个数据子集重复: t 检验 / Cohen's d / 卡方 / 95% CI)
**feedback_rule**: 领域特定--学生提交 APA 格式字符串, 自动检查 (a) `t(df) = ` 后是否两位小数, (b) `p < .001` 是否用点前缀 (APA 规定 p 值前不加 0), (c) `d = ` 是否解读小/中/大 (0.2/0.5/0.8), (d) χ² 的 N 是否大写。任一错误触发: "重读 notes.md 关键回顾 4, APA 规范第 7 版对 p 值的写法, 你用了 `p = 0.001`, 应为 `p = .001`。" 引用 statsmodels/scipy 输出对象, 不抽象评价。
**worked_faded**:
- 完整示范: 给出 `ttest_ind` 调用 + 完整 APA 字符串生成函数, 含 Cohen's d 手算公式
- 部分填空: 给出统计调用结果对象, 留空 APA 格式化函数 (`format_t_apa(t, df, p, d)` 函数体空)
- 独立解: 学生自行用 `chi2_contingency` 跑卡方, 从零生成 `χ²(2, N = 400) = 9.84, p = .007, φ = 0.16`

### drill_id: D3
**子技能**: C 批判性 Discussion + 自评
**difficulty**: 4
**reps_required**: 2 (2 个 Discussion 段落: 一个高效应量场景 / 一个无显著差异场景)
**feedback_rule**: 领域特定--学生提交 Discussion 段落, 检查六要素是否齐全 (用关键词扫描: "局限"/"未来"/"伦理"/"理论"/"实践"/"解读")。若缺"伦理声明", 反馈: "你的 Discussion 缺伦理维度, 本单元营销研究涉及用户行为数据 A/B 测试, 必须声明数据匿名化和知情同意。重读 notes.md 关键回顾 5。" LLM-as-a-judge 评分时强制学生写出"judge 给我 Introduction 多打了 1.2 分, 因为我的句子更长 (长度偏差)"--不接受"评分合理"这种空话。
**worked_faded**:
- 完整示范: 给出一份满分 Discussion 范文 + LLM-as-a-judge 评分 JSON (含 score_per_section + bias_analysis)
- 部分填空: 给出 Discussion 骨架 (6 个小标题), 学生填 3 段 (局限性/未来方向/伦理), 其余已写
- 独立解: 学生从零撰写 Discussion, 自行调 LLM-as-a-judge (静态模拟), 输出评分+偏差分析

### drill_id: D4 (可选拔高)
**子技能**: A+B+C 综合
**difficulty**: 5
**reps_required**: 1
**feedback_rule**: 学生用 arxiv 下载任选一篇 arXiv 2024 后的营销/Agent 论文, 完整重写其 IMRaD 为中文版, 并用 LLM-as-a-judge 对比原文与改写版的可读性差异。反馈: "你的 Introduction 漏斗第三层 (研究空白) 不够窄, 改写版把空白写成了'前人未充分研究', 太宽泛, 应具体到'未在 N<500 的中小 A/B 测试场景下评估 Agent vs 人工的边际成本'。"
**worked_faded**: 完整示范->部分填空 (留空 Methods 部分)->独立解

---

## progressive_project (CS230 式渐进交付)

- **Proposal (Day 6 第 30 分钟提交)**: 选定一篇 arXiv 论文 (建议 2210.03629 / 2306.05685 / 2402.xxxxx 中任一), 写 1 页 proposal, 声明你将复刻其哪一部分的 IMRaD 结构, 用什么数据子集 (N=400 A/B 测试或 8 位营销人员访谈)。
- **Milestone (Day 6 第 90 分钟提交)**: 提交 Introduction + Methods 草稿 (各 200-400 字), 必须含 `arxiv` 解析的真实论文引用和 `statsmodels` 调用伪代码。
- **Final (Day 6 课后 48 小时提交)**: 完整 IMRaD 短文 (1500-2500 字), 四部分齐全, APA 第 7 版参考文献 6 条, 统计检验结果格式准确。
- **Poster (Day 7 Capstone 整合)**: 1 页海报, 用图表呈现 t 检验结果 + Discussion 关键发现, 与 Day 7 端到端交付对接。

---

## interleaving (A1B1C1...B2C2A2...C3A3B3 交叉排布, 不块状)

不要先做完所有结构识别再做统计写作。**强制交叉顺序** (每 25 分钟一个 pomodoro):

```
P1: A1 (D1 完整示范 ReAct 抽取)
P2: B1 (D2 完整示范 t 检验 APA)
P3: C1 (D3 完整示范 Discussion 范文阅读)
P4: A2 (D1 部分填空 抽 2306.05685)
P5: B2 (D2 部分填空 APA 格式化函数)
P6: C2 (D3 部分填空 6 要素骨架)
P7: A3 (D1 独立解 抽自选论文)
P8: B3 (D2 独立解 卡方检验)
P9: C3 (D3 独立解 撰写+自评)
```

迁移原理: 交叉练习 (interleaving) 强制大脑在不同心智模型间切换, 比块状练习更能促进迁移 (Rohrer, 2012)。本单元三项子技能共享"IMRaD 骨架"但调用不同工具 (arxiv/statsmodels/LLM-judge), 交叉能避免"工具依赖"。

---

## retry_policy (CS230 式)

- **10 free late days**: 整个 skill-5 共享 10 天迟到豁免, 用完即止, 无需理由
- **失败重试不罚分**: D1/D2/D3 任一 drill 首次未达 reps_required 的反馈标准, 可重做, 不扣分。重做时必须先阅读 feedback_rule 指定的 notes.md 段落
- **Proposal 重提**: Proposal 被拒 (如选了非 arXiv 论文) 可在 24 小时内换题, 不占 late days
- **Milestone 部分分**: Milestone 只交 Introduction 不交 Methods, 得 50%, 不触发 weak_loop

---

## weak_loop (连续 2 次失败触发弱项循环)

判定: 同一 drill 连续 2 次提交均未达 feedback_rule 标准 (如 D2 两次都把 `p = .001` 写成 `p = 0.001`)。

触发后:
1. **回退上一 drill**: 如 D2 失败, 回退到 D1 重做 1 rep (强化结构识别, 间接巩固"哪段是 Results 哪段是 Methods")
2. **补充 worked example**: 重读 D2 完整示范阶段的 `ttest_ind` 调用代码, 抄写一遍 APA 格式化函数
3. **诊断盲点**: 写一段 100 字自评, "我为什么把 p 写成 0.001? 是不知道 APA 第 7 版规定, 还是习惯了 Python 默认输出?"
4. **重做 D2**: reps_required 从 4 降为 2, 通过后再回到 D3

弱项循环不计入 late days, 不扣分。目的是诊断+巩固, 不是惩罚。

---

## 反馈层级映射 (与 tutorial.ipynb 的 Hattie 四级对齐)

- **[TASK]**: drill 提交的 APA 字符串格式是否正确 (任务级)
- **[PROCESS]**: 你选择 t 检验还是卡方, 依据是什么 (过程级)
- **[SELF-REG]**: 你能否在 LLM-as-a-judge 给出高分前, 自评发现潜在偏差 (自我调节级)
- **[FEED-FORWARD]**: 下一篇 IMRaD 论文你会在哪个部分先写 (前馈级)

---

*本 practice.md 基于 Ericsson (1993) deliberate practice + MIT CS229/CS230 渐进交付 + Hattie (2007) formative feedback。所有 feedback_rule 引用本单元真实数据集/库 (arxiv/statsmodels/ReAct 2210.03629/LLM-as-a-judge 2306.05685), 非通用模板。*
