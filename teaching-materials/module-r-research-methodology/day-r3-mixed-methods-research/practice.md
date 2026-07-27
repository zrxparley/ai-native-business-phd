---
unit: U-R3
title: 混合方法研究 (Mixed Methods Research) · 刻意练习
version: v6.0
algorithm: Ericsson deliberate practice + MIT CS229 pset0 diagnostic + CS230 progressive project + Harvard/Stanford interleaving
---

# practice.md · U-R3 混合方法研究 · 刻意练习

## skill_target (本单元核心可观察技能)

> 给定 causaldata NSW 真实数据 + 8 条基于真实研究的访谈摘录，学生能独立完成：① 用 pandas+scipy.stats 执行 t 检验并计算 Cohen's d；② 用 codebook 对访谈摘录做主题分析编码并计算 Cohen's kappa 编码者间一致性；③ 构建 joint display 联合展示矩阵并用 Beta-Binomial 模型做贝叶斯整合；④ 论证选择 Creswell 三种设计（Convergent/Explanatory/Exploratory）与 Morse 三种整合策略（Merging/Explaining/Building）的理由。产物可被 solution.ipynb 与 tutorial.ipynb 后测打分（mastery >=80%）。

---

## diagnostic (CS229 pset0 式先测题, 探测先验知识缺口)

> 3 道先测，每题独立作答，不查资料。用于诊断你是否已经具备 R3 所需先验：python 数据分析、假设检验、定性研究基础。答错不扣分，仅定位缺口。

### D-1 (定量先验)
 NSW 数据集中 `treat=1` 组 (培训组) 与 `treat=0` 组 (对照组) 的 `re78` (1978 年真实收入) 均值分别为 μ₁, μ₀。请写出：
  - (a) 双样本 t 检验的零假设 H₀ 与备择假设 H₁
  - (b) Cohen's d 的计算公式 (用 μ₁, μ₀, s_pooled 表示)
  - (c) 若 p<0.05 但 d=0.2，你如何解读"统计显著但效应量小"？

### D-2 (定性先验)
 给定编码框架 codebook = {`就业障碍`, `培训收益`, `信心提升`, `社会网络`, `无主题`}，请对以下两条访谈摘录编码，并说明你的判定依据：
  - 摘录 A："参加培训后我学会了操作车床，但更关键是我现在敢去面试了。" → 主题?
  - 摘录 B："培训老师介绍我进了一家机械厂，那里有我老乡。" → 主题?
  - 反思：你的两次编码是否可能受"主观先验"影响？定性编码如何控制这种偏差？

### D-3 (整合先验)
 Morse (1991) 提出三种整合策略：Merging / Explaining / Building。
  - (a) 请把 Creswell 三种设计 (Convergent / Explanatory Sequential / Exploratory Sequential) 与 Morse 三策略做最自然的映射 (一对一)。
  - (b) joint display (联合展示矩阵) 主要服务于哪种 Morse 策略？
  - (c) 贝叶斯 Beta-Binomial 整合相比 joint display 的"并排展示"强在哪？请用一句话回答。

> 评分：3 题全对 → 直接进 drill D1 (跳过 worked 阶段)；答错 1 题 → 进对应 drill 的 worked 示范阶段；答错 >=2 题 → 进 weak_loop 预备态 (从 worked 阶段开始全部 drill)。

---

## subskills (3 个子技能拆解)

### S1 · NSW 因果推断定量分析
- 用 `causaldata.nsw()` 加载 445 条真实观测，pandas groupby 计算 μ₁, μ₀, s_pooled
- `scipy.stats.ttest_ind(..., equal_var=False)` 执行 Welch t 检验，正确解读 p 值与置信区间
- 计算 Cohen's d 效应量，区分"统计显著"与"实际重要"

### S2 · 主题分析定性编码
- 构建 codebook (基于 LaLonde 1986 / Dehejia & Wahba 1999 真实研究主题)
- 对 8 条访谈摘录逐条编码，计算各主题频次
- 用 Cohen's kappa 评估"人工编码 vs LLM-as-a-judge 编码"一致性，识别 LLM 偏差主题

### S3 · joint display + 贝叶斯 Beta-Binomial 整合
- 构建 joint display：定量统计 (t, d, p, CI) × 定性主题 (频次, 代表性摘录) 对照矩阵
- 用 Beta(α, β) 先验编码定性主题置信度，似然用 NSW 二项化结果，求后验
- 论证后验均值 vs 频率派 t 检验结论的差异，识别"概率整合"优势

---

## drills (>=3 个, 每个 drill_id/difficulty(1-5)/reps_required/feedback_rule/worked_faded)

### drill_id: D1
- **target subskill**: S1 (NSW 因果推断定量分析)
- **difficulty**: 2
- **reps_required**: 3
- **feedback_rule**: 用 NSW `re78` 真实分布 (μ₁≈6349, μ₀≈4554, LaLonde 1986 原始报告) 做数值对照；若学生 Cohen's d 落在 [0.15, 0.30] 区间外，触发"效应量解读"反馈提示 (引用 Cohen 1988 conventions: 0.2 small / 0.5 medium / 0.8 large)；用 `scipy.stats.ttest_ind` 文档校验参数
- **worked_faded** (三阶段):
  - Stage 1 · Worked (完整示范): 给出 NSW t 检验完整代码 + 解读 (`solution.ipynb` TODO1-2 对应段)
  - Stage 2 · Faded (部分填空): 给出 `ttest_ind` 调用骨架，学生填 `equal_var` 参数与 Cohen's d 公式
  - Stage 3 · Independent (独立解): 仅给数据加载骨架，学生独立完成 t 检验 + d + 解读

### drill_id: D2
- **target subskill**: S2 (主题分析定性编码)
- **difficulty**: 3
- **reps_required**: 4
- **feedback_rule**: 用 8 条基于真实研究的访谈摘录 (见 `data/README.md`) 做编码对照；用 Cohen's kappa (人工 vs LLM-as-a-judge) 量化编码者间一致性；若 kappa < 0.4 (低一致性)，触发"codebook 边界模糊"反馈，要求学生重写 codebook 定义；引用 RAGAS faithfulness 指标检查 LLM 编码是否忠于原文
- **worked_faded** (三阶段):
  - Stage 1 · Worked: 给出前 3 条摘录的完整编码 + codebook 定义
  - Stage 2 · Faded: 给出 codebook，学生编码第 4-6 条 (填空式)
  - Stage 3 · Independent: 学生独立构建 codebook + 编码第 7-8 条 + 计算 kappa

### drill_id: D3
- **target subskill**: S3 (joint display + 贝叶斯 Beta-Binomial 整合)
- **difficulty**: 4
- **reps_required**: 3
- **feedback_rule**: 用 NSW 真实 t 检验结果 (频率派) 与 Beta-Binomial 后验均值做对照；若后验均值与频率派估计偏差 >20%，触发"先验过强"反馈，要求学生重审 α, β 选择依据；joint display 必须含至少 4 个主题 × 3 个统计量 (t, d, p)，缺失任一即打回
- **worked_faded** (三阶段):
  - Stage 1 · Worked: 给出 joint display 完整模板 (4×3) + Beta(2,2) 先验的完整后验计算
  - Stage 2 · Faded: 给出 joint display 骨架，学生填后验公式与先验参数
  - Stage 3 · Independent: 学生独立选 α, β (须论证选择依据) + 完整后验 + 论证后验 vs 频率派差异

### drill_id: D4
- **target subskill**: S1+S2+S3 整合 (设计类型选择 + Morse 策略论证)
- **difficulty**: 4
- **reps_required**: 2
- **feedback_rule**: 给定 3 个 Capstone 场景 (营销AI效果评估 / 内部培训评估 / 新产品探索)，学生须选择 Creswell 设计 + Morse 策略并论证；若设计与策略不匹配 (如 Convergent+Building)，触发"逻辑断裂"反馈，引用 Creswell 2015 "整合即混合方法的核心"原则；用 `tutorial.ipynb` Socratic 追问"凭什么"检验论证深度
- **worked_faded** (三阶段):
  - Stage 1 · Worked: 给出"NSW 解释性序列 + Explaining"完整论证示范
  - Stage 2 · Faded: 给出场景 + 设计选择，学生填 Morse 策略论证
  - Stage 3 · Independent: 学生独立为 3 个 Capstone 场景做"设计+策略"配对论证

---

## progressive_project (CS230 式 proposal → milestone → final → poster)

> 渐进交付：为你的 Capstone 设计一个混合方法评估方案，分 4 阶段。

| 阶段 | 交付物 | 评估标准 | 对应 drill |
|------|--------|---------|-----------|
| **Proposal** (Week 1) | 1 页提案：研究问题 + 为什么必须用混合方法 (而非纯定量/纯定性) + Creswell 设计选择 | 研究问题必须含 "what + why" 双重性；设计选择须有 1 段论证 | D4 |
| **Milestone** (Week 3) | 定量分析脚本 (NSW-style pandas+scipy.stats) + 定性 codebook + 8 条编码示例 | t 检验正确；codebook 边界清晰；kappa >=0.4 | D1, D2 |
| **Final** (Week 5) | joint display + 贝叶斯 Beta-Binomial 整合 + 300 字一致性/差异分析 | joint display 4×3 完整；后验计算正确；差异分析非空话 | D3 |
| **Poster** (Week 7) | 1 页 poster：研究问题 → 方法 → joint display → 后验结论 → 局限性 | 必须含 joint display 可视化；局限性须含"贝叶斯先验主观性" | 全部 |

---

## interleaving (A1B1C1D1...B2C2A2D2...C3A3B3D3 交叉排布, 不块状)

> **不块状练习**：每个 subskill 不连续做完 3 次，而是与其他 subskill 交叉。降低 4.7% 短期表现但提升 47% 长期保持 (Rohrer & Taylor 2007)。

排布顺序 (A=S1, B=S2, C=S3, D=D4 设计论证)：

```
Day 1: A1 (D1 Stage 1 worked) → B1 (D2 Stage 1 worked) → C1 (D3 Stage 1 worked) → D1 (D4 Stage 1 worked)
Day 2: B2 (D2 Stage 2 faded) → C2 (D3 Stage 2 faded) → A2 (D1 Stage 2 faded) → D2 (D4 Stage 2 faded)
Day 3: C3 (D3 Stage 3 independent) → A3 (D1 Stage 3 independent) → B3 (D2 Stage 3 independent) → D3 (D4 Stage 3 independent)
```

> 关键：Day 2 故意打乱顺序 (B→C→A→D 而非 A→B→C→D)，强制每次切换都重新加载上下文，强化检索练习 (retrieval practice)。

---

## retry_policy (CS230 式 retry)

- **10 free late days**: 整个 R3 单元最多 10 天延迟不扣分 (CS230 风格)
- **失败重试不罚分**: 任一 drill Stage 3 独立解未达 mastery (>=80%) 可重做，取最高分
- **重试间隔**: 第一次重试隔 1 天，第二次隔 3 天 (强制间隔重复, 与 schedule.json FSRS-6 对齐)
- **重试上限**: 单 drill 最多 3 次，超 3 次触发 weak_loop

---

## weak_loop (连续 2 次失败触发弱项循环)

> 触发条件：同一 drill 连续 2 次 Stage 3 独立解 < 80%。

**弱项循环流程**：
1. **回退**：从 Stage 3 退回 Stage 1 (worked 完整示范)，重新通读 `solution.ipynb` 对应段
2. **补充 worked example**：在 tutorial.ipynb 触发 Socratic 追问，针对失败 subskill 做 4 轮苏格拉底对话
3. **诊断盲点**：写入 `student_model.json` 的 `blind_spots` 字段，标注失败 subskill + 具体错误模式 (如"Cohen's d 公式分母用错")
4. **再练习**：间隔 1 天后重做 Stage 2 (faded)，通过后再进 Stage 3
5. **追踪**：在 `student_model.json` 的 `weak_history` 字段记录触发次数与恢复时间

---

*本 practice.md 遵循 Ericsson 刻意练习 (deliberate practice) 原则：可观察技能 + 即时反馈 + 重复 + 难度递增。Worked-Faded 三阶段源自 Sweller 认知负荷理论 + Renkl 渐退示范。Interleaving 源自 Rohrer & Taylor 2007。Retry/weak_loop 源自 CS230 mastery learning。*
