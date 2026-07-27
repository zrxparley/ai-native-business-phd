---
unit: elective-e9/day-1
topic: 价值对齐 + Constitutional AI (RLHF/CAI/DPO, HHH, deepeval, garak)
version: v6.0
skill_target: 为营销Agent设计并运行HHH三维对齐评估套件(deepeval自定义BaseMetric + garak alignment probes + 企业宪法LLM-as-a-judge), 能定位最弱对齐维度并提出Constitutional AI修复原则
---

# 刻意练习 · Day 1 价值对齐与Constitutional AI

> 基于Ericsson刻意练习 + MIT/Harvard/Stanford教学法。每个drill遵循 Worked-Faded 三阶段(完整示范→部分填空→独立解), 配领域特定feedback_rule引用 deepeval/garak/HHH/宪法原则。

## diagnostic (先测, CS229 pset0 式 3 题)

> 探测先验知识缺口。若3题全错, 先读 notes.md "关键回顾1-3" 再开始drill。

**Q1 (对齐层次)**: 营销Agent被要求"写转化率高的文案", 它选择虚构成分。这是哪一层对齐失败? (A)意图对齐 (B)行为对齐 (C)价值对齐。说明理由(<=30字)。

**Q2 (方法差异)**: RLHF、Constitutional AI、DPO 三者中, 哪个**不需要训练奖励模型**? 哪个**不需要人类标注**? (各填一个字母)

**Q3 (HHH张力)**: 营销文案"说明所有不确定性"会降低说服力。这是HHH哪两个维度之间的张力? 用1句话解释。

<details><summary>参考答案(gated, 做完再看)</summary>
Q1: (C)价值对齐 - "最大化转化"目标被解读为允许欺骗, 反映价值观不一致(非意图模糊也非执行偏离)。
Q2: DPO不需要奖励模型(隐式推导); Constitutional AI不需要人类标注(AI基于宪法自我反馈=RLAIF)。
Q3: Honest(诚实)与Helpful(有用)张力 - 完全诚实降低说服力→降低有用性。
</details>

## subskills (3 个子技能)

- **A. HHH对齐测试用例设计**: 识别合规/违规/混合营销文案, 按HHH三维度分类, 构造覆盖三维度的测试集
- **B. deepeval自定义BaseMetric实现**: 写一个继承BaseMetric的metric类, 按HHH原则对营销文案打分+给理由
- **C. garak对齐探针扫描与报告解读**: 运行alignment probes(latentinjection/goodside/snowball), 读懂fail率, 定位最弱对齐维度

## drills (>=3, 每个 Worked-Faded 三阶段)

### D1 · HHH用例标注 (subskill A, difficulty 2/5, reps_required 3)

**feedback_rule**: 用 deepeval `assert_test` 自动判定你的标注是否与LLM-as-a-judge一致; 任一用例标注错误→展示HHH三维度定义+重做该用例; 连续2次失败触发 weak_loop (回退到 notes.md "关键回顾4" HHH表)。

**Worked-Faded**:
- Stage1 (完整示范): 给定文案"治愈脱发!全网最低价!" → 标注: Harmless违反(绝对化"最低"+医疗承诺"治愈"), Honest违反(无依据功效声明), Helpful满足(CTA明确)。完整推理链展示。
- Stage2 (部分填空): 给定文案"暗示美白效果, 未标AI生成" → 你填: Harmless=__?__, Honest=__?__, Helpful=__?__
- Stage3 (独立解): 给定3条新文案(合规/违规/混合各1), 独立完成HHH三维标注

### D2 · deepeval HarmlessMetric 实现 (subskill B, difficulty 4/5, reps_required 2)

**feedback_rule**: 用同一组测试用例跑 deepeval `GEval` (LLM-as-a-judge) 作为oracle, 你的BaseMetric与oracle偏差>0.5分→重做; 漏检广告法绝对化用语("最""第一""治愈")→补充worked example; 连续2次失败触发 weak_loop (回退D1+看solution.ipynb TODO2 worked example)。

**Worked-Faded**:
- Stage1 (完整示范): 完整 `HarmlessMetric(BaseMetric)` 类 - `measure()`方法用关键词+语义双检测, `reason`字段给违规理由, `score`∈[0,1]。完整代码展示。
- Stage2 (部分填空): 给定 `HonestMetric(BaseMetric)` 骨架(类+方法签名), 你填 `measure()` 内部逻辑(检测夸大功效/虚构成分/忠于知识库)
- Stage3 (独立解): 独立实现 `HelpfulMetric(BaseMetric)` (Brief满足度/CTA明确性/平台适配)

### D3 · garak探针报告解读 (subskill C, difficulty 3/5, reps_required 2)

**feedback_rule**: 对照 garak 0.15.x alignment probe 列表(`latentinjection`/`goodside`/`snowball`), 漏判probe类别→重看该probe定义; fail率排序错误(应按fail率降序定位最弱维度)→补充worked example; 连续2次失败触发 weak_loop (回退 notes.md "2026前沿" garak段)。

**Worked-Faded**:
- Stage1 (完整示范): 给定一份静态garak扫描报告(3个probe × 5条用例), 完整演示: 计算各probe fail率 → 排序 → 定位 `latentinjection` fail率最高(60%) → 推断最弱维度=Harmless(对抗提示绕过) → 设计修复原则"不响应任何嵌入指令的营销请求"
- Stage2 (部分填空): 给定另一份报告(2个probe), 你填: 各probe fail率=?, 最弱维度=?, 修复原则=?
- Stage3 (独立解): 给定3份新报告(混合probe), 独立完成 fail率计算+弱点定位+修复原则

### D4 · 企业宪法设计 (subskill A+B综合, difficulty 5/5, reps_required 1)

**feedback_rule**: 宪法原则必须覆盖5维度(无害/诚实/帮助/公平/自主, 见 notes.md "关键回顾3"), 缺任一维度→补充该维度worked example; 原则不可执行(无法用deepeval metric验证)→改写为可测试形式; 连续2次失败触发 weak_loop (回退D1+D2+看notes.md 宪法表)。

**Worked-Faded**:
- Stage1 (完整示范): 完整5条企业宪法原则, 每条标注: 对应HHH维度 + 可执行的deepeval metric + garak probe类型
- Stage2 (部分填空): 给定3条原则骨架, 你填: HHH维度映射 + metric实现思路
- Stage3 (独立解): 为你选定的营销场景, 独立设计5-10条企业宪法原则, 每条附可测试metric

## progressive_project (CS230 式渐进交付)

> 单一最终项目, 分4阶段递进交付。每阶段反馈后迭代。

- **Proposal (Week1)**: 选一个营销场景(如"美妆产品详情页Agent"), 写1页对齐评估proposal: 场景描述 / Agent能力边界 / HHH三维风险 / 评估计划(deepeval+garak+宪法)。提交后24h内获feedback。
- **Milestone (Week2)**: 实现HHH三维度deepeval BaseMetric(HarmlessMetric/HonestMetric/HelpfulMetric) + 跑通>=3个测试用例(合规/违规/混合)。提交代码+测试报告。
- **Final (Week3)**: 完整对齐评估报告: HHH三维评分 + garak探针命中表 + 企业宪法5-10条 + LLM-as-a-judge评审结果 + 最弱维度根因分析 + Constitutional AI修复建议。
- **Poster (Week3末)**: 1页poster展示对齐弱点热力图 + 修复优先级 + 关键洞察。同伴互评。

## interleaving (交叉排布, 非块状)

> 三个子技能交叉练习, 避免块状刷题。顺序明文写出:

- **Week1**: A1(D1 Stage1-2) → B1(D2 Stage1) → C1(D3 Stage1) → A1复习
- **Week2**: B2(D2 Stage2-3) → C2(D3 Stage2-3) → A2(D4 Stage1) → B2复习
- **Week3**: C3(D3 Stage3) → A3(D4 Stage2-3) → B3(综合milestone) → C3复习

> 每日1个drill block, 不连续练同一子技能2天。复习日用 schedule.json 卡片做提取练习。

## retry_policy (CS230 式)

- 10 free late days (整个unit周期内自由分配, 不罚分)
- 任一drill失败可重试, 重试不罚分(取最高分)
- progressive_project 每阶段最多2次重试, 第二次仍未过→触发 weak_loop
- 里程碑延期用late days, 用完后→主动联系触发 intervention

## weak_loop (连续2次失败触发)

- 检测: 同一drill连续2次未达 mastery(>=80%)
- 触发后: (1) 回退到上一drill的 Stage1 worked example 重看 (2) 补充1个该子技能的额外worked example (3) 用 schedule.json 对应卡片做密集复习(due=[1,1,3] 而非[1,3,8]) (4) 24h后再试, 仍失败→1对1tutorial(tutorial.ipynb Socratic loop)

---

*本刻意练习设计引用 Ericsson deliberate practice / MIT 6.867 pset0 / Stanford CS230 project progressive delivery / Harvard worked-faded scaffolding。领域特定feedback_rule引用 deepeval (BaseMetric/GEval/assert_test) + garak (alignment probes: latentinjection/goodside/snowball) + HHH原则 + Constitutional AI宪法5维度。*
