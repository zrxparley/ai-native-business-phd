# 前沿语料库: elective-e9-ai-safety-alignment - 机制可解释性与可扩展监督与Agent安全

> v9.0 前沿注入层共享语料库. 论文来自 arXiv 搜索 (2025-09 ~ 2026-07, post 2025-08 cutoff). 标注 verified 的论文经 abstract 页抽查. wave agent 仅可引用本文档列出的论文, 禁止编造.

## 论文

### 1. Quantifying LLM Attention-Head Stability: Implications for Circuit Universality
- **arXiv**: https://arxiv.org/abs/2602.16740
- **作者**: Karan Bali, Jack Stanley
- **年份**: 2026
- **摘要**: 系统研究transformer语言模型中注意力头在独立初始化训练运行间的稳定性。发现中间层头部最不稳定但最具表征独特性，深层模型中不稳定的头部功能上更重要，权重衰减可显著改善稳定性。将电路的跨实例鲁棒性确立为可扩展监督的前提，对AI系统白盒可监测性有直接启示。
- **验证**: verified

### 2. CircuitKIT: Circuit Discovery, Evaluation, and Application Toolkit for Mechanistic Interpretability
- **arXiv**: https://arxiv.org/abs/2607.19317
- **作者**: Pratinav Seth, Hem Gosalia
- **年份**: 2026
- **摘要**: 提出CircuitKIT，一个连接电路分析工作流的源可用库，提供类型化可序列化表示。包含发现算法、声明式接口、电路诊断及下游应用模块（剪枝、编辑、转向、选择性微调）。解决当前机制可解释性方法碎片化、难以比较的问题，为电路分析提供通用基础设施。
- **验证**: verified

### 3. OPIUM: Mitigating Steering Externalities and Over-Refusal via Dual Objective Latent Optimization
- **arXiv**: https://arxiv.org/abs/2607.19806
- **作者**: Kavin Aravindan, Arihant Rastogi
- **年份**: 2026
- **摘要**: 提出OPIUM，一种无需训练的方法，通过表示匹配净化转向向量。优化新转向向量以保留期望干预的下游表示，同时在原始向量失败的提示上匹配更安全的参考行为。被ICML 2026机制可解释性工作坊接收，直接服务于安全对齐中的转向控制。
- **验证**: unverified

### 4. Measuring Monosemanticity in Sparse Autoencoders via Latent Activation Coherence
- **arXiv**: https://arxiv.org/abs/2607.17770
- **作者**: Katarzyna Filus, Sebastian Pokuciński
- **年份**: 2026
- **摘要**: 提出Tversky单义性评分（TMS），一种无标签指标，将单义性操作化为二值化SAE潜在激活集的相干性。在DINOv3、CLIP和BLIP2特征上训练的SAE上评估，显示TMS比基于嵌入的替代方案更不受编码器各向异性影响。为可解释性研究提供可量化的单义性度量。
- **验证**: unverified

### 5. Are Arithmetic Heuristic Neurons Form-Invariant? A Mechanistic Analysis of Symbols, Text, and Code in LLMs
- **arXiv**: https://arxiv.org/abs/2607.16693
- **作者**: Sharath Naganna, Tanvir Ahmed Sijan
- **年份**: 2026
- **摘要**: 研究算术启发式神经元在符号算术、自然语言应用题和Python代码之间是否形式不变。在三个Llama-3模型中发现一组紧凑的神经元在三种格式间共享，跨格式激活迁移可恢复大多数错误预测，加减法准确率超过97%。揭示LLM中算术处理的跨模态电路共性。
- **验证**: unverified

### 6. Collaborative Disagreement Resolution for Scalable Oversight
- **arXiv**: https://arxiv.org/abs/2607.01251
- **作者**: Yuyang Jiang, Chacha Chen
- **年份**: 2026
- **摘要**: 提出AI辩论的替代方案——"分歧解决"，将交互重新构建为受人类调解启发的"协作真理寻求"。引导模型协作识别分歧点并趋向共识，达到62.1%的判断准确率，相比标准对抗辩论的49.2%。为可扩展监督提供从对抗说服到协作求真范式转移的实证证据。
- **验证**: unverified

### 7. The Unverifiability of Artificial General Intelligence (AGI) Alignment, Static and Dynamic: From Trakhtenbrot's Wall to the Safety-Generality Tension
- **arXiv**: https://arxiv.org/abs/2606.28639
- **作者**: Jose Pascual Gumbau Mezquita
- **年份**: 2026
- **摘要**: 建立AGI安全性的数学极限，证明没有算法能无误地认证高表达性AGI的安全行为。障碍来自Rice定理、哥德尔定理和Trakhtenbrot定理，持久认证仅对已停止语义演化的系统可行。将结果联系到可扩展监督和Yampolskiy验证者理论，揭示安全-通用性张力。
- **验证**: unverified

### 8. Automated alignment is harder than you think
- **arXiv**: https://arxiv.org/abs/2605.06390
- **作者**: Aleksandr Bowkis, Marie Davidsen Buhl
- **年份**: 2026
- **摘要**: 论证使用AI代理自动化对齐研究可能产生令人信服但灾难性误导的安全评估。识别核心风险：优化压力将错误集中在人类审查者最不可能发现的地方，代理产生非人类类错误，共享权重使AI输出比人类等效物更相关。对自动化对齐与可扩展监督的新挑战进行系统分析。
- **验证**: unverified

### 9. The Digital Apprentice: A Framework for Human-Directed Agentic AI Development
- **arXiv**: https://arxiv.org/abs/2606.04321
- **作者**: Travis Weber, Rohit Taneja
- **年份**: 2026
- **摘要**: 提出实现可扩展、安全AI代理的框架，其中自治权是赢得的而非假设的。数字学徒通过方法论捕获、授权（自治升级由明确人类批准门控）和持续对齐三个组件内化人类隐性方法论。数学建模质量框架并展示从数据漂移中恢复的能力，直接服务于Agent安全设计。
- **验证**: unverified

### 10. The Endogeneity of Miscalibration: Impossibility and Escape in Scored Reporting
- **arXiv**: https://arxiv.org/abs/2605.07671
- **作者**: Lauri Lovén, Sasu Tarkoma
- **年份**: 2026
- **摘要**: 解决从自主代理引出真实报告的问题，这是可扩展AI监督的核心。证明不可能性：委托人的最优监督必然使用非仿射批准函数，使真实报告次优。显示尖锐阈值是校准保持设计，福利等价性对Brier评分唯一。为可扩展监督的机制设计提供理论基础。
- **验证**: unverified

## 备注
- 本模块覆盖三大子主题：机制可解释性（论文1-5，含电路稳定性、工具包、转向向量、单义性度量、跨模态神经元）、可扩展监督（论文6-7、10，含协作分歧解决、AGI对齐不可验证性、评分报告机制设计）、Agent安全（论文8-9，含自动化对齐风险、人主导代理框架）。
- verified 论文（1、2）经 arXiv abstract 页面直接确认存在且标题/作者/日期匹配。其余论文来自 arXiv 搜索结果页（按提交日期降序），尚未逐页验证。
- 论文3（OPIUM）被ICML 2026机制可解释性工作坊接收，可信度较高。
- 论文7建立AGI安全性的数学极限，与可扩展监督的理论边界直接相关，适合作为理论锚点。
- 注意：机制可解释性领域2026年7月论文密集涌现（论文2-6均为2607.xxxxx），反映该领域研究热度。
