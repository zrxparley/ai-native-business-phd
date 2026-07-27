---
unit: capstone-phase-5
topic: 商业模式+估值 (Business model, AI monetization, valuation, CLV, unit economics, sensitivity analysis)
version: v6.0
layer: 学习科学-刻意练习
---

# 刻意练习手册 (Deliberate Practice) · Capstone Phase 5

> 理论基础: Ericsson (1993) deliberate practice + MIT 6.036 pset0 + Harvard/Stanford CS230 渐进交付 + Worked-Faded 示范渐退法。
> 本手册聚焦本单元真实库与真实数据: numpy-financial, scipy.stats, pandas, matplotlib, ATE=+3.8pp (CI [2.2pp, 5.4pp]), HubSpot gross margin 78%, Jasper $1.5B, α=3.33%, 月触达 10,000, AOV $158, ARPU $24K/yr。

---

## skill_target (核心可观察技能)

**学生能在 90 分钟内独立完成**: 给定 Phase 4 输出的 ATE 与置信区间, 用 `numpy-financial` 构建 5 年 DCF 模型, 用 `scipy.stats` 跑 10,000 次蒙特卡洛传播不确定性得到 NPV 分布并报告 P(NPV>0), 用 `matplotlib` 画龙卷风图识别 NPV 高杠杆因子 (含 ATE/推理成本/毛利率), 用天道推演产出 Bull/Base/Bear 三路径投资建议。

---

## diagnostic (CS229 pset0 式先测题, 探测先验缺口)

> 不计分, 仅诊断。答不出 = 该 subskill 进入弱项循环。

**Q1 (DCF 基础)**: 给定 FCF=[-100000, 30000, 35000, 40000, 45000, 50000] (USD, 5年), 折现率 r=10%, 用 `numpy-financial` 写一行算 NPV 与 IRR。预期: `npf.npv(0.10, FCF)`, `npf.irr(FCF)`。若你写的是手算公式 = 缺口 #1。

**Q2 (ATE->ARPU 推导链)**: Phase 4 给出 ATE=+3.8pp 转化率提升, 月触达 10,000, AOV $158, 价值捕获率 α=3.33%。请推到年 ARPU。预期: 10,000 × 0.038 × 158 × 0.0333 × 12 ≈ $24,000/yr。若你直接假设 ARPU=$24K 而非推导 = 缺口 #2。

**Q3 (蒙特卡洛 vs 点估计)**: 为什么 P(NPV>0) 比 "NPV=$X" 更适合 AI 项目投资决策? 请用 Phase 4 ATE 的 95% CI 解释。若你只回答 "更准确" 而未提 "不确定性传播" = 缺口 #3。

---

## subskills (3 个子技能拆解)

- **S1: DCF 建模与 numpy-financial 工具链** — 把 ATE->ARPU->FCF 链条翻译为 `npf.npv/irr/mi` 调用, 正确设定折现率与时间窗口。
- **S2: 蒙特卡洛不确定性传播** — 用 `scipy.stats` (truncnorm/normal) 对 ATE 的 CI 抽样, 跑 N=10,000 次仿真, 输出 NPV 分布与 P(NPV>0)。
- **S3: 敏感性分析与天道推演整合** — 用 `matplotlib` 画龙卷风图排序 NPV 高杠杆因子, 把 Bull/Base/Bear 三路径与 ATE CI 上下界对齐。

---

## drills (>=3, 每个 drill 含 difficulty/reps_required/feedback_rule/worked_faded)

### drill-1: ATE->ARPU->NPV 单链推导
- **drill_id**: D1
- **difficulty**: 2
- **reps_required**: 3
- **feedback_rule**: 比对 `npf.npv(0.10, FCF)` 输出与预期 $24K ARPU 基线; 若 ARPU 没从 ATE 严格推导 (跳过 α 或 AOV) 即标红; 用 HubSpot 78% 毛利率核对 FCF 量级。
- **worked_faded**:
  - Stage A (Worked): 完整示例 — 给出 `npf.npv(0.10, [-1.2e6, 24000*1000*0.78-200000, ...])` 完整代码, 学生阅读并解释每行。
  - Stage B (Faded): 部分填空 — 给出 DCF 框架但留空 α=3.33% 与 AOV=$158 的填入位, 学生补全。
  - Stage C (Independent): 学生独立从 Phase 4 ATE 推到 NPV, 不给框架。

### drill-2: 蒙特卡洛传播 ATE CI
- **drill_id**: D2
- **difficulty**: 4
- **reps_required**: 3
- **feedback_rule**: 检查是否用 `scipy.stats.truncnorm` (避免负 ATE), N>=10000; P(NPV>0) 必须在 [0,1]; 直方图必含 95% CI 标注; 与 Jasper $1.5B 估值交叉验证量级合理性。
- **worked_faded**:
  - Stage A: 完整 `np.random.seed(42); ates = truncnorm.rvs((0.022-0.038)/0.0082, (0.054-0.038)/0.0082, loc=0.038, scale=0.0082, size=10000)` 示范。
  - Stage B: 给出 truncnorm 框架, 留空 size 与 scale 参数。
  - Stage C: 学生独立写完整蒙特卡洛循环 + P(NPV>0) 计算 + 直方图。

### drill-3: 龙卷风图与天道推演三路径
- **drill_id**: D3
- **difficulty**: 4
- **reps_required**: 3
- **feedback_rule**: 龙卷风图必须按 |ΔNPV| 降序排列; ATE/推理成本/毛利率三个因子必出现; Bull=ATE=5.4pp / Base=3.8pp / Bear=2.2pp 必与 CI 对齐; 每路径需 immediate/near/far 三层推演。
- **worked_faded**:
  - Stage A: 给出完整 `matplotlib` 龙卷风图代码 + Bull/Base/Bear 表格。
  - Stage B: 给出龙卷风图框架, 留空排序逻辑; 三路径表留空 far 层。
  - Stage C: 学生独立画图 + 写三路径三层推演。

---

## progressive_project (CS230 式 渐进交付)

- **proposal** (Week 1, 10%): 选定一个真实 AI 营销 Agent 场景 (基于 Phase 4 ATE), 提交商业模式画布 9 宫格草稿 + 1 段价值主张陈述。引用 Osterwalder 画布 + Day 1-5 类型学。
- **milestone** (Week 2, 30%): 提交可运行的 `npf.npv` + `npf.irr` 调用, 给出 MarketingAgent Pro 的 NPV/IRR/PI/回收期四指标 + 一张蒙特卡洛直方图 (N>=10000) + P(NPV>0) 数值。
- **final** (Week 3, 40%): 提交龙卷风图 + Bull/Base/Bear 三路径推演表 (每路径三层) + 一段 300 字投资建议 (含推理成本对毛利率的影响分析, 引用 DeepSeek 效应)。
- **poster** (Week 4, 20%): 2 分钟视频话术 + 一页 poster, 用 GSB 风格汇报 P(NPV>0) 与最优路径。

---

## interleaving (交叉排布, 反块状)

> 不要按 D1->D2->D3 块状刷题。按下列 A1B1C1... 交叉顺序练习, 促进迁移。

记 S1=A, S2=B, S3=C。建议顺序 (每轮 ~30 min):
- **Round 1**: A1 (D1 Stage A) → B1 (D2 Stage A) → C1 (D3 Stage A)
- **Round 2**: B2 (D2 Stage B) → C2 (D3 Stage B) → A2 (D1 Stage B)
- **Round 3**: C3 (D3 Stage C) → A3 (D1 Stage C) → B3 (D2 Stage C)

即: A1B1C1 → B2C2A2 → C3A3B3。这样 S2 (蒙特卡洛) 与 S3 (敏感性) 不会连续两轮出现, 避免近迁移假象。

---

## retry_policy (CS230 式 retry)

- **10 free late days**: 学期内任意分配, 不扣分, 鼓励试错。
- **失败重试不罚分**: milestone 的 P(NPV>0) 算错或 N<10000, 可重交, 不扣分, 但需附 1 段反思 (哪里推理错)。
- **Plagiarism = 0**: 允许引用 `npf` / `scipy.stats` 官方文档, 但禁止抄同学代码。

---

## weak_loop (连续 2 次失败触发弱项循环)

判定: 同一 drill 连续 2 次未通过 (如 D2 Stage C 蒙特卡洛两次 P(NPV>0) 计算错)。

触发后:
1. **回退**: 退到该 drill 的 Stage A (Worked), 重读完整示例。
2. **补充 worked example**: 额外阅读 starter.ipynb 对应 TODO 的 solution 单元。
3. **降 reps**: 该 drill 的 reps_required 临时 +2, 强化训练。
4. **诊断反馈**: 在 `student_model.json` (见 tutorial.ipynb) 中标记 `weak_subskill: "S2"`, 下次 tutorial 优先追问该 subskill。
5. **解除**: 连续 2 次重新通过 Stage C 后退出循环。

---

## 引用库与真实数据 (领域特定, 非通用)

- `numpy-financial` (npf.npv / npf.irr / npf.mi / npf.ror) — 金融计算标准库
- `scipy.stats.truncnorm` — 蒙特卡洛抽样 (避免负 ATE)
- `pandas.DataFrame` — 商业模式画布 9 宫格载体
- `matplotlib` — 龙卷风图 + NPV 分布直方图
- Phase 4 ATE = +3.8pp (95% CI: [2.2pp, 5.4pp])
- HubSpot 2023 gross margin 78% / Jasper $1.5B / OpenAI API 真实定价 / DeepSeek 推理成本 -90%
- α=3.33% 价值捕获率, 月触达 10,000, AOV $158, ARPU $24K/yr

---

*本手册由 v6.0 学习科学层生成。与 notes.md / starter.ipynb / solution.ipynb / alignment.md / tutorial.ipynb / schedule.json 共同构成完整学习材料包。*
