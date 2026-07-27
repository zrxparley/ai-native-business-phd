# Constructive Alignment - U-skill1-day4 多模态融合与跨域对齐

> Biggs 建构对齐 (Constructive Alignment): ILO (Intended Learning Outcomes) ↔ TLA (Teaching/Learning Activities) ↔ AT (Assessment Tasks) 三者必须对齐，学生才会在正确的认知活动上投入精力。本单元 v6.0 学习科学层在 v5.0 上机基础上显式化对齐矩阵。

## ILO ↔ TLA ↔ AT 矩阵

| ILO (预期学习产出) | TLA (教学学习活动) | AT (评估任务) | mastery_threshold |
|---|---|---|---|
| **ILO1**: 能实现多模态融合三策略（早/中/晚融合）并说明营销场景适用条件 | starter.ipynb TODO1 + practice.md drill D1 Stage 1-3 (Worked->Faded->Independent) + tutorial.ipynb Socratic 第 1-2 轮 | solution.ipynb TODO1 完整解 + practice.md D1 Stage 3 独立产出 + 300 字分析"何时选早 vs 晚融合" | >=80% (D1 Stage 3 通过 + 分析达标) |
| **ILO2**: 能从零实现 InfoNCE + CLIP 对称损失，理解温度 τ 的影响 | starter.ipynb TODO2 + practice.md drill D1/D2 + schedule.json 卡片 C1/C3 复习 + tutorial Socratic 第 3 轮追问 τ | solution.ipynb TODO2 + practice.md D2 Stage 3 + τ 实验 τ∈{0.01,0.07,0.5} 热力图 | 能独立解 + τ 实验热力图视觉区分明显 |
| **ILO3**: 能用 transformers CLIP 实现图文检索与零样本分类，分析对齐差距 | starter.ipynb TODO3/5 + practice.md drill D2 + schedule.json C3/C5 + tutorial Socratic 第 4 轮追问 prompt engineering | solution.ipynb TODO3/5 + D2 Stage 3 独立 image_to_text_retrieval + zero-shot confusion matrix | top-1 准确率 >=70% (模拟数据) + margin 分析正确 |
| **ILO4**: 能用 BLIP-2 实现 captioning/VQA 并对比 CLIP 双塔本质区别 | starter.ipynb TODO4 + practice.md drill D3 Stage 1-2 + schedule.json C4 + tutorial Socratic 第 5 轮追问 Q-Former | solution.ipynb TODO4 + D3 Stage 2 架构图填空 + 口头对比"双塔 vs Q-Former vs 原生多模态" | 能独立调 BlipForConditionalGeneration + 口头对比通过 |
| **ILO5**: 能设计企业级多模态架构，评估各模块延迟与瓶颈 | starter.ipynb TODO6 + practice.md drill D3 Stage 3 (progressive project M3) + schedule.json C7 + tutorial 限频 exit artifact | solution.ipynb TODO6 + D3 Stage 3 独立架构图 + 2 瓶颈标注 + 1 单点故障 | 架构图含 4 层 + 瓶颈分析通过 |

## mastery_threshold (单元整体)

- **及格 (B-)**: 5 个 ILO 中 >=4 个达标 + schedule.json 7 卡片 21 天复习完成率 >=80%
- **精通 (A)**: 5 个 ILO 全部达标 + progressive project M3 交付 + tutorial.ipynb exit artifact 列出 >=2 个认知盲点
- **不达标**: 任意 ILO 连续 2 次 AT 失败且 weak_loop 3 轮未恢复 -> 触发 1:1 tutorial 升级

## 3 自检问题 (Biggs 三反馈)

> 教师与学生共用。每次 AT 后必答。来自 Hattie & Timperley (2007) 的 Feed Up / Feed Back / Feed Forward 三问。

1. **Feed Up (TLA 是否训练 ILO?)**：本单元的 6 个 TODO 填空 + 3 个 drill + 7 张复习卡，是否真的训练了"实现+对齐+架构"三个能力？有没有哪个 ILO 学生只能通过死记 schedule.json 答案而绕过 TLA 直接过 AT？如果存在，TLA 设计失败，需补 drill。
2. **Feed Back (AT 是否测量 ILO?)**：solution.ipynb 解题 + D1-D3 Stage 3 独立产出 + τ 实验热力图，是否真的能区分"懂了 vs 没懂"？还是只要抄 solution 就能过？需要加口头辩护环节（tutorial.ipynb Socratic 追问）防止抄答案。
3. **Feed Forward (不经 TLA 能过 AT 吗？)**：如果学生不写 starter.ipynb、不跑 drill、不复习 schedule.json，只看 solution.ipynb 然后照抄，能否通过 AT？若能 = 对齐失败。修复：AT 加入"现场限时手写 InfoNCE 公式 + 口述 Q-Former 作用"环节，抄答案无法通过。

## 跨单元对齐

- **回看 Day 3**：本单元 ILO2 的对比学习对齐是 Day 3 表示学习的延伸（从单模态到跨模态）
- **前置 Day 5**：本单元 ILO5 的企业架构是 Day 5 系统设计 Capstone 的子模块
- **跨技能 3**：本单元"跨域对齐"与技能 3 因果推断的"跨域"在方法论上互通（都是让异构数据在共享空间可比）

---

*本对齐矩阵基于 Biggs (1996) Constructive Alignment + Hattie & Timperley (2007) RER 77(1):81-112 三反馈 + MIT 6.5940 mastery 阈值设计。*
