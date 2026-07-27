# practice.md - 刻意练习 (Ericsson + MIT 4C/ID)

> v6.0 学习科学层 · 配合 notes.md / starter.ipynb / tutorial.ipynb / schedule.json / alignment.md
> 哲学：**科学即高效 · 反馈即成长** - 把"练习"升级为"刻意练习+间隔重复+建构对齐+牛津tutorial仿真"

---

## skill_target

**可观察的核心技能**：给定一个 AI 平台生态情境（如 Hugging Face / MCP 生态 / 企业营销平台），能用 **networkx** 构建多边生态网络（26节点40边级别），用 **pandas** 量化多归属率/锁定度/网络效应强度，用 **numpy 蒙特卡洛+贝叶斯先验** 推演平台 tipping point（临界点），并给出 2-3 条差异化战略路径 + 已知盲点标注。

---

## diagnostic（前测，3 道，<10 分钟）

> 检测起点。任一道答错 → 进入对应 subskill 的弱项循环。这是 ScholAstic/NUS 自定步调风格的前测。

1. **D-diag-1（网络效应识别）**：以下哪个不是数据网络效应的典型环节？(A) 用户使用产生数据 (B) 数据改善模型 (C) 模型吸引更多使用 (D) 用户数量驱动 Metcalfe 定律 n² 增长
   - **正解**：D（这是传统网络效应，不是 AI 平台特有的"数据网络效应"飞轮）
2. **D-diag-2（networkx 基础）**：用 networkx 计算 `G` 的度分布与聚类系数，写出至少 2 行 API 调用。
   - **正解要点**：`nx.degree_histogram(G)` / `nx.cluster.average_clustering(G)` 或 `nx.clustering(G)`
3. **D-diag-3（tipping 概念）**：解释"平台 tipping point"为何是概率分布而非宿命点，并指出 2 个影响 tipping 的关键变量。
   - **正解要点**：tipping 是天道推演概率树上的条件概率跃迁，受网络效应强度、多归属率、数据飞轮速度等变量共同决定；非宿命而是概率分布。

---

## subskills（3 项，对应 ILO1/ILO2/ILO3 见 alignment.md）

- **S1 - 生态建模**：用 networkx 构建多边平台生态网络（节点类型：平台/开发者/消费者/互补者；边类型：PUBLISHES_ON/USES/INTEGRATES_WITH/DEPENDS_ON），并执行度分布/聚类系数/核心-边缘分析。
- **S2 - 战略量化**：用 pandas 量化多归属率、锁定度、网络效应强度、赢者通吃（WTA）倾向，按参与者类型分组。
- **S3 - 天道推演**：用 numpy 蒙特卡洛模拟 + 贝叶斯先验，推演平台 tipping point，输出 2-3 条时间线 + 风险预警 + 认知盲点。

---

## drills（3 个，每个含 drill_id/difficulty/reps_required/feedback_rule/worked_faded）

### drill_id: D1
- **subskill**：S1 - 生态建模
- **difficulty**: 3 (1-5)
- **reps_required**: 3
- **feedback_rule**:
  - 若 networkx 图构建缺节点类型属性 → 提示"重新检查 `add_node(type=...)`，参考 notes.md §上机任务 TODO1 真实平台生态结构"
  - 若未做核心-边缘分析 → 提示"用 `nx.algorithms.core.wrap_core_sequence` 或 `nx.k_core(G)`，思考：谁是生态核心？谁是边缘？这与 MCP/A2A 生态的'开放协议核心'有何不同？"
  - 若可视化混乱 → 提示"matplotlib 双面板：左完整网络，右核心-边缘着色，参考 solution.ipynb TODO4"
- **worked_faded**（Worked → Faded → Independent 三阶段）:
  1. **Worked（完整示范）**：教师演示构建一个 4 平台 + 12 开发者 + 5 消费者 + 5 互补者（共 26 节点 40 边）的完整生态网络，含 `add_node(type=...)` / `add_edge(u, v, relation=...)` / 度分布 / 核-边分析全流程
  2. **Faded（部分填空）**：starter.ipynb TODO1/TODO2 给出图结构与 80% 代码，学生填节点类型枚举 + 边类型枚举 + 2 行核心-边缘调用
  3. **Independent（独立解）**：学生独立构建一个新生态（如 MCP 工具生态：1 MCP host + 3 MCP server + 8 工具开发者 + 5 Agent 构建者 + 4 数据源 = 21 节点），完成度分布+核-边分析

### drill_id: D2
- **subskill**：S2 - 战略量化
- **difficulty**: 4 (1-5)
- **reps_required**: 3
- **feedback_rule**:
  - 若多归属率计算错误（分母取错） → 提示"多归属率 = 该类型中多平台参与者数 / 该类型总参与者数；不是总参与者数。检查 pandas groupby 分母"
  - 若 WTA 倾向只给 0/1 二元判断 → 提示"WTA 倾向是连续概率而非二元标签，参考 notes.md §关键回顾 1 的'数据网络效应阈值效应'"
  - 若锁定度未结合数据飞轮 → 提示"锁定度不止转换成本，还要乘数据网络效应强度——AI 平台的锁定度来自数据不可速成"
- **worked_faded**:
  1. **Worked**：完整演示按参与者类型分组的多归属率/锁定度计算（含 pandas groupby + 聚合 + 可视化），覆盖广告主/创作者/数据方/工具开发者 4 类
  2. **Faded**：starter.ipynb TODO3 给出 groupby 框架，学生填 4 类参与者的多归属率公式 + 锁定度加权
  3. **Independent**：学生独立计算 MCP 生态的多归属率（Agent 构建者同时使用多个 MCP server 的比例）+ 锁定度（迁移到 A2A 协议的成本）

### drill_id: D3
- **subskill**：S3 - 天道推演
- **difficulty**: 5 (1-5)
- **reps_required**: 3
- **feedback_rule**:
  - 若蒙特卡洛未用贝叶斯先验 → 提示"天道推演 = 主观贝叶斯先验 + 蒙特卡洛更新，不是纯频率主义模拟。参考 notes.md §关键回顾 'L1 关联分析 ≠ L2 因果验证'"
  - 若 tipping point 给单一阈值 → 提示"tipping 是概率分布而非单点，需输出 P(tipping | 条件) 的分布，至少 1000 次蒙特卡洛采样"
  - 若未标注盲点 → 提示"天道推演必含'认知盲点'字段，至少列出 2 个未知变量（如监管政策/黑天鹅技术跃迁）"
  - 若未交叉验证 → 提示"对照 networkx 核心-边缘结构与 tipping 概率：核心节点是否在 tipping 后仍稳？边缘节点是否被吞并？"
- **worked_faded**:
  1. **Worked**：完整演示 numpy 蒙特卡洛（1000 次采样 × 3 时间线 × 2-3 战略路径）+ 贝叶斯先验设置 + tipping 概率分布输出 + 盲点标注
  2. **Faded**：starter.ipynb TODO6 给出蒙特卡洛骨架，学生填贝叶斯先验 + 网络效应强度参数 + tipping 判定条件 + 盲点列表
  3. **Independent**：学生独立推演 Hugging Face vs 新进入者的 tipping 概率，输出 2-3 条时间线 + 风险预警 + 认知盲点

---

## progressive_project（渐进交付，MIT Sloan 行动学习 + CS230 脚手架）

仿 CS230 翻转课堂四组件 + 渐进项目脚手架（proposal → milestone → final → poster），本单元项目分 4 阶段：

- **P1 - Proposal（Day4 当天）**：选定一个真实 AI 平台生态（Hugging Face / LangChain / MCP / A2A / 自选），提交 1 页 proposal：节点/边定义 + 数据来源 + 推演问题
- **P2 - Milestone（Day4 + 3 天）**：提交 networkx 生态网络 + 核-边分析 + 多归属率/锁定度量化（对应 D1+D2）
- **P3 - Final（Day4 + 7 天）**：提交天道推演蒙特卡洛结果 + 2-3 时间线 + 风险预警 + 盲点（对应 D3）
- **P4 - Poster（Day4 + 10 天）**：1 页 A3 海报：生态拓扑图 + tipping 概率分布 + 战略建议 + 盲点，给同伴 5 分钟讲

> retry 政策参考 CS229：每阶段 1 次重交机会，重交不扣分（鼓励迭代）。逾期每天 -20%（仿 CS230）。

---

## interleaving（A1B1C1 交叉，不块状）

> MIT Open Learning 明文原则：A1B1C1...B2C2A2...C3A3B3 模式，避免块状练习导致"近因混淆"。

本单元练习交叉排布如下（A=S1 生态建模, B=S2 战略量化, C=S3 天道推演）：

| 序号 | drill | subskill | 备注 |
|---|---|---|---|
| 1 | A1 | S1 | D1 worked 阶段 |
| 2 | B1 | S2 | D2 worked 阶段 |
| 3 | C1 | S3 | D3 worked 阶段 |
| 4 | A2 | S1 | D1 faded 阶段 |
| 5 | B2 | S2 | D2 faded 阶段 |
| 6 | C2 | S3 | D3 faded 阶段 |
| 7 | A3 | S1 | D1 independent 阶段 |
| 8 | B3 | S2 | D2 independent 阶段 |
| 9 | C3 | S3 | D3 independent 阶段 |

> 不允许 A1A2A3 块状刷完再做 B——交叉才能训练"识别何时用哪个子技能"的元认知。

---

## retry_policy（CS230 + CS229 风格）

- 每个 drill 独立评分，<70% 触发 retry
- retry 不限次数，但每次 retry 后必须等待 30 分钟（防短期记忆作弊，配合 schedule.json 间隔重复）
- 单元总 retry 上限：每个 drill 3 次，超出转人工辅导
- 项目 P1-P4 各 1 次免费重交，不扣分

---

## weak_loop（弱项循环，连续 2 次失败触发）

> 连续 2 次同一 drill 失败（<70%）→ 自动触发弱项循环：

1. **回退**：当前 drill 退回上一阶段（independent → faded → worked），若已在 worked 阶段则退回 diagnostic 重测
2. **补充 worked example**：从 solution.ipynb 提取对应 TODO 的完整解，学生口述每行代码的"为什么"（费曼）
3. **限频补练**：在 schedule.json 中插入额外 2 张复习卡（间隔 1 天/3 天），针对失败子技能
4. **tutorial 续约**：自动预约一次牛津 tutorial（限频规则下，额外+1 次/天，标记为 "weak_loop remediation"）
5. **exit 条件**：连续 2 次同 drill 通过 ≥85% 才退出弱项循环

> 弱项循环记录到 student_model.json 的 `weak_history` 字段，跨单元复用，避免同类错误重复。

---

*本文件配合 schedule.json（间隔重复）、alignment.md（建构对齐）、tutorial.ipynb（牛津 Socratic）使用。*
*最后更新：2026-07-25*
