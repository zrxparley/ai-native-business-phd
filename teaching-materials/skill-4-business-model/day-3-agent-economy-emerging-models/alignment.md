# Constructive Alignment - U4D3 Agent经济 + 新兴商业模式 (v6.0 学习科学层)

> 理论依据: Biggs 建构对齐 (Constructive Alignment) - ILO (Intended Learning Outcomes) ↔ TLA (Teaching/Learning Activities) ↔ AT (Assessment Tasks) 三者必须对齐。
> v6.0 新增 mastery_threshold (掌握阈值) + 3 自检问题 (Feed Up / Feed Back / Feed Forward)。

---

## ILO ↔ TLA ↔ AT 矩阵 (>=3 行)

| ILO (预期学习产出) | TLA (教学学习活动) | AT (评估任务) | mastery_threshold |
|---|---|---|---|
| **ILO1**: 能用 mesa 构建 Agent经济仿真（3 类 Agent + DataCollector + 8 个 model_reporters + 破产机制） | starter.ipynb drill D1 (Worked->Faded->独立) + tutorial.ipynb Socratic 追问 Q1-Q2 + schedule.json C1 卡片复习 | solution.ipynb 解题 (6 TODO 全填) + tutorial 后测 + D1 drill 3 次重复通过 | >=80% TODO 正确率 + D1 reps_required=3 全通过 |
| **ILO2**: 能用 pandas + matplotlib 分析涌现现象（Gini 0.108->0.857 / A2A 104 笔 / 价格收敛 / Agent 存活）背后微观 Agent 行为 | drill D2 (单变量->双变量->三变量 batch_run 扫描) + schedule.json C2/C3 卡片 + 天道推演「因果链追踪」章节 | 300 字涌现分析文 + 4 个子图 (基尼/价格/存活/A2A) + D2 drill 双变量扫描曲面图 | >=70% 量表评分 (涌现机制 3 条 + 反单一变量归因) |
| **ILO3**: 能用天道推演视角做商业模式沙盘对比（方案A 高抽成低推理成本 vs 方案B 低抽成高推理成本，3 层推演 + 概率评估 + 最优路径） | drill D3 (单场景->双场景->三场景含黑天鹅) + worked-faded 示范 + 天道推演×多Agent仿真章节 + tutorial Q3-Q5 | 天道推演沙盘报告 (2-3 条时间线 + 风险预警 + 最优路径 + 认知盲点) | 能独立解 (无 scaffold, Faded-2 阶段) + 报告含全部 5 要素 |

---

## mastery_threshold (掌握阈值)

- **ILO1**: >=80% TODO 正确率 + D1 drill `reps_required=3` 全通过（每次 >15 分钟不算水过）
- **ILO2**: >=70% 量表评分（涌现机制 3 条 + 反单一变量归因 + DataCollector 时间序列引用）
- **ILO3**: 能独立解（Faded-2 阶段无 scaffold）+ 沙盘报告含 5 要素（2-3 时间线 / 风险预警 / 最优路径 / 概率分布 / 认知盲点）

未达 mastery_threshold 触发 `practice.md` 的 `weak_loop`：回退上一 drill 的 Worked 示范 + 隔天重做。

---

## 3 自检问题 (Biggs 构建构对齐自检)

### 1. TLA 是否训练 ILO? (Feed Up - 目标对齐)
- drill D1 (mesa 编码) 是否训练了 ILO1 的"3 类 Agent + DataCollector + 8 个 model_reporters"？
  - 是。D1 的 Worked->Faded->独立 三阶段恰好覆盖 ConsumerAgent / MerchantAgent / MediatorAgent 三类 + DataCollector 配置。
- drill D3 (天道推演沙盘) 是否训练了 ILO3 的"3 层推演 + 概率评估 + 最优路径"？
  - 是。D3 的 Faded-2 阶段强制要求 2-3 条时间线 + 概率分布 + 最优路径 + 风险预警 + 认知盲点。
- **若 TLA 未训练 ILO**: 调整 drill 的 feedback_rule 或增加 worked example。

### 2. AT 是否测量 ILO? (Feed Back - 评估对齐)
- solution.ipynb 正确率是否测量 ILO1？是，6 TODO 覆盖 3 类 Agent + DataCollector + 仿真运行 + 绘图。
- 300 字涌现分析是否测量 ILO2？是，要求引用 DataCollector 时间序列 + 反单一变量归因。
- 沙盘报告是否测量 ILO3？是，5 要素清单对应天道推演 5 能力。
- **若 AT 未测量 ILO**: 增加 AT 的评分量表 (rubric) 维度。

### 3. 不经 TLA 能过 AT 吗? 若能 = 对齐失败 (Feed Forward - 反投机)
- 若学生跳过 mesa 上机 (TLA)，能否写 300 字涌现分析 (AT)？
  - **若能 = 对齐失败**。修复：AT 强制要求引用具体 tick 数据 + DataCollector 输出，未跑仿真无法伪造。
- 若学生跳过 D3 drill (TLA)，能否写沙盘报告 (AT)？
  - **若能 = 对齐失败**。修复：AT 强制要求 2-3 条平行世界场景 + 概率分布，未做 batch_run 扫描无法伪造。
- **Feed Forward**: 不经 TLA 能过 AT 的漏洞一经发现，立即在 AT 中加入"必须引用 TLA 产物"的硬约束（如具体 tick 数据 / batch_run 曲面图）。

---

## 对齐矩阵可视化 (Biggs 三角)

```
        ILO1 (mesa 编码)
         /            \
   TLA: D1 drill     AT: solution.ipynb
        \            /
         mastery>=80%
         
        ILO2 (涌现分析)
         /            \
   TLA: D2 drill     AT: 300字分析+4子图
        \            /
         mastery>=70%
         
        ILO3 (天道推演)
         /            \
   TLA: D3 drill     AT: 沙盘报告
        \            /
         mastery=独立解
```

三者闭环: ILO -> TLA -> AT -> 反馈 -> 回到 TLA (弱项循环) 或进入下一 ILO。
