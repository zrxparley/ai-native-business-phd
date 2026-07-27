# Constructive Alignment · Day 3 企业知识图谱 + GraphRAG (v6.0)

> **理论依据**：Biggs (1996) 建构对齐 Constructive Alignment--ILO（Intended Learning Outcomes 预期学习产出）↔ TLA（Teaching/Learning Activities 教学学习活动）↔ AT（Assessment Tasks 评估任务）三者必须对齐，否则学生可通过不经 TLA 的捷径通过 AT，对齐即失败。
> **mastery_threshold** 借鉴 MIT 6.5940 "至少 4/5 实验提交方可及格" 与 CS229 pset0 mastery 门槛设计。

---

## ILO ↔ TLA ↔ AT 矩阵

| ILO（预期学习产出） | TLA（教学学习活动） | AT（评估任务） | mastery_threshold |
|---|---|---|---|
| **ILO1**：能用 `networkx` 构建营销知识图谱（≥4 类实体/≥3 类关系），执行图查询（最短路径/邻居/中心性/社区发现） | ① 阅读 notes.md "关键回顾 1" + 营销映射表 ② 完成 starter.ipynb TODO1（Faded）③ tutorial.ipynb Socratic 第 1-2 轮追问本体设计 ④ drill D1 三阶段 Worked-Faded-Independent | ① starter.ipynb TODO1 提交可运行的 KG（≥20 节点 ≥30 边）② practice.md D1 Independent 产物 `kg_build.json` ③ tutorial.ipynb 口头辩护"为何选这 7 类实体而非 5 类" | 节点≥20、边≥30、查询 API 全部正确、`successors` 非 `neighbors`；≥80% 通过 |
| **ILO2**：能用 `numpy` 从零实现 TransE KGE（嵌入初始化/负采样/margin-based ranking loss/梯度更新），解释 h+r≈t 几何意义与一对多局限 | ① 阅读 notes.md "关键回顾 2" + TransE/RotatE/ComplEx 对比表 ② 完成 starter.ipynb TODO2（Faded）③ drill D2 三阶段 ④ schedule.json C1/C3 间隔复习 ⑤ tutorial.ipynb Socratic 第 3 轮"为何 TransE 无法建模对称关系" | ① starter.ipynb TODO2 提交可训练的 TransE（loss 收敛曲线）② practice.md D2 Independent 把 TransE 改造为 RotatE + Hit@10 对比 ③ 手算 1 轮 TransE 梯度更新（weak_loop 微题） | loss 收敛、负采样等概率替换 head/tail、能解释一对多局限；≥70% 通过 |
| **ILO3**：能实现 GraphRAG 多跳检索与 TF-IDF 传统 RAG 基线的对比实验，给出召回率数字与原因分析 | ① 阅读 notes.md "关键回顾 3" + 2026 前沿 GraphRAG 段 ② 完成 starter.ipynb TODO4-6（Faded）③ drill D3 三阶段 ④ schedule.json C2/C5 间隔复习 ⑤ tutorial.ipynb Socratic 第 4-5 轮"为何 TF-IDF 无法回答共同弱点问题" | ① starter.ipynb TODO4-6 提交对比表（≥2 多跳问题，召回率数字）② practice.md D3 Independent 产物 `graphrag_vs_tfidf.md`（5 多跳问题 + 300 字原因 + 1 反例） | GraphRAG 召回率严格优于 TF-IDF、能落原因到"关系链 vs 语义相似度"、能提 GraphRAG 构建成本；能独立解 |
| **ILO4**（迁移）：能判断何时用 GraphRAG vs 传统 RAG vs KGE，并说明业务场景的因果阶梯层级 | ① notes.md "怎么用"段 ② tutorial.ipynb Hattie [FEED-FORWARD] 推荐复习单元 ③ practice.md interleaving C3 阶段反思 | ① 300 字分析"GraphRAG 在哪个营销场景下显著优于传统 RAG？为什么？"（见 notes.md 作业） | 能区分 L1 关联/L2 A-B 验证、能提 GraphRAG 构建成本与适用边界；通过即可 |

---

## mastery_threshold（掌握阈值）

本单元整体 mastery 判定（任一未达即未收敛）：

- **D1**：节点≥20、边≥30、3 类图查询 API 全部正确（`successors`/`shortest_path`/`betweenness_centrality`/`louvain_communities`）-> ≥80%
- **D2**：TransE loss 收敛（末轮 loss < γ）、负采样正确、能口述 h+r≈t 几何意义 -> ≥70%
- **D3**：GraphRAG 召回率严格 > TF-IDF、5 个多跳问题、1 个反例、300 字原因分析 -> 能独立解
- **整体**：4 个 ILO 全部达到 mastery_threshold + schedule.json 5 卡 21 天内不漏复习 = 本单元 v6.0 收敛

未达 mastery 触发 practice.md 的 weak_loop；连续 2 次未达触发 tutorial.ipynb 限频内的 Socratic 追问。

---

## 3 自检问题（Biggs 三问 · Feed Up / Feed Back / Feed Forward）

> Hattie (2007, RER 77(1):81-112) formative feedback 三问，对应三个对齐自检：

1. **Feed Up（TLA 是否训练 ILO？）**：本单元的 starter.ipynb TODO1-6 + drill D1-D3 + tutorial.ipynb Socratic 是否真的训练了 ILO1-3？
   - 自检：随机抽 1 个 TODO，问"这训练的是哪个 ILO？"若答不出 -> 对齐失败 -> 重排 TLA
   - 本单元答案：TODO1/D1→ILO1，TODO2/D2→ILO2，TODO4-6/D3→ILO3

2. **Feed Back（AT 是否测量 ILO？）**：practice.md 的 `kg_build.json`/`transe_training.log`/`graphrag_vs_tfidf.md` 是否真的测量了 ILO1-3？
   - 自检：把 AT 给一个未学本单元的同行做，若他能凭常识通过 -> AT 测的不是 ILO -> 加严
   - 本单元答案：`kg_build.json` 测 ILO1（看节点/边数+API）、`transe_training.log` 测 ILO2（看 loss 曲线）、`graphrag_vs_tfidf.md` 测 ILO3（看召回率+反例）

3. **Feed Forward（不经 TLA 能过 AT 吗？）**：学生若不读 notes.md、不做 starter.ipynb、不跑 drill，能否直接交 AT？
   - 自检：自己尝试不看任何 TLA 直接做 `graphrag_vs_tfidf.md`--若能凑出 300 字 -> AT 太松 -> 加盲点要求（如必须给 TransE 手算、必须给 GraphRAG 失效反例）
   - 本单元设计：D3 Independent 要求 1 个 GraphRAG 失效反例（如简单事实问答 GraphRAG 不如 TF-IDF），不经 TLA 难以构造

> **若 3 自检任一失败** -> 该 ILO 的 TLA/AT 需修订，回到 practice.md 调整 drill 或 feedback_rule。

---

## 与 v5.0 基线的对齐保证

- v5.0 的 notes.md 学习目标 1-5 = v6.0 的 ILO1-4（合并 v5.0 目标 4-5 为 ILO3，新增 ILO4 迁移）
- v5.0 的 starter.ipynb TODO1-6 不变，v6.0 仅在 TODO 之上加 drill/feedback/mastery
- v5.0 的 solution.ipynb 作为 Worked 阶段示范，v6.0 不修改

---

*本对齐表依据 Biggs (1996) Constructive Alignment + Hattie (2007) formative feedback + MIT 6.5940 mastery 阈值设计。*
