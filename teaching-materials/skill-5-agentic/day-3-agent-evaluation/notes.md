# 技能5 · Day 3：Agent评估与Benchmarking · 讲义（v5.0 学习材料包版）

> **所属**：AI原生化商业博士 · 技能5 Agentic系统工程与落地 · Day 3
> **版本**：v5.0（从独立教材升级为学习材料包）
> **预计**：2h 讲义 + 2h 上机练习
> **核心命题**：Agent系统非确定性、多步推理、工具调用--如何科学评估它"好不好"？
> **v5.0 升级点**：① 新增真实库上机（deepeval）② 新增 TODO 填空式起始笔记本 ③ Notebook 化 ④ 深链阅读 ⑤ 2026 前沿（LLM-as-a-judge + deepeval 可运行评测框架）

---

## 学习目标（学完你能做到）

1. 能解释 Agent 评估与传统软件测试的根本差异（非确定性、多步推理、工具调用、长尾效应），并说明为什么传统断言式测试在 Agent 上失效
2. 能区分**轨迹评估**（Trajectory Evaluation）与**端到端评估**（End-to-End Evaluation），并指出各自适合的营销 Agent 场景
3. 能用 **deepeval** 框架为营销 Agent 搭建可运行的评测套件：定义测试用例（LLMTestCase）、用 GEval 做 LLM-as-a-judge 自动评分、用 FaithfulnessMetric 检测幻觉
4. 能设计营销 Agent 的核心评估指标：任务完成率、工具调用准确率、幻觉率，并用 deepeval 的 `evaluate()` 批量运行并汇总
5. 能用自定义 BaseMetric 实现轨迹级评估（工具选择是否正确、参数是否准确），把"人工抽检"变成"CI 可运行的自动测试"

---

## 理论部分：精炼索引（详见独立教材）

> Day 3 的完整理论讲义见 [`../../AI原生化商业博士_独立教材_技能5_Agentic系统工程与落地.md` § Day 3](../../AI原生化商业博士_独立教材_技能5_Agentic系统工程与落地.md)（3.3.1–3.3.6 节，已包含评估挑战/方法论/AgentBench/指标设计/Langfuse可观测性）。本讲义不重复，仅做上机所需的关键回顾。

### 关键回顾 1：Agent 评估的四大挑战

| 挑战 | 传统测试假设 | Agent 现实 | 后果 |
|:----:|------------|-----------|------|
| 非确定性 | 输入A必然得到输出B | 同一输入可能不同输出（温度/上下文/模型版本） | 断言式测试失效 |
| 多步推理 | 只看最终结果 | 推理过程可能错误但碰巧答对 | 结果对≠过程对 |
| 工具调用 | 无此维度 | 要评估选对工具、参数正确、无冗余调用 | 新增评估维度 |
| 长尾效应 | 采样足够即可 | 95% OK 但 5% 完全失控 | 需要对抗性测试 |

**核心洞察**：Agent 评估不能只看"答案对不对"，必须评估"过程好不好"--这是轨迹评估存在的根本原因。

### 关键回顾 2：轨迹评估 vs 端到端评估

```
端到端评估（End-to-End）：
  用户输入 -> [Agent 黑盒] -> 最终输出 -> 对比期望输出 -> 对/错

轨迹评估（Trajectory）：
  用户输入 -> Thought1 -> Action1(工具A, 参数x) -> Obs1 -> Thought2 -> Action2(工具B) -> Obs2 -> 最终输出
                    ↑               ↑                              ↑
              推理合理？        工具选对？参数对？              步骤冗余？
```

| 维度 | 端到端评估 | 轨迹评估 |
|------|----------|---------|
| 评估对象 | 最终输出 | 完整执行轨迹 |
| 粒度 | 粗 | 细 |
| 成本 | 低 | 高（需标注或LLM-as-judge） |
| 发现问题 | 答案错 | 哪一步错、为什么错 |
| 营销场景 | 内容是否符合Brief | 是否选对工具、推理链是否合理 |

**实践建议**：两层都要--端到端做基础门禁，轨迹做深度诊断。

### 关键回顾 3：AgentBench 等评估框架

**AgentBench**（arXiv: 2308.03688）是清华等机构提出的综合 Agent 能力评估框架，覆盖8个场景（操作系统/数据库/知识图谱/卡牌游戏/横向思维/家务/网页购物/网页浏览），提供标准化基准来比较不同 LLM 作为 Agent backbone 的能力。

其他重要框架：
- **SWE-bench**（arXiv 2310.06770）：软件工程能力（修真实 GitHub issue）
- **WebArena**（arXiv 2307.13854）：网页交互能力
- **GAIA**（arXiv 2311.12983）：通用AI助手能力

> ⚠️ AgentBench/SWE-bench 是**学术 benchmark**，用于横向比较模型能力。你的营销 Agent 评估需要**自建测试集**（收集50-100个真实营销Brief），用 deepeval 框架运行--这是今天上机的核心。

### 关键回顾 4：营销 Agent 的六大评估指标

| 指标 | 定义 | 营销 Agent 目标 |
|------|------|----------------|
| 任务完成率 | 成功完成的测试用例比例 | ≥ 85% |
| 工具调用准确率 | 正确选择+正确参数+无冗余 | ≥ 90% |
| 幻觉率 | 包含虚构信息的输出比例 | ≤ 5% |
| 延迟 P50/P95 | 完成一次任务的时间 | P50 < 30s, P95 < 60s |
| 成本 | 单次任务 token 费用 | < $0.5/次 |
| 用户满意度 | 采纳率/评分 | ≥ 7/10 |

---

## 上机部分：用 deepeval 搭建营销 Agent 评测套件

> 📓 **配套笔记本**：[`starter.ipynb`](./starter.ipynb)（TODO 填空版，你来做）｜ [`solution.ipynb`](./solution.ipynb)（参考答案，gated，做完再看）
> 📊 **真实数据/库**：[`data/README.md`](./data/README.md)（deepeval 库 + 营销 Agent 真实轨迹测试用例）

### 为什么用真实库（deepeval）而非手写评估脚本

v4.0 的代码用"手写 if-else 检查输出格式"--手写评估只能做规则匹配（字数、关键词），无法评估"内容质量""推理合理性"这类需要语义理解的维度。v5.0 改用 **deepeval**（confident-ai/deepeval，17k★，LLM 评估框架）：

- **GEval**：LLM-as-a-judge 自动评分（给一段 criteria，LLM 自动打分+给理由），可评估内容质量、品牌调性、CTA明确性等语义维度
- **FaithfulnessMetric**：自动检测幻觉（对比 actual_output 与 retrieval_context，判断每条声明是否忠于知识库）
- **BaseMetric**：自定义轨迹评估指标（继承后实现 measure 方法，可评估工具调用正确性）
- **assert_test / evaluate**：pytest 风格断言 + 批量运行，可纳入 CI

> **在线可观测性补充**：deepeval 做离线测试套件，**LangSmith**（LangChain 出品，https://github.com/langchain-ai/langgraph ）做在线可观测性（trace/eval/score），记录 Agent 执行的完整调用链。两者互补：离线测试防回归，在线监控防线上故障。详见 `data/README.md`。

### 营销映射（关键桥接）

本 Day 评估一个"营销内容生成 Agent"（生成小红书种草文案/朋友圈广告），评估对象是 Agent 的**真实输出轨迹**：

| 评估维度 | 营销场景 | deepeval 实现 |
|---------|---------|--------------|
| 内容质量（端到端） | 文案是否符合品牌调性、CTA是否明确 | GEval + criteria |
| 工具调用正确性（轨迹） | 是否选对工具（搜索知识库 vs 生成文案）、参数是否准确 | 自定义 BaseMetric |
| 幻觉率 | 是否虚构产品成分/功效（违反广告法） | FaithfulnessMetric |
| 综合指标 | 任务完成率/工具准确率/幻觉率 | evaluate() 批量运行 |

### 上机任务（6 个 TODO，见 starter.ipynb）

1. **TODO1**：准备营销 Agent 真实轨迹测试数据（3个 LLMTestCase：好/坏/混合轨迹）
2. **TODO2**：端到端评估--用 GEval 评估营销内容质量（品牌调性+CTA+平台适配）
3. **TODO3**：轨迹评估--自定义 BaseMetric 评估工具调用正确性
4. **TODO4**：幻觉检测--用 FaithfulnessMetric 检测输出是否忠于知识库
5. **TODO5**：LLM-as-a-judge 自动评审--用 GEval criteria 实现轨迹质量自动评分
6. **TODO6**：综合评估--用 evaluate() 运行完整测试套件，计算任务完成率/工具准确率/幻觉率

---

## 2026 前沿补充：LLM-as-a-judge 评估 Agent 轨迹

> v5.0 新增前沿点。Agent 评估的核心难题是"轨迹质量"需要语义理解--人工标注太慢，规则匹配太浅。2026 年的趋势是用 **LLM-as-a-judge**（NeurIPS 2023, arXiv 2306.05685）自动评估 Agent 轨迹质量，并用 **deepeval** 框架将其做成可运行的 CI 测试用例。

**怎么用**：把 Agent 的完整轨迹（Thought/Action/Observation/最终输出）整理成结构化文本，让一个 LLM 扮演"Agent 评审"，按预设 criteria 打分：

- **工具选择**：每一步是否选了正确的工具？（该搜索知识库时有没有调用搜索？）
- **推理链质量**：Thought 是否合理？有没有逻辑跳跃或幻觉推理？
- **最终答案质量**：内容是否符合 Brief？品牌调性一致？CTA明确？

用 deepeval 的 GEval 把上述 criteria 写成可测试用例，`assert_test` 断言通过/失败，`deepeval test run` 在 CI 中自动执行。

**注意**：LLM-as-a-judge 是**辅助评估工具**，有自身偏差（偏好长答案、位置偏差、自我偏好）。它对应因果阶梯的 L1（对轨迹文本的关联分析），不能替代真实业务指标（L2 干预：A/B测试）。定位为"开发期自检工具"，生产期仍需 A/B 测试 + 用户满意度反馈。

> 🔗 深入阅读见 [`reading.md`](./reading.md) 的 LLM-as-a-judge 条目。

---

## 与后续 Day 的衔接

- **Day 4**：安全防护与对抗（Prompt Injection 防御）--今天的"对抗性测试"方法是 Day 4 安全评估的基础
- **Day 5**：生产化部署（监控/灰度/回滚）--今天的评估指标（延迟/成本/完成率）是 Day 5 生产监控的核心 SLI

---

## 作业与评估

作业、5 分制量表、费曼演练、2 分钟话术、复盘自诊表--沿用独立教材 § Day 3 既有设计。本学习材料包不重复，仅新增上机交付物：

**新增交付物（v5.0）**：
- [ ] 完成的 `starter.ipynb`（6 个 TODO 全部填好，能跑通）
- [ ] 一段 300 字分析：你的营销 Agent 在哪个评估维度表现最差？根因是什么（工具选择/参数/推理/幻觉）？
- [ ] （可选）设计1个对抗性测试用例（模糊指令/知识库不存在的问题），观察 Agent 是否会"不知道说不知道"

---

*本讲义由 v5.0 学习材料包升级生成。理论部分引用独立教材，上机部分用真实库（deepeval）+ TODO 脚手架。*
*最后更新：2026-07-24*


---

## 学习科学层 (v6.0)

本单元采用刻意练习(Ericsson)/间隔重复(FSRS-6,SM-2)/建构对齐(Biggs ILO↔TLA↔AT)/牛津tutorial LLM仿真(Socratic,Hattie四级反馈)。mastery 阈值与 Worked-Faded 示例见 practice.md 与 alignment.md。交叉练习(interleaving)促进迁移, 提取练习(retrieval practice)优于重读。

- **practice.md**: 4 个 drill (D1-GEval/D2-Trajectory/D3-Faithfulness/D4-EvalBatch) 含 Worked-Faded 三阶段 + weak_loop 弱项循环 + A1B1C1...B2C2A2...C3A3B3 交叉排布 + CS230 渐进项目 (proposal->milestone->final->poster)
- **schedule.json**: FSRS-6 (SM-2 backup) 6 张卡片覆盖 轨迹vs端到端/deepeval五组件/AgentBench8场景/六大指标/LLM-as-judge三大偏差/四大挑战, due=[1,3,8,21,60,180]
- **alignment.md**: Biggs ILO↔TLA↔AT 5 行矩阵 + mastery_threshold + Feed Up/Feed Back/Feed Forward 三自检
- **tutorial.ipynb**: Oxford tutorial Socratic 仿真 (4 轮静态 if/else, >=5 苏格拉底问) + Hattie 四级反馈 [TASK]/[PROCESS]/[SELF-REG]/[FEED-FORWARD] + student_model.json 读写 + 限频 1次/天

*v6.0 学习科学层升级, 追加于 2026-07-26, 不改动 v5.0 原文一字.*

---

## 研究产出与产业链接层 (v7.0)
本单元产出可发表研究工件 (research.md: 研究问题+贡献声明+arXiv链接+IMRaD大纲+NeurIPS可复现清单+research-to-practice翻译) 与产业链接 (industry.md: >=3真实企业+部署场景+Imperial咨询项目+HBS教学案例+客座讲座+实习指针)。研究产出遵循IMRaD/DSR(Hevner)/OSF预注册/FAIR/可复现研究标准; 产业链接遵循Imperial MSc BA咨询项目(Burberry/Expedia/J&J)/HBS案例法/MIT Sloan行动学习模式。详见 research.md 与 industry.md。

---

## 学术前沿层 (v9.0)

本单元新增 `frontier.md`：注入 2025-2026 最新学术前沿（5 篇真实 arXiv 论文 + 批判性综述 + delta_to_unit + ≥3 开放研究问题 + 方法论批评）。论文来自 `_frontier_corpus/skill-5-agentic.md` 共享语料库（arXiv 搜索 + abstract 页抽查验证），覆盖前沿课题：Agent评估与LLM-as-a-Judge。面向博后/教授级读者：批判性综述非罗列，delta_to_unit 显式指出前沿如何更新本单元所教，开放问题为可发表研究方向。详见 `frontier.md`。
