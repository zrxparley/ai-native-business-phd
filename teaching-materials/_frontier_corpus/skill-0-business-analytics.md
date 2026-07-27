# 前沿语料库: skill-0-business-analytics - LLM-as-data-analyst & 列式引擎(Polars/DuckDB)

> v9.0 前沿注入层共享语料库. 论文来自 arXiv 搜索 (2025-09 ~ 2026-07, post 2025-08 cutoff). 标注 verified 的论文经 abstract 页抽查. wave agent 仅可引用本文档列出的论文, 禁止编造.

## 论文

### 1. A Query Engine for the Agents
- **arXiv**: https://arxiv.org/abs/2605.27785
- **作者**: Kenny Daniel
- **年份**: 2026
- **摘要**: 提出 Hyperparam, 三个开源 JavaScript 库 (under 70 KB), 可在 AI-native 客户端应用中直接从对象存储读取 Parquet 和 Apache Iceberg. Squirreling 在 filter-bounded 查询上比 DuckDB-WASM 快 300 倍以上, 以更低成本支持 agent analyst 套件.
- **验证**: verified

### 2. Demonstration of Pneuma-Seeker: Agentic System for Reifying and Fulfilling Information Needs on Tabular Data
- **arXiv**: https://arxiv.org/abs/2604.14422
- **作者**: Muhammad Imam Luthfi Balaka, Raul Castro Fernandez
- **年份**: 2026
- **摘要**: 演示 Pneuma-Seeker 系统, 将用户信息需求具体化为可检视的关系规范 (relational specifications), 支持迭代精化. 通过两个采购用例, 将 LLM 作为透明、交互式的分析协作者而非黑盒答案引擎.
- **验证**: verified

### 3. Intelligent Drill-Down: Large Language Model-Driven Drill-Down Technique for Human-AI Collaborative Visual Exploration
- **arXiv**: https://arxiv.org/abs/2604.17002
- **作者**: Zhijun Zheng, Tian Qiu
- **年份**: 2026
- **摘要**: 提出智能下钻框架, LLM 生成视觉洞察、解释用户意图并推荐多维数据探索的下钻路径. LLM 经训练近似已验证的贪心路径推荐算法, 配备分支管理系统和分层导航的混合界面.
- **验证**: unverified

### 4. The CRISTAL Method: Neurosymbolic analysis from AI-synthesized world models
- **arXiv**: https://arxiv.org/abs/2606.29799
- **作者**: Rafael Kaufmann, Felix Neubürger
- **年份**: 2026
- **摘要**: 神经符号框架用于自动化复杂分析工作流, 以基本面投资分析为主要用例. 构建动态概率程序支持贝叶斯推断, 在公司分类任务上仅用 5 个样本即达到 Bayes-optimal accuracy, 超越准确率停滞在 40% 左右的 LLM.
- **验证**: unverified

### 5. Beyond Semantic Similarity: A Two-Phase Non-Parametric Retrieval Workflow for Corporate Credit Underwriting
- **arXiv**: https://arxiv.org/abs/2605.20684
- **作者**: Linus Ng Junjia, Ezekiel Tee Kongquan
- **年份**: 2026
- **摘要**: 两阶段检索架构, 分离高召回候选检索与高精度效用排序, 使用 LLM-as-a-Judge 评分. 部署于 800+ 信用分析师, 文档审阅时间从数小时降至约三分钟, 在多语言金融文档上超越朴素检索基线.
- **验证**: unverified

### 6. AI Scientists Are Only as Good as Their Evidence: A Stratified Ablation of Proprietary Data and Reasoning Skills in Drug-Asset Valuation
- **arXiv**: https://arxiv.org/abs/2606.09556
- **作者**: Yinan Wang
- **年份**: 2026
- **摘要**: 在生产级药物资产估值 agent 上进行受控三臂消融实验, 表明专有证据设定 AI 决策质量上限. 完整系统 (含专有语料) 恢复 0.96 的 gold competitive records, 而非专有变体仅 0.25-0.38. 推理支架改善校准但无法突破事实天花板.
- **验证**: unverified

### 7. PMAx: An Agentic Framework for AI-Driven Process Mining
- **arXiv**: https://arxiv.org/abs/2603.15351
- **作者**: Anton Antonov, Humam Kourani
- **年份**: 2026
- **摘要**: 自主 agentic 框架, 作为虚拟流程分析师运行, 采用隐私保护多 agent 架构. Engineer agent 生成本地脚本运行流程挖掘算法, Analyst agent 解读结果, 通过分离计算与解读确保数学准确性与数据隐私.
- **验证**: unverified

### 8. Detection, Attribution, Narration: An End-to-End Pipeline for Explainable Money Mule Identification
- **arXiv**: https://arxiv.org/abs/2607.17586
- **作者**: Yuge Zhang, Yuanxing Zhang
- **年份**: 2026
- **摘要**: 端到端管道用于洗钱骡户检测, 结合 LightGBM、TreeSHAP 归因和 LLM 生成的分析师叙事. 生产环境中 yield rate 达 89% (规则系统仅 61%), 增量检出 60%. 分析师反馈 LLM 叙事降低告警分诊的认知负荷.
- **验证**: unverified

### 9. AI Coding Agents in Social Science: Methodologically Diverse, Empirically Consistent, Interpretively Vulnerable
- **arXiv**: https://arxiv.org/abs/2606.11456
- **作者**: Meysam Alizadeh, Fabrizio Gilardi
- **年份**: 2026
- **摘要**: 在移民/社会政策研究的 many-analysts 人类基线上测试 LLM 编码 agent (Claude Code, Codex). 在设计层 agent 匹配或超越人类方法论多样性; 在裁决层, 显式确认性提示将 Claude Code 的裁决从 10% 翻转至 90% 支持, 揭示解释层为 AI 偏见所在.
- **验证**: unverified

### 10. Agent-as-Peer-Debriefer: A Multi-Agent Framework with Perspective-Based Refinement for Qualitative Analysis
- **arXiv**: https://arxiv.org/abs/2605.24600
- **作者**: Zhimin Lin, Kun Cheng
- **年份**: 2026
- **摘要**: 多 agent 定性数据分析框架, 引入同行辩论, 三个 Peer-Debriefing Agent 分别采用理论驱动、数据驱动、应用视角. 在三个数据集和三个 LLM 上, 基于视角的精化比单 LLM 基线更贴近人类编码, 各视角产生不同的权衡.
- **验证**: unverified

## 备注
- 论文 1 (Hyperparam/2605.27785) 直接对比 DuckDB-WASM, 是列式引擎×LLM 主题最相关的一篇, 已 verified.
- 论文 2 (Pneuma-Seeker/2604.14422) 聚焦表格数据上的 LLM 分析协作, 已 verified.
- arXiv 搜索查询: "LLM data analyst", sorted by newest first. 搜索返回 40 篇可见论文, 全部在 2025-09 ~ 2026-07 范围内.
- 选材偏向: LLM-as-analyst 工作流、列式/表格引擎、多 agent 分析协作、生产部署案例.
