# Constructive Alignment - A/B 测试 (NSW RCT + CUPED + causaldata)

> Biggs 建构对齐: ILO (Intended Learning Outcomes) ↔ TLA (Teaching/Learning Activities) ↔ AT (Assessment Tasks)
> Loop Engineering v6.0 学习科学层 · 配套 notes.md / starter.ipynb / solution.ipynb / practice.md / tutorial.ipynb / schedule.json

---

## ILO ↔ TLA ↔ AT 矩阵

| ILO (预期学习产出) | TLA (教学学习活动) | AT (评估任务) | mastery_threshold |
|---|---|---|---|
| ILO1: 能在 NSW RCT 数据上验证随机化均衡性, 解释为什么 RCT 均值差=ATE (无需后门调整) | starter.ipynb TODO1+TODO2 (加载+均衡性检验) + tutorial.ipynb Socratic 第1-2轮 + practice.md D1 worked-faded + schedule.json C1/C4 间隔重复 | solution.ipynb 对应 cell + tutorial.ipynb 后测 + 300字分析"NSW RCT 均衡 vs Day1 观测不均衡" | >=80% TODO 正确 + 能口头解释 E[Y(0)\|T=1]=E[Y(0)\|T=0] |
| ILO2: 能为营销 A/B 测试计算样本量, 完成显著性检验/CI/事后功效, 正确解读 p 值 (不被 p<0.05 绑架) | starter.ipynb TODO3+TODO4+TODO5 + practice.md D2 worked-faded + schedule.json C2/C5 间隔重复 + tutorial Socratic 第2轮 | solution.ipynb 对应 cell + practice.md D2 阶段3 独立解 + diagnostic 第2题 | >=70% TODO 正确 + 能识别"p<0.05 但功效不足"陷阱 |
| ILO3: 能用 CUPED 方差缩减提升 A/B 灵敏度, 解释 1-ρ² 的工业意义 (Deng et al. 2013) | starter.ipynb TODO6 (可选) + practice.md D3 worked-faded + tutorial.ipynb Socratic 第3轮 + schedule.json C3 间隔重复 | solution.ipynb TODO6 + practice.md D3 阶段3 独立解 + diagnostic 第3题 | 能独立解 (无 scaffold) + 能写出 β=Cov(Y,X)/Var(X) + 能解释前提 (X 不受 T 影响) |
| ILO4: 能区分 RCT (Day2) vs 观测因果 (Day1) vs 准实验 (Day3) 的适用条件, 在营销场景中正确选择方法 | tutorial.ipynb Socratic 第4轮 + practice.md interleaving (跨 Day 交叉) + notes.md §与后续 Day 的衔接 | 2 分钟话术 "假如我是营销负责人" + progressive_project M4 poster | 能在 3 种场景中正确选择方法 (3/3) + 口头辩护 |

---

## mastery_threshold (单元整体)
- 4 个 ILO 全部达到各自阈值 (上表第4列)
- starter.ipynb 6 个 TODO 至少 5 个正确 (>=83%)
- diagnostic 3 题至少 2 题正确 (识别弱项后进 weak_loop)
- 至少完成 1 次 tutorial.ipynb Socratic 后测 + 2 个盲点记录到 student_model.json
- schedule.json 5 张卡片首次复习正确率 >=60% (FSRS-6 EF 不下降)

---

## 3 自检问题 (Biggs Feed Up / Feed Back / Feed Forward)

### 1. Feed Up (TLA 是否训练 ILO?)
practice.md 的 D1/D2/D3 + starter.ipynb 的 6 个 TODO + tutorial.ipynb 的 4 轮 Socratic + schedule.json 的 5 张卡片, 是否覆盖了 ILO1-ILO4 的全部技能?
- **自检**: 每条 ILO 至少有 1 个 drill + 1 个 TODO + 1 个 Socratic 轮次 + 1 张 schedule 卡片对应。
  - ILO1 ↔ D1 + TODO1/2 + Socratic 第1轮 + C1/C4 ✓
  - ILO2 ↔ D2 + TODO3/4/5 + Socratic 第2轮 + C2/C5 ✓
  - ILO3 ↔ D3 + TODO6 + Socratic 第3轮 + C3 ✓
  - ILO4 ↔ interleaving + Socratic 第4轮 + 跨 Day 交叉 ✓
- **结论**: TLA 训练覆盖 ILO, 对齐。

### 2. Feed Back (AT 是否测量 ILO?)
solution.ipynb + diagnostic + progressive_project M1-M4, 是否能区分"掌握了 ILO"与"没掌握"?
- **自检**: 每条 ILO 都有可观测的 AT (代码能跑/选择题对了/话术能讲), 不是模糊自评。
  - ILO1 = solution.ipynb TODO1/2 + 300字分析 ✓
  - ILO2 = D2 阶段3 独立解 + diagnostic 第2题 ✓
  - ILO3 = D3 阶段3 独立解 + diagnostic 第3题 ✓
  - ILO4 = M4 poster 2分钟话术 ✓
- **结论**: AT 可测量 ILO, 对齐。

### 3. Feed Forward (不经 TLA 能过 AT 吗? 若能 = 对齐失败)
若学生跳过 starter.ipynb 和 practice.md, 直接抄 solution.ipynb, 能过 AT 吗?
- **自检**: 若能, 对齐失败。修复机制:
  - progressive_project M3 要求 300 字营销业务建议 (无标准答案, 必须真做) ✓
  - tutorial.ipynb Socratic 追问要求口头辩护 (抄的答不出, 每轮降 scaffold) ✓
  - diagnostic 前测在 tutorial 中随机抽查 (学生无法预判) ✓
  - M4 poster 2 分钟话术 (口头, 无法照读) ✓
- **结论**: 不经 TLA 无法过 AT, 对齐成功。

---

## 与 v5.0 的关系
v5.0 的 notes.md / data / starter.ipynb / solution.ipynb / reading.md 提供**内容**, v6.0 的本文件 + practice.md / schedule.json / tutorial.ipynb 提供**学习科学的脚手架**。Biggs 建构对齐确保内容与评估对齐, 不脱节。
