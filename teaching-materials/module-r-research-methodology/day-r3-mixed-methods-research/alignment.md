# alignment.md · U-R3 混合方法研究 · 建构对齐 (Biggs ILO ↔ TLA ↔ AT)

> **理论基础**：Biggs (1996) 建构对齐 (Constructive Alignment) -- 预期学习产出 (ILO) 驱动教学学习活动 (TLA) 与评估任务 (AT)，三者对齐则学习发生；不对齐则学生"钻空子"通过考试但未达成 ILO。
> **本单元 mastery 阈值**：>=80% (每个 AT 的评分细则见下表)。

---

## ILO ↔ TLA ↔ AT 矩阵

| ILO (预期学习产出) | TLA (教学学习活动) | AT (评估任务) | mastery_threshold |
|---|---|---|---|
| **ILO1**：能阐述 MMR 三种核心设计 (Convergent/Explanatory Sequential/Exploratory Sequential) 与 Morse 三种整合策略 (Merging/Explaining/Building) 的适用场景与逻辑 | ① `notes.md` 关键回顾 2-3 (理论索引)<br>② `practice.md` drill D4 (设计类型选择 worked-faded 三阶段)<br>③ `tutorial.ipynb` Socratic 追问 (cell3-cell4) | ① `starter.ipynb` TODO3-4 (codebook+主题分析)<br>② `tutorial.ipynb` 后测 (cell5 Hattie 4 级反馈)<br>③ `practice.md` D4 Stage 3 独立解 (3 场景配对论证) | >=80% (3 场景设计+策略全对 2 个以上) |
| **ILO2**：能用 pandas+scipy.stats 对 causaldata NSW 真实数据 (445 条观测) 执行 Welch t 检验并计算 Cohen's d，正确解读"统计显著 vs 实际重要" | ① `starter.ipynb` TODO1-2 (TODO 填空脚手架)<br>② `practice.md` drill D1 (S1 worked-faded 三阶段)<br>③ `solution.ipynb` 对应段 worked 示范 | ① `solution.ipynb` TODO1-2 完整 t 检验+d 计算<br>② `practice.md` D1 Stage 3 独立解<br>③ 300 字分析 (作业) 中的效应量解读 | >=80% (t, p, d, 解读 4 项全对 3 项以上) |
| **ILO3**：能构建 joint display 联合展示矩阵 (4 主题 × 3 统计量) 并用 Beta-Binomial 模型做贝叶斯整合，论证后验 vs 频率派结论差异 | ① `starter.ipynb` TODO4-5 (joint display + Beta-Binomial)<br>② `practice.md` drill D3 (S3 worked-faded)<br>③ `solution.ipynb` 贝叶斯后验 worked | ① `solution.ipynb` TODO4-5 联合矩阵+后验<br>② `practice.md` D3 Stage 3 独立解 (含 α,β 选择论证)<br>③ 300 字分析中"贝叶斯 vs 频率派"差异段 | >=80% (joint display 4×3 完整 + 后验计算正确 + 差异论证非空话) |
| **ILO4**：能设计 LLM-as-a-judge 定性编码提示词并用 Cohen's kappa 评估人工 vs LLM 编码一致性，识别 LLM 偏差主题 | ① `starter.ipynb` TODO6 (LLM 编码提示词模板)<br>② `practice.md` drill D2 (S2 worked-faded)<br>③ `tutorial.ipynb` cell4 student_model 盲点追踪 | ① `solution.ipynb` TODO6 kappa 计算<br>② `practice.md` D2 Stage 3 独立解 (codebook+8 条编码+kappa)<br>③ `tutorial.ipynb` 后测 (LLM 偏差主题识别) | >=80% (kappa 计算正确 + 识别 >=1 个 LLM 偏差主题) |

---

## 3 自检问题 (Feed Up / Feed Back / Feed Forward)

### 自检 1 · Feed Up (TLA 是否训练 ILO?)
> **问题**：每个 ILO 是否都有至少 1 个 TLA 直接训练其可观察技能？

**答**：是。
- ILO1 -> TLA② D4 worked-faded 三阶段直接训练"设计+策略配对论证"
- ILO2 -> TLA② D1 worked-faded 三阶段直接训练"t 检验 + Cohen's d"
- ILO3 -> TLA② D3 worked-faded 三阶段直接训练"joint display + 贝叶斯整合"
- ILO4 -> TLA② D2 worked-faded 三阶段直接训练"codebook + kappa"

**结论**：4/4 ILO 都有 drill 直接训练。对齐成立。

### 自检 2 · Feed Back (AT 是否测量 ILO?)
> **问题**：每个 AT 是否都直接测量对应 ILO 的可观察产出，而非测量无关技能？

**答**：是。
- AT(ILO1)=D4 Stage 3 独立解 -> 直接测量"3 场景配对论证" (ILO1 产出)
- AT(ILO2)=D1 Stage 3 独立解 + 300 字分析 -> 直接测量"t, p, d, 解读" (ILO2 产出)
- AT(ILO3)=D3 Stage 3 独立解 + 差异段 -> 直接测量"joint display + 后验 + 差异论证" (ILO3 产出)
- AT(ILO4)=D2 Stage 3 独立解 -> 直接测量"codebook + kappa + 偏差主题" (ILO4 产出)

**结论**：4/4 AT 都精准测量对应 ILO。无"考的与学的脱节"。对齐成立。

### 自检 3 · Feed Forward (不经 TLA 能过 AT 吗?)
> **问题**：若学生跳过所有 TLA (不做 starter TODO、不练 drill、不上 tutorial)，能直接通过 AT 吗？若能，则对齐失败 (说明 AT 太简单或与 TLA 无关)。

**答**：否。
- AT(ILO1)=D4 Stage 3 要求"3 场景设计+策略配对论证" -- 不读 notes.md 关键回顾 (TLA①) 不可能知道 Morse 三策略；不练 D4 worked-faded (TLA②) 不可能写出 3 个场景的配对论证
- AT(ILO2)=D1 Stage 3 要求"独立 t 检验+d+解读" -- 不练 `scipy.stats.ttest_ind` (TLA① starter TODO1-2) 不可能写出 `equal_var=False`；不练 D1 worked (TLA②) 不可能正确解读 d=0.2
- AT(ILO3)=D3 Stage 3 要求"α,β 选择论证" -- 不读 `solution.ipynb` 贝叶斯段 (TLA③) 不可能知道如何把定性置信度转 Beta 先验
- AT(ILO4)=D2 Stage 3 要求"kappa + 偏差主题" -- 不练 TODO6 (TLA①) 不可能写 LLM-as-a-judge 提示词；不上 tutorial.ipynb cell4 (TLA③) 不可能追踪 LLM 偏差主题

**结论**：4/4 AT 都必须经过 TLA 才能通过。无"绕过 TLA 钻空子"路径。对齐成立。

---

## mastery 阈值与补救

- **总 mastery 阈值**：4 个 ILO 的 AT 平均 >=80%
- **单 ILO 未达 80%**：触发 `practice.md` weak_loop (回退 Stage 1 worked + 补充 worked example + 1 天后重做 Stage 2)
- **2 个以上 ILO 未达 80%**：触发 `tutorial.ipynb` Socratic 深度追问 (cell3 多轮) + `schedule.json` FSRS-6 间隔缩短 (due 改为 [0.5, 2, 5, 14, 30, 90])
- **全 ILO 达 80% 以上**：进入下一单元 (R4 PRISMA)，并在 schedule.json 标记 C1-C6 ef0 +0.2

---

*本 alignment.md 遵循 Biggs (1996) 建构对齐理论：ILO 驱动 TLA 与 AT，三者对齐则学习发生。Feed Up/Back/Forward 三自检源自 Hattie & Timperley (2007) 反馈模型。mastery 阈值源自 Bloom (1968) mastery learning。*
