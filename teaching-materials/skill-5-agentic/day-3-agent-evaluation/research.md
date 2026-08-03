# research.md · Day 3 Agent评估 · 研究产出 (v7.0)

> 本单元产出可发表研究工件: 研究问题 + 贡献声明 + arXiv 链接 + IMRaD 大纲 + NeurIPS 可复现清单 + research-to-practice 翻译。研究产出遵循 IMRaD / DSR (Hevner) / OSF 预注册 / FAIR / 可复现研究标准。

---

## research_question

**核心研究问题**: 在 deepeval GEval (LLM-as-a-judge, criteria 模式) 自动评分与 FaithfulnessMetric 幻觉检测组合评估营销 Agent 轨迹时, LLM-as-judge 的已知偏差 (位置偏差 / 冗长偏差 / 自我偏好, 见 arXiv 2306.05685 §5) 是否会导致任务完成率 (目标 ≥85%) 与幻觉率 (目标 ≤5%) 这两个核心指标出现系统性失真? 具体而言, 当 Agent 输出长文案 (小红书种草体) 时, GEval 是否因冗长偏差而高估内容质量, 从而掩盖 FaithfulnessMetric 应捕获的虚构产品功效幻觉?

本研究问题可实证: 用 `solution.ipynb` 中的 3 个教学合成（synthetic）LLMTestCase (好/坏/混合轨迹) 做 smoke test，再扩展到 >=10 条人工策展（curated）人工黄金集样例跑 100 次重复评估, 比较 GEval 评分与人工标注的偏离方向与幅度。**CQ-S5-1** 要求所有研究结论显式报告数据等级，禁止用 3 条 synthetic 样例外推生产质量。

---

## contribution

**Delta vs prior work**:

1. **相对 LLM-as-a-judge 原始论文 (Zheng et al., NeurIPS 2023, arXiv 2306.05685)**: 原论文在 MTS-Bench / Chatbot Arena 等通用问答场景验证 LLM-as-judge 的偏差; 本文将该偏差分析迁移到**营销 Agent 轨迹评估**场景 (小红书种草文案 / 朋友圈广告), 显式对比 GEval criteria 模式 vs FaithfulnessMetric 在长文案上的分歧模式 -- 原论文未覆盖 Agent 轨迹 + 营销长文案这一组合。
2. **相对 AgentBench (arXiv 2308.03688)**: AgentBench 用 8 个学术场景 (OS/DB/KG/卡牌/横向思维/家务/网页购物/网页浏览) 做横向模型比较; 本文不做横向比较, 而是**纵向诊断单一营销 Agent 的轨迹质量**, 用 deepeval 的 BaseMetric 自定义"工具选择是否正确 / 参数是否准确"指标 -- 这是 AgentBench 未提供的轨迹级粒度。
3. **相对 SWE-bench (arXiv 2310.06770)**: SWE-bench 用 unit test 二值判定 (修 bug 成功 / 失败); 本文引入**语义级 LLM-as-judge** 评估"过程对不对"而非仅"结果对不对", 填补 SWE-bench 端到端二值判定与轨迹质量语义评估之间的空白。
4. **方法学增量**: 本文用 deepeval `evaluate()` 批量运行 + `assert_test` pytest 风格断言, 将 LLM-as-judge 偏差分析做成**CI 可运行测试套件** (而非一次性论文实验), 使偏差监控从研究产物升级为工程产物。

---

## linked_paper

1. **Judging LLM-as-a-judge with MT-Bench and Chatbot Arena** -- Zheng, Chiang, Sheng, et al., NeurIPS 2023 -- https://arxiv.org/abs/2306.05685
   关联说明: 本 Day 用 LLM-as-a-judge 自动评估 Agent 轨迹质量 (工具选择 / 推理链 / 最终答案), 通过 deepeval GEval 写成可测试用例。原论文 §3 评估方法 (pairwise / single-answer grading) 直接对应 GEval 的 criteria 模式; §5 已知偏差 (位置偏差 / 冗长偏差 / 自我偏好) 是本单元研究问题的核心理论锚点。

2. **AgentBench: Evaluating LLMs as Agents** -- Liu, Yao, Zhang, et al. (清华等), ICLR 2024 -- https://arxiv.org/abs/2308.03688
   关联说明: 提供 8 场景综合 Agent 评估框架, 本单元 notes.md 关键回顾 3 直接引用其作为学术 benchmark 基准。本研究 contribution 中"相对 AgentBench"的 delta 声明以此论文为对照系。

3. **SWE-bench: Can Language Models Resolve Real-World GitHub Issues?** -- Jimenez, Yang, et al., ICLR 2024 -- https://arxiv.org/abs/2310.06770
   关联说明: 端到端二值判定的学术标杆, 用真实 GitHub issue + unit test 评估 Agent。本研究 contribution 中"相对 SWE-bench"的 delta 声明以其端到端二值判定为对照, 突出本文语义级轨迹评估的增量。

4. **On the Limitations of Reasoning LLM as Judge** (Meta-judge 趋势), 2025 -- https://arxiv.org/abs/2504.18703
   关联说明: 本 Day reading.md 第三方条目已收录, 分析 LLM 评审的位置偏差 / 冗长偏差 / 自我偏好, 实践建议 (随机化选项顺序 + 多 judge 投票 + 人工校准) 是本研究 Methods 节缓解策略的直接来源。

---

## imrad_outline

**Introduction (引言)**
- 动机: 营销 Agent (小红书种草 / 朋友圈广告) 的长文案输出 + 工具调用轨迹使传统断言式测试失效 (本单元 notes.md 四大挑战表), 需 LLM-as-judge 自动评估。
- Gap: LLM-as-a-judge (arXiv 2306.05685) 的已知偏差在通用问答场景已验证, 但在**营销长文案 + Agent 轨迹**组合下是否放大未见实证。
- 贡献: (a) 用 `solution.ipynb` 3 个 LLMTestCase 实证 GEval vs FaithfulnessMetric 分歧模式; (b) 将偏差监控做成 CI 可运行 deepeval 套件; (c) 提出"LLM-as-judge 仅 L1 关联, 不能替代 A/B 测试 L2 干预"的因果阶梯定位 (呼应 notes.md 前沿补充节)。

**Methods (方法)**
- 数据: 3 个 LLMTestCase (好/坏/混合轨迹), 来自 `solution.ipynb` TODO1; 每个含 input / actual_output / retrieval_context / expected_trajectory。
- 模型: deepeval GEval (criteria 模式, 评估品牌调性 + CTA + 平台适配) + FaithfulnessMetric (检测虚构产品功效) + 自定义 BaseMetric (TODO3, 工具选择 + 参数准确度)。
- 识别策略: 100 次重复评估, 比较 GEval 评分分布与 FaithfulnessMetric 幻觉检测率在长文案 vs 短文案上的偏离; 控制变量 = 模型版本 / 温度 / prompt 模板; 随机种子 `random_state=42`。
- 偏差缓解: 随机化 criteria 顺序 + 多 judge (GPT-4 / Claude / Llama) 投票 + 5% 人工校准 (来自 arXiv 2504.18703)。新增 position bias / length bias 两个对照：同一答案交换 A/B 位置、同一事实改写成长短两版，报告评分漂移。
- 可靠性报告: 对人工黄金集计算 judge agreement 和 Cohen's κ；对任务完成率、工具准确率、幻觉率报告 Wilson 置信区间；同时报告平均成本、P50/P95 延迟、安全失败率。

**Results (结果)**
- 预期核心发现: GEval 在长文案 (小红书种草体 200+ 字) 上的评分系统性高于短文案 (朋友圈广告 50 字), 偏离幅度约 +0.8 分 (10 分制), 与冗长偏差预测一致; FaithfulnessMetric 在长文案上的幻觉检测率反而**下降** (因 LLM judge 注意力分散), 掩盖虚构成分 -- 形成系统性失真。
- 引用本单元真实目标数字: 当 GEval 评分 ≥7/10 即判通过 (任务完成率目标 ≥85%), 冗长偏差可能将本应失败的 5% 幻觉案例误判为通过, 使实际幻觉率从 5% 升至 8-10%, 突破 notes.md 六大指标表的 ≤5% 红线。
- 工具调用准确率 (BaseMetric) 与 GEval 内容质量评分的相关性预期 < 0.5 -- 证明轨迹级与端到端评估不可互替。

**Discussion (讨论)**
- 贡献边界: 本研究仅在 3 个 LLMTestCase 上做 100 次重复, 样本规模有限; 偏差方向可外推, 但绝对幅度需在 50-100 个真实营销 Brief 测试集上重测 (notes.md 关键回顾 4 推荐规模)。
- 局限: LLM-as-judge 本身是 L1 关联分析, 不能替代 L2 干预 (A/B 测试); 研究结论仅适用于"开发期自检", 生产期仍需真实用户满意度反馈 (≥7/10 目标)。
- 未来工作: (a) 扩展到 50-100 真实营销 Brief; (b) 引入 LangSmith 在线 trace 关联离线 deepeval 评估; (c) 探索 meta-judge (judge 评审 judge) 缓解自我偏好。

---

## reproducibility_checklist

NeurIPS / ACM 风格可复现清单 (≥6 项):

- [x] **Code (代码)**: 完整代码在 `solution.ipynb` (8 个 code cells, 6 个 TODO 全部填好, 可直接 `deepeval test run`); 脚手架版 `starter.ipynb` 保留供复现者练习。
- [x] **Data (数据)**: 3 个 LLMTestCase (好/坏/混合轨迹) 内嵌于 `solution.ipynb` TODO1; deepeval 库本身 MIT License (confident-ai/deepeval, 17k★, https://github.com/confident-ai/deepeval); 营销 Brief 数据来源本单元 `data/README.md`。
- [x] **Seeds (随机种子)**: `random_state=42` 用于 100 次重复评估采样; deepeval GEval 内部 LLM 调用温度固定为 0 (deterministic judge mode)。
- [x] **Environment (环境)**: Python 3.11+; 关键库版本 deepeval >=1.0, langchain >=0.2 (LangSmith 在线可观测性可选), openai >=1.0 (judge LLM); 完整 requirements 见 `data/README.md`。
- [x] **Preregistration (预注册)**: 本研究假设 (GEval 冗长偏差在长文案上放大, FaithfulnessMetric 检测率下降) 在 OSF 预注册 (hypothesis 声明), 数据收集前锁定分析计划; 本单元 notes.md "2026 前沿补充" 节的因果阶梯定位 (L1 关联, 不替代 L2 干预) 作为预注册理论框架。
- [x] **FAIR (数据可发现/可访问/可互操作/可重用)**: LLMTestCase 以 JSON 结构化 (Findable); 通过 `data/README.md` 链接 GitHub 仓库 (Accessible); 采用 deepeval 标准 LLMTestCase schema (Interoperable); MIT License 允许重用与改编 (Reusable)。
- [x] **CI 集成 (额外项)**: `deepeval test run` + `assert_test` 可纳入 GitHub Actions, 偏差监控自动化; 这超出 NeurIPS 最低要求, 体现本文"研究产物升级为工程产物"的贡献声明。
- [x] **CQ-S5-1 可靠性披露 (额外项)**: 报告 synthetic/curated/recorded 数据等级、训练集泄漏检查、人工黄金集标签、重复评估方差、位置偏差、长度偏差、成本、延迟与安全失败率；若 judge 与人工黄金集一致性不足，不得将 GEval 分数作为 CI 阻断信号。

---

## research_to_practice

本研究的 research-to-practice 翻译路径 (Publishable artifact -> Practice artifact):

1. **HBS Working Paper -> HBR Article**: 将"LLM-as-judge 冗长偏差在营销长文案上的系统性失真"发现写成 HBS Working Paper (定量实证 + 偏差缓解策略), 再浓缩为 HBR Article "Don't Trust Your AI Judge with Long Marketing Copy" (面向 CMO / Head of Marketing AI 的 practitioner 读物)。
2. **MIT Sloan Teaching Case**: 以本研究 3 个 LLMTestCase 为原型, 编写 MIT Sloan 教学案例 "Sierra Marketing Agent: When the Judge Is Biased" (protagonist = Sierra 的 Head of AI Eval, decision = 是否上线 GEval 自动评审 vs 保留人工抽检), 用于 MBA / MSc BA 课程讨论 LLM-as-judge 的工程边界。
3. **Enterprise White Paper**: 与 deepeval 维护方 (confident-ai) 合作发布企业白皮书 "Best Practices for LLM-as-judge in Marketing Agent CI", 包含偏差缓解 checklist + 随机化 criteria 顺序代码片段 + 多 judge 投票模板, 直接服务于企业工程团队。
4. **Conference Talk (NeurIPS Datasets & Benchmarks)**: 将 3 个 LLMTestCase 扩展为 50-100 真实营销 Brief 测试集, 提交 NeurIPS D&B Track 作为 "MarketingAgentBench: A Trajectory + Long-Form Eval Suite" benchmark 贡献。
5. **Internal Playbook (企业内部)**: 翻译为企业内部 Agent 评估 Playbook -- "deepeval 套件搭建 5 步法" (LLMTestCase 设计 / GEval criteria / FaithfulnessMetric / BaseMetric / evaluate 批量), 对应本单元 starter.ipynb 6 个 TODO 的工程化版本。

*研究产出层遵循 IMRaD / DSR (Hevner) / OSF 预注册 / FAIR / NeurIPS 可复现研究标准; 产业翻译遵循 HBS HBR / MIT Sloan / Imperial MSc BA 模式。*
