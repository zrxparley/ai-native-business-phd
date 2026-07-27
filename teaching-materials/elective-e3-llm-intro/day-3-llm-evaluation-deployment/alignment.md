---
unit: U-E3-D3
title: LLM 评估与部署 - 建构对齐 (Constructive Alignment)
version: v6.0
frameworks: [Biggs-constructive-alignment, Bloom-revised, mastery-learning]
---

# 建构对齐 - LLM 评估与部署 (v6.0)

> 基于 Biggs (1996) 建构对齐: ILO (Intended Learning Outcome) ↔ TLA (Teaching-Learning Activity) ↔ AT (Assessment Task) 三者对齐。Mastery threshold 借鉴 Bloom (1968) mastery learning。每行对齐可追溯。

---

## 1. ILO ↔ TLA ↔ AT 对齐矩阵

> ILO = 预期学习产出 (本单元学完能做到什么)
> TLA = 教学学习活动 (引用本单元的 starter/drill/tutorial)
> AT = 评估任务 (引用 solution/tutorial 后测)
> mastery_threshold = 通过阈值 (Bloom mastery: >=80%)

| ID | ILO (预期学习产出) | TLA (教学学习活动) | AT (评估任务) | mastery_threshold |
|----|-------------------|-------------------|--------------|-------------------|
| **L1** | 能阐述 LLM 评估三层框架 (通用/任务/系统), 并说明"标准基准用于初筛, 最终评估须在真实业务数据上"的工程原则 | ① 读 notes.md § 关键回顾 1<br>② 做 practice.md Diagnostic D1<br>③ tutorial.ipynb cell2 pre-tutorial essay | ① practice.md Drill-01 的 F 阶段 (写 `_score_faithfulness`)<br>② solution.ipynb TODO1 (评测集构建)<br>③ tutorial.ipynb cell3 Socratic round 1 | >=80% (四维度评分合理 + 能指出 MMLU 初筛的局限) |
| **L2** | 能用 deepeval 自定义 `MarketingQualityMetric` (继承 `BaseMetric`), 对营销文案做四维度 (准确/相关/无害/忠实) 评分, 输出 `MetricMeasurement(score, reason)` | ① 读 notes.md § 关键回顾 3 (四维度营销映射)<br>② 做 practice.md Drill-01 (W->F->I 三阶段)<br>③ starter.ipynb TODO2/TODO3<br>④ tutorial.ipynb cell5 Hattie [TASK] 反馈 | ① practice.md P2 Milestone (deepeval 可跑 .ipynb)<br>② solution.ipynb TODO2/TODO3 对拍<br>③ practice.md Drill-01 I 阶段独立解 | >=80% (4 维度评分 + reason 引用真实文案 + 权重可配置) |
| **L3** | 能用 langsmith `@traceable` + tiktoken 监控部署后 LLM 调用, 输出 gpt-4o vs DeepSeek V3 日均万次成本对比 | ① 读 notes.md § 上机任务 TODO4/TODO5<br>② 做 practice.md Drill-02 (W->F->I)<br>③ starter.ipynb TODO4/TODO5<br>④ tutorial.ipynb cell4 student_model 读写 | ① practice.md P3 Final (成本对比 + 300 字分析)<br>② solution.ipynb TODO4/TODO5 对拍<br>③ practice.md Drill-02 I 阶段 (成本瓶颈识别) | >=80% (@traceable + tiktoken 精确计数 + 成本误差<5%) |
| **L4** | 能解释 vLLM/投机解码/MoE/量化 四大推理优化技术原理, 并按 GPU/延迟/吞吐给出选型决策树 | ① 读 notes.md § 关键回顾 5 + § 2026 前沿 (vLLM/投机解码/MoE)<br>② 做 practice.md Drill-03 (W->F->I)<br>③ starter.ipynb TODO6 (LLM-as-Judge 规则近似)<br>④ tutorial.ipynb cell3 Socratic round 4 | ① practice.md P4 Poster (决策树 + 真实 case)<br>② practice.md Drill-03 I 阶段 (选型报告)<br>③ tutorial.ipynb cell6 exit artifact | >=80% (4 方案 + 5 维输入 + 真实 case 验证) |
| **L5** | 能说明为什么 DeepSeek V3 (MoE, 671B/37B) 能用 1/10 成本逼近 GPT-4o 质量, 并对模型选型与部署架构给出启示 | ① 读 notes.md § 2026 前沿 MoE 节<br>② 做 practice.md Diagnostic D3<br>③ tutorial.ipynb cell3 Socratic round 3 (反例追问) | ① practice.md P3 Final 的 300 字分析<br>② tutorial.ipynb cell5 Hattie [FEED-FORWARD] | >=80% (MoE 激活参数解释 + 成本测算 + 选型启示) |

---

## 2. 三自检问题 (Hattie Feed Up / Feed Back / Feed Forward)

> Hattie (2007) Visible Learning: 反馈分三层 - Feed Up (目标在哪) / Feed Back (现在到哪) / Feed Forward (下一步去哪)。

### Q1. Feed Up: TLA 是否训练 ILO?

逐行检查 TLA 列:

- **L1**: TLA 含 notes.md 阅读 + Diagnostic D1 + tutorial essay。D1 直接问 "MMLU 初筛的局限", 与 ILO "阐述三层框架" 直接对齐。✅ 训练
- **L2**: TLA 含 Drill-01 (W->F->I) + starter TODO2/3 + tutorial [TASK] 反馈。Drill-01 的 I 阶段要求从零写 `MarketingQualityMetric`, 与 ILO "自定义 BaseMetric" 直接对齐。✅ 训练
- **L3**: TLA 含 Drill-02 + starter TODO4/5 + student_model 读写。Drill-02 的 I 阶段要求输出日均万次成本预测, 与 ILO "成本对比" 直接对齐。✅ 训练
- **L4**: TLA 含 Drill-03 + starter TODO6 + Socratic round 4。Drill-03 的 I 阶段要求选型报告, 与 ILO "决策树" 直接对齐。✅ 训练
- **L5**: TLA 含 MoE 节 + D3 + Socratic round 3。D3 直接问 "非价格因素", 与 ILO "启示" 对齐。✅ 训练

**结论**: 5/5 TLA 均训练 ILO。无空转活动。

### Q2. Feed Back: AT 是否测量 ILO?

逐行检查 AT 列:

- **L1**: AT = Drill-01 F 阶段 + solution TODO1 + Socratic round 1。F 阶段要求写 `_score_faithfulness`, 直接测量 "理解四维度"。✅ 测量
- **L2**: AT = P2 Milestone + solution TODO2/3 对拍 + Drill-01 I 阶段。P2 要求 "可跑 .ipynb", 直接测量 "自定义 BaseMetric"。✅ 测量
- **L3**: AT = P3 Final + solution TODO4/5 对拍 + Drill-02 I 阶段。P3 要求 "成本对比 + 300 字分析", 直接测量 "成本对比"。✅ 测量
- **L4**: AT = P4 Poster + Drill-03 I 阶段 + tutorial exit artifact。P4 要求 "决策树 + 真实 case", 直接测量 "决策树"。✅ 测量
- **L5**: AT = P3 的 300 字分析 + tutorial [FEED-FORWARD]。300 字分析要求 "成本差异 + 选型启示", 直接测量 "启示"。✅ 测量

**结论**: 5/5 AT 均测量 ILO。无测量空隙。

### Q3. Feed Forward: 不经 TLA 能过 AT 吗? 若能 = 对齐失败

> 这是 Biggs 建构对齐的关键检验: 如果学生跳过 TLA 仍能过 AT, 说明 AT 测量的是先验知识而非 TLA 训练的产出, 对齐失败。

- **L1**: 跳过 notes.md 阅读 + D1, 能否过 Drill-01 F 阶段? 不能, 因为 F 阶段要求写 `_score_faithfulness`, 需要先理解 RAGAS 检索忠实度概念。✅ 对齐
- **L2**: 跳过 Drill-01 W/F + starter TODO2/3, 能否过 P2 Milestone? 不能, P2 要求可跑 .ipynb, 需要 deepeval API 实操经验。✅ 对齐
- **L3**: 跳过 Drill-02 + starter TODO4/5, 能否过 P3 Final? 不能, P3 要求成本误差 <5%, 需要 tiktoken 精确计数经验 (非 split 估算)。✅ 对齐
- **L4**: 跳过 Drill-03 + starter TODO6, 能否过 P4 Poster? 理论上能 (决策树可背), 但 P4 要求 "真实 case 验证", 无 Drill-03 经验难以完成 case 部分。⚠️ 部分对齐, 加固: P4 评分维度加 "case 可复现性" 20% 权重
- **L5**: 跳过 MoE 节 + D3, 能否过 300 字分析? 不能, 300 字要求 "MoE 激活参数解释", 需要先读 notes.md § 2026 前沿 MoE 节。✅ 对齐

**结论**: 4/5 严格对齐, L4 部分对齐已加固 (P4 加 case 复现权重)。无致命对齐失败。

---

## 3. Mastery Threshold 校准 (Bloom mastery learning)

> Bloom (1968) mastery learning: 80% 阈值。本单元 5 个 ILO 均设 >=80%。

| ILO | mastery_threshold | 校准依据 |
|-----|-------------------|---------|
| L1 | >=80% | 四维度评分合理 + 能指出 MMLU 局限, 缺一不可 |
| L2 | >=80% | 4 维度 + reason 引用 + 权重可配置, 三项全对 |
| L3 | >=80% | @traceable + tiktoken + 误差<5%, 三项全对 |
| L4 | >=80% | 4 方案 + 5 维输入 + 真实 case, 三项全对 |
| L5 | >=80% | MoE 激活解释 + 成本测算 + 启示, 三项全对 |

**未达 mastery 的补救**: 触发 practice.md § 7 Weak Loop (回退 + Worked Example + 24h 间隔重试 + tutorial Socratic)。

---

*v6.0 建构对齐层。基于 Biggs (1996) + Bloom (1968) + Hattie (2007)。*
