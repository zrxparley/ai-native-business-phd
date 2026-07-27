# 刻意练习 - U4D3 Agent经济 + 新兴商业模式 (v6.0 学习科学层)

> 理论依据: Ericsson 刻意练习 5 要素 (目标/专注/反馈/重复/渐难) + MIT Worked-Faded 示例 + 交叉练习 A1B1C1
> 适配本单元: mesa ABM 63 agents / 100 ticks / Gini 0.108->0.857 / 104 笔 A2A + 天道推演×多Agent仿真

---

## skill_target

能用 **mesa** 构建 Agent经济仿真（3类Agent + DataCollector + 8个 model_reporters），用 **pandas + matplotlib** 分析涌现现象（基尼/A2A/价格收敛/推理成本约束），并用 **天道推演**视角做商业模式沙盘对比（方案A vs B，3层推演 + 概率评估 + 最优路径推荐）。

## subskills

- **S1 (mesa 编码)**: mesa 的 Model/Agent 基类使用 + DataCollector 的 model_reporters / agent_reporters 配置 + AgentSet 的 shuffle_do/select 操作
- **S2 (涌现分析)**: 三类 Agent（消费者/商家/AI中介）行为规则编码 + 破产机制 + 用 pandas 提取 DataCollector 时间序列 + matplotlib 4 子图（基尼/价格/存活/A2A）
- **S3 (天道推演)**: 用天道推演 5 能力（局势感知/因果链/沙盘3层/概率评估/最优路径）做参数扫描对比，输出 2-3 条时间线 + 风险预警 + 认知盲点

## diagnostic (3 道先测，检测起点)

1. **D1-diag**: mesa 中 `Agent.step(self)` 和 `Model.step(self)` 的职责分工是什么？`DataCollector` 的 `model_reporters` 与 `agent_reporters` 区别？(检测 ABM 框架基本概念)
2. **D2-diag**: 给定 Gini 0.108 -> 0.857 的仿真输出，你能解释这个变化背后的微观 Agent 行为吗？是消费者破产、商家动态定价、还是 AI中介 fee 累积？依据是什么？(检测涌现思维 + 反单一变量归因)
3. **D3-diag**: 若推理成本从 $0.0025/匹配（GPT-4o）降到 $0.000135/匹配（DeepSeek V3），AI中介 Agent 的存活曲线会如何变化？为什么？请用天道推演沙盘做 3 层推演（immediate/near/far）。(检测推理成本约束 + 天道推演视角)

---

## drills (>=3, 每含 difficulty/reps_required/feedback_rule/worked_faded)

### drill_id: D1
- **difficulty**: 2
- **reps_required**: 3
- **feedback_rule**: 失败时提示"回顾 mesa Agent 基类签名 (`class XAgent(Agent)`) + DataCollector 的 `model_reporters` 表结构"。引用天道推演「局势感知」对应 Agent 初始化阶段--初始 Agent 分布与参数设置决定初始 Gini/价格/存活率。若学生在 TODO1（ConsumerAgent）卡住，让其先抄写 solution.ipynb 的 ConsumerAgent 完整代码，再合上答案默写一遍。
- **worked_faded**: 
  - **完整示范** (Worked): solution.ipynb 的 `ConsumerAgent` 全代码（预算管理 + 比价 + 直接购买 + 破产机制）
  - **部分填空** (Faded-1): `MerchantAgent` 留 3 处 TODO（动态定价策略 / 平台抽成扣除 / 补货逻辑）
  - **独立解** (Faded-2): `MediatorAgent`（AI中介）全部自写，包括 A2A 信息交换 + 推理成本扣除 + 动态调费

### drill_id: D2
- **difficulty**: 3
- **reps_required**: 3
- **feedback_rule**: 失败时让学习者对比两次仿真："推理成本=0 vs 推理成本=$0.0025/匹配"的 AI中介存活曲线 + A2A 交易量时间序列。引用天道推演「因果链追踪」--购买 -> 降价 -> 竞争 -> 破产 的因果有向图。若学生无法区分平台抽成 30% 与 AI中介 fee 2-5% 的因果贡献，让其用 `mesa.batch_run` 做 fee × commission 双变量扫描，看 Gini 曲面。
- **worked_faded**:
  - **完整示范** (Worked): 单变量 `batch_run`（fee=[0.02, 0.05, 0.10]）的 Gini 时间序列 + 代码
  - **部分填空** (Faded-1): 双变量扫描（fee × commission）留 4 处 TODO（参数字典 / `batch_run` 调用 / 结果 DataFrame 透视 / 曲面图绘制）
  - **独立解** (Faded-2): 三变量扫描（fee × commission × inference_cost）+ 统计分布 + 95% CI

### drill_id: D3
- **difficulty**: 4
- **reps_required**: 2
- **feedback_rule**: 失败时让学习者写一段 300 字天道推演分析「方案A 高抽成低推理成本 vs 方案B 低抽成高推理成本」的 3 层推演（immediate tick 1-10 / near tick 11-50 / far tick 51-100）+ 概率评估（多 seed 分布）+ 最优路径推荐。引用天道推演「沙盘模拟（3层推演）」+「概率评估」+「最优路径推荐」。若学生只给单一时间线，强制要求 2-3 条平行世界场景（含黑天鹅：推理成本突降 / A2A 协议标准化 / 平台反垄断）。
- **worked_faded**:
  - **完整示范** (Worked): 单场景 Gini 分析（方案A，3 层推演 + 1 条时间线）
  - **部分填空** (Faded-1): 双场景对比（方案A vs B）留 5 处 TODO（immediate 层 / near 层 / far 层 / 概率分布 / 最优路径）
  - **独立解** (Faded-2): 三场景（A/B/C 黑天鹅）+ 概率分布 + 最优路径 + 风险预警 + 认知盲点

---

## interleaving (A1B1C1 明文交叉，不块状)

交叉排布说明: **A1B1C1 ... B2C2A2 ... C3A3B3** 模式（参考 MIT Open Learning 交叉练习原则）。

- **A 类** = mesa 编码 drill (S1 子技能)
- **B 类** = pandas/matplotlib 涌现分析 drill (S2 子技能)
- **C 类** = 天道推演沙盘对比 drill (S3 子技能)

| 日 | 第1题 | 第2题 | 第3题 |
|----|-------|-------|-------|
| Day 1 | A1 (D1 Worked 示范) | B1 (D2 单变量扫描) | C1 (D3 单场景推演) |
| Day 2 | B2 (D2 Faded-1 双变量) | C2 (D3 Faded-1 双场景) | A2 (D1 Faded-1 MerchantAgent) |
| Day 3 | C3 (D3 Faded-2 三场景独立) | A3 (D1 Faded-2 MediatorAgent 独立) | B3 (D2 Faded-2 三变量独立) |

**禁止块状连做 3 个 A**--块状练习会制造假性熟练（块内同质提示），交叉练习强制每次切换子技能检索路径，强化长期保留（Butler 2010 检索练习证据）。

## retry_policy

- 每个 drill 每天最多 **2 次重试**。失败后强制 **20 分钟冷却**（防止挫败循环 / 情绪过载）。
- 3 次总失败触发 `tutorial.ipynb` 的 Socratic 介入（限频 1 次/天）。
- 重试时 drill 的 `worked_faded` 阶段回退一级（如 Faded-2 失败 -> 重做 Faded-1）。

## weak_loop (连续 2 次失败触发)

连续 2 次失败触发**弱项循环**：
1. 回退到上一 drill 的完整示范（Worked）--例如 D2 连续失败则回退 D1 的 ConsumerAgent 完整代码
2. 补充 worked example：solution.ipynb 对应 TODO + 30 分钟 mesa DataCollector 官方文档阅读
3. 隔天重做（不强求当天通关，避免疲劳累积）
4. 若 weak_loop 仍失败，触发 alignment.md 的 ILO 对齐自检（是否 TLA 未训练 ILO？）

---

## progressive_project (脚手架渐退，proposal -> milestone -> final)

参考 MIT 6.5940 / CS230 渐进项目脚手架：

- **阶段 1 (proposal)**: Agent经济模型设计文档（1页）--定义 3 类 Agent 的 step 逻辑 + 8 个 model_reporters + 破产规则 + 参数表（fee/commission/inference_cost 取值依据）。提交后获 Hattie [TASK] 级反馈。
- **阶段 2 (milestone)**: 可运行仿真 + 4 个子图（基尼/价格/存活/A2A）+ 1 段 300 字涌现分析。提交后获 [PROCESS] + [SELF-REG] 反馈。
- **阶段 3 (final)**: 参数扫描 + 双场景对比 + 天道推演沙盘报告（含 3 层推演 + 概率评估 + 最优路径 + 风险预警 + 认知盲点）。提交后获 [FEED-FORWARD] 反馈 + 推荐复习单元。

每阶段提交后 fellow 用 `tutorial.ipynb` 做 Socratic 追问，未通过则不进入下一阶段。
