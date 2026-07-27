# Day 3 刻意练习：营销 Agent 评估套件设计 (v6.0 学习科学层)

> 配套 v5.0 `notes.md` / `starter.ipynb` / `solution.ipynb`。本文件用 Ericsson 刻意练习 + MIT CS229 pset0 先测 + Harvard/Stanford Worked-Faded 示例 + CS230 渐进项目 + 交叉 interleaving 重构 Day 3 的练习路径。所有 drill 的 feedback_rule **领域特定**：引用 deepeval 的 GEval / FaithfulnessMetric / BaseMetric / AgentBench / 营销Agent六大指标。

---

## skill_target

**核心可观察技能**：给定一个营销内容生成 Agent（小红书种草文案/朋友圈广告），能用 deepeval 框架独立搭建一个可纳入 CI 的评测套件，包含 (1) >=3 条 LLMTestCase 含真实轨迹；(2) 用 GEval 做 LLM-as-a-judge 端到端质量打分；(3) 用自定义 BaseMetric 做轨迹级工具调用准确率评估；(4) 用 FaithfulnessMetric 检测幻觉；(5) 用 evaluate() 跑出任务完成率/工具准确率/幻觉率三大指标。可评估标准：套件能跑通且三大指标数字合理（不是 0 或 100）+ 给出根因诊断。

---

## diagnostic（先测，CS229 pset0 式，3 题，探先验缺口）

> 答错任意 1 题 = 该子技能进入 weak_loop。答题前不看 notes.md / solution.ipynb。

**D1（非确定性 vs 断言）**：你给营销 Agent 同一个 Brief（"烟酰胺精华液，小红书种草"）跑了 3 次得到 3 段不同文案，传统 `assert output == expected` 会怎样？为什么 Agent 评估不能用纯相等断言？请用一句话回答，并指出温度/上下文/模型版本中哪个变量最致命。

**D2（轨迹 vs 端到端定位）**：下面是一条 Agent 轨迹：`Thought1(该搜知识库) -> Action1(调 search) -> Obs1(空) -> Thought2(没搜到，直接编) -> Action2(生成文案，虚构"含5%烟酰胺") -> 最终输出`。最终输出文字流畅、CTA 明确，端到端 GEval 打 0.82。请问：(a) 端到端评估会发现这个错误吗？(b) 轨迹评估应该在哪一步报警？(c) 这是幻觉还是工具选择错误？

**D3（指标计算）**：你跑了 100 条 LLMTestCase，其中 88 条任务完成、9 条工具选错、6 条有幻觉（部分重叠）。任务完成率/工具调用准确率/幻觉率分别是多少？这三个数字能直接相加吗？为什么？（提示：因果阶梯 L1 关联 vs L2 干预）

---

## subskills（拆 3 个子技能）

- **S1 端到端评估子技能**：用 GEval + criteria 描述（品牌调性/CTA/平台适配）对营销文案做 LLM-as-a-judge 打分；理解 LLM-as-judge 三大偏差（偏好长答案/位置偏差/自我偏好）并设计对照。
- **S2 轨迹评估子技能**：继承 BaseMetric 实现 `ToolCallCorrectnessMetric`，对 trajectory 中每一步评估 (a) 工具选择是否正确（该搜知识库时有没有调 search）(b) 参数是否准确 (c) 是否冗余调用；输出 score + reason。
- **S3 幻觉+综合指标子技能**：用 FaithfulnessMetric 检测营销文案是否虚构成分/功效（违反广告法），用 evaluate() 批量运行得到任务完成率/工具准确率/幻觉率，并对照 AgentBench/SWE-bench 等学术基准定位自己的 Agent 水平。

---

## drills（>=3 个，每个含 drill_id/difficulty/reps_required/feedback_rule/worked_faded 三阶段）

### drill_id: D1-GEval
- **difficulty**: 3
- **reps_required**: 4
- **目标子技能**: S1
- **任务**: 给定 3 条营销文案（小红书烟酰胺种草/朋友圈口红广告/小红书防晒霜），写一段 GEval criteria（含品牌调性+CTA+平台适配三维度），让 LLM-as-judge 自动打分。需输出 score(0-1) + reason。
- **worked_faded**:
  - **阶段1 完整示范 (Worked)**：参考 solution.ipynb TODO2，criteria 写法 = `"评估小红书种草文案质量。维度1：品牌调性是否一致（轻松/科学）；维度2：CTA 是否明确（评论/收藏/点击）；维度3：平台适配（emoji/标题党/字数 100-300）。打分 0-1，给理由。"`，`GEval(criteria=..., evaluation_params=[EvaluationParam.ACTUAL_OUTPUT, EvaluationParam.EXPECTED_OUTPUT])`。
  - **阶段2 部分填空 (Faded)**：给出 criteria 骨架但留 3 个 `<FILL>`（CTA 维度/平台维度/scoring 量纲），学生填。
  - **阶段3 独立解 (Independent)**：换一个渠道（B站/抖音），从零写 criteria 并解释为什么这个 criteria 不会触发 LLM-as-judge 的"偏好长答案"偏差。
- **feedback_rule**: 跑 `deepeval test run`，若 score 全 =1.0 或全 =0.0 → 判定 criteria 过松/过紧，回退阶段1；若 reason 包含"good"/"nice" 等空洞词 → 触发 LLM-as-judge 自我偏好自检（对照 reading.md 偏差清单）；若同 Brief 跑 3 次 score 方差 >0.15 → 判定温度过高，要求学生标注不确定性。

### drill_id: D2-Trajectory
- **difficulty**: 4
- **reps_required**: 5
- **目标子技能**: S2
- **任务**: 继承 BaseMetric 实现 `ToolCallCorrectnessMetric`，输入 trajectory（List[{thought, action, observation}]），输出工具选择/参数/冗余三子分 + 综合 score。
- **worked_faded**:
  - **阶段1 Worked**：参考 solution.ipynb TODO3，`class ToolCallCorrectnessMetric(BaseMetric)` 实现 `measure(test_case)`，遍历 `test_case._trajectory`，对照 `expected_tools` 字典逐步打分。
  - **阶段2 Faded**：给出类骨架但 `measure` 方法体留 5 个 `<FILL>`（遍历/对照/扣分/累加/返回 reason），学生填。
  - **阶段3 Independent**：扩展支持"参数准确性"子分（不只看工具名对不对，还看参数 dict 是否含必填字段），并解释为什么 AgentBench 8 个场景里 OS/DB 场景对参数评估更严。
- **feedback_rule**: 用 starter.ipynb 用例2（朋友圈口红，工具选错+虚构成分）跑测，若 score >0.7 → 判定 BaseMetric 漏检（应触发 weak_loop 回退阶段1）；若 reason 没指出"该调 search 却直接生成" → 判定推理链缺失，要求学生重写 measure 的 reason 模板；若参数子分恒 =1 → 判定 expected_tools schema 过松。

### drill_id: D3-Faithfulness
- **difficulty**: 3
- **reps_required**: 4
- **目标子技能**: S3
- **任务**: 用 FaithfulnessMetric 检测 3 条营销文案是否虚构成分/功效（"含5%烟酰胺"" SPF50+"等），并写一段 300 字根因分析：幻觉来自检索失败（retrieval_context 空）还是生成阶段编造？
- **worked_faded**:
  - **阶段1 Worked**：参考 solution.ipynb TODO4，`FaithfulnessMetric(threshold=0.7)`，`LLMTestCase(input=..., actual_output=文案, retrieval_context=[知识库片段])`，跑 `assert_test`。
  - **阶段2 Faded**：给 3 条文案但 retrieval_context 留 `<FILL>`，学生判断每条该填什么知识库片段才能让 FaithfulnessMetric 通过。
  - **阶段3 Independent**：设计一个对抗性用例（知识库不存在的问题，比如"这款精华能治痘痘吗"），观察 Agent 是否"不知道说不知道"，并解释这对应因果阶梯 L1 还是 L2。
- **feedback_rule**: 若用例1（好轨迹）FaithfulnessMetric 报警 → 判定 retrieval_context 拼接错误，回退阶段1；若用例2（虚构"含5%烟酰胺"）通过 → 判定 threshold 过低，要求调到 0.8 重测；若所有用例 score 一致 → 判定学生没区分"检索失败"和"生成编造"两类幻觉，触发 weak_loop。

### drill_id: D4-EvalBatch
- **difficulty**: 5
- **reps_required**: 3
- **目标子技能**: S1+S2+S3 综合
- **任务**: 用 `evaluate([test_case1, test_case2, test_case3], metrics=[geval, tool_metric, faith_metric])` 批量跑，输出三大指标（任务完成率/工具准确率/幻觉率），并对照 AgentBench 报告里 LLM-X 的水平定位自己的 Agent。
- **worked_faded**:
  - **阶段1 Worked**：参考 solution.ipynb TODO6，组装 metrics list，跑 evaluate，从结果对象抽 score。
  - **阶段2 Faded**：给 evaluate 调用骨架但 metrics list 留 `<FILL>`，学生组装顺序。
  - **阶段3 Independent**：写一段 300 字根因：你的营销 Agent 在哪个评估维度最差？根因是工具选择/参数/推理/幻觉？给出 1 条改进建议并预测改进后哪个指标会变（自评因果链）。
- **feedback_rule**: 若任务完成率=100% → 判定测试集过易（无对抗性用例），要求加 1 条模糊指令用例；若工具准确率 <60% → 判定 Agent 工具路由层有问题（不是评估层问题），引导学生回 Day 2 复习工具选择 prompt；若三大指标数字无法对齐 AgentBench 报告 → 判定学生没读懂 AgentBench 8 场景与自己营销场景的差异。

---

## progressive_project（CS230 式 proposal → milestone → final → poster）

- **Proposal (Day 3 当晚)**：选 1 个真实营销 Agent（自己 Day 2 搭的 or 公开 demo），写 1 页 proposal：(a) 评估什么（端到端/轨迹/幻觉）；(b) 用哪些 deepeval 组件；(c) 测试集规模（>=10 条 LLMTestCase）；(d) 预期三大指标数字。
- **Milestone (Day 4 课前)**：提交 `starter.ipynb` 完成的 6 个 TODO + 3 条 LLMTestCase + GEval/ToolCall/Faithfulness 三 metric 跑通的最小可运行版本。
- **Final (Day 5 课前)**：提交 evaluate() 批量结果（>=10 条用例）+ 300 字根因分析 + 1 条改进建议 + 改进前后对比数字。
- **Poster (Day 5 课上 2 分钟)**：1 张 slide，标题="我的营销 Agent 在 ___ 维度最差，根因是 ___，改进后 ___ 指标从 X 提升到 Y"。

---

## interleaving（交叉排布，不块状）

不要把 D1 跑 4 遍再跑 D2——这会形成块状肌肉记忆，迁移性差。按以下 A1B1C1...B2C2A2...C3A3B3 顺序交叉（A=D1-GEval, B=D2-Trajectory, C=D3-Faithfulness, D=D4-EvalBatch）：

```
Day3 晚:  A1 → B1 → C1
Day4 早:  B2 → C2 → A2
Day4 晚:  C3 → A3 → B3 → D1
Day5 早:  D2 → D3 (综合收尾)
```

每个 session 只跑 1 个 drill 的 1 次 rep，不连续跑同 drill 2 次。间隔中穿插 reading.md 的 LLM-as-a-judge / AgentBench 论文阅读。

---

## retry_policy（CS230 式，失败重试不罚分）

- **10 free late days**：整个技能5 跨 Day 1-5 共 10 天免费迟到额度，用完才开始扣分。
- **drill 失败重试不罚分**：每次 rep 跑 `deepeval test run` 失败（score 不达标 / assert_test 报错）不计入扣分，但必须附 1 段失败根因（哪一步错 / 为什么 / 下次怎么改）。
- **plagiarism 红线**：直接抄 solution.ipynb 的 criteria 字符串 = 0 分；必须用自己的话写 criteria。
- **mastery 门槛**：4 个 drill 各达到阶段3 独立解 + 三大指标数字合理（非 0/100）= mastery 通过。

---

## weak_loop（连续 2 次失败触发弱项循环）

判定规则：同一 drill 连续 2 次 rep 都 FAIL（score 不达标 / feedback_rule 触发回退）→ 自动进入 weak_loop：

1. **回退**：强制回到该 drill 的阶段1（Worked 完整示范），重新抄一遍参考答案并用自己的话复述。
2. **补充 worked example**：从 solution.ipynb 抽 1 条额外的 worked example（不是当前 drill 的那条），对照阅读。
3. **诊断盲点**：写 1 段"我为什么卡住"——是 deepeval API 不熟？还是轨迹评估概念没懂？还是 LLM-as-judge 偏差没识别？
4. **重做**：重新跑阶段2（Faded），通过后再回阶段3。
5. **退出条件**：阶段3 独立解连续 2 次 PASS 才退出 weak_loop。

weak_loop 触发不扣分，但必须在 progressive_project 的 Milestone 提交前退出，否则 Milestone 延期用 late days。

---

*v6.0 学习科学层：刻意练习 (Ericsson) + Worked-Faded (Harvard/Stanford) + 交叉 interleaving (MIT CS229) + CS230 渐进项目 + 弱项循环。领域特定 feedback_rule 引用 deepeval / GEval / FaithfulnessMetric / BaseMetric / AgentBench。*
