# 刻意练习 - skill4-day5 商业模式画布+投资 (v6.0 学习科学层)

> Ericsson 刻意练习 5 要素 + MIT Worked-Faded 渐退示例 + 交叉练习 (A1B1C1 模式)
> 本文件与 schedule.json / alignment.md / tutorial.ipynb / notes.md 共同构成 v6.0 学习科学层

---

## skill_target (核心可观察技能)

能用 **pandas** 构建 AI 商业模式画布九宫格 DataFrame（识别推理成本/数据成本为 AI 独有），用 **numpy-financial** 计算 NPV/IRR/PI 判断投资可行性，用 **scipy.stats + numpy** 做蒙特卡洛模拟得 P(NPV>0)，并用**天道推演**做 Bull/Base/Bear 三路径三层推演，给出投资决策建议。

---

## diagnostic (诊断性前测 - 3 道, 检测先备知识缺口)

- **Q1 (画布差异识别)**: 商业模式画布九宫格中，AI 适配版相比传统 SaaS 画布新增了哪两项 AI 独有的成本结构？为什么 HubSpot 78% 毛利率在 AI SaaS 上会被拉低到 65%？
- **Q2 (基础财务计算)**: 给定 5 年现金流 `[-100, 30, 40, 50, 60, 70]`（单位 $K），用 `numpy-financial` 计算 NPV（折现率 10%）和 IRR。cashflows[0] 为什么必须是负数？`npf.irr()` 为什么要求至少一次符号变化？
- **Q3 (分布思维)**: MarketingAgent Pro 的 NPV=$451.2K（均值），P(NPV>0)=55.7%。这两个数矛盾吗？为什么单点 NPV 比 P(NPV>0) 决策价值低？

> 诊断结果写入 student_model.json 的 `diagnostic_score` 字段，决定 D1/D2/D3 的初始 scaffold_level。

---

## subskills (3 项子技能)

- **S1 画布构建**: 用 pandas 构建 AI 商业模式画布九宫格 DataFrame，识别 AI 适配的独有变化（推理成本 + 数据成本 + Agent 渠道 + outcome-based 收入流）
- **S2 DCF 财务计算**: 用 numpy-financial 计算 NPV/IRR/回收期/PI，符号方向正确，判断 AI 项目投资可行性（MarketingAgent Pro 基准 NPV=$451.2K IRR=20.08%）
- **S3 蒙特卡洛+天道推演**: 用 scipy.stats 做 10000 次蒙特卡洛模拟得 P(NPV>0) 分布，用天道推演做 Bull/Base/Bear 三路径×三层（immediate/near/far）推演，理解频率派分布与场景路径的互补关系

---

## drills (3 个刻意练习, 每个 worked-faded 三阶段)

### drill_id: D1 (画布构建)
- **difficulty**: 3
- **reps_required**: 3
- **feedback_rule**: 若九宫格漏掉推理成本或数据成本作为 AI 独有成本结构，反馈："AI SaaS 毛利率因推理成本被拉低到 65% vs HubSpot 78%。重画'成本结构'格，必须列出推理成本（持续）+ 数据成本。Agent 渠道作为新渠道也应在'渠道'格。" 让学习者重画成本结构与渠道两格
- **worked_faded**:
  - 阶段1（完整示范 Worked）: 给出 MarketingAgent Pro 的完整九宫格填法（含推理成本 30% + 数据成本 5% + Agent 分发渠道）
  - 阶段2（部分填空 Faded）: 给出 8 格完整留"成本结构"和"渠道"两格空，学习者填
  - 阶段3（独立解 Independent）: 学习者独立构建另一个 AI 产品（如 CodingAgent）的完整九宫格，必须标注 AI 适配的 4 项独有变化

### drill_id: D2 (DCF 财务计算)
- **difficulty**: 4
- **reps_required**: 3
- **feedback_rule**: 若 NPV 符号错误（cashflows[0] 写成正数）或 IRR 报错无解，反馈："`npf.npv(rate, cashflows)` 中 cashflows[0] 为负投资支出（t=0 现金流出），t>=1 为正流入。`npf.irr()` 要求现金流序列至少一次符号变化，否则无解。重写 cashflows 序列确保符号方向正确。" 让学习者重写现金流序列并重算
- **worked_faded**:
  - 阶段1（完整示范 Worked）: 给出 MarketingAgent Pro 5 年 DCF 完整代码（NPV=$451.2K, IRR=20.08%, PI=1.45, 回收期 3.2 年）
  - 阶段2（部分填空 Faded）: 留 `npf.npv()` 和 `npf.irr()` 调用空，给定现金流序列让学习者填
  - 阶段3（独立解 Independent）: 学习者对 CodingAgent 重做 5 年 DCF，自定现金流假设并计算 NPV/IRR/PI/回收期

### drill_id: D3 (蒙特卡洛 + 天道推演)
- **difficulty**: 5
- **reps_required**: 3
- **feedback_rule**: 若蒙特卡洛 P(NPV>0) 计算错误（如未对营收/毛利率/增长率同时抽样），或天道推演三路径未推演三层（immediate/near/far），反馈："蒙特卡洛评估参数不确定性（频率派分布），天道推演评估场景路径优不优（因果推演），两者互补。Bull/Base/Bear 每路径必须推演 immediate（1 年内）/near（1-3 年）/far（3-5 年）三层。" 让学习者重做 Bull 路径的三层推演
- **worked_faded**:
  - 阶段1（完整示范 Worked）: 给出 MarketingAgent Pro 蒙特卡洛 10000 次模拟完整代码（P(NPV>0)=55.7%）+ Bull/Base/Bear 三路径×三层完整推演表
  - 阶段2（部分填空 Faded）: 留 `scipy.stats.norm.rvs()` 抽样代码和 Bear 路径 far 层空，学习者填
  - 阶段3（独立解 Independent）: 学习者对另一个 AI 产品做蒙特卡洛 10000 次 + 三路径×三层天道推演，输出投资决策建议

---

## interleaving (交叉练习 - A1B1C1...B2C2A2...C3A3B3 明文排布)

不块状练习。按 MIT Open Learning 明文原则采用交叉排布：

- **A = 画布构建 (D1)**
- **B = DCF 计算 (D2)**
- **C = 蒙特卡洛 + 天道推演 (D3)**

排布顺序：
1. **第1轮 A1B1C1**: 各 drill 的阶段1 Worked 完整示范（先画布→再 DCF→再蒙特卡洛+天道推演）
2. **第2轮 B2C2A2**: 各 drill 的阶段2 Faded 部分填空（先 DCF→再蒙特卡洛→再画布，**故意打乱顺序**避免同类型连续形成块状记忆）
3. **第3轮 C3A3B3**: 各 drill 的阶段3 Independent 独立解（先蒙特卡洛+天道推演→再画布→再 DCF，**强制交叉检索**）

> 块状练习（AAA BBB CCC）会让学习者短期记忆同类型操作，交叉练习（ABC BCA CAB）强制每次切换都重新检索，长期保留更好（Butler 2010 检索练习证据）。

---

## weak_loop (弱项循环 - 连续2次失败触发)

连续 2 次同一 drill 失败（如 D3 阶段2 两次提交都不通过）触发弱项循环：

1. **回退上一 drill**: D3 失败回退到 D2 阶段1 Worked（巩固前置技能）
2. **补充 worked example**: 给出 MarketingAgent Pro 同类产品的完整解答（含代码 + 推演表 + 决策建议）
3. **24h 间隔重试**: 等 24 小时（利用间隔重复效应）后重试 D3 阶段2
4. **若仍失败**: 触发 tutorial.ipynb 的 Socratic 对话（见 tutorial.ipynb cell3），需通过 Socratic 追问后才回到 drill

---

## retry_policy (重试策略)

- **第1次失败**: 立即按 feedback_rule 反馈 + 提示阶段1 Worked 示范可参考
- **第2次失败**: 进入 weak_loop（回退上一 drill + worked example）
- **第3次失败**: 触发 tutorial.ipynb Socratic 对话，需通过 Socratic 才回到 drill
- **3次后仍失败**: 标记为盲点写入 student_model.json，推荐复习 schedule.json 对应卡片 + reading.md 深链

---

## progressive_project (渐进式项目 - 6 个 TODO 难度递增)

starter.ipynb 的 6 个 TODO 按难度递增排布，对应 D1/D2/D3 的阶段3 Independent：

| TODO | 难度 | 对应 drill | 交付物 |
|------|------|-----------|--------|
| TODO1 | 2 | D1 阶段3 | 画布九宫格 DataFrame |
| TODO2 | 3 | D2 阶段3 | 5 年 DCF + NPV |
| TODO3 | 3 | D2 阶段3 | IRR/PI/回收期 |
| TODO4 | 4 | D3 阶段3 | 蒙特卡洛 10000 次 + P(NPV>0) |
| TODO5 | 4 | D3 阶段3 | 敏感性分析龙卷风图 |
| TODO6 | 5 | D3 阶段3 | 天道推演 Bull/Base/Bear × 三层 |

最终交付：6 个 TODO 全跑通 + 300 字分析（NPV/IRR/P(NPV>0) + 投资决策建议）= 完整投资评估交付物。
