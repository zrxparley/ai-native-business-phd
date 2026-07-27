# 刻意练习 · Day 5：规模实验与营销因果 (NSW + Thompson MAB + Uplift)

> v6.0 学习科学层. 实现 Ericsson 刻意练习 5 要素 + MIT 6.5940 渐退示例 (Worked-Faded) + ScholAstic 交叉练习 A1B1C1 interleaving 模式.

skill_target: 在 NSW 真实响应率数据上，独立完成"固定 A/B 基线 -> Thompson Sampling MAB -> CausalForestDML 异质效应 -> Uplift/Qini 增量决策"全链路，并解释探索-利用权衡与选择性停止陷阱。

subskills:
  - S1: 用 Thompson Sampling 在真实响应率上跑自适应分配，计算累计转化增益与实验成本节省
  - S2: 用 econml CausalForestDML 估计 CATE，识别"对培训/优惠券响应最大"的子群体并做安慰剂反驳检验
  - S3: 用 scikit-uplift 画 Qini 曲线，把用户分四类（persuadables / sure things / lost causes / sleeping dogs）并给出精准投放建议

## 诊断性先测 (3 道, 不超过 6 分钟)

1. NSW 数据中 `treat` 组 `re78>0` 比例为 0.42，对照组为 0.35。若用固定 A/B 在 5000 用户上跑，预期实验成本（被分到较差臂的损失）约为多少？
2. Thompson Sampling 为何在探索-利用上优于 ε-Greedy？请用一句"后验采样"原理解释。
3. CATE 估计告诉你"哪类用户响应最大"，但 Uplift Modeling 进一步把用户分四类。请列出四类并指出哪类是"真正该投放的"。

> 三题全对 → 直接进入 D2；任一题答错 → 从 D1 开始；两题以上错 → 先重读独立教材 §5.1-5.3。

## Drills (3 组, Worked -> Faded -> Independent)

### Drill D1: Thompson MAB on NSW

drill_id: D1
- difficulty: 2
- reps_required: 3
- feedback_rule: 若学生混淆"探索 vs 利用"或在 NSW 响应率上算错累计转化增益 → 反馈指向"Thompson Sampling 后验采样 = 自动平衡：不确定时上界高→探索，确定时均值大→利用" + 让其在 starter.ipynb TODO3 重跑一次并打印 regret 曲线
- worked_faded:
  - Worked (完整示范): 给定响应率 [0.35, 0.42]，演示 Beta(1,1) 先验 → 采样 → 更新 → 累计转化 vs 固定 A/B（代码 + 图）
  - Faded (部分填空): 给出 Beta 更新框架，学生填 `np.random.beta(a, b)` 采样行与后验更新 `a += reward` 行
  - Independent: 学生独立完成 starter.ipynb TODO3，对比固定 A/B 累计转化并解释为何 MAB 节省实验成本

### Drill D2: CATE + 安慰剂检验

drill_id: D2
- difficulty: 4
- reps_required: 3
- feedback_rule: 若学生在 CausalForestDML 上混淆 ATE/CATE，或安慰剂检验 p<0.05 不报告 → 反馈指向"ATE 是平均，CATE 是条件平均；安慰剂检验若显著说明混杂未控" + 让其重跑 TODO5 并写出效应大小而非仅 p 值
- worked_faded:
  - Worked: 用 NSW 数据跑 CausalForestDML，打印 feature_importance 找 top-3 调节变量（age/education/re75），画 CATE 分布直方图
  - Faded: 给出模型框架，学生填 `discrete_treatment=True` 与 `inference="statsmodels"` 参数，并填安慰剂检验循环
  - Independent: 学生独立完成 TODO4+TODO5，找出"响应最大"用户群特征，并写 100 字"为何这群人响应最大"的因果解释

### Drill D3: Uplift + Qini

drill_id: D3
- difficulty: 5
- reps_required: 3
- feedback_rule: 若学生把"必然转化(sure things)"也投券 → 反馈指向"Uplift 四类：persuadables 才该投；sure things 投了浪费，sleeping dogs 投了有害" + 让其在 Qini 曲线上指出"拐点前 30% 用户"的增量贡献
- worked_faded:
  - Worked: 用 scikit-uplift `SoloModel` + CausalForestDML 的 CATE 预测，画 Qini 曲线，标注 persuadables 区段
  - Faded: 给出 Qini 计算框架，学生填累计增量 `np.cumsum` 与随机基线对比行
  - Independent: 学生独立完成 TODO6（可选 Uplift 扩展），在 300 字分析中给出"按 CATE 高到低投前 30% 用户的增量转化"数字

## 渐进式项目脚手架 (Progressive Project)

- M1 (Day 5 当堂): 完成 D1 - 在真实响应率上跑 Thompson MAB，输出累计转化对比图
- M2 (Day 5 课后 3 天): 完成 D2 - CATE 估计 + 安慰剂检验 + 100 字因果解释
- M3 (Day 5 课后 7 天): 完成 D3 - Qini 曲线 + 精准投放建议 300 字
- M4 (技能3 结业): 把 NSW 综合案例的"数据→因果→决策"流程迁移到自选营销场景（如 DCO 创意优化或定价实验）

## 交叉练习 (Interleaving - A1B1C1 而非块状)

不要把所有 MAB 题一次性做完再做 CATE 题。按以下交叉排布：

```
A1: Thompson MAB 单步采样 (D1 第1次)
B1: CATE 单棵树拟合 + feature importance (D2 第1次)
C1: Uplift 四类用户分类 (D3 第1次)
A2: Thompson MAB regret 曲线绘制 (D1 第2次)
B2: CATE 安慰剂检验 (D2 第2次)
C2: Qini 曲线单点计算 (D3 第2次)
A3: Thompson MAB 实验成本节省定量 (D1 第3次)
B3: CATE 因果解释 100 字 (D2 第3次)
C3: Uplift 精准投放建议 300 字 (D3 第3次)
```

明文模式: A1B1C1 → A2B2C2 → A3B3C3。每轮跨子技能，强制检索切换，避免块状练习的假性掌握。这是 interleaving 交叉练习的核心。

## 弱项循环 (Weak Loop)

连续 2 次在同一 drill 失败 → 触发 weak_loop：
1. 回退到上一 difficulty（D3→D2, D2→D1）
2. 补充一个 worked example（完整示范版）让学生重读
3. 在 student_model.json 标记 `weak_drill: <Dn>`，下次 tutorial 优先追问该点
4. 通过该 drill 后追加 1 次 cross-skill interleaving（与前一 drill 交叉一次）再进入下一 drill

```
if drill_fail_count(drill_id) >= 2:
    go_back(prev_drill)
    show_worked_example(prev_drill)
    student_model["weak_drill"] = drill_id
    if pass(drill_id):
        do_one_interleaving_with(prev_drill)
        advance(next_drill)
```

## retry_policy

- 每个 drill 最多重试 3 次/天（限频防依赖，参考 CS230 late-day 与 NUS autograder 即时反馈）
- 跨日累计失败 5 次 → 触发 1:1 tutorial（tutorial.ipynb cell 6 exit 流程）
- 重试时 feedback_rule 升级：第1次失败给 hint，第2次给 worked example 指引，第3次给完整 worked example

---

*本 practice.md 实现 Ericsson 刻意练习 5 要素 + MIT 6.5940 渐退示例 (Worked-Faded) + ScholAstic 交叉练习 A1B1C1 interleaving 模式。*
