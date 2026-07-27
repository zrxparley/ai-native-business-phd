# Constructive Alignment - 营销数据表示 + 多模态 (v6.0)

> **Biggs 建构对齐原则**: ILO (Intended Learning Outcomes) ↔ TLA (Teaching/Learning Activities) ↔ AT (Assessment Tasks) 三者必须对齐, 任何一环脱节即"对齐失败"。
> **研究依据**: Biggs (1996) 建构对齐 + Hattie (2007 RER 77(1):81-112) 形成性反馈 + MIT 6.5940 mastery 阈值
> **本单元定位**: 技能1 · Day 2 · 营销数据表示实战 + 多模态大模型演进

---

## ILO ↔ TLA ↔ AT 矩阵

| ILO (预期学习产出) | TLA (教学学习活动) | AT (评估任务) | mastery_threshold |
|---|---|---|---|
| ILO1: 能解释营销四大表示类型 (客户/产品/内容/跨域对齐) 的编码方法与核心挑战, 说明"分通道编码+拼接+MLP映射"融合策略 | notes.md 理论回顾 + practice.md diagnostic D0-1 + tutorial.ipynb Socratic 追问 + schedule.json C1 间隔复习 | starter.ipynb TODO1+TODO2 (客户+产品 embedding) + tutorial 后测口头辩护 | >=80% 正确率 + 能口头说出"对齐"一词 |
| ILO2: 能用 sentence-transformers 将客户行为文本/产品描述/营销文案编码为语义向量, 用 cosine 相似度做检索, KMeans+Silhouette 做分群 | practice.md drill D1 (Worked->Faded->Independent) + starter.ipynb TODO1-3 + interleaving A1/A2/A3 | starter.ipynb TODO1-3 完成 + progressive_project P1 (Silhouette>0.1, top-5 主观合理) | Silhouette > 0.1 + reps_required=3 全过 |
| ILO3: 能用 PyTorch 实现 Two-Tower 双塔模型, 理解 InfoNCE 对比损失+负采样如何让客户向量与产品向量在共享空间对齐 | practice.md drill D2 (Worked->Faded->Independent) + starter.ipynb TODO4 + tutorial Socratic loop 4轮 + schedule.json C3+C6 间隔复习 | starter.ipynb TODO4 完成 + progressive_project P2 (InfoNCE loss 100 epoch 下降>30%) | loss 下降 > 30% + 能解释温度参数 τ 的作用 |
| ILO4: 能用 transformers CLIPModel 做图文对齐 (产品图-文匹配), 理解对比学习双塔架构与温度参数 τ | practice.md drill D3 + starter.ipynb TODO5 + interleaving C1/C2/C3 + schedule.json C4 间隔复习 | starter.ipynb TODO5 完成 + progressive_project P3 (top-1 匹配准确率>60%) | top-1 准确率 > 60% + 能解释对称 InfoNCE |
| ILO5: 能梳理 CLIP->BLIP-2->GPT-4o->LLaVA 演进路线, 指出每阶段营销应用与局限 (双塔 vs 原生多模态本质区别) | notes.md 2026前沿补充 + reading.md 深链 + tutorial devil's advocate 角色 + schedule.json C5 间隔复习 | starter.ipynb TODO6 演进对比表 + progressive_project P4 (300字反思+四阶段表) | 四阶段完整 + 反思含数据/模型/融合三维度至少一个判断 |

---

## mastery_threshold 总览

> **研究依据**: MIT 6.5940 "至少 4/5 实验提交方及格" + NUS Autograder 即时反馈 + Schol-Astic 自定步调。

| 层级 | 阈值 | 触发动作 |
|---|---|---|
| 通过 | 所有 ILO 的 AT 均达 mastery_threshold | 进入 Day 3 (企业知识图谱 + GraphRAG) |
| 部分通过 | 4/5 ILO 达标, 1 ILO 接近 (>=70%) | 触发 schedule.json 弱项卡片复习 + practice.md weak_loop |
| 不通过 | >=2 ILO 未达 70% | 回退到 Day 1 表示工程基础 + tutorial.ipynb 重做 Socratic loop |
| 重做上限 | 同一 ILO 重做 3 次仍未过 | 写入 student_model.json `blocked: true`, 触发人工干预 |

---

## 3 自检问题 (Biggs 三问, 对应 Hattie 三反馈方向)

> **研究依据**: Biggs 建构对齐 + Hattie (2007) 3 问 × 4 级反馈。每个 TLA 设计后必过这 3 问。

### 1. TLA 是否训练 ILO? (Feed Up - 目标对齐)
- ILO3 要求"用 PyTorch 实现 Two-Tower", TLA 列的 practice.md drill D2 是否真的让学生手写 InfoNCE loss?
- **自检**: 是。D2 的 Faded 阶段学生填 InfoNCE 分子分母, Independent 阶段独立实现负采样。TLA 直接训练 ILO3 的可观察技能。
- **风险**: 若学生抄 solution.ipynb, TLA 失效。缓解: tutorial.ipynb Socratic 追问"为什么 InfoNCE 分母需要多个负样本"。

### 2. AT 是否测量 ILO? (Feed Back - 测量对齐)
- ILO4 要求"用 CLIPModel 做图文对齐", AT 列的 progressive_project P3 (top-1 准确率>60%) 是否真的测量图文对齐能力?
- **自检**: 是。P3 要求学生独立完成产品图-文相似度矩阵 + 错配分析, top-1 准确率直接测量 CLIP 对齐效果。
- **风险**: top-1 准确率 60% 可能因数据偏置虚高 (如所有产品图背景相似)。缓解: P3 强制要求错配分析, 不仅看准确率, 还要分析失败原因 (背景干扰/角度/风格偏差)。

### 3. 不经 TLA 能过 AT 吗? 若能 = 对齐失败 (Feed Forward - 防绕过)
- ILO5 要求"梳理 CLIP->GPT-4o 演进", 学生能不能不看 notes.md 理论回顾、不做 TODO6, 直接抄 reading.md 的链接混过?
- **自检**: 不能。TODO6 要求学生填写四阶段对比表 (架构/能力/营销应用/局限), 每格必须用自己的话写, 抄链接无效。tutorial.ipynb 的 devil's advocate 角色会追问"为什么 GPT-4o 能理解跨模态细微关联而 CLIP 不能", 抄表答不出。
- **风险**: 学生用 ChatGPT 生成对比表。缓解: tutorial Socratic loop 口头辩护, 追问因果链 (如"温度参数 τ 变小, CLIP 的对比损失如何变化")。

---

## 与 v5.0 基线的衔接

- ILO1-5 直接复用 v5.0 notes.md 的"学习目标 (学完你能做到)"5 条, 不改原文。
- TLA 列引用 v5.0 的 starter.ipynb TODO1-6 + 新增 v6.0 的 practice.md drill + tutorial.ipynb。
- AT 列引用 v5.0 的 solution.ipynb + 新增 progressive_project 4 阶段 gate。
- mastery_threshold 是 v6.0 新增, v5.0 只有"5 分制量表", v6.0 把它量化为可测量阈值。
