# practice.md — Day 3 Agent生态治理 · 刻意练习 (v6.0)

> 基础理论: Ericsson deliberate practice + MIT CS229 pset0 + CS230 progressive project + Stanford interleaving/retrieval.
> 所有 drill 的 feedback_rule 均绑定本单元真实库 (pydantic / networkx / mesa / numpy-financial) 与真实生态案例 (MCP / A2A / Coze / Dify / OpenAI GPT Store / Hugging Face Spaces)。

---

## skill_target

**一句话可观察技能**: 给定一个 Agent 平台场景 (如 Coze 营销 Agent 平台或自建 MCP+A2A 生态), 能用 `pydantic` 定义四类治理规则 schema (准入/分润/惩罚/信誉), 用 `networkx` 构建生态拓扑并提取核心-边缘/中心性指标, 用 `mesa` 仿真 30 agents/15 ticks 下两种治理规则的 Gini/成交率/欺诈率/平台收入差异, 用 `numpy-financial` 计算平台 12 月 NPV, 并基于三时间线 (immediate tick / near 年 / far 3 年) 给出治理规则的最优路径推荐 — 所有结论必须以仿真 Gini 分布与 NPV 敏感度为证据。

---

## diagnostic (CS229 pset0 式先测, 探测先验缺口)

> 3 题, 每题独立作答, 限时 5 分钟/题。用于诊断你是否已具备上机所需的先验知识。打分后按缺口进入对应 drill。

### Q1 (网络效应识别)
某 Agent 平台规定 "开发者越多, 同类 Agent 越多, 用户越容易找到合适 Agent" — 这属于四类网络效应中的哪一类? 同一平台"使用越多 -> 数据越多 -> Agent 越强" 又属于哪一类? 它们与传统双边市场 (App Store) 的本质区别是什么?

### Q2 (责任归属分层)
某营销 Agent 在自主投放过程中产生虚假宣传内容, 给品牌方造成损失。请按"责任归属 4 层模型" (开发者/部署者/用户/Agent 本身) 分析每一层可能承担的责任, 并指出哪一层是 2026 前沿法律未定问题。

### Q3 (治理规则-生态健康因果)
"严准入+高分润" 与 "宽准入+低分润" 两种治理规则, 你直觉哪种会让平台 12 月 NPV 更高? 你的因果链是什么? 你如何用 mesa 仿真与 numpy-financial NPV 验证你的直觉? 写出至少 3 个你预期会影响结论的混淆变量。

---

## subskills (拆 3 个子技能)

- **S1. 治理规则 schema 化 (pydantic)**: 把"准入门槛/分润比例/惩罚机制/信誉评分"4 类治理规则, 翻译为 pydantic BaseModel schema 契约, 支持 API Economy 2.0 的"Agent 可发现治理声明"。
- **S2. 生态拓扑分析 (networkx)**: 用 MultiDiGraph 构建平台=hub、Agent=节点、A2A/MCP=边, 计算度分布/聚类系数/核心-边缘/degree-betweenness-closeness 三类中心性, 识别单点故障风险。
- **S3. 治理-生态-价值因果链仿真 (mesa + numpy-financial + 天道推演三时间线)**: 用 mesa 跑 30 agents/15 ticks 仿真, 用 numpy-financial 算 12 月 NPV, 用三时间线 (immediate tick / near 年 / far 3 年 MCP-A2A 演化) 推演最优治理路径。

---

## drills (>=3 个, 每个 drill 含 5 字段)

### drill_id: D1
- **skill**: S1 (pydantic 治理 schema)
- **difficulty**: 2 (1-5)
- **reps_required**: 3
- **feedback_rule**: 用 `pydantic` 跑 `model.validate()` 验证 schema; 若 `AdmissionRule` 缺字段或 `RevenueShare.split_ratio` 不归一, pydantic 抛 `ValidationError` 即反馈; 引用真实生态案例: 对比 OpenAI GPT Store 30%/15% 抽成 vs MCP 0 抽成, 验证你的 `RevenueShare` schema 是否能同时表达这两种契约。
- **worked_faded** (完整示范 -> 部分填空 -> 独立解 三阶段):
  - **阶段1 完整示范**: 给出 `AdmissionRule` 的完整 pydantic 定义 (含 `threshold: float`, `audit_flow: Literal["self","platform","third_party"]`), 学生读懂。
  - **阶段2 部分填空**: 给出 `RevenueShare` 骨架, 学生填 `platform_take: float = Field(ge=0, le=1)` 与 `developer_split: float` 的归一约束。
  - **阶段3 独立解**: 学生独立写 `PenaltyRule` 与 `ReputationScoring`, 并写一段 `model_dump_json()` 输出可被其它 Agent 发现的治理声明。

### drill_id: D2
- **skill**: S2 (networkx 生态拓扑)
- **difficulty**: 3 (1-5)
- **reps_required**: 3
- **feedback_rule**: 用 `networkx.degree_centrality(G)`、`betweenness_centrality(G)`、`core_extent(G)` (或近似 `nx.k_core`) 计算指标; 反馈规则: 若 A2A 调用边集中在 <3 个 hub 节点, 则 `betweenness` 标准差 > 0.2 → 单点故障风险高, 提示学生标注 hub 节点; 引用真实生态: Coze/Dify/LangGraph/OpenAI GPT Store/Hugging Face Spaces/MCP/A2A 7 个平台构建的 MultiDiGraph 必须包含至少 7 个 hub。
- **worked_faded**:
  - **阶段1 完整示范**: 给出 `MultiDiGraph` 构建代码, 添加 3 个平台 hub + 5 个 Agent 节点 + A2A 边, 计算 `degree_centrality`。
  - **阶段2 部分填空**: 给出 7 平台+开发者+用户节点骨架, 学生补全 A2A/MCP 边的添加与 `betweenness_centrality`/`closeness_centrality` 计算。
  - **阶段3 独立解**: 学生独立判断"谁是生态核心、谁是单点故障风险", 并写出 100 字结论引用具体中心性数值。

### drill_id: D3
- **skill**: S3 (mesa + numpy-financial 因果仿真)
- **difficulty**: 5 (1-5)
- **reps_required**: 4
- **feedback_rule**: 用 `mesa.Model` + `DataCollector` 跑 30 agents/15 ticks, 收集 `Gini`/`成交率`/`欺诈率`/`平台收入`; 反馈规则: 若两种治理规则下 Gini 差 < 0.05 或 NPV 差 < 10% → 仿真未体现治理差异, 提示检查 `PlatformAgent.apply_rule()` 是否真正执行; 引用真实生态: 仿真结果必须与 OpenAI GPT Store 30% 抽成 vs MCP 0 抽成的真实差异做 sanity check。
- **worked_faded**:
  - **阶段1 完整示范**: 给出 `PlatformAgent` + `DevAgent` + `UserAgent` 的完整 mesa 框架, 跑通严准入+高分润 1 次。
  - **阶段2 部分填空**: 给出宽准入+低分润的骨架, 学生补全 `step()` 中的治理规则执行与 `DataCollector` 指标收集。
  - **阶段3 独立解**: 学生独立跑两种治理各 5 次, 用 `numpy-financial.npv` 算 12 月 NPV, 写 300 字结论: "在我的营销场景下, 哪种治理规则更优? Gini 与 NPV 证据如何支持?"

### drill_id: D4 (附加, 天道推演×生态治理)
- **skill**: S3 + 三时间线推演
- **difficulty**: 5 (1-5)
- **reps_required**: 2
- **feedback_rule**: 用天道推演框架对 MCP vs OpenAI GPT Store 做沙盘推演; 反馈规则: 必须标注 (a) 推演假设 (b) 已知盲点 (c) 三时间线 (immediate 月/near 年/far 3 年); 若 far 3 年线未涉及 MCP+A2A 协议演化, 则提示补全。
- **worked_faded**:
  - **阶段1 完整示范**: 给出 MCP 生态的 immediate 月推演完整示例 (零抽成 + 开放协议 -> 短期开发者涌入)。
  - **阶段2 部分填空**: 给出 near 年推演骨架, 学生补全数据飞轮与同边负向效应。
  - **阶段3 独立解**: 学生独立推演 far 3 年 MCP+A2A 标准化下的生态终局, 标注假设与盲点。

---

## progressive_project (CS230 式渐进交付)

- **proposal** (Day 3 第 1 小时末提交): 选定一个真实 Agent 平台 (Coze / Dify / LangGraph / OpenAI GPT Store / Hugging Face Spaces / MCP / A2A 任选一), 写 1 页 proposal: 你要为它设计什么治理规则? 为什么这个规则对该平台最重要? (引用该平台公开数据)
- **milestone** (Day 3 第 3 小时末提交): 跑通 D1+D2, 提交 `pydantic` schema 文件 + `networkx` 生态拓扑图 (matplotlib) + 中心性指标表。
- **final** (Day 3 末提交): 跑通 D3+D4, 提交完整 `solution.ipynb` (6 个 TODO 全填), 含两种治理规则的 mesa 仿真 Gini 曲线 + numpy-financial 12 月 NPV 对比 + 天道推演三时间线分析。
- **poster** (次周展示): 1 页 poster, 标题 "在 X 平台, Y 治理规则最优, 因为仿真 Gini=___ 与 12 月 NPV=___ 证据"。Poster 必须包含 3 张图: 生态拓扑、Gini 演化、NPV 敏感度。

---

## interleaving (A1B1C1 → B2C2A2 → C3A3B3 交叉排布, 不块状)

> 不要把 D1 全部刷完再刷 D2 — 那是块状练习, 迁移效果差。按以下交叉顺序练习:

- **Round 1**: A1(D1 阶段1) → B1(D2 阶段1) → C1(D3 阶段1)
- **Round 2**: B2(D2 阶段2) → C2(D3 阶段2) → A2(D1 阶段2)
- **Round 3**: C3(D3 阶段3) → A3(D1 阶段3) → B3(D2 阶段3)
- **Round 4 (天道推演整合)**: D4 阶段1 → D4 阶段2 → D4 阶段3 (作为跨 S1+S2+S3 的整合练习)

每 Round 之间间隔至少 1 小时 (spaced retrieval), 不连续刷。

---

## retry_policy (CS230 式 retry)

- 每个学生有 **10 free late days** 可分摊到任意 drill/final/poster (1 day = 24h 顺延, 不罚分)。
- 任何 drill 若 < 80% mastery, 可 **失败重试不罚分** (取最高分), 但重试必须间隔至少 1 小时 (spaced, 非massed)。
- final 若未达标, 可重交一次, 但必须附 200 字反思说明上次哪里错了、这次怎么改的。

---

## weak_loop (连续 2 次失败触发弱项循环)

若学生在同一 drill 连续 2 次未达 80% mastery:

1. **回退上一 drill**: 若 D3 失败 2 次, 回退到 D2 阶段3 重做 (巩固前置技能)。
2. **补充 worked example**: 重新看该 drill 的"阶段1 完整示范", 并在纸上手写一遍关键代码 (pydantic schema / networkx 构图 / mesa step 函数)。
3. **再次尝试**: 间隔 1 小时后重做"阶段2 部分填空", 若仍失败, 触发导师介入 (tutorial.ipynb 的 Oxford Socratic tutorial)。
4. **盲点记录**: 失败原因写入 `student_model.json` 的 `blindspots` 字段, 供 schedule.json 间隔重复卡片优先复习。

---

## mastery 阈值

- 单 drill mastery: 该 drill 阶段3 独立解得分 >= 80%
- 单元 mastery: D1+D2+D3+D4 全部 >= 80% + final `solution.ipynb` 6 个 TODO 全填且 mesa 仿真能跑通 + 300 字分析有 Gini/NPV 证据
- 不达 mastery 不进入下一 Day (Day 4 平台战略+生态设计依赖本 Day 的 mesa/networkx 基础)
