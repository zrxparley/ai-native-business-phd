# 刻意练习 · Day 1 表示学习理论 (v6.0 学习科学层)

> 本文件落实 Ericsson 刻意练习 5 要素 + MIT 6.5940 Worked-Faded 渐退示例 + CS229 pset0 诊断性先测 + CS230 渐进项目脚手架 + 间隔交叉 (A1B1C1...B2C2A2...C3A3B3)。

## skill_target
**核心可观察技能**: 给定 20 条营销评论 (护肤/电子/健身 × 正面/负面), 能用 sentence-transformers `all-MiniLM-L6-v2` 编码为 384 维 embedding, 用 scikit-learn 做 t-SNE/PCA 降维 + KMeans 聚类 + silhouette 评估, 用 torch 实现 Autoencoder 压缩 (384→64), 并用 DSR 六步框架把工程实践定义为研究问题。交付物: 可运行 notebook + 300 字结构分析 + progressive_project milestone。

## diagnostic (pset0 式, 3 道, CS229 风格诊断性先测, 不计分)
开课先测, 仅诊断先备知识, 不影响及格:
- D0.1 [线性代数]: 给定 `x=[1,2,3]`, `w=[0.5,-1,0]`, 计算 `wᵀx`, 并解释"投影"的几何含义 (提示: 点积 = 投影长度 × 模)。
- D0.2 [概率/KL]: 写出 KL(q‖p) 公式 `Σ q log(q/p)`, 解释为什么 VAE 用 KL 正则 (提示: 让后验接近先验, 防止过拟合)。
- D0.3 [Python/sklearn]: 用 `sklearn.manifold.TSNE` 对随机 100×50 矩阵降维到 2 维, 写出 3 行核心代码 (提示: `TSNE(n_components=2).fit_transform(X)`)。

## subskills
- S1: 文本表示工程 -- 用 sentence-transformers 把营销文本编码为 embedding, 理解余弦相似度反映语义距离 (对应 TODO1)
- S2: 降维与聚类 -- 用 scikit-learn 做 t-SNE/PCA 可视化 + KMeans 聚类 + silhouette 选 K, 理解 Neural Collapse 对聚类的启示 (对应 TODO2/TODO4)
- S3: 自编码器与表示评估 -- 用 torch 实现 Autoencoder 压缩 + 下游分类评估表示质量, 理解 CMU 10741 概念一"无约束=记忆非学习" (对应 TODO3/TODO6)

## drills (>=3, 每含 drill_id / difficulty 1-5 / reps_required / feedback_rule / worked_faded 三阶段)

drill_id: D1
difficulty: 2
reps_required: 3
feedback_rule: 若学生误用 `model.encode` 单条而非 list, 反馈"batch 输入才是 sentence-transformers 的正确姿势, 单条 encode 会丢失 batch norm 语义"; 若 embedding 维度答错, 引导查 `model.get_sentence_embedding_dimension()`; 若余弦相似度方向反了 (越小越相似), 反馈"cos(θ) 越大越相似, 不是越小, 余弦相似度 = 1 - 余弦距离"; 若混淆 L2 与 cosine, 反馈"sklearn.metrics.pairwise.cosine_similarity 用内积归一化, 不是欧氏距离"。
worked_faded:
  - 阶段1 (Worked 完整示范): 给出 5 条评论的完整代码 `model = SentenceTransformer('all-MiniLM-L6-v2'); emb = model.encode(comments); print(emb.shape)` + 维度输出 `(5, 384)` + 余弦相似度矩阵 `cosine_similarity(emb)`
  - 阶段2 (Faded 部分填空): 给出模型加载 `model = SentenceTransformer('all-MiniLM-L6-v2')`, 留空 `emb = model._____(comments)` 和 `dim = model._____()`, 留空相似度 `cosine_similarity(_____)`
  - 阶段3 (Independent 独立解): 学生独立完成 20 条评论编码 + 维度验证 + 余弦相似度 Top-3 配对, 并解释为什么护肤正面评论彼此相似度高

drill_id: D2
difficulty: 3
reps_required: 3
feedback_rule: 若 t-SNE 没设 `random_state` 导致不可复现, 反馈"DSR 第 5 步评估要求可复现, 必须固定 random_state=42, 否则论文不可复现"; 若 KMeans 没设 `n_init='auto'`, 反馈"sklearn 1.4+ 默认 n_init 变了, 显式设置避免 warning"; 若 silhouette 选 K 时只看最高不看业务可解释性, 引导回 Neural Collapse"特征几何结构应与业务标签对齐, K=3 可能比 K=5 更符合产品三类"; 若 PCA 没标准化, 反馈"PCA 对尺度敏感, embedding 已归一化但若用原始特征需 StandardScaler"。
worked_faded:
  - 阶段1 (Worked 完整示范): 完整 t-SNE 降维 `TSNE(n_components=2, random_state=42, perplexity=5).fit_transform(emb)` + KMeans `KMeans(n_clusters=3, n_init='auto', random_state=42).fit(emb)` + silhouette 评估 K=2..6 的代码 + 可视化散点图
  - 阶段2 (Faded 部分填空): 给出 t-SNE 部分, 留空 `KMeans(n_clusters=___, n_init=___, random_state=42).fit(___)` 和 `silhouette_score(___, labels=___)`, 留空可视化 `plt.scatter(tsne[:,0], tsneau[:,___], c=___)`
  - 阶段3 (Independent 独立解): 学生独立完成降维-聚类-评估-可视化全链路, 选出最优 K 并用业务语言解释 (为什么 K=3 对应护肤/电子/健身三类)

drill_id: D3
difficulty: 4
reps_required: 3
feedback_rule: 若 Autoencoder 没用 bottleneck 层 (维度 384->64), 反馈"瓶颈设计是表示学习的核心约束, 无约束的 encoder 会退化成 lookup table (CMU 10741 概念一: 不加约束的表示学习没有意义)"; 若重构损失不收敛, 引导查 `nn.MSELoss()` + 学习率 (建议 1e-3) + epoch 数 (至少 100); 若评估只看重构损失不看下游任务, 反馈"DSR 第 5 步要求多指标评估 (Recall@K / Silhouette / 下游分类准确率), 单一指标会过拟合"; 若没设 `torch.manual_seed`, 反馈"不可辨识性 (CMU 概念三) 要求固定种子, 否则数值不可复现"。
worked_faded:
  - 阶段1 (Worked 完整示范): 完整 torch Autoencoder `class AE(nn.Module): def __init__(self): self.enc = nn.Sequential(nn.Linear(384,128), nn.ReLU(), nn.Linear(128,64)); self.dec = nn.Sequential(nn.Linear(64,128), nn.ReLU(), nn.Linear(128,384))` + 训练循环 (100 epoch, Adam 1e-3, MSELoss) + 重构损失曲线
  - 阶段2 (Faded 部分填空): 给出 encoder 结构 `self.enc = nn.Sequential(nn.Linear(384,128), nn.ReLU(), nn.Linear(128,64))`, 留空 `self.dec = nn.Sequential(nn.Linear(___,___), nn.ReLU(), nn.Linear(___,___))` 和 `loss = criterion(recon, ___)` 以及 `optimizer = optim._____(ae.parameters(), lr=___)`
  - 阶段3 (Independent 独立解): 学生独立实现 Autoencoder + 训练 + 评估压缩后 embedding (64 维) 对下游情感分类 (LogisticRegression) 的影响, 对比原始 384 维 baseline, 写 300 字分析

## progressive_project (CS230 风格渐进脚手架: proposal → milestone → final → poster)
- **proposal** (Day 1 当天提交): 选定一个企业场景 (客户分群 / 产品推荐 / 内容审核), 用 DSR 第 1-2 步定义问题与目标 (500 字, IMRaD 的 Intro 结构)
- **milestone** (Day 2 前): 用 sentence-transformers + sklearn 跑出 baseline embedding + 初步聚类, 提交中期报告 (1000 字 + t-SNE 可视化 + silhouette 表)
- **final** (Day 3 前): 完整 Autoencoder + 下游任务评估 + 与 baseline 对比, 提交最终报告 (IMRaD 结构, 2000 字, 含 Recall@K / Silhouette / 分类准确率三指标)
- **poster** (Skill 1 末): 5 分钟海报展示 + 2 分钟 Q&A, 同伴互评 (用 rubric 评估: 技术深度 30% / 业务洞察 30% / 可复现性 20% / 表达 20%)

## interleaving (A1B1C1...B2C2A2...C3A3B3 交叉排布, 不块状)
不块状练习, 改用交叉排布 (MIT 6.5940 间隔与交叉练习原则):
- 第 1 轮: A1(D1 文本编码) → B1(D2 降维聚类) → C1(D3 Autoencoder)
- 第 2 轮: B2(D2 变体: 换 UMAP 降维) → C2(D3 变体: 加 KL 正则成 VAE) → A2(D1 变体: 多语言评论, 用 paraphrase-multilingual-MiniLM-L12-v2)
- 第 3 轮: C3(D3 变体: 加对比学习损失 InfoNCE) → A3(D1 变体: 长文本截断策略, max_seq_length=256 vs 512) → B3(D2 变体: 不同 K 的 silhouette 曲线 + elbow method 对比)

每轮间隔 1-2 天 (由 schedule.json FSRS-6 排程), 强制切换上下文, 避免块状练习的假性掌握。交叉顺序 A1B1C1...B2C2A2...C3A3B3 明文, 不随机。

## retry_policy (CS230 风格)
- 10 late days (整个 Skill 1 共享, 用完为止), 用 1 天扣 1 天
- 失败不罚: drill 未达标可重做, 取最高分, 不累加罚分
- 4/5 实验提交即及格 (MIT 6.5940 mastery 阈值: "至少 4/5 实验提交方可及格")
- progressive_project 各阶段可重交一次, 取最高分

## weak_loop (连续 2 次失败触发弱项循环)
连续 2 次失败 (drill 评分 < 60%) 触发弱项循环:
1. **回退**: 回退到上一 drill (D3 失败回 D2, D2 失败回 D1, D1 失败回 diagnostic)
2. **补充 Worked Example**: 重看上一 drill 的阶段 1 完整示范, 不进 Faded
3. **缩小任务粒度**: D3 失败, 改为先只实现 encoder (384→64), 不训 decoder; D2 失败, 改为先只做 PCA 不做 t-SNE
4. **重进**: 通过弱项 drill 后, 重新进入原 drill 的 Faded 阶段 (阶段 2)
5. **升级**: 若仍失败, 触发 tutorial.ipynb Socratic 追问 (限频 1 次/天), 由 Oxford tutorial fellow 引导定位盲点
6. **记录**: 盲点写入 student_model.json 的 `blind_spots`, 跨单元复用, 避免重复触发

---

*v6.0 学习科学层 · 刻意练习文件 · 基于 Ericsson + MIT 6.5940 + CS229 + CS230 · 2026-07-25*
