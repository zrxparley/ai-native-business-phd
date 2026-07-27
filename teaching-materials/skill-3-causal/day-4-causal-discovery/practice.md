# 刻意练习 - Day 4 因果发现 (Ericsson + MIT Worked-Faded)

## skill_target
能在真实数据（sklearn糖尿病 / NSW）上独立完成「PC/NOTEARS 因果发现 + 因果森林 CATE 估计 + LLM 因果图融合」全流程，并解读结果的因果含义与统计可靠性。

## diagnostic (前测诊断, 3 道, 检测先验掌握度)
1. 给定糖尿病 10 变量相关性矩阵，凭直觉画出 3 条因果边并标注方向假设依据。→ 暴露"相关≠因果"直觉偏误
2. NSW 数据中 treat 与 re78 的相关系数是否等于 ATE？为什么？→ 检测混杂偏差理解
3. 若 LLM 说"BMI 导致血压升高"，你如何用数据驱动方法验证或反驳？→ 检测 LLM+数据融合思维

## subskills
- S1: PC/FCI 因果发现（条件独立性检验 + v-结构定向 + 隐混杂 PAG 边类型）
- S2: NOTEARS 连续优化因果发现（矩阵指数 trace 约束 + 阈值截断 + 收敛诊断）
- S3: 因果森林 CausalForestDML 异质处理效应估计 + LLM 因果图融合交叉验证

## drills

drill_id: D1
difficulty: 3
reps_required: 3
feedback_rule: 若学生在 sklearn 糖尿病数据上跑 PC 后无法解读"无向边 vs 有向边"含义 → 反馈"无向边=方向未定（v-结构未触发），有向边=数据支持的方向。请指出哪条边触发 v-结构 X->Z<-Y 并列出条件集 S"。若误把无向边当因果方向 → 让其列举条件集 S，重算条件独立性。若忽略因果充分性假设 → 提示"糖尿病数据可能有隐混杂（age/genetics），PC 假设无隐混杂，FCI 放宽此假设"。
worked_faded:
  - 完整示范 (worked): 用 gumbel 模拟 3 节点链 A->B->C，展示 PC 如何通过两步独立性检验删除 A-C 边并定向，含完整代码+图示
  - 部分填空 (faded): 给定糖尿病数据加载代码 + PC 调用骨架，学生填 `pc()` 参数与 `graph.draw_pydot()` 调用
  - 独立解: 学生独立在 NSW 前 5 变量上跑 PC 并写 300 字解读（哪条边最符合直觉？哪条最反直觉？）

drill_id: D2
difficulty: 4
reps_required: 3
feedback_rule: 若学生把 NOTEARS 输出 W 矩阵直接当因果图 → 反馈"NOTEARS 输出权重矩阵 W，需设阈值 λ 截断弱边（如 |W|<0.1 置零）才得到稀疏 DAG。请重画截断后的图"。若忽略 DAG 约束 tr(e^{W∘W})-d=0 未收敛 → 让其打印该约束值，若 >1e-3 说明未收敛需增 max_iter。若假设非线性关系却用 NOTEARS-Linear → 提示改用 NOTEARS-MLP。
worked_faded:
  - 完整示范 (worked): 3 节点线性 NOTEARS 完整代码 + W 矩阵可视化 + 收敛诊断输出
  - 部分填空 (faded): 给定 NOTEARS 骨架，学生填 `notears_linear()` 调用 + 阈值截断 + DAG 约束验证
  - 独立解: 在糖尿病数据上跑 NOTEARS 并与 PC 结果对比，写 1 段差异分析（哪条边两者一致？哪条不一致？为什么？）

drill_id: D3
difficulty: 5
reps_required: 3
feedback_rule: 若学生只看 CausalForestDML 的 `feature_importances_` 而不看 CATE 分布 → 反馈"特征重要性只告诉你'谁驱动异质性'，不告诉你'效应大小方向'。请画 CATE 直方图 + 按特征分组的 boxplot"。若 LLM 因果图与数据驱动结果冲突时直接信 LLM → 引用 Kiciman 2023 警告"LLM 可能幻觉因果边"，强制要求交叉验证：列出 LLM 独有边、PC 独有边、两者一致边三类。若不做置换检验 → 提示"shuffle treatment labels 重跑因果森林，feature_importances_ 应不稳定"。
worked_faded:
  - 完整示范 (worked): NSW 因果森林完整流程（CausalForestDML 拟合 + CATE 分布 + 特征重要性 + 置换检验）
  - 部分填空 (faded): 给定拟合代码，学生填 `effect_intervals()` 调用 + LLM 因果图对比 + 3 类边分类
  - 独立解: 在糖尿病+NSW 组合上完成"LLM 候选图→PC 验证→NOTEARS 修正→因果森林 CATE"全流程

## progressive_project (渐进式项目, 参考 Imperial MSc BA Consulting Project)
- Milestone 1 (Day 4 当天): 完成 D1+D2，提交糖尿病数据上 PC 与 NOTEARS 对比报告（300 字）
- Milestone 2 (Day 5 前): 完成 D3，提交 NSW 因果森林 CATE 分析 + LLM 因果图融合报告
- Milestone 3 (Day 7): 整合 3 个 drill，提交"因果发现→CATE→营销投放策略"端到端 case study

## interleaving (交叉练习, A1B1C1...B2C2A2...C3A3B3 明文排布)
不按块状练习，而是交叉排布以强化长期保持（Butler 2010 检索练习证据，MIT Open Learning 明文原则）：
- A = PC 因果发现, B = NOTEARS, C = 因果森林 + LLM 融合
- 第 1 轮: A1(糖尿病 PC) → B1(糖尿病 NOTEARS) → C1(NSW 因果森林)
- 第 2 轮: B2(NSW NOTEARS 对比) → C2(糖尿病 CATE) → A2(NSW PC)
- 第 3 轮: C3(LLM+数据融合) → A3(FCI 隐混杂) → B3(NOTEARS-MLP 非线性)
- 每轮间隔 1 天，强化跨子技能迁移，避免块状练习的短期记忆假象

## retry_policy
- 每个 drill 允许最多 2 次重试，每次重试必须先看 worked example 再重做
- 累计 3 次 drill 失败 → 触发弱项循环
- late submission: 参考 Stanford CS230 政策，每天扣 20% 分数，最多 3 天

## weak_loop (弱项循环)
连续 2 次同一 drill 失败触发：
1. 回退到上一 drill（D3 失败→回 D2，D2 失败→回 D1）
2. 重看该 drill 的 worked example 完整版
3. 完成 1 道补充 worked example（faded 级别）
4. 通过后才重试原 drill
5. 记录到 tutorial.ipynb 的 student_model.json 的 `weak_concepts` 字段，跨单元复用
