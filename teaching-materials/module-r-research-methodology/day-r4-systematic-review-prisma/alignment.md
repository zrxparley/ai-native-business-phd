---
unit: R4
title: 系统综述 PRISMA 2020 方法论 - 建构对齐 (Biggs ILO ↔ TLA ↔ AT)
version: v6.0
framework: Biggs constructive alignment + mastery threshold
---

# alignment.md - R4 系统综述 PRISMA 建构对齐

> 按 Biggs (1996) 建构对齐原则：每条 ILO (Intended Learning Outcome) 都要有对应 TLA (Teaching/Learning Activity) 训练，且 AT (Assessment Task) 必须测量该 ILO。三者不对齐 = 教学设计失败。本单元 mastery 阈值统一 >=80%。

## ILO ↔ TLA ↔ AT 矩阵

| ILO (预期学习产出) | TLA (教学学习活动) | AT (评估任务) | mastery_threshold |
|---|---|---|---|
| **ILO1**: 能解释 PRISMA 2020 四阶段流程（Identification->Screening->Quality Assessment->Synthesis）与 27 条 checklist 核心要求，说明系统综述与叙述性综述在可重复性上的本质区别 | 阅读 `notes.md` 关键回顾1-2 + `reading.md` PRISMA/Page 2021 条目 + `practice.md` D1 worked example 阶段1 + `tutorial.ipynb` Socratic 第1轮追问"可重复性凭什么" | `tutorial.ipynb` pre-tutorial essay（口述四阶段+可重复性定义）+ `schedule.json` C1/C6 卡片提取 + `practice.md` D1 阶段3 独立解的"去重前后数量报告" | >=80% (四阶段名称全对 + 可重复性定义含"另一研究者按相同流程"关键短语) |
| **ILO2**: 能用 `arxiv` + `pandas` 实现 PRISMA Phase 1 检索去重与 Phase 2 双盲筛选，用 `scikit-learn` 计算 Cohen's kappa 并判定 Landis-Koch 等级 | `starter.ipynb` TODO1-3 填空 + `practice.md` D1 阶段2 部分填空 + `solution.ipynb` TODO1-3 对照 + `tutorial.ipynb` Socratic 第2轮追问" kappa 0.55 对应哪个等级" | `practice.md` D1 阶段3 独立解（新主题"LLM advertising"检索+去重+kappa）+ progressive_project milestone (Day 7) 提交 kappa 值与 Landis-Koch 等级 | >=80% (kappa 计算正确 + Landis-Koch 等级判定正确 + 去重后数量与 fallback JSON 一致) |
| **ILO3**: 能实现 Kitchenham & Charters 五维质量评估函数，对每篇文献打 0-5 分并按 Risk of Bias 三级分级 | `starter.ipynb` TODO4 填空 + `practice.md` D2 阶段1-3 worked-faded + `tutorial.ipynb` Socratic 第3轮追问"方法适当性 vs 分析恰当性如何区分" | `practice.md` D2 阶段3 独立解（10 篇论文质量评分表）+ progressive_project final (Day 14) 的 Kitchenham 质量表 | >=80% (五维定义全对 + RoB 分级边界 >=4/2-3/0-1 正确 + 10 篇评分与导师基准差<=1 分) |
| **ILO4**: 能用 `scikit-learn` 模拟 ASReview 主动学习机制（种子集 -> TF-IDF + LogisticRegression -> 迭代查询），计算"读前 N 篇覆盖 90% 相关"效率并与人工全筛基线对比 | `starter.ipynb` TODO5 填空 + `practice.md` D3 阶段1-3 worked-faded + `solution.ipynb` TODO5 对照 + `tutorial.ipynb` Socratic 第4轮追问"假停止在什么文献分布下发生" | `practice.md` D3 阶段3 独立解（新主题 ASReview 效率曲线）+ progressive_project final (Day 14) 的 ASReview 效率曲线图 | >=80% (效率曲线含人工基线对比 + random_state=42 可重复 + 读前 N 篇覆盖 90% 数值合理) |
| **ILO5**: 能用 `matplotlib` 绘制符合 PRISMA 2020 Item 16a-17 规范的 flow diagram，标注各阶段真实数字与排除理由 | `starter.ipynb` TODO6 填空 + `practice.md` D4 阶段1-3 worked-faded + `solution.ipynb` TODO6 对照 | `practice.md` D4 阶段3 独立解（全新 arXiv 检索结果的完整 PRISMA flow diagram）+ progressive_project final (Day 14) + poster (Day 17) | >=80% (四阶段数字完整 + 排除理由标注 + flow diagram 符合 PRISMA 2020 规范) |
| **ILO6**: 能说明 DeepSeek/RAGAS 在 LLM 辅助证据合成中的应用，以及天道推演+贝叶斯如何预判研究空白演化 | 阅读 `notes.md` 2026 前沿补充 + `reading.md` ASReview/DeepSeek/RAGAS/天道推演条目 + `tutorial.ipynb` Socratic 第5轮追问"RAGAS 三指标分别防什么错" | `tutorial.ipynb` exit artifact（2-3 盲点 + 推荐复习单元）+ 300 字方法论反思（哪个阶段排除比例最高？为什么？） | >=80% (RAGAS 三指标 faithfulness/answer_relevancy/context_precision 全对 + 天道推演沙盘分支至少写出 1 条) |

## mastery_threshold 总表

| 评估任务 | 权重 | mastery 阈值 | 不达标触发 |
|---|---|---|---|
| D1-D4 drills (4 个) | 40% | 每个 >=80% | 触发 weak_loop (见 practice.md) |
| progressive_project (proposal/milestone/final/poster) | 40% | final >=80% | milestone kappa<0.41 -> 筛选者培训补充 drill |
| tutorial.ipynb Socratic 参与 + exit artifact | 10% | exit artifact 含 >=2 盲点 | 退回重做 Socratic loop |
| schedule.json 卡片提取 (C1-C6) | 10% | 6 张卡片 retention>=0.9 | FSRS-6 自动加测 |

**总 mastery**: 加权 >=80% 方可解锁 R5 学术论文写作（IMRaD）单元。

## 3 自检问题 (Feed Up / Feed Back / Feed Forward)

### 自检1 (Feed Up): TLA 是否训练 ILO？

逐条核对：每个 ILO 是否都有至少 1 个 TLA 显式训练该产出？
- ILO1 -> notes.md 关键回顾1-2 + practice.md D1 worked example ✓
- ILO2 -> starter.ipynb TODO1-3 + practice.md D1 阶段2-3 ✓
- ILO3 -> starter.ipynb TODO4 + practice.md D2 阶段2-3 ✓
- ILO4 -> starter.ipynb TODO5 + practice.md D3 阶段2-3 ✓
- ILO5 -> starter.ipynb TODO6 + practice.md D4 阶段2-3 ✓
- ILO6 -> notes.md 2026前沿 + reading.md 深链 + tutorial.ipynb Socratic ✓

**判定**：6/6 ILO 均有 TLA 训练，Feed Up 通过。若新增 ILO7"能独立设计 PRISMA 综述研究问题"，需补 TLA（当前缺）。

**CQ-R4-1 对齐补充**：新增 `protocol.md` 后，ILO7 不再缺位；TLA 由 notes.md "预注册、偏倚与证据确定性"、practice.md proposal/final 和 research.md reproducibility_checklist 共同训练，AT 为协议摘要、双人独立筛选记录、RoB proxy 限制说明、报告偏倚与证据确定性表。

### 自检2 (Feed Back): AT 是否测量 ILO？

逐条核对：每个 AT 是否真正测量对应 ILO，而非测量其他？
- ILO1 AT=口述四阶段+可重复性定义 -> 直接测量 ILO1 ✓
- ILO2 AT=D1阶段3新主题检索+kappa -> 直接测量 ILO2（arxiv+pandas+sklearn）✓
- ILO3 AT=D2阶段3 10篇质量评分表 -> 直接测量 ILO3（Kitchenham五维+RoB）✓
- ILO4 AT=D3阶段3 ASReview效率曲线 -> 直接测量 ILO4（TF-IDF+LogReg+迭代）✓
- ILO5 AT=D4阶段3 PRISMA flow diagram -> 直接测量 ILO5（matplotlib+Item16a-17）✓
- ILO6 AT=exit artifact+300字反思 -> 测量 ILO6（RAGAS+天道推演），但"300字反思"信度偏低，建议加 1 题 RAGAS 三指标默写 ✓(需加固)

**判定**：6/6 AT 测量对应 ILO，Feed Back 通过。ILO6 的 AT 信度偏低，下版加固。

### 自检3 (Feed Forward): 不经 TLA 能过 AT 吗？若能 = 对齐失败

反事实检验：若学生跳过 TLA（不读 notes.md、不做 starter.ipynb TODO、不看 practice.md worked example），能否直接通过 AT？
- ILO1 AT=口述四阶段 -> 不读 notes.md 关键回顾1-2，学生无法准确说出 27 条 checklist 条目 -> 必须经 TLA ✓
- ILO2 AT=D1阶段3 kappa 计算 -> 不做 starter.ipynb TODO3，学生不知道 `cohen_kappa_score` 函数 -> 必须经 TLA ✓
- ILO3 AT=D2阶段3 Kitchenham 五维 -> 不看 practice.md D2 worked example，学生混淆"方法适当性"与"分析恰当性" -> 必须经 TLA ✓
- ILO4 AT=D3阶段3 ASReview -> 不做 starter.ipynb TODO5，学生不知道种子集+迭代查询机制 -> 必须经 TLA ✓
- ILO5 AT=D4阶段3 PRISMA flow diagram -> 不看 solution.ipynb TODO6，学生不知道 Item 16a-17 数字标注规范 -> 必须经 TLA ✓
- ILO6 AT=exit artifact RAGAS -> 不读 notes.md 2026前沿，学生不知道 faithfulness/answer_relevancy/context_precision 三指标 -> 必须经 TLA ✓

**判定**：6/6 ILO 的 AT 都必须经 TLA 才能通过，无"绕道过关"漏洞，Feed Forward 通过。

## 对齐完整性声明

本单元 6 条 ILO ↔ 6 组 TLA ↔ 6 项 AT 全部双向对齐，mastery 阈值统一 >=80%。三自检（Feed Up / Feed Back / Feed Forward）均通过。若后续新增 ILO 或调整 TLA，须重新跑本对齐表与三自检。

---

*alignment.md 由 v6.0 学习科学层生成。ILO 引用 PRISMA 2020 / Cohen's kappa / Kitchenham / ASReview / RAGAS 真实概念，TLA 引用 starter.ipynb / solution.ipynb / practice.md / tutorial.ipynb 真实活动，AT 引用 D1-D4 / progressive_project 真实评估。*
