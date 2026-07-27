# 刻意练习册 · Day 3：企业知识图谱 + GraphRAG (v6.0)

> **学习科学依据**：Ericsson 刻意练习 5 要素（specific goal / feedback / repetition / difficulty / motivation）+ MIT 6.5940 Worked-Faded 示例 + ScholAstic/A1B1C1 交叉排布
> **配套**：notes.md / starter.ipynb / solution.ipynb / tutorial.ipynb / schedule.json / alignment.md

---

## skill_target（可观察的核心技能）

**能独立用 `networkx` 构建企业营销知识图谱（≥4 类实体/≥3 类关系），用 `numpy` 从零实现 TransE KGE（margin-based ranking loss + 负采样），并实现 GraphRAG 多跳检索与 TF-IDF 传统 RAG 基线的对比实验，给出多跳问答召回率/准确率数字与原因分析。**

判断标准：在不查看 solution.ipynb 的前提下，60 分钟内完成 6 个 TODO，TransE 训练 loss 收敛，GraphRAG 在 ≥2 个多跳问题上召回率优于 TF-IDF 基线。

---

## diagnostic（诊断性前测，3 道 · 不计分）

> 出自 Harvard CS229 pset0 先测理念。诊断仅用于发现盲点，决定从哪一档 drill 起步。

- **D0-1**：给定一段营销文本（"跑鞋 -> 属于 -> 运动装备 -> 互补 -> 运动护具"），用中文写出至少 3 条 you would 抽取的三元组（h, r, t），并标注哪些是一对一、哪些是一对多关系。
- **D0-2**：写出 TransE 的得分函数 f(h, r, t) 与 margin loss L；说明为何 TransE 无法建模对称关系（如"相似"）。
- **D0-3**：用一句话回答："传统向量 RAG 为何无法回答'竞品 A 和 B 的共同弱点是什么'？"——若你只能答出"语义相似度不够"，则需先补 Day 1-2 表示工程。

诊断结果映射：3 题全对 → D1 起步；2 题对 → D1 起步但加做 D0 复习；≤1 题对 → 先读 notes.md "关键回顾 1-3" 再来。

---

## subskills（3 项 · 对应 ILO1/ILO2/ILO3）

- **S1 图构建**：能用 `networkx.MultiDiGraph` 设计本体并构建产品-品牌-品类-客户-评论-活动-渠道七类实体、八类关系的营销知识图谱，并执行图查询（最短路径/邻居/中心性/社区发现）
- **S2 KGE 训练**：能用 `numpy` 从零实现 TransE（嵌入初始化 / 负采样 / margin-based ranking loss / 梯度更新），理解 h+r≈t 的几何意义与一对多局限性
- **S3 GraphRAG 对比**：能实现 GraphRAG 多跳检索（Local/Global/DRIFT 三模式任选其一）与 TF-IDF 传统 RAG 基线，在多跳问答上对比召回率并解释差异原因

---

## drills（3 个 · Worked-Faded 三阶段）

> 每个 drill 遵循 **Worked（完整示范）→ Faded（部分填空）→ Independent（独立解）** 三阶段，对应 starter.ipynb 的 TODO 渐退结构。

### drill_id: D1
- **覆盖子技能**：S1（图构建）
- **difficulty**: 2
- **reps_required**: 3
- **feedback_rule**：
  - 若图构建遗漏≥2 类实体或关系类型 → 反馈"你的本体缺失了 [评论/活动/渠道] 节点——回到 notes.md 营销映射表核对七类实体；问自己：客户买了产品后会留下什么？产品由谁制造？通过什么渠道分发？"
  - 若图查询 API 用错（如 `G.neighbors()` vs `G.successors()`）→ 反馈"`MultiDiGraph` 是有向的，请用 `successors/predecessors` 而非 `neighbors`；用 `nx.shortest_path(G, source, target)` 做最短路径，`nx.community.louvain_communities(G)` 或 Leiden 做社区发现"
  - 若未执行中心性分析 → 反馈"补上 `nx.betweenness_centrality(G)` 与 `nx.pagerank(G)`，回答'哪类产品是流量枢纽'"
- **worked_faded**：
  - **Worked（示范）**：solution.ipynb TODO1 给出完整的 7 节点 8 边构建 + 3 类查询，学生在 notes.md 阅读后跑通
  - **Faded（填空）**：starter.ipynb TODO1 给出图骨架但抽空 3 类边和 2 个查询，学生填空
  - **Independent（独立）**：学生用自己业务场景（如电商/在线教育）重新构建一个 ≥5 类实体的小型 KG

### drill_id: D2
- **覆盖子技能**：S2（KGE 训练）
- **difficulty**: 4
- **reps_required**: 3
- **feedback_rule**：
  - 若负采样错误（如仅随机替换 head）→ 反馈"TransE 负采样需等概率替换 head 或 tail；写 `neg_h, neg_t = random.choice([replace_h, replace_t])`；检查你的负样本是否让 margin loss 真的非零"
  - 若 margin loss 不收敛 → 反馈"检查学习率（建议 lr=0.01）、margin γ（建议 1.0）、嵌入维度（建议 50）；打印每轮 loss 曲线；若 loss 卡在 γ 说明正负样本得分未拉开"
  - 若 h+r≈t 几何意义解释不出 → 反馈"画一张二维图：h 在原点，r 是向量，t = h + r；负样本 t' 远离 h+r；margin loss 强制 ‖h+r-t‖ + γ < ‖h+r-t'‖"
  - 若未对比 RotatE/ComplEx → 反馈"补一段：用 `pip install pykeen` 的 RotatE 跑同一图，对比链接预测 Hit@10；解释为何 RotatE 能处理一对多"
- **worked_faded**：
  - **Worked**：solution.ipynb TODO2 给出完整 TransE 实现（init/neg_sample/loss/grad_step）
  - **Faded**：starter.ipynb TODO2 抽空负采样函数与 loss 计算，学生填空
  - **Independent**：学生把 TransE 改造为 RotatE（复数旋转），在同一图上对比 Hit@10

### drill_id: D3
- **覆盖子技能**：S3（GraphRAG 对比）
- **difficulty**: 5
- **reps_required**: 3
- **feedback_rule**：
  - 若 GraphRAG 多跳检索实现错误（如只做 1 跳邻居）→ 反馈"GraphRAG 的核心是'多跳'+ '社区摘要'；用 `nx.single_source_shortest_path(G, source, cutoff=3)` 做 3 跳检索；若用微软 GraphRAG，需先跑 Leiden 社区检测再生成社区摘要——回答 notes.md 中 3 种搜索模式的差异"
  - 若未做对比实验 → 反馈"必须给出 ≥2 个多跳问题（如'买跑鞋的客户还买什么'/'竞品 A 和 B 的共同弱点'）在 GraphRAG vs TF-IDF 上的召回率数字；TF-IDF 用 `sklearn.feature_extraction.text.TfidfVectorizer`"
  - 若未解释原因 → 反馈"原因要落到'向量相似度只能找语义近邻，无法沿关系链推理'；引用 notes.md 关键回顾 3 的对比表"
  - 若未提 GraphRAG 构建成本 → 反馈"补一句：GraphRAG 需 LLM 抽取实体关系（如 `langchain_experimental.LLMGraphTransformer`），构建成本远高于 TF-IDF；适合需要推理的复杂问题，简单事实问答传统 RAG 仍够用"
- **worked_faded**：
  - **Worked**：solution.ipynb TODO4-6 给出 TF-IDF 基线 + GraphRAG 多跳 + 对比表
  - **Faded**：starter.ipynb TODO4-6 抽空 GraphRAG 多跳检索与对比表生成
  - **Independent**：学生在自己业务 KG 上设计 5 个多跳问题，给出 GraphRAG vs TF-IDF 召回率对比与原因分析（300 字）

---

## progressive_project（渐进交付 · MIT CS230 风格）

> 模仿 CS230 proposal → milestone → final → poster 四阶段，本项目分 3 阶段交付，每阶段对应一个 drill：

- **Stage 1（D1 完成后）**：提交 `kg_build.json`——你的营销知识图谱的本体设计 + ≥20 节点 ≥30 边的实例（networkx 导出 JSON）
- **Stage 2（D2 完成后）**：提交 `transe_training.log`——TransE 训练 loss 曲线 + 3 个链接预测示例（"客户 A 可能购买产品 B"）
- **Stage 3（D3 完成后）**：提交 `graphrag_vs_tfidf.md`——5 个多跳问题的召回率对比表 + 300 字原因分析 + 1 个 GraphRAG 失效案例（反例）

每阶段延迟提交：扣 10%/天，最多 5 天（仿 CS230 late-day policy）。

---

## interleaving（A1B1C1...B2C2A2...C3A3B3 交叉排布）

> 不做"块状练习"（先做完所有 D1 再做 D2）——研究表明交叉练习（interleaving）提升长期保持 40%+（Butler 2010）。

**第 1 轮（A1B1C1）**：
- A1 = D1 Worked 阶段（跑通 solution TODO1，理解图构建）
- B1 = D2 Worked 阶段（跑通 solution TODO2，理解 TransE）
- C1 = D3 Worked 阶段（跑通 solution TODO4-6，理解对比实验）

**第 2 轮（B2C2A2）**：
- B2 = D2 Faded 阶段（填空 starter TODO2 负采样 + loss）
- C2 = D3 Faded 阶段（填空 starter TODO4-6 多跳检索 + 对比表）
- A2 = D1 Faded 阶段（填空 starter TODO1 边 + 查询）

**第 3 轮（C3A3B3）**：
- C3 = D3 Independent（自己业务 KG + 5 多跳问题）
- A3 = D1 Independent（自己场景重新构建 KG）
- B3 = D2 Independent（TransE → RotatE 改造 + Hit@10 对比）

每轮总时长约 40 分钟，三轮共 2 小时。轮间休息 5 分钟做 retrieval practice（合上电脑默写 TransE loss 公式 + GraphRAG 三搜索模式）。

---

## retry_policy（重试政策 · CS229 pset0 风格）

- 每个 drill 的 Faded 阶段可重试 ≤3 次；每次重试前必须先看一遍 Worked 示范
- Independent 阶段可重试无限次，但每次重试需写一段 50 字"上次为何失败"反思
- 诊断前测 D0 不计入重试次数
- 连续 2 次失败 → 触发 **weak_loop**（见下）

---

## weak_loop（弱项循环 · 连续 2 次失败触发）

当某 drill 在 Faded 或 Independent 阶段连续 2 次失败（未达 reps_required=3 中的任一次通过标准）：

1. **回退一级**：从 Faded 回退到 Worked 阶段重看一遍 solution 对应 TODO；从 Independent 回退到 Faded 重做
2. **补充 worked example**：阅读 notes.md "关键回顾 1-3" + reading.md 中 TransE / GraphRAG 条目
3. **微型补救**：完成 1 道针对盲点的微题
   - 若 D1 弱：画出"产品-品牌-品类-客户-评论-活动-渠道"七节点图，标注所有合理边
   - 若 D2 弱：手算 1 轮 TransE（给定 h=[0,0], r=[1,0], t=[1,0], γ=1, lr=0.1，负样本 t'=[2,0]，算 1 步梯度更新）
   - 若 D3 弱：写一段 100 字解释"为何 TF-IDF 无法回答'竞品 A 和 B 的共同弱点'，而 GraphRAG 可以"
4. **重新挑战**：回到原 drill 的 Faded/Independent 阶段重试

weak_loop 触发后该 drill 的 reps_required 重置为 1（即只需再通过 1 次即可放行），但总数仍需凑满 3 reps。

---

## 进度追踪表（学生自填）

| drill | Worked | Faded (try1/2/3) | Independent | weak_loop 触发? | 备注 |
|-------|--------|------------------|-------------|-----------------|------|
| D1 | ☐ | ☐/☐/☐ | ☐ | ☐ | |
| D2 | ☐ | ☐/☐/☐ | ☐ | ☐ | |
| D3 | ☐ | ☐/☐/☐ | ☐ | ☐ | |

全 9 格打勾 = 该单元 mastery 达成，可进入 Day 4。

---

*本练习册依据 Ericsson 刻意练习 + MIT 6.5940 Worked-Faded + Butler (2010) interleaving 设计。反馈规则全部引用 networkx/Neo4j/GraphRAG/TransE/KGE 真实库与算法。*
