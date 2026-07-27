# 刻意练习 - 营销数据表示 + 多模态 (v6.0)

> **所属单元**：技能1 · Day 2 · 营销数据表示实战 + 多模态大模型演进
> **研究依据**：Ericsson 刻意练习 5 要素 + MIT 6.5940 渐退示例 + Butler 2010 检索练习证据
> **设计原则**：每个 drill 都有明确 feedback_rule 引用本单元真实库 (sentence-transformers / transformers CLIP / torch Two-Tower / 对比学习 InfoNCE)

---

## skill_target

**核心可观察技能**：给定一个美妆电商营销场景（客户行为文本 / 产品描述 / 产品图片 / 营销文案），学生能独立选择并实现合适的表示方案（sentence-transformers 文本嵌入 / Two-Tower 对齐 / CLIP 图文对齐），并用 cosine 相似度 + KMeans 完成检索/分群/匹配任务，且能用 InfoNCE 对比损失的原理解释每一步设计选择。

---

## diagnostic (前测, 3 道, 检索练习启动)

> 不查资料, 限时 5 分钟, 检测先备知识盲点。任何一题失败 -> 标记进 student_model.json 的 `weak_points`。

1. **D0-1**：客户嵌入空间和产品嵌入空间为什么不能直接算 cosine 相似度？请用"对齐"一词作答。
2. **D0-2**：InfoNCE 损失 `L = -log[exp(sim(u,v⁺)) / Σ exp(sim(u,vᵢ))]` 中, v⁺ 和 vᵢ 分别指什么？温度参数 τ 变小会让模型对正确匹配的"信心"变强还是变弱？
3. **D0-3**：CLIP (2021) 到 GPT-4o (2024) 的本质转变是什么？请用"双塔 vs 原生多模态"对比一句话作答。

---

## subskills (3 项, 对应 Ericsson 子技能分解)

- **S1 文本语义嵌入**：用 sentence-transformers 把客户行为文本 / 产品描述 / 营销文案编码为 384 维向量, 并用 cosine 相似度做检索、用 KMeans + Silhouette 做分群。
- **S2 双塔对齐**：用 torch 实现 Two-Tower 模型, 理解 InfoNCE 对比损失 + 负采样如何让客户向量和产品向量在共享空间对齐。
- **S3 图文对齐与多模态演进**：用 transformers CLIPModel 做产品图-文匹配, 理解 CLIP -> BLIP-2 -> GPT-4o -> LLaVA 的演进路线及每个阶段的营销应用与局限。

---

## drills (>=3, 每 drill 含 difficulty / reps_required / feedback_rule / worked_faded)

### drill_id: D1
- **目标 subskill**：S1 文本语义嵌入
- **difficulty**：2 (1-5)
- **reps_required**：3
- **feedback_rule**：
  - 若学生用 TF-IDF 或 bag-of-words -> 反馈："TF-IDF 词不重叠时相似度为 0, '跑步鞋'和'运动鞋'语义相关但 TF-IDF 抓不到。回到 sentence-transformers, 它基于 BERT/RoBERTa 预训练, 能编码语义。"
  - 若学生 KMeans 选 K 时只看 inertia -> 反馈："inertia 单调下降无法选 K, 必须用 Silhouette score 评估簇内紧密度 vs 簇间分离度。参考对比学习的思想: 同类拉近、异类推远。"
  - 若学生 cosine 相似度忘记归一化 -> 反馈："cosine 要求 ||u||·||v||, sentence-transformers 输出未归一化, 必须先 normalize 或用 model.encode(..., normalize_embeddings=True)。"
- **worked_faded** (三阶段渐退示例)：
  - **完整示范 (Worked)**：给定 3 条客户行为文本, 完整演示 `model.encode() -> normalize -> cosine_similarity -> argsort top-3`。
  - **部分填空 (Faded)**：给出 encode 调用, 学生填 normalize + cosine 部分。
  - **独立解 (Independent)**：学生从 0 实现 "产品描述 -> 向量 -> top-5 相似产品检索"。

### drill_id: D2
- **目标 subskill**：S2 双塔对齐 (Two-Tower + InfoNCE)
- **difficulty**：4 (1-5)
- **reps_required**：3
- **feedback_rule**：
  - 若学生把客户和产品塞进同一个 MLP -> 反馈："Two-Tower 的关键是双塔分离, 客户塔和产品塔独立编码后在共享空间对齐。这是对比学习的核心: 同一个对象不同视图对齐, 不是特征堆叠。"
  - 若学生 InfoNCE 分母只用 1 个负样本 -> 反馈："InfoNCE 是多分类, 分母需要多个负样本才能形成对比信号。参考 CLIP 的 N×N 相似度矩阵: 对角线为正, 非对角线为负。负采样数太少会让对比信号过弱。"
  - 若学生忘记温度参数 τ -> 反馈："CLIP 对称 InfoNCE 中 τ 控制区分敏感度, τ 越小模型对正确匹配的信心越强。试 τ=0.01 vs τ=1.0 对比 loss 曲线。"
  - 若学生在线服务阶段重新计算产品向量 -> 反馈："工业部署产品向量预计算 + ANN 索引, 实时只算用户向量。你这是把推理成本搞错了 1000 倍。"
- **worked_faded**：
  - **Worked**：完整演示 Two-Tower 前向 + InfoNCE loss 计算 (batch_size=4, 1 正 3 负)。
  - **Faded**：给出双塔结构, 学生填 InfoNCE loss 部分 (分子正样本 sim, 分母 sum exp)。
  - **Independent**：学生独立实现负采样 + 在线检索 (预计算产品向量 + cosine top-k)。

### drill_id: D3
- **目标 subskill**：S3 图文对齐 (CLIP) + 多模态演进
- **difficulty**：3 (1-5)
- **reps_required**：3
- **feedback_rule**：
  - 若学生用 CLIPModel 直接生成文案 -> 反馈："CLIP 是对比学习双塔, 只能做图文匹配/检索, 不能生成。要生成需 BLIP-2 / GPT-4o / LLaVA。这是 CLIP vs GPT-4o 的本质区别: 双塔 vs 原生多模态。"
  - 若学生 CLIP 相似度矩阵忘记对称 -> 反馈："CLIP 训练用对称 InfoNCE, 同时最大化图文和文图方向。你的 loss 只算了图->文方向, 缺了文->图方向。"
  - 若学生把 CLIP 和 GPT-4o 都归为"多模态" -> 反馈："CLIP 是'编码后对齐', GPT-4o 是'统一 token 空间, 无对齐步骤'。前者只能匹配, 后者能理解跨模态细微关联。这个区别决定你的营销系统能不能'看图评价文案语气'。"
- **worked_faded**：
  - **Worked**：完整演示 CLIPModel 输入 1 图 + 3 文本, 输出相似度 + argmax 匹配。
  - **Faded**：给出图像预处理 + 文本 tokenize, 学生填相似度矩阵 + 对称 InfoNCE 计算。
  - **Independent**：学生独立完成 CLIP->BLIP-2->GPT-4o->LLaVA 四阶段对比表 (架构/能力/营销应用/局限)。

---

## progressive_project (渐进交付, 对应 MIT Sloan 行动学习 + CS230 milestone)

> 一个贯穿本单元 6 TODO 的小项目, 分 4 阶段交付, 每阶段有 gate 检查:

- **P1 Proposal (TODO1-2)**：选定美妆电商场景, 完成客户 embedding + KMeans 分群 + 产品 embedding + cosine 检索。Gate: Silhouette > 0.1, 检索 top-5 主观合理。
- **P2 Milestone (TODO3-4)**：完成内容 embedding + Two-Tower 双塔 + InfoNCE 训练。Gate: InfoNCE loss 在 100 epoch 内下降 > 30%。
- **P3 Final (TODO5)**：完成 CLIP 图文对齐, 给出产品图-文相似度矩阵 + 错配分析。Gate: top-1 匹配准确率 > 60%。
- **P4 Poster (TODO6)**：CLIP->GPT-4o 演进对比表 + 300 字 "我的营销场景中四大表示类型哪个最难构建" 反思。Gate: 演进表四阶段完整 + 反思含"数据/模型/融合"三维度至少一个判断。

---

## interleaving (A1B1C1 交叉排布, 不块状)

> 研究依据: MIT Open Learning 明文原则 - 交叉练习 (A1B1C1...B2C2A2...C3A3B3) 比块状 (AAABBBCCC) 长期保留度高 40%+。

本单元练习不按 S1->S2->S3 块状排, 而是交叉:

```
A1 (D1 Worked 文本嵌入) -> B1 (D2 Worked Two-Tower) -> C1 (D3 Worked CLIP)
-> B2 (D2 Faded InfoNCE) -> C2 (D3 Faded 对称损失) -> A2 (D1 Faded normalize)
-> C3 (D3 Independent 演进表) -> A3 (D1 Independent 检索) -> B3 (D2 Independent 负采样)
```

明文: 学生每轮都切换 subskill, 强迫大脑每次重新加载上下文 -> 检索练习效应 (Butler 2010: 推断题 68% vs 重学 44%)。

---

## retry_policy (CS229 / CS230 风格)

- **late days**：每单元 2 天宽限期, 每天罚 20% 分数 (CS230 风格)。
- **重做**：drill 未达 reps_required=3 的熟练度阈值, 可重做, 取最高分。
- **诊断失败**：diagnostic 3 题任一失败不扣分, 但必须触发 weak_loop。

---

## weak_loop (连续 2 次失败触发弱项循环)

> 研究依据: NUS Autograder 即时反馈 + Schol-Astic mastery learning。

**触发条件**：学生同一 drill 连续 2 次提交失败 (autograder 红灯)。

**回退路径**：
1. 回退到上一 difficulty (如 D2 difficulty=4 -> 退到 D2 的 Worked 阶段重看)。
2. 补充 1 个 worked example (与本 drill 同类, 但更简单的场景)。
3. 触发 tutorial.ipynb 的 Socratic loop, 由 Oxford fellow persona 追问失败点的因果链。
4. 写入 student_model.json: `{"weak_drill": "D2", "fail_count": 2, "scaffold_level": "faded", "recommended_review": ["D1", "InfoNCE basics"]}`。
5. 通过 worked example 后才能重试本 drill, 防止"瞎试"。

---

## 与本单元其他文件的对齐

- `starter.ipynb` 6 个 TODO 对应 P1-P4 progressive_project 的交付物。
- `schedule.json` 间隔重复覆盖 S1-S3 的核心概念 (CLIP / Two-Tower / InfoNCE / 对比学习)。
- `alignment.md` ILO↔TLA↔AT 矩阵的 TLA 列引用本文件的 drill_id。
- `tutorial.ipynb` 的 Socratic loop 在 D2/D3 失败时触发 weak_loop。
