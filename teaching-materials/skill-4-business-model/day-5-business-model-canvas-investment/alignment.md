# Constructive Alignment - skill4-day5 商业模式画布+投资 (v6.0 学习科学层)

> Biggs 建构对齐 (Constructive Alignment): ILO ↔ TLA ↔ AT 三者必须对齐, mastery_threshold 显式标注
> 本文件与 practice.md / schedule.json / tutorial.ipynb / notes.md 共同构成 v6.0 学习科学层

---

## ILO ↔ TLA ↔ AT 矩阵 (Biggs Constructive Alignment)

| ILO (预期学习产出 Intended Learning Outcome) | TLA (教学学习活动 Teaching/Learning Activity) | AT (评估任务 Assessment Task) | mastery_threshold |
|---|---|---|---|
| ILO1: 能用 pandas 构建 AI 商业模式画布九宫格 DataFrame, 识别 AI 适配的 4 项独有变化(推理成本+数据成本+Agent渠道+outcome-based收入流) | starter.ipynb TODO1 + practice.md D1 worked-faded 三阶段 + tutorial.ipynb Socratic 追问"画布漏项" + schedule.json C1 间隔重复 | solution.ipynb TODO1 解题 + tutorial.ipynb 后测"九宫格 AI 独有成本" + 300字分析中画布部分 | >=80% (9宫格全对 + AI独有4项全识别) |
| ILO2: 能用 numpy-financial 计算 NPV/IRR/PI/回收期, 符号方向正确, 判断 AI 项目投资可行性 | starter.ipynb TODO2-3 + practice.md D2 worked-faded 三阶段 + schedule.json C2 间隔重复 + tutorial.ipynb Socratic 追问"NPV符号" | solution.ipynb TODO2-3 解题 + tutorial.ipynb 后测"NPV符号/IRR符号变化" + 300字分析中财务计算 | >=80% (NPV/IRR/PI/回收期数值全对 + 符号正确) |
| ILO3: 能用 scipy.stats 做蒙特卡洛 10000 次模拟得 P(NPV>0), 用天道推演做 Bull/Base/Bear × 三层(immediate/near/far) 推演, 理解频率派分布与场景路径互补 | starter.ipynb TODO4-6 + practice.md D3 worked-faded 三阶段 + schedule.json C3-C4 间隔重复 + tutorial.ipynb Socratic 追问"蒙特卡洛vs天道推演" | solution.ipynb TODO4-6 解题 + tutorial.ipynb 后测"频率派vs场景路径" + 300字分析中决策建议 | 能独立解 (P(NPV>0)代码正确 + 三路径×三层完整 + 决策建议有依据) |

---

## mastery_threshold (掌握阈值)

- **ILO1 (画布构建)**: >=80% - 九宫格全对, AI 独有 4 项(推理成本+数据成本+Agent渠道+outcome-based收入流)必识别
- **ILO2 (DCF 财务计算)**: >=80% - NPV/IRR/PI/回收期数值正确, 符号方向正确, cashflows[0] 必为负
- **ILO3 (蒙特卡洛+天道推演)**: 能独立解 - 蒙特卡洛 P(NPV>0) 代码正确(对营收/毛利率/增长率同时抽样), 天道推演三路径×三层完整, 决策建议引用 P(NPV>0) 与三路径
- **整体单元 (6 TODO + 300字分析)**: 6 个 TODO 全跑通 + 300 字分析引用 NPV=$451.2K / IRR=20.08% / P(NPV>0)=55.7% + 投资决策建议 + (可选)蒙特卡洛vs贝叶斯对比
- **MIT 6.5940 借鉴**: "至少 4/5 实验提交方可及格" -> 本单元至少 5/6 TODO 跑通方可及格, 6/6 + 300字分析为 A

---

## 3 自检问题 (Biggs Self-Check - Feed Up / Feed Back / Feed Forward)

### 1. Feed Up - TLA 是否训练 ILO?
practice.md 的 D1/D2/D3 worked-faded 三阶段是否真的训练了画布构建/DCF计算/蒙特卡洛+天道推演?
- **检测点**: 若学生在阶段1 Worked 直接抄答案即过, 则 TLA 失败
- **修复**: 提高阶段2 Faded 的填空比例(从留1格空改为留3格空), 阶段3 Independent 必须独立解不允许参考
- **证据**: tutorial.ipynb 的 student_model.json 记录每个 drill 的 mastery 分数, <0.7 触发 weak_loop

### 2. Feed Back - AT 是否测量 ILO?
solution.ipynb 的 6 个 TODO 是否覆盖 ILO1-3? 若 TODO1-3 全过但学生无法口述"AI画布 vs SaaS画布差异", 则 AT 对 ILO1 测量不足
- **检测点**: TODO1 测 ILO1, TODO2-3 测 ILO2, TODO4-6 测 ILO3 - 一一对应
- **修复**: 补充口头辩护(tutorial.ipynb Socratic 追问)作为 AT 一部分, 未过 tutorial 不允许提交 solution
- **证据**: tutorial.ipynb 5 轮 Socratic 追问覆盖 ILO1-3 的概念理解, 而非数值计算

### 3. Feed Forward - 不经 TLA 能过 AT 吗?
若学生跳过 practice.md D1-D3, 直接抄 solution.ipynb 能过 6 个 TODO 吗?
- **检测点**: 若能, 则对齐失败(学生未真正掌握 ILO)
- **修复**: tutorial.ipynb Socratic 追问强制要求概念理解(如"凭什么说推理成本是AI独有"), 未过 tutorial 不允许提交 solution; solution.ipynb 提交需附 student_model.json 显示 drill mastery >=0.7
- **证据**: student_model.json 跨单元复用, 下一单元(技能5)可检查本单元 drill mastery 是否达标

---

## 复盘对齐缺口 (反馈学习 - Feedback Learning)

每次学生 AT 失败后, 记录 ILO ↔ TLA ↔ AT 哪一环断链, 下次迭代该 drill 的 worked-faded 比例与 tutorial 追问深度:

| 失败模式 | 断链环节 | 修复动作 |
|---------|---------|---------|
| TODO1 过但口述不出 AI 独有项 | AT 对 ILO1 测量不足 | tutorial 加口头辩护追问 |
| TODO2 NPV 符号错 | TLA D2 阶段1 Worked 未强调符号 | D2 feedback_rule 已覆盖, 加强 worked 示范的符号检查清单 |
| TODO4 P(NPV>0) 计算错 | TLA D3 阶段2 Faded 抽样代码空太多 | 降低 Faded 比例, 阶段2 留更多 hint |
| TODO6 三路径缺层 | TLA D3 阶段3 Independent 太难 | 回退阶段2 + worked example 补充 |

> 本表与项目 CLAUDE.md 的「天道推演系统 - 自我进化机制」同构: 记录前提假设 -> 追踪 outcomes -> 复盘差异 -> 更新因果模型。
