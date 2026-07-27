# frontier.md (v9.0 学术前沿注入层)

> **所属**：skill-4-business-model · day-2-value-creation-pricing
> **版本**：v9.0（学术前沿注入层）
> **本单元前沿课题**：2025-2026 年 capability-priced micro-markets 与 agentic markets 均衡定价如何更新本单元的 outcome-based pricing 数学模型与推理成本定价逻辑，以及"隐私需求弹性"如何修正本单元的价格弹性估计。

---

## frontier_topic

本单元教 AI 价值创造三维度（效率提升/体验重塑/模式创新）与四种定价策略（成本加成/价值定价/渗透/撇脂），用 OLS 回归量化定价驱动因素、NPV 评估财务可行性、scipy.stats 估计价格弹性、天道推演做竞争反应沙盘。前沿子问题是：2025-2026 年 capability-priced micro-markets 的"隐私需求弹性"概念与 agentic markets 均衡分析如何更新本单元 outcome-based pricing 的数学模型（P = α × V）与价格弹性估计（log-log 回归斜率）。

---

## recent_papers

> 从本模块 `_frontier_corpus/skill-4-business-model.md` 语料库中挑 5 篇最贴本单元的 2025-2026 论文。

### 1. Capability-Priced Micro-Markets: A Micro-Economic Framework for the Agentic Web over HTTP 402
- **arXiv**: https://arxiv.org/abs/2603.16899
- **作者**: Ken Huang, Jerry Huang
- **年份**: 2026
- **摘要**: 提出面向自主 AI 代理间鲁棒、可扩展、安全商业交易的微观经济框架，将代理交互形式化为不完全信息重复双边博弈。引入"隐私需求弹性"概念量化信息披露与价格之间的权衡。
- **与本单元的关联**: 直接对应本单元 outcome-based pricing 数学模型（P = α × V），"隐私需求弹性"是本单元价格弹性概念在 agentic web 中的推广--当定价单位从 token 转为 capability，弹性需纳入隐私维度。

### 2. Agentic Markets: Equilibrium Effects of Improving Consumer Search
- **arXiv**: https://arxiv.org/abs/2603.25893
- **作者**: Brendan Lucier, Nicole Immorlica
- **年份**: 2026
- **摘要**: 研究 AI 代理辅助搜索对双边市场均衡定价的影响。发现更便宜的搜索改善学习与消费者剩余，但更具信息量的搜索可能反而恶化福利，除非市场方能从消费者交互中学习。
- **与本单元的关联**: 对应本单元天道推演竞争反应沙盘的均衡分析，"信息搜索可能恶化福利"修正了渗透定价（低价高量）的乐观假设。

### 3. Modeling Agentic Technical Debt and Stochastic Tax: A Standalone Framework for Measurement, Simulation, and Dashboarding
- **arXiv**: https://arxiv.org/abs/2605.27320
- **作者**: Muhammad Zia Hydari, Raja Iqbal
- **年份**: 2026
- **摘要**: 构建形式化模型区分"代理技术债"（累积的设计与治理负债）与"随机税"（周期性运营负担），为 agentic AI 系统的成本度量与仿真提供可管理框架。
- **与本单元的关联**: 对应本单元推理成本定价（$0.30/1M tokens）与 NPV 计算中的成本结构，"随机税"概念揭示 AI 产品定价需纳入周期性运营负担而非仅边际推理成本。

### 4. When Machines Meet Each Other: Network Effects and the Strategic Role of History in Multi-Agent AI
- **arXiv**: https://arxiv.org/abs/2510.06903
- **作者**: Yu Liu, Wenwen Li
- **年份**: 2025
- **摘要**: 研究 LLM 代理在经典网络效应博弈中的行为，经济理论预测其收敛于预期均衡。发现价格是偏离的主导驱动因素，历史调节此效应，网络效应放大情境扭曲。
- **与本单元的关联**: 对应本单元价格弹性估计与天道推演竞争反应，"价格是偏离的主导驱动"为本单元 OLS 回归中价值创造机制系数的显著性提供博弈论解释。

### 5. From Augmentation to Reconstruction: Guiding the AI Disruption to the Good Place
- **arXiv**: https://arxiv.org/abs/2605.29207
- **作者**: David M. Rothschild, Jake M. Hofman
- **年份**: 2026
- **摘要**: 提出增强-自动化-重建三阶段框架，遵循通用目的技术的"生产率 J 曲线"模式，需在信任、数据基础设施与激励机制上互补投资。
- **与本单元的关联**: 对应本单元价值创造三维度，"重建"阶段的互补投资概念修正了 NPV 模型中仅考虑推理成本而忽略信任/数据基础设施投资的成本结构。

---

## critical_synthesis

这 5 篇论文共同指向一个核心**共识**：AI 产品定价正从"按 token 计量的边际成本定价"转向"按 capability 定价的不完全信息博弈定价"。Huang & Huang (2603.16899) 的 capability-priced micro-markets 框架将代理交互形式化为不完全信息重复双边博弈，引入"隐私需求弹性"--**共识在于定价单位应从 input/output token 升级为 capability（能力），且价格弹性需纳入隐私披露维度**。Lucier & Immorlica (2603.25893) 的均衡分析进一步支持：代理辅助搜索改变市场均衡，定价策略需考虑搜索成本与信息学习的外部性。

然而存在显著**争议**。本单元教的 outcome-based pricing 数学模型（P = α × V, α=10%-30%）假设价值 V 可客观度量且买卖双方信息对称，而 Huang & Huang 的"不完全信息"框架与 Lucier 的"信息搜索可能恶化福利"结论共同**挑战**这一假设--**争议焦点是：outcome 的度量权归谁？当代理"阅读"消费者对话以学习价值时，隐私披露与价格之间的权衡（隐私需求弹性）可能使 α 的取值内生依赖于隐私规制，而非外生给定**。方法学**趋势**上，Hydari & Iqbal (2605.27320) 的"代理技术债 + 随机税"形式化模型与 Liu & Li (2510.06903) 的"价格是偏离主导驱动"博弈论证据代表一种从静态定价公式走向动态博弈定价的趋势。但**局限**明显：Huang 的"隐私需求弹性"未经真实交易数据校准（unverified），属概念框架；Lucier 的均衡依赖强理性假设；Liu & Li 的 LLM 代理博弈行为可能因模型版本不同而不稳定（benchmark 污染风险）；Rothschild & Hofman 的 J 曲线是宏观历史模式，无法预测单个产品的定价拐点。

---

## delta_to_unit

1. **outcome-based pricing 模型的隐私维度缺失**：本单元 notes.md 的 outcome-based pricing 数学模型（`P = α × V`, α=10%-30% 价值捕获比例）假设价值 V 可客观度量，而 Huang & Huang (2603.16899) 的"隐私需求弹性"概念揭示：在 agentic web 中，定价需考虑信息披露与价格之间的权衡。本单元 solution.ipynb TODO4 的 log-log 回归估计弹性（elasticity=-0.6169, 95% CI 宽）仅基于价格-需求二维数据，未纳入隐私维度--前沿提示应扩展为三维弹性（价格 × 需求 × 隐私披露量），否则在 agentic 市场中弹性估计存在遗漏变量偏误。

2. **NPV 成本结构的"随机税"缺失**：本单元 solution.ipynb TODO3 的 NPV 计算将成本简化为"初始投资 $5,576,000 + 推理成本 $0.30/1M tokens"，而 Hydari & Iqbal (2605.27320) 的"代理技术债 + 随机税"框架揭示 AI 产品还存在周期性运营负担（随机税）与累积治理负债（技术债）。本单元的渗透定价 NPV 为负（DeepSeek $0.14/1M 水平），本单元将其归因于推理成本高，但前沿提示：即使推理成本趋零，随机税与技术债仍可能使渗透定价不可持续--这是本单元 NPV 模型未覆盖的成本维度。

3. **天道推演竞争反应概率的均衡校准**：本单元 solution.ipynb TODO6 的天道推演沙盘手工设定竞品反应概率（渗透定价：跟降 55%/不变 25%/反击 5%/退出 15%），而 Lucier & Immorlica (2603.25893) 的均衡分析提供了理论校准：当搜索成本下降时，竞品"跟降"概率应内生取决于信息学习效应而非外生给定。Liu & Li (2510.06903) 的"价格是偏离主导驱动"进一步提示：价格变动是触发竞品偏离均衡的主导因素，本单元的 55% 跟降概率可能低估了价格战的触发概率。

4. **价值创造三维度的"重建"成本**：本单元 notes.md 的价值创造三维度（效率/体验/模式创新）将"模式创新"对应撇脂定价，但 Rothschild & Hofman (2605.29207) 的"增强-自动化-重建"框架揭示：模式创新（对应"重建"阶段）需在信任、数据基础设施与激励机制上互补投资。本单元 solution.ipynb TODO3 的 NPV 仅计入开发成本与推理成本，未计入信任建设（审计/合规）与数据基础设施的互补投资成本--这会使模式创新类型的 NPV 系统性高估。

---

## open_questions

1. 当定价单位从 token 升级为 capability（Huang & Huang 框架），本单元 log-log 回归的弹性估计（-0.6169）是否需要重新以 capability 为单位估计--隐私需求弹性的引入是否会改变"非弹性需求"（|e|<1）的结论从而翻转"撇脂最优"的策略推荐？
2. Hydari 的"随机税"与"代理技术债"如何在 NPV 模型中形式化--是作为固定运营成本、随时间累积的负债、还是与推理成本成比例的附加项？这三种形式化对渗透定价 NPV 的影响差异有多大？
3. Lucier & Immorlica 的"信息搜索可能恶化福利"结论在 AI SaaS 定价中如何体现--当买方用 AI 代理比价（搜索成本趋零），卖方是否能通过"阅读"代理对话重新获取信息优势，从而维持高价而非走向完全竞争？
4. 本单元 OLS 回归 R²=0.859 但调整 R²=0.698（样本量 n=16，自变量 8 个），当加入"隐私需求弹性"与"随机税"两个新变量后，模型是否过拟合？贝叶斯定价（PyMC）的先验正则化能否缓解？
5. Rothschild & Hofman 的 J 曲线提示 AI 产品价值滞后 3-5 年，本单元 NPV 评估窗口为 5 年--若 J 曲线拐点在第 4-5 年，本单元的 NPV 是否系统性低估了"重建"阶段产品的价值？

---

## methodological_critique

这些前沿论文的方法学局限值得博后级读者警惕。Huang & Huang (2603.16899) 标注为 unverified，其"隐私需求弹性"概念虽具理论吸引力，但未经真实 agentic web 交易数据校准，属概念框架而非实证结果，不应直接用于定价决策。Lucier & Immorlica (2603.25893) 虽经 abstract 页 verified，但均衡分析依赖理性代理与可观测对话假设，在 GDPR/CCPA 隐私规制下"阅读代理对话"可能违法，结论的外部效度存疑。Hydari & Iqbal (2605.27320, unverified) 的"随机税"与"代理技术债"区分依赖主观界定，两者边界模糊，可复现性顾虑大--论文未开源 dashboard 代码与仿真参数。Liu & Li (2510.06903, unverified) 的 LLM 代理博弈实验存在模型版本依赖性（不同 LLM 可能产生不同均衡偏离），且"价格是偏离主导驱动"的结论可能因 benchmark 设计而放大（网络效应博弈的选择偏倚）。Rothschild & Hofman (2605.29207, verified) 的 J 曲线是宏观历史模式（基于既往 GPT 如电气化/蒸汽机），无法预测 AI 的具体拐点时间，将其用于单个 AI 产品 NPV 评估存在生态谬误。

---

*本文件由 v9.0 学术前沿注入层生成。所有论文链接来自 `_frontier_corpus/skill-4-business-model.md` 共享语料库（arXiv 搜索 + abstract 页抽查验证）。*
