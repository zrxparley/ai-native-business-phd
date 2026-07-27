# Constructive Alignment - Skill 1 Day 1: 表示学习理论

> Biggs 建构对齐 (Constructive Alignment): ILO (Intended Learning Outcomes, 预期学习产出) ↔ TLA (Teaching/Learning Activities, 教学学习活动) ↔ AT (Assessment Tasks, 评估任务) 三者必须对齐。学生才不会"学的是 A, 考的是 B"。不经 TLA 能过 AT = 对齐失败。

## ILO ↔ TLA ↔ AT 矩阵

| ILO (预期学习产出) | TLA (教学学习活动) | AT (评估任务) | mastery_threshold |
|---|---|---|---|
| ILO1: 能解释从 `f(x)=wᵀφ(x)` 到 `f(x)=wᵀφ_θ(x)` 的范式转移, 阐述 CMU 10741 三概念 (无约束=记忆 / Neural Collapse / 不可辨识性), 并说明对营销的意义 | starter.ipynb drill D1 worked-faded 阶段 1-3 + tutorial.ipynb Socratic 追问"为什么 θ 可训练就比手工特征强" + schedule.json 卡片 C1/C2 复习 | solution.ipynb TODO1 + tutorial 后测: 写出范式转移对客户分群的 2 条具体影响 + 300 字分析 | >=80% (4/5 概念题答对) |
| ILO2: 能用 sentence-transformers + scikit-learn 做 embedding 编码 + t-SNE/PCA 降维 + KMeans 聚类 + silhouette 选 K | starter.ipynb drill D2 (难度 3) worked-faded + data/README.md 真实数据浏览 + reading.md 深链阅读 + interleaving A1B1C1 交叉练习 | solution.ipynb TODO2+TODO4 + progressive_project milestone: baseline embedding + 聚类可视化 + silhouette 表 | >=70% + silhouette > 0.3 + K 选择有业务理由 |
| ILO3: 能用 torch 实现 Autoencoder 压缩 (384→64) + 评估表示质量, 理解 CMU 10741 概念一 (无约束=记忆非学习) + RepE (Zou 2023, arXiv 2310.01405) | starter.ipynb drill D3 (难度 4) worked-faded + tutorial.ipynb Socratic"瓶颈为何是约束" + reading.md RepE 条目 + interleaving C2/C3 变体 (VAE/对比学习) | solution.ipynb TODO3+TODO6 + progressive_project final: 重构损失曲线 + 下游分类准确率对比 baseline + IMRaD 报告 | 能独立解 + 重构损失收敛 + 分类准确率 > baseline 384 维 |

## mastery_threshold 汇总
- ILO1: >=80% (4/5 概念题答对, 涵盖范式转移 + CMU 三概念)
- ILO2: >=70% + silhouette > 0.3 + K 选择有业务理由 (不只看数值最高)
- ILO3: 能独立解 (worked-faded 阶段 3 通过) + 重构损失收敛 (100 epoch 内 < 0.1) + 下游分类准确率 > baseline 384 维
- 整单元 mastery: 6/6 TODO 跑通 + 300 字分析合格 + progressive_project milestone 提交 + diagnostic pset0 完成 (不计分但必交)

## 3 自检问题 (Biggs Feed Up / Feed Back / Feed Forward)

1. **Feed Up** (TLA 是否训练 ILO? 学生知道要学什么吗?)
   - 检查: drill D1-D3 的 worked-faded 三阶段是否覆盖 ILO1-ILO3 的全部可观察行为?
   - D1 训练"解释范式转移 + 用 sentence-transformers 编码" (ILO1)
   - D2 训练"用 sklearn 做降维聚类 + silhouette 选 K" (ILO2)
   - D3 训练"用 torch 实现 Autoencoder + 评估表示质量" (ILO3)
   - 结论: 是, TLA 训练 ILO, 对齐成立。

2. **Feed Back** (AT 是否测量 ILO? 学生知道学得怎样吗?)
   - 检查: solution.ipynb 的 TODO1-6 + progressive_project 是否能区分"学会 vs 没学"?
   - TODO1 测 ILO1 (编码正确性 + 维度验证)
   - TODO2-4 测 ILO2 (降维聚类 + silhouette)
   - TODO3-6 测 ILO3 (Autoencoder + 下游评估)
   - progressive_project 测 ILO1-3 综合 (DSR 框架 + 工程实践)
   - 结论: 是, AT 测量 ILO, 对齐成立。

3. **Feed Forward** (不经 TLA 能过 AT 吗? 若能 = 对齐失败, 学生知道下一步去哪吗?)
   - 检查: 学生能否不做 drill 直接抄 solution.ipynb 过 AT?
   - 若跳过 starter.ipynb 的 6 个 TODO 填空脚手架 + tutorial Socratic 追问 + worked-faded 示例, 直接抄答案能过 TODO, 但 progressive_project (proposal→milestone→final→poster) 需独立完成, 无法抄。
   - diagnostic pset0 虽不计分但强制提交, 暴露先备知识缺口。
   - tutorial.ipynb 限频 1 次/天, student_model.json 记录盲点跨单元复用, 防止抄答案依赖。
   - 结论: 不经 TLA 难过 AT (progressive_project 卡死), 对齐成立。Feed Forward: 盲点指向 reading.md + schedule.json 下次 due + 下一单元 Day 2。

---

*v6.0 学习科学层 · 建构对齐文件 · 基于 Biggs Constructive Alignment · 2026-07-25*
