# 选修E2 · Day 1：营销分析框架 · 刻意练习 (Deliberate Practice v6.0)

> **理论依据**：Ericsson "Deliberate Practice" + MIT CS229 pset0 先测 + Harvard/Stanford Worked-Faded 示例 + CS230 渐进交付 + 交叉练习 (Interleaving)
> **适用单元**：elective-e2-marketing-analytics/day-1-framework-descriptive-diagnostic
> **核心数据集/库**：causaldata (NSW RCT) / pandas / scipy.stats / statsmodels

---

## skill_target

学生能独立用 pandas + scipy.stats + statsmodels 对 NSW RCT 营销映射数据完成描述性漏斗 + 诊断性检验 + RFM 分群, 并用业务语言解释 p 值、Cohen's d、OLS 系数的营销含义 (而非仅打印数字)。

---

## diagnostic (先测, 3 道 CS229 pset0 式)

> 探测先验知识缺口, 不计分。每题先答, 再对答案, 自标弱项。

1. **概念辨析**：某电商发现"本月 GMV 同比下降 15%", 这属于四层框架中哪一层? 如果接着问"为什么下降", 需要调用哪一层? 写出两层的方法各 1 个。
2. **统计直觉**：A/B 测试两组各 10000 人, 转化率 3.1% vs 3.0%, p=0.04。这个"统计显著"在营销上可忽略吗? 为什么? 提示: 想效应量与商业成本。
3. **数据映射**：NSW 数据里 treat=1 表示参加就业培训。在营销映射里, re74 / re75 / re78 分别对应什么? 为什么 OLS 回归要把 re75 放进协变量 (与 CUPED 思想相通)?

---

## subskills

- **S1 漏斗与描述统计**: 用 pandas groupby/agg 计算 AARRR 各阶段转化率与流失节点, 并对比 treated vs control 基线 (对应 TODO1/TODO2)
- **S2 假设检验与效应量**: 用 scipy.stats.ttest_ind + chi2_contingency 判断差异是否显著, 并计算 Cohen's d, 区分"统计显著"与"商业显著" (对应 TODO4/TODO5)
- **S3 回归诊断与 RFM 行动**: 用 statsmodels.OLS 控制混杂变量解读 treat 净效应, 并基于 RFM 五分群给出差异化营销动作 (对应 TODO3/TODO6)

---

## drills (>=3, Worked-Faded 三阶段)

### drill_id: D1
- **subskill**: S1
- **difficulty**: 2
- **reps_required**: 3
- **feedback_rule**: 用 NSW 数据 `causaldata.nsw` 做 groupby(treat).describe() 对比 re75 基线; 若 treated/control 的 re75 均值差 > 200 美元则提示检查 RCT 平衡性 (基线不平衡即信号); 输出必须含中位数 vs 均值两列对比, 漏掉即反馈"重读 notes.md 数据治理-准确性维度"
- **worked_faded**:
  - 完整示范: `df.groupby('treat')[['re74','re75','re78']].agg(['mean','median'])` + 解读"re75 均值高于中位数 ⇒ 右偏分布"
  - 部分填空: `df.groupby('treat')[['re75']].agg([____, ____])` (学生填 mean/median)
  - 独立解: 学生自行写一行 pandas 输出 treated 组 re78 的均值/中位数/标准差

### drill_id: D2
- **subskill**: S2
- **difficulty**: 3
- **reps_required**: 4
- **feedback_rule**: 用 `scipy.stats.ttest_ind(treated_re78, control_re78, equal_var=False)` 检验干预后消费差异; 必须同时报告 Cohen's d = (mean_t - mean_c) / pooled_sd; 若学生只报 p 值未报 d, 反馈"p 值只说有没有, d 才说多大--回到 notes.md 关键认知"; 若 d < 0.2 视为"小效应, 商业上需评估成本"
- **worked_faded**:
  - 完整示范: ttest_ind + 手算 Cohen's d + 解读 "p<0.05 但 d=0.12 ⇒ 统计显著但商业不显著"
  - 部分填空: 给 t 值和 pooled_sd, 学生补 d 公式
  - 独立解: 学生对 re78 做 t 检验 + Cohen's d, 写一句营销建议 (是否值得放量)

### drill_id: D3
- **subskill**: S2
- **difficulty**: 3
- **reps_required**: 3
- **feedback_rule**: 用 `scipy.stats.chi2_contingency` 检验 treat × marr (是否已婚) 独立性; 卡方检验前必须先 `pd.crosstab(df['treat'], df['marr'])` 看期望频数, 若任一格期望 <5 提示"Fisher 精确检验更稳"; 输出必须含 chi2 stat / p / dof / expected 四项
- **worked_faded**:
  - 完整示范: pd.crosstab → chi2_contingency → 解读"p>0.05 ⇒ 分组与婚姻状态独立, RCT 平衡"
  - 部分填空: 给 crosstab, 学生填 chi2_contingency 调用
  - 独立解: 学生对 treat × nodegree 做卡方检验并解读

### drill_id: D4
- **subskill**: S3
- **difficulty**: 4
- **reps_required**: 5
- **feedback_rule**: 用 `statsmodels.api.OLS` 拟合 re78 ~ treat + re75 + age + educ; 必须解读 treat 系数的业务含义 ("控制基线消费/年龄/教育后, 干预的净效应"); 若学生未放 re75 协变量, 反馈"re75 是预处理变量, 不放则混杂--回 notes.md CUPED 段"; 必须报告 R-squared 和 treat 的 95% CI
- **worked_faded**:
  - 完整示范: sm.OLS(y, sm.add_constant(X)).fit() + .summary() + 解读 treat 系数 + CI
  - 部分填空: 给 X 矩阵缺 re75 列, 学生补上
  - 独立解: 学生自选协变量集, 拟合 OLS, 写一段 200 字营销洞察

### drill_id: D5
- **subskill**: S3
- **difficulty**: 3
- **reps_required**: 3
- **feedback_rule**: 用 pandas 实现 RFM 五分群: R = 今天 - max(re75 日期代理), F = 消费频次 (re75>0 的月数), M = re75 总额; 用 `pd.qcut(..., 5)` 分桶; 必须输出 "Champions / Loyal / Potential / At-Risk / Lost" 五群人数与平均消费; 若学生用固定阈值 (如 R<30) 而非分位数, 反馈"用 qcut 让分群自适应分布"
- **worked_faded**:
  - 完整示范: 计算 R/F/M → qcut 分 5 档 → 拼成 RFM score → 映射 5 类
  - 部分填空: 给 R/F/M 列, 学生补 qcut 与映射逻辑
  - 独立解: 学生对 NSW 数据自建 RFM, 给每群写 1 条营销动作

---

## progressive_project (CS230 式渐进交付)

- **proposal** (Day1 课后 2 天): 选一个真实营销场景 (电商/内容/SaaS), 设计 AARRR 漏斗图 + 标注每阶段数据来源 + 声明你打算用 NSW 映射哪个阶段 (300 字)
- **milestone** (Day1 课后 5 天): 跑通 TODO1+TODO2+TODO4, 提交 NSW 营销映射的描述性 + t 检验结果 (notebook + 200 字解读)
- **final** (Day1 课后 9 天): 跑通全部 6 个 TODO, 提交完整 solution.ipynb + 300 字分析 (p 值/Cohen's d/OLS 系数/Champions 人数)
- **poster** (Day1 课后 12 天): 1 页 A4 海报, 含漏斗图 + RFM 分群柱状图 + OLS 系数表 + 3 条营销建议, 在小组 (3-4 人) 做 5 分钟 walkthrough

---

## interleaving (交叉排布, 不块状)

按 **A1B1C1 → B2C2A2 → C3A3B3** 交叉, 防止块状练习导致的"短期记忆假象":

- **A1** (S1 漏斗): D1 第 1 次 rep
- **B1** (S2 检验): D2 第 1 次 rep
- **C1** (S3 回归/RFM): D4 第 1 次 rep
- **B2** (S2 检验): D3 第 1 次 rep
- **C2** (S3 回归/RFM): D5 第 1 次 rep
- **A2** (S1 漏斗): D1 第 2 次 rep (换数据子集: 只看 marr=1)
- **C3** (S3 回归/RFM): D4 第 2 次 rep
- **A3** (S1 漏斗): D1 第 3 次 rep (换数据子集: 只看 nodegree=1)
- **B3** (S2 检验): D2 第 2 次 rep + D3 第 2 次 rep

理由: S1/S2/S3 三个子技能交替激活, 每次切换需重新加载任务上下文, 强化长期记忆与迁移。

---

## retry_policy (CS230 式)

- 全程 **10 个 free late days**, 用完才扣分
- 任一 drill 未达 reps_required **不扣分**, 可无限重试, 取最高分
- final 报告若被 reviewer 标"统计显著≠商业显著"错误, 必须重交 (这是本单元红线)

---

## weak_loop (弱项循环)

- 触发条件: 同一 subskill 连续 2 次失败 (如 D2 两次 rep 都漏报 Cohen's d)
- 处置: 自动回退到上一难度 drill + 补一个 worked example 重看
  - 例: D2 失败 2 次 → 回退 D1 (重做基线对比) → 重读 D2 worked_faded 第一阶段 → 再试 D2
- 退出条件: 该 subskill 连续 2 次成功, 方可继续 interleaving 序列
- 记录: 每次弱项循环写入 student_model.json 的 `weak_history` 字段 (见 tutorial.ipynb)
