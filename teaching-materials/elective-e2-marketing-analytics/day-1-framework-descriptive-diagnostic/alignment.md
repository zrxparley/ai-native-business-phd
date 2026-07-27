# 选修E2 · Day 1：建构对齐 (Constructive Alignment v6.0)

> **理论依据**：Biggs (1996) Constructive Alignment - ILO ↔ TLA ↔ AT 三者对齐 + Bloom 掌握学习 (mastery threshold) + Hattie 可见学习 (visible feedback)
> **适用单元**：elective-e2-marketing-analytics/day-1-framework-descriptive-diagnostic

---

## ILO ↔ TLA ↔ AT 对齐矩阵

| ILO (预期学习产出, Intended Learning Outcome) | TLA (教学学习活动, Teaching/Learning Activity) | AT (评估任务, Assessment Task) | mastery_threshold |
|:---|:---|:---|:---|
| **ILO1**: 能阐述营销分析四层框架 (描述→诊断→预测→处方) 并诊断企业在框架中的当前位置 | 讲义 § 关键回顾1 + reading.md 深链 + tutorial.ipynb 苏格拉底追问"描述与诊断边界" + schedule.json C1 间隔重复 | starter.ipynb TODO1 (描述统计) 后的 300 字分析; tutorial.ipynb pre-tutorial essay | >=80% (能正确说出每层核心问题+1方法+1输出) |
| **ILO2**: 能用 pandas 实现 AARRR 漏斗分析, 计算各阶段转化率与流失节点 | starter.ipynb TODO2 + practice.md D1 (S1 漏斗) Worked-Faded 三阶段 + 交叉练习 A1/A2/A3 | solution.ipynb TODO2 对应代码; practice.md D1 独立解 (输出 treated 组 re78 均值/中位数/SD) | >=80% (漏斗五阶段全对 + 流失节点正确识别) |
| **ILO3**: 能用 pandas 实现 RFM 五分群, 给每群写 1 条差异化营销动作 | starter.ipynb TODO3 + practice.md D5 (S3 RFM) + schedule.json C3 间隔重复 + tutorial.ipynb 追问"Champions 群怎么营销" | solution.ipynb TODO3; practice.md D5 独立解 (五群人数 + 5 条营销动作); progressive_project final | >=80% (R/F/M 定义正确 + qcut 分桶 + 五群动作可执行) |
| **ILO4**: 能用 scipy.stats 执行 t 检验与卡方检验, 区分统计显著与商业显著 (Cohen's d) | starter.ipynb TODO4/5 + practice.md D2/D3 (S2 检验) + schedule.json C4/C5 + tutorial.ipynb 追问"p<0.05 但 d=0.12 放不放量" | solution.ipynb TODO4/5; practice.md D2/D3 独立解; progressive_project milestone | >=80% (四项输出 chi2/p/dof/expected + Cohen's d 公式 + 商业判断) |
| **ILO5**: 能用 statsmodels OLS 控制混杂变量, 解读 treat 净效应, 理解 re75 协变量与 CUPED 思想相通 | starter.ipynb TODO6 + practice.md D4 (S3 回归) + schedule.json C6 + tutorial.ipynb 追问"为何必须放 re75" | solution.ipynb TODO6; practice.md D4 独立解 (200 字营销洞察); progressive_project final | >=80% (OLS 拟合 + treat 系数 p/CI 解读 + re75 与 CUPED 连接) |
| **ILO6**: 能用 causaldata 加载 NSW RCT, 将就业培训实验映射为营销干预场景 | 讲义 § 营销映射 + schedule.json C7 + reading.md NSW 深链 + tutorial.ipynb pre-tutorial 任务 | starter.ipynb TODO1; practice.md diagnostic 第 3 题; progressive_project proposal | >=80% (treat/re74/75/78 营销含义全对) |

---

## 3 自检问题 (Feed Up / Feed Back / Feed Forward)

> Biggs 对齐的核心: TLA 必须训练 ILO, AT 必须测量 ILO, 不经 TLA 能过 AT = 对齐失败。

### Feed Up: TLA 是否训练 ILO? (目标对齐)

1. 自检: practice.md 的 D2 (t 检验 + Cohen's d) 是否真的训练了 ILO4 "区分统计显著与商业显著"?
   - 验证: D2 的 feedback_rule 强制要求"同时报告 p 值和 Cohen's d", 且 d<0.2 时触发"商业不显著"判断 ⇒ TLA→ILO 对齐。
   - 若学生只交 p 值未交 d, TLA 未完成, 不进入 AT。

### Feed Back: AT 是否测量 ILO? (评估对齐)

2. 自检: solution.ipynb TODO4 是否真的测量了 ILO4?
   - 验证: TODO4 要求输出 t 值/p 值/Cohen's d + 一句营销建议, 三者缺一不可 ⇒ AT→ILO 对齐。
   - 若学生只输出 ttest_ind 返回值而无 d 与建议, AT 不通过, 触发 weak_loop。

### Feed Forward: 不经 TLA 能过 AT 吗? (逃逸检测)

3. 自检: 学生能否不练 practice.md D4 (OLS Worked-Faded), 直接抄 solution.ipynb TODO6 过 AT?
   - 检测: tutorial.ipynb 苏格拉底追问"为何必须放 re75 协变量? 不放会怎样?"。若学生答不出"混杂偏误/CUPED", 即使 TODO6 代码跑通也判 AT 不通过 ( tutorial 是 AT 的口试环节)。
   - 逃逸处置: 回退到 D4 worked_faded 第一阶段重看 + 补做 diagnostic 第 3 题。
   - 若能逃逸 ⇒ 对齐失败, 需在 practice.md D4 feedback_rule 增加"必须口述 re75 作用"约束。

---

## mastery 阈值总览

- **单元过关**: 6 个 ILO 全部 >=80%, 且 ILO4 的"统计显著≠商业显著"红线零错误
- **tutorial 过关**: student_model.json 中 6 个 ILO 的 mastery 字段全部 >=0.8
- **重修触发**: 任一 ILO 连续 2 次 <80% → 触发 weak_loop, 回退上一难度 drill
- **进阶资格**: 全部 6 个 ILO >=90% → 可进入 Day 2 (CLV 预测) 挑战题
