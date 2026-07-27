---
unit: U-R2
topic: 行动研究 (Action Research)
version: v6.0
skill_target: 能用 pandas 独立建模 4 轮 Plan-Act-Observe-Reflect 行动研究循环、量化评估 trustworthiness 三准则 (三角验证/成员校验/反思性)、并用贝叶斯更新从每轮观察数据推断"干预有效"的后验概率
---

# R2 行动研究 · 刻意练习 (Deliberate Practice)

> 基于 Ericsson (1993) 刻意练习 + MIT CS229 pset0 先测 + Harvard/Stanford worked-faded 三阶段 + CS230 渐进交付 + interleaving 交叉排布。
> 领域锚定：本单元的 drill 全部使用 R2 真实上机数据 (4 轮 AR 循环 × 4 个 KPI、三角验证数据源数、成员校验率、贝叶斯先验/似然/后验)，引用 pandas / numpy / matplotlib 真实库。

---

## 1. 先测 Diagnostic (CS229 pset0 式, 探测先验缺口)

> 在做任何 drill 之前, 先做这 3 道先测题。每题独立作答, 不查资料, 5 分钟内完成。目的不是评分, 而是让 tutor 看清你的盲点。

### Q1 (认识论层)
Susman & Evered (1978) 把行动研究者称为 "change agent", 而 Yin (2018) 案例研究的研究者尽量不干预场景。请用一句话说明：**如果你在博士论文里"推动企业营销 AI 转型并系统化记录变革过程", 你应该选 AR 还是 Case Study? 为什么?**

### Q2 (循环建模层)
给定 4 轮 Plan-Act-Observe-Reflect 螺旋, 每轮收集 4 个 KPI。请写出 pandas DataFrame 的最小 schema (列名 + dtypes), 使其能直接支撑"高杠杆轮次识别"和"贝叶斯后验更新"两类下游分析。

### Q3 (效度层)
Lincoln & Guba (1985) 的 trustworthiness 四准则中, **Credibility** 用三角验证量化 (每轮数据源数量), **Confirmability** 用成员校验率量化。请说明：如果某轮只有 1 个数据源且成员校验率为 0.4, 这一轮的可信度是否合格? 凭什么阈值判断?

> 评分规则：tutor 用 [TASK] 级反馈标注每题的"盲点类型" (认识论混淆 / schema 缺字段 / 阈值经验缺失)，写入 `student_model.json` 的 `blind_spots` 字段。

---

## 2. 子技能拆解 (subskills)

| subskill_id | 名称 | 可观察行为 | 关联 drill |
|-------------|------|-----------|-----------|
| S1 | AR 循环数据建模 | 用 pandas 构建 4 轮 × 4 KPI 的长/宽格式 DataFrame, 含 round/stage/kpi_name/kpi_value 列 | D1, D2 |
| S2 | Trustworthiness 量化评估 | 给定数据源数、成员校验率、反思性评分, 计算每轮 trustworthiness 综合分并识别不合格轮次 | D3 |
| S3 | 干预贝叶斯更新 | 给定先验 Beta(α,β) 与每轮观察 (成功数/总数), 顺序更新后验并绘制后验演化曲线 | D4 |

---

## 3. Drills (>=3, 每个 difficulty 1-5 + reps_required + feedback_rule + worked-faded)

### drill_id: D1
- **target_subskill**: S1
- **difficulty**: 2
- **reps_required**: 3
- **task**: 用 pandas 构造 `ar_cycles` DataFrame, 4 轮 (Round 0-3) × 4 KPI (决策时间/方案质量/AI使用率/团队满意度), 每轮含 stage=Plan/Act/Observe/Reflect 标记。宽格式转长格式。
- **feedback_rule**: 校验 `df.round.unique()` 含 0-3 且 `df.stage.unique()` 含四阶段; 若长格式 melt 后行数 != 16 触发弱项循环 D1-w。引用 `data/README.md` 的 4 轮 KPI 真实文献幅度作为 sanity check (改善幅度应在 [-20%, +60%] 区间)。
- **worked_faded**:
  - 阶段 1 (完整示范): tutor 给出 Round 0 的完整 dict + pd.DataFrame 构造代码
  - 阶段 2 (部分填空): 给出 Round 1-2 的 dict skeleton, 学生填 KPI 值
  - 阶段 3 (独立解): 学生独立构造 Round 3 + 长格式 melt

### drill_id: D2
- **target_subskill**: S1
- **difficulty**: 3
- **reps_required**: 3
- **task**: 基于 D1 的 DataFrame, 计算每轮相对 Round 0 基线的改善%, 识别"高杠杆轮次" (改善幅度 > 20% 的轮次), 用 matplotlib 绘制 4 KPI × 4 轮的趋势线图。
- **feedback_rule**: 校验 `improvement_pct = (df - df.loc[0]) / df.loc[0] * 100`; 若高杠杆轮次数 = 0 触发弱项循环 D2-w (回退 D1 + worked example: 改善% 计算的完整推导)。引用 `solution.ipynb` TODO2 的真实改善幅度区间作为对照。
- **worked_faded**:
  - 阶段 1: 完整示范"决策时间"KPI 的改善% 计算
  - 阶段 2: 部分填空"方案质量"和"AI使用率"的计算
  - 阶段 3: 独立解"团队满意度" + 高杠杆轮次识别 + matplotlib 图

### drill_id: D3
- **target_subskill**: S2
- **difficulty**: 3
- **reps_required**: 4
- **task**: 给定每轮的 `data_sources` (列表, 长度即三角验证数据源数)、`member_check_rate` (0-1)、`reflexivity_score` (1-5), 计算 trustworthiness 综合分 = 0.4*min(data_sources/3,1) + 0.3*member_check_rate + 0.3*reflexivity_score/5, 标记 < 0.6 的轮次为不合格。
- **feedback_rule**: 校验 trustworthiness 分在 [0,1] 区间且不合格轮次标注非空; 若学生用 internal validity 而非 trustworthiness 触发弱项循环 D3-w (回退 notes.md § 关键回顾 4 + worked example: Lincoln & Guba 四准则对应表)。
- **worked_faded**:
  - 阶段 1: 完整示范 Round 0 的 trustworthiness 计算
  - 阶段 2: 部分填空 Round 1-2 的权重求和
  - 阶段 3: 独立解 Round 3 + 不合格轮次识别 + 审计追踪 (audit trail) 文本说明

### drill_id: D4
- **target_subskill**: S3
- **difficulty**: 4
- **reps_required**: 5
- **task**: 设先验 Beta(2, 2) (即"干预有效"先验概率 0.5, 弱信息先验)。给定每轮观察 (成功次数/总试验数), 用 scipy.stats.beta 顺序更新后验 α' = α + successes, β' = β + failures, 绘制 4 轮后验 PDF 演化曲线, 报告最终后验均值和 95% HDI。
- **feedback_rule**: 校验后验 α' = 2 + sum(successes) 且 β' = 2 + sum(failures); 若学生用频率派 p-hat 而非贝叶斯后验触发弱项循环 D4-w (回退 notes.md § 贝叶斯更新与行动研究 + worked example: Beta-Binomial 共轭推导)。引用 `solution.ipynb` TODO7 的真实后验值作为对照。
- **worked_faded**:
  - 阶段 1: 完整示范 Round 0 的 Beta 后验更新 + PDF 绘制
  - 阶段 2: 部分填空 Round 1-2 的 α'/β' 更新
  - 阶段 3: 独立解 Round 3 + 95% HDI + 后验演化曲线

### drill_id: D5 (extension, PAR 共创)
- **target_subskill**: S2
- **difficulty**: 4
- **reps_required**: 3
- **task**: 给定 5 个利益相关方 (营销团队/AI工程师/客户/管理层/法务), 用 pandas 构造 power-interest grid (高/低权力 × 高/低利益), 标注 Key Players/Show Consideration/Meet Their Needs/Least Important 四象限, 计算每轮共创度 = (Key Players 数 + Show Consideration 数) / 总数, 绘制共创度演化。
- **feedback_rule**: 校验四象限标注与 power/interest 列一致且共创度在 [0,1]; 若学生把"低权力高利益"标为 Key Players 触发弱项循环 D5-w (回退 notes.md § 关键回顾 3 权力-利益矩阵 + worked example: Kemmis PAR 共创度公式)。
- **worked_faded**:
  - 阶段 1: 完整示范"营销团队"象限归属
  - 阶段 2: 部分填空"AI工程师"和"客户"
  - 阶段 3: 独立解"管理层""法务" + 共创度演化曲线

---

## 4. 交叉练习 Interleaving (A1B1C1...B2C2A2...C3A3B3, 不块状)

> 不按 D1->D2->D3->D4->D5 块状刷, 而是按下面 3 段交叉排布。每段做完才进入下一段, 强迫大脑切换子技能, 促进迁移 (Rohrer 2012 interleaving effect)。

**Block-1 (A1B1C1)**: D1-阶段1 → D3-阶段1 → D4-阶段1
  - 切换：AR 循环建模 → trustworthiness 量化 → 贝叶斯后验
**Block-2 (B2C2A2)**: D3-阶段2 → D4-阶段2 → D1-阶段2
  - 切换：trustworthiness 部分填空 → 贝叶斯部分填空 → AR 循环部分填空
**Block-3 (C3A3B3)**: D4-阶段3 → D1-阶段3 → D3-阶段3
  - 切换：贝叶斯独立解 → AR 循环独立解 → trustworthiness 独立解
**Extension (D2+D5)**: D2 全阶段 → D5 全阶段 (作为 S1/S2 的迁移应用)

---

## 5. 渐进项目 Progressive Project (CS230 式 proposal → milestone → final → poster)

| 阶段 | 交付物 | 关联 drill | 字数/规模 | 评估重点 |
|------|--------|-----------|----------|---------|
| Proposal | 用 200 字陈述你将用 AR 方法研究的一个企业营销 AI 部署问题, 列出诊断假设 + 4 KPI + 4 轮 Plan 草案 | D1 | 200 字 | 假设的可证伪性 |
| Milestone | 提交 D1+D2+D3 完整代码 (4 轮 DataFrame + 改善% + trustworthiness 综合分), 附 300 字中期反思 | D1, D2, D3 | 3 个 notebook + 反思 | 数据建模正确性 |
| Final | 提交 D1-D5 全部代码 + 贝叶斯后验曲线 + PAR 共创度演化, 附 500 字天道推演视角反思 (Plan 阶段沙盘推演了几个干预方案? 各推演了什么 3 层未来走向?) | D1-D5 | 5 个 notebook + 反思 | 后验更新逻辑 + 共创度演化 |
| Poster | 一页 A3 海报: AR 循环图 + KPI 趋势图 + 后验演化图 + 3 个关键盲点 | 全部 | 1 页 | 可视化表达力 |

---

## 6. 重试策略 Retry Policy (CS230 式)

- **10 free late days**: 整个 R2 单元共 10 天迟到额度, 自由分配给任意 drill/milestone/final, 不扣分。
- **失败重试不罚分**: 任何 drill 未达 reps_required 或触发 weak_loop, 可无限次重试, 取最高分, 不扣分。
- **worked-faded 重置**: 连续 2 次失败后, 下一次重试必须从阶段 1 (完整示范) 重新开始, 而非从失败点继续。

---

## 7. 弱项循环 Weak Loop (连续 2 次失败触发)

```
drill D_k 连续 2 次未达 reps_required
  ↓
触发 D_k-w (weak loop):
  1. 回退到 D_k 的阶段 1 (完整示范), 重新看一遍 worked example
  2. 完成 D_k-w 补充 worked example (1 个额外小题, 同 subskill)
  3. 重新进入 D_k 阶段 2, 必须连续 2 次通过才解锁阶段 3
  4. 若再次连续 2 次失败, 升级为 1-on-1 tutorial (tutorial.ipynb 限频豁免 1 次)
```

**弱项循环 worked example 库** (领域特定):
- D1-w: 给定 2 轮 × 2 KPI 的微型 DataFrame, 完整推导宽转长
- D2-w: 给定 3 个 KPI 值, 完整推导改善% 和高杠杆判定
- D3-w: 给定 1 轮的 3 个 trustworthiness 输入, 完整推导综合分 + 不合格判定
- D4-w: 给定 Beta(1,1) 先验 + 1 轮观察, 完整推导后验 α'/β' + 95% HDI
- D5-w: 给定 2 个利益相关方, 完整推导象限归属 + 共创度

---

## 8. 自检 (做完所有 drill 后)

- [ ] 我能在不查 notes.md 的情况下, 写出 Plan-Act-Observe-Reflect 四阶段螺旋的完整定义
- [ ] 我能解释 trustworthiness 与 internal validity 的本质区别 (认识论层)
- [ ] 我能用 Beta-Binomial 共轭手算 1 轮贝叶斯更新 (不依赖 scipy)
- [ ] 我能说出 AR vs DSR 的 3 个认识论差异 (研究者角色/知识生产/效度标准)
- [ ] 我能用天道推演视角说明 Plan 阶段的沙盘推演如何减少试错成本
