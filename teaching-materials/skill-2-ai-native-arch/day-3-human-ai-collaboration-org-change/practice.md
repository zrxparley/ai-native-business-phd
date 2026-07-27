# 刻意练习 (Ericsson + MIT 4C/ID) · Day 3 人机协作治理 + 组织变革

> v6.0 学习科学层：把 v5.0 的 "练习即掌握" 升级为 **刻意练习 + 间隔重复 + 交叉 + Worked-Faded**。
> 研究依据：Ericsson deliberate practice 5 要素 / MIT 6.5940 mastery 阈值 / Butler 2010 retrieval practice / Worked Example Effect (Sweller, Renkl)。

---

## skill_target

**能独立完成**：给定一份人机协作审计日志（CSV）+ 一份组织角色清单，用 **pandas** 计算人工干预率/Agent自主完成率/人工修正率，用 **networkx** 构建组织协作网络并识别桥接节点，用 **McKinsey 7S** 评估组织就绪度，用 **ADKAR** 诊断阻力阶段，并用**天道推演**对阻力扩散路径做 3 层沙盘推演，输出 1 个高杠杆干预点 + 2-3 条时间线 + 风险预警。

---

## subskills

- **S1 · pandas 审计日志多维聚合**：`groupby` 按分工模式 × 任务类型切片，计算人工干预率/Agent自主完成率/人工修正率，定位"AI成熟度被高估"的任务（干预率 >30%）
- **S2 · networkx 组织网络拓扑分析**：构建节点（人/Agent 角色）+ 边（协作关系），计算 `degree_centrality` 找关键枢纽、`betweenness_centrality` 找桥接节点（信息瓶颈），识别"去掉哪个节点网络会碎片化"
- **S3 · 综合治理推演**：McKinsey 7S 七维评分 + ADKAR 五阶段阻力诊断 + 天道推演 3 层沙盘（immediate → near → far），输出高杠杆干预点 + 概率分布 + 黑天鹅预警

---

## drills

### drill_id: D1
- **difficulty**: 2
- **reps_required**: 3
- **feedback_rule**: 失败时回放审计日志样本前 5 行 + 给出 `df.groupby('分工模式')['人工干预'].mean()` 骨架，要求学生解释每行代码的"因果含义"而非补全语法；若学生把干预率算成 `sum` 而非 `mean`，触发 [TASK] 级反馈："干预率是比例 (mean of 0/1) 不是计数 (sum)，重读 notes.md 关键回顾 1"
- **worked_faded**:
  - **Worked（完整示范）**：给出完整 `df.groupby('分工模式').agg(干预率=('人工干预','mean'), 完成率=('Agent自主完成','mean'))` + 输出表 + 文字解读
  - **Faded（部分填空）**：留 `df._____('分工模式')._____(干预率=('人工干预','____'))` 三处空
  - **Independent（独立解）**：只给原始 CSV，要求输出"哪类任务 AI 成熟度被高估"的一句话结论 + 数据支撑

### drill_id: D2
- **difficulty**: 3
- **reps_required**: 3
- **feedback_rule**: 失败时让学生先画"组织协作草图"（人/Agent 节点 + 协作边）再写代码；若 `degree_centrality` 与 `betweenness_centrality` 结果混淆，触发 [PROCESS] 级反馈："degree = 谁连接最多（枢纽），betweenness = 谁在最多最短路径上（桥接/瓶颈），重读 notes.md TODO3"；若学生把 Agent 节点当"工具节点"忽略，触发 [FEED-FORWARD]："Agentic Organization 下 Agent 是 first-class member，必须参与网络中心性计算"
- **worked_faded**:
  - **Worked**：完整 `nx.Graph()` + `add_nodes_from` + `add_edges_from` + `nx.degree_centrality(G)` + `nx.betweenness_centrality(G)` + 雷达图
  - **Faded**：留 `G = nx._____()` / `nx.______(G)` / `sorted(____.items(), key=lambda x:-x[1])[0]` 三处空
  - **Independent**：给角色清单 + 协作矩阵，要求输出"哪个节点是信息瓶颈" + 移除该节点后网络连通性变化

### drill_id: D3
- **difficulty**: 5
- **reps_required**: 4
- **feedback_rule**: 失败时降级到 D2 + 补充 worked example（单一角色阻力扩散）；若学生只给单条时间线，触发 [SELF-REG] 级反馈："天道推演要求并行 >=3 条时间线 + 概率分布，不是单点预测，重读 notes.md 关键回顾 3"；若未识别高杠杆点，触发 [FEED-FORWARD]："高杠杆点 = 小投入改变大局，如 '中层管理者的 Desire 阶段阻力' 往往是 ADKAR 全链路的瓶颈"
- **worked_faded**:
  - **Worked**：完整 7S 评分表 + ADKAR 阻力热力图 + 天道推演 3 层沙盘（A 干预 → 立即/近期/远期 各 2-3 个分支 + 概率 + 风险）
  - **Faded**：留 7S 三维空 + ADKAR 两阶段空 + 天道推演 "远期" 层空（要求学生补）
  - **Independent**：给真实组织场景（如"营销团队导入投放优化 Agent"），要求独立输出 7S + ADKAR + 天道推演 3 层沙盘 + 1 个高杠杆点

---

## progressive_project (脚手架渐进交付 · MIT CS230 模式)

模仿 CS230 proposal → milestone → final → poster 的渐进脚手架，本单元项目分 4 阶段：

1. **Proposal（D1 后）**：提交审计日志分析计划 + 假设（哪类任务 AI 成熟度被高估）+ 数据来源
2. **Milestone（D2 后）**：提交 pandas 分析结果 + networkx 网络图 + 初步发现
3. **Final（D3 后）**：提交完整 7S + ADKAR + 天道推演 3 层沙盘 + 高杠杆干预点
4. **Poster（单元末）**：1 页 A3 海报，面向"AI 伦理委员会"汇报，3 分钟话术

每阶段未达 mastery_threshold（>=70%）需 retry，最多 2 次。

---

## interleaving (A1B1C1 交叉排布 · MIT 6.5940)

> 不块状练习。按 A1B1C1...B2C2A2...C3A3B3 模式交叉，防止"块状效应"（block practice) 的假性掌握。

- **A = pandas 审计日志聚合**（D1 子技能 S1）
- **B = networkx 网络拓扑**（D2 子技能 S2）
- **C = 综合治理推演**（D3 子技能 S3）

交叉排布示例（一次训练 session 9 题）：
```
A1 → B1 → C1 → B2 → C2 → A2 → C3 → A3 → B3
```
- A1/B1/C1：D1/D2/D3 的 Worked 阶段（看示范）
- B2/C2/A2：D2/D3/D1 的 Faded 阶段（部分填空）
- C3/A3/B3：D3/D1/D2 的 Independent 阶段（独立解）

**禁止** A1→A2→A3 块状做完再做 B。块状练习短期正确率高但 1 周后遗忘率 >60%（Butler 2010 retrieval practice 证据）。

---

## retry_policy (CS229 pset0 + CS230 late days 模式)

- 每个 drill 首次提交未达 mastery_threshold（D1/D2: >=70%, D3: >=60%）可 retry
- **最多 2 次 retry**，每次 retry 间隔 >= 4 小时（防短期记忆假性掌握）
- Retry 时 feedback_rule 自动降级一档（Independent → Faded → Worked），第三次直接看 Worked 重做
- Late submission：参考 CS230，每 late day 扣 20%，最多 10 late days

---

## weak_loop (弱项循环 · 连续 2 次失败触发)

**触发条件**：同一 drill 连续 2 次未达 mastery_threshold。

**回退路径**：
1. 回退到上一 difficulty 的 drill（D3 → D2, D2 → D1, D1 → 补充 Worked Example）
2. 补充一个 worked example（完整示范 + 文字解读），学生必须口头复述每一步因果链
3. 24 小时后再 retry（间隔重复，防短期记忆）
4. 若仍失败，触发 **student_model.json** 的 `weak_concepts` 字段更新，跨单元复习时优先召回

**退出条件**：独立解阶段 1 次通过 + 24 小时后交叉练习中 1 次通过（双重验证）。

---

## v6.0 升级说明

本 practice.md 把 v5.0 的 6 个 TODO 升级为 3 个 drill × 3 阶段（Worked/Faded/Independent）= 9 个练习点，并加入交叉排布、retry、弱项循环。**v5.0 的 starter.ipynb 6 TODO 保留不变**，practice.md 是其上的学习科学层映射。
