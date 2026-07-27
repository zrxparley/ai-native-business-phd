# 刻意练习册 -- 选修E10 · Day 2：Agent商业模式设计 (AaaS / outcome-based pricing)

> **方法论**：Ericsson 刻意练习 + MIT OCW 习题脚手架 + Harvard/Stanford 渐进式项目。每个 drill 遵循 Worked-Faded 三阶段（完整示范 -> 部分填空 -> 独立解），feedback_rule 全部锚定本单元真实库（pydantic / numpy-financial / statsmodels）与真实数据（Cursor / Devin / Intercom Fin / Sierra / 11x.ai / DevRev 定价案例 + GPT-4o $5/1M vs DeepSeek V3 $0.27/1M 推理成本基准）。
> **与 starter.ipynb 的关系**：本练习册把 starter 的 6 个 TODO 拆成更细粒度的 drill，方便弱项循环回退。

---

## skill_target

**一句话可观察技能**：给定一个真实 Agent 产品（如 Sierra 客服 Agent 或自选营销 Agent），能在 90 分钟内独立输出一份「定价契约 + 12月 NPV/IRR 财务对比 + 弹性回归最优定价点 + 推理成本敏感度结论」四件套，且每个数字可追溯到 pydantic schema 字段 / numpy-financial 输出 / statsmodels 系数 / 公开定价页。

---

## diagnostic (先测, CS229 pset0 式, 探测先验缺口)

> 限时 15 分钟，闭卷。三题全对可跳过 drill-1 的 worked 阶段；任意一题错则进入弱项循环。

**D1. 概念辨析**：以下四个 Agent 产品的定价分别属于五阶段演进的哪一阶段？
- (a) GitHub Copilot $10-39/月/用户
- (b) OpenAI API $5/1M input tokens
- (c) Intercom Fin $0.99/解决
- (d) 11x.ai 按预约会议收费
> 写出阶段号 (1.0 按席位 / 2.0 按用量 / 3.0 按任务 / 4.0 按结果 / 5.0 按价值分成)。

**D2. 财务直觉**：某 outcome-based Agent 每月 150 次转化，每次 $10，推理成本 GPT-4o 下每次 $0.005。若改用 DeepSeek V3 ($0.00027/次)，月利润提升多少倍？写出算式。

**D3. 弹性直觉**：log-log OLS 回归 log(采纳率) ~ log(价格) 得系数 -1.4。这是弹性还是非弹性？该涨价还是降价？为什么？

---

## subskills (拆解为 3 个可独立练习的子技能)

- **S1: Schema 契约设计** -- 用 pydantic 定义四种定价契约 (AaaSSubscription / PerCallPricing / OutcomeBasedPricing / RevenueShare)，并实现 API Economy 2.0 的 Agent 可发现能力声明。
- **S2: 财务对比与推理成本敏感度** -- 用 numpy-financial 对三种定价模式做 12 月 NPV/IRR，量化推理成本对利润率的影响，找盈亏平衡的推理成本阈值。
- **S3: 弹性回归与最优定价** -- 用 statsmodels 拟合 log-log OLS log(adopt) ~ log(price)，解释弹性系数 95% CI，找利润最大化定价点。

---

## drills (>=3, 每个 drill 含 worked_faded 三阶段 + feedback_rule)

### drill-1: pydantic 四种定价契约 schema (子技能 S1, difficulty=3, reps_required=4)

- **drill_id**: D1-schema
- **difficulty**: 3/5
- **reps_required**: 4 次独立完成（前 2 次可看 worked，后 2 次独立）
- **worked_faded**:
  - **阶段A (Worked 完整示范)**：讲师演示 AaaSSubscription 的完整 pydantic 模型（含 price_per_month / billing_cycle / structured output 字段），逐字段解释为什么用 `condecimal(ge=0)` 而非 `float`。
  - **阶段B (Faded 部分填空)**：学生补全 PerCallPricing（price_per_call + calls_per_month + unit 字段留空），再补 OutcomeBasedPricing 的 price_per_outcome + outcome_metric 字段。
  - **阶段C (Independent 独立解)**：学生独立写 RevenueShare（share_pct / baseline_revenue / attribution_window），并用 `model_validate_json` 验证一个 Sierra 案例的 JSON。
- **feedback_rule**:
  - 若 schema 字段类型用 `float` 而非 `condecimal(ge=0)` -> 提示"为什么定价不能为负？参考 Intercom Fin $0.99/解决 的非负约束"
  - 若缺 structured output 注解 -> 提示"API Economy 2.0 要求 Agent 可发现，你的 schema 缺 `json_schema_extra` 吗？查 pydantic v2 文档"
  - 若四种契约无公共基类 -> 提示"用 `Union[AaaSSubscription, PerCallPricing, OutcomeBasedPricing, RevenueShare]` 作为 PricingContract，让 Agent 自动 dispatch"

### drill-2: numpy-financial 三模式 12月 NPV/IRR + 推理成本敏感度 (子技能 S2, difficulty=4, reps_required=5)

- **drill_id**: D2-npv-irr
- **difficulty**: 4/5
- **reps_required**: 5 次（含 1 次 DeepSeek V3 重算）
- **worked_faded**:
  - **阶段A (Worked)**：讲师用 Cursor Pro $20/月 跑完整 12 月 AaaS 现金流，演示 `numpy_financial.npv(rate=0.1, values=cashflows)` 和 `numpy_financial.irr(cashflows)`，展示推理成本为 0（订阅制不按调用计费）。
  - **阶段B (Faded)**：学生补全 Intercom Fin $0.99/解决 的 outcome-based 现金流（每月解决数留空，推理成本 GPT-4o $0.005/解决 留空），计算 NPV/IRR。
  - **阶段C (Independent)**：学生独立计算 Devin $500/月 + 任务混合定价的 NPV/IRR，并把推理成本从 GPT-4o ($5/1M) 换成 DeepSeek V3 ($0.27/1M)，重算 NPV，写出利润率变化百分比。
- **feedback_rule**:
  - 若 NPV/IRR 算出来 outcome-based 优于 AaaS 但没标注推理成本假设 -> 提示"你的 outcome-based NPV 依赖每解决推理成本，GPT-4o 下 $0.005 vs DeepSeek V3 下 $0.00027，差 18 倍，你的结论在哪个假设下成立？"
  - 若现金流没用负号表示成本 -> 提示"numpy-financial 的 cashflows[0] 是初始投入（负数），你写成正数会得到错误 IRR"
  - 若 IRR 报 `nan` -> 提示"检查是否有月份现金流全负（推理成本超过收入），这是 outcome-based 在高推理成本下亏钱的信号"

### drill-3: statsmodels log-log OLS 弹性回归 + 最优定价 (子技能 S3, difficulty=5, reps_required=4)

- **drill_id**: D3-elasticity
- **difficulty**: 5/5
- **reps_required**: 4 次（含 1 次置信区间解释）
- **worked_faded**:
  - **阶段A (Worked)**：讲师用模拟的 (price, adoption) 数据跑 `smf.ols("log(adopt) ~ log(price)", data=df).fit()`，解释系数 = 弹性，输出 `summary()` 高亮 coef / std err / [0.025 0.975]。
  - **阶段B (Faded)**：学生补全利润最大化定价点公式 `price_opt = elasticity * marginal_cost / (elasticity - 1)`（Lerner 指数），并代入 Intercom Fin 的边际成本。
  - **阶段C (Independent)**：学生独立用 9 个真实 Agent 定价案例（Cursor/Devin/Intercom Fin/Sierra/11x.ai/DevRev 等）拟合弹性，解释 95% CI 是否包含 -1（单位弹性），并讨论"弹性需求下降价增收 vs 非弹性需求下涨价增收"在本数据集的结论。
- **feedback_rule**:
  - 若学生把 OLS 系数直接当"弹性"而不看 p-value -> 提示"statsmodels summary 的 P>|t| > 0.05 说明弹性不显著，你的定价建议不可靠，需要更多数据或换方法"
  - 若最优定价点算出负数 -> 提示"Lerner 公式 price_opt = ε·MC/(ε-1) 当 |ε|<1 时分母同号变负，这是非弹性市场的陷阱，检查你的 ε 符号"
  - 若学生用线性 OLS 而非 log-log -> 提示"弹性必须 log-log，线性系数不是弹性，参考独立教材 §Day 2 弹性回归小节"

---

## progressive_project (CS230 式渐进交付)

模仿 CS230 项目分阶段，把整个 Day 2 的产出组织成一份可答辩的 Agent 商业模式设计报告：

- **Proposal (Week 1)**：选定一个真实 Agent 产品（从 9 个案例中选或自选营销 Agent），写 1 页 proposal：产品定位、目标客户、初步定价假设、3 个待验证假设。
- **Milestone (Week 2)**：提交 pydantic schema + 9 案例数据加载 + 三模式 12 月现金流初版，跑通 `numpy_financial.npv/irr`，标注推理成本假设。
- **Final (Week 3)**：提交完整 starter.ipynb（6 TODO 全填）+ 弹性回归 + 4 子图 + 300 字分析。
- **Poster (Week 4)**：一页 A3 海报，三栏：定价契约 schema / NPV-IRR-弹性数值 / 推理成本敏感度结论，附天道推演三时间线 (immediate/near/far) 推演该 Agent 在 2026-2028 的定价演化。

---

## interleaving (A1B1C1...B2C2A2...C3A3B3 交叉排布, 不块状)

> 研究显示块状练习 (blocked practice) 短期手感好但迁移差；交叉练习 (interleaving) 短期手感差但长期迁移强。本单元采用 A1B1C1-B2C2A2-C3A3B3 三轮交叉。

**子技能标记**：A=S1 schema / B=S2 财务 / C=S3 弹性

**交叉顺序（明文写出，不要块状）**：
1. A1: drill-1 阶段A (worked AaaS schema 示范)
2. B1: drill-2 阶段A (worked Cursor Pro NPV 示范)
3. C1: drill-3 阶段A (worked log-log OLS 示范)
4. B2: drill-2 阶段B (faded Intercom Fin 现金流填空)
5. C2: drill-3 阶段B (faded Lerner 公式填空)
6. A2: drill-2 阶段B (faded PerCallPricing schema 填空) -- 故意打乱，强迫上下文切换
7. C3: drill-3 阶段C (independent 真实 9 案例弹性)
8. A3: drill-1 阶段C (independent RevenueShare schema)
9. B3: drill-2 阶段C (independent Devin + DeepSeek V3 重算)

> 关键：每两次同子技能练习之间至少隔 2 个其他子技能练习，强迫学生重新 load 上下文，强化长期记忆。

---

## retry_policy (CS230 式 retry)

- **10 free late days**：整个单元任意 drill / proposal / milestone / final 可累计迟到 10 天不扣分（CS230 经典政策）。
- **失败重试不罚分**：drill 阶段C (Independent) 首次未达标（见 mastery 阈值 alignment.md），可在 7 天内重交一次，分数取最高，不扣重试罚分。
- **proposal/milestone 互评**：proposal 和 milestone 强制 2 位同学互评（用 alignment.md 的 ILO/AT 自检表），互评质量计入 participation。

---

## weak_loop (连续 2 次失败触发弱项循环)

> Ericsson 研究指出，刻意练习的关键不是"做更多"，而是"在弱项上回退一步重建"。

**触发条件**：任意 drill 的阶段C (Independent) 连续 2 次未达 mastery 阈值（如 drill-2 NPV 误差 > 5% / IRR 符号错 / drill-3 弹性 p-value > 0.05 未识别）。

**弱项循环步骤**：
1. **回退**：退回该 drill 的阶段B (Faded)，重做 1 次，重点标注"卡在哪一步"。
2. **补充 Worked Example**：阅读 solution.ipynb 对应 TODO 的完整解，逐行注释 why（不是 what）。
3. **简化变体**：把数据量减半（如 9 案例减到 4 案例），或把推理成本固定为单一值（去掉 GPT-4o vs DeepSeek V3 对比），先掌握核心流程再加复杂度。
4. **重新挑战阶段C**：用新数据（如换 Sierra 案例为 11x.ai 案例）独立重做。
5. **元认知日志**：在 student_model.json（见 tutorial.ipynb）的 `blind_spots` 字段追加 1 条"我原来卡在哪、回退后懂了什么、下次怎么避免"。

> 连续 3 次弱项循环仍失败 -> 触发 tutorial.ipynb 牛津 tutorial 仿真，预约一次 Socratic 对话。

---

## 评估标准 (与 alignment.md 对齐)

- drill mastery 阈值：阶段C 独立解 >=80% 正确（NPV/IRR 误差 <5%、schema 通过 `model_validate_json`、弹性 p-value <0.05 且方向正确）。
- progressive_project final 评分量表（rubric）：见 alignment.md 的 AT 列。
