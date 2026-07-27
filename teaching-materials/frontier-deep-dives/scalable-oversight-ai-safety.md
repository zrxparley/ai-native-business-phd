# deep_dive.md (v10.0 旗舰课题深挖, 专著式)

> **课题**：可扩展监督 × 机制可解释性 × Agent安全
> **版本**：v10.0（旗舰课题深挖层）
> **定位**：专著式前沿专题章，供博后研讨班/教授深度教学用。非全58单元，仅覆盖被选中的旗舰课题（elective-e9 模块）。
> **论文来源**：v9.0 `_frontier_corpus/elective-e9-ai-safety-alignment.md` 语料库（10 篇，2 verified + 8 unverified）+ 本深挖 arXiv 深研（4 篇，3 篇经 abstract 页验证 + 1 篇搜索结果页确认）。共 14 篇，无编造。

---

## topic

可扩展监督 × 机制可解释性 × Agent安全——在"对齐不可完全验证"的数学极限下，如何为自主 AI 系统构建可扩展、白盒可监测、纵深防御的安全基础设施。本课题处在 2025-2026 AI 安全研究的交汇点：可扩展监督正从对抗辩论范式向协作求真范式转移；机制可解释性正从单电路发现向可迁移、可组合的基础设施成熟；Agent 安全正直面多智能体能力悖论与存储型间接注入等新攻击面。三者共享一个根本张力——监督需要"可验证的安全证据"，但形式化不可验证性定理（Rice/Gödel/Trakhtenbrot 经由 Gumbau Mezquita 2026）表明高表达性 AGI 的对齐无法被任何算法无误认证。

---

## abstract

2025-2026 年，AI 安全三大子领域同时发生范式位移。可扩展监督方面，Jiang & Chen 的"协作分歧解决"以 62.1% vs 49.2% 判断准确率超越对抗辩论，Sudhir et al. 提供首个可泛化 oversight 基准（ASD 指标），而 Gumbau Mezquita 与 Lovén-Tarkoma 分别从可计算性与机制设计证明对齐认证与校准报告的不可完全性。机制可解释性方面，Bali-Stanley 揭示注意力头跨训练稳定性是白盒监督前提且远未解决，CircuitKIT 试图统一碎片化基础设施，FADE 与 TMS 为特征-描述对齐与单义性提供可量化度量。Agent 安全方面，DualView 揭示"存储型间接注入"这一被既往 Dual-LLM 防御遗漏的新攻击面，能力悖论证明更聪明的审计者反而使多智能体系统更不安全。核心张力：监督寻求可验证证据，但不可验证性定理划出形式化边界；机制可解释性提供白盒逃逸但电路迁移性脆弱；纵深防御在多智能体场景遭遇能力-安全反相关。对博士课程，本课题迫学生超越"对齐即工程"的朴素信念，理解对齐的数学极限、机制可解释性作为监督基础设施的成熟度边界，以及 compositional 场景下的新失效模式——这是从"会部署安全 agent"到"能论证安全边界"的研究者跃迁。

---

## paper_landscape

### 子主题 A：可扩展监督（不可验证性、协作求真 vs 对抗辩论、debate 基准）

#### 1. Collaborative Disagreement Resolution for Scalable Oversight
- **arXiv**: https://arxiv.org/abs/2607.01251 | **作者**: Yuyang Jiang, Chacha Chen | **年份**: 2026
- **批判摘要**：将可扩展监督的交互从对抗性辩论重构为"受人类调解启发的协作真理寻求"。模型被引导协作识别分歧点并趋向共识，而非相互说服裁判。在判断任务上达到 62.1% 准确率，显著高于标准对抗辩论的 49.2%（ICML 2026 接收）。关键发现是"协作求真"范式在同等模型能力下可超越"对抗说服"。局限在于：实验规模有限，且协作框架可能被一个策略性欺骗的参与者利用——诚实协作假设未受对抗压力测试。
- **与他篇关系**：直接挑战 debate 范式（即 Sudhir et al. 2025 基准所评估的对象）；与 Gumbau Mezquita (2026) 形成张力——若对齐不可完全验证，协作求真能否逃逸该限制尚无定论。它为 Lovén & Tarkoma (2026) 的机制设计难题提供了一个"协作而非激励"的逃逸方向，但未形式化证明逃逸。

#### 2. A Benchmark for Scalable Oversight Protocols
- **arXiv**: https://arxiv.org/abs/2504.03731 | **作者**: Abhimanyu Pallavi Sudhir, Jackson Kaunismaa | **年份**: 2025
- **批判摘要**：指出此前的 debate 实验不可泛化到其他 oversight 协议，提出首个系统性可扩展监督基准。核心贡献是"agent score difference (ASD)"指标，度量一个机制多大程度上"让诚实比欺骗占优"。提供 Python 包支持快速竞技式评估，并给出 debate 的示范性基准实验（ICLR 2025 BiAlign Workshop）。其价值在于把 oversight 从"各做各的实验"推向可比的实证科学。局限在于：ASD 是聚合标量，可能掩盖协议在不同错误类型上的差异表现；且基准任务仍以人类可判断为主，未触及 superhuman 能力区间。
- **与他篇关系**：为 Jiang & Chen (2026) 与经典 debate 提供了本应共同的比较底座——但 Jiang 的工作使用自有判断准确率而非 ASD，说明基准采纳尚不统一。它把 Gumbau Mezquita (2026) 的不可验证性从"全有全无的定理"转化为"ASD 能被推到多高"的实证问题。

#### 3. The Unverifiability of Artificial General Intelligence (AGI) Alignment, Static and Dynamic: From Trakhtenbrot's Wall to the Safety-Generality Tension
- **arXiv**: https://arxiv.org/abs/2606.28639 | **作者**: Jose Pascual Gumbau Mezquita | **年份**: 2026
- **批判摘要**：建立 AGI 安全性的数学极限，证明没有算法能无误认证高表达性 AGI 的安全行为。障碍来自 Rice 定理（非平凡语义性质不可判定）、Gödel 不完备与 Trakhtenbrot 定理（有限逻辑不可判定）。关键区分：静态认证仅对"已停止语义演化"的系统可行，动态 AGI 因持续学习而本质不可完全验证。将结果联系到 Yampolskiy 验证者理论与可扩展监督。其理论贡献是把分散的不可能性结果统一为"安全-通用性张力"。局限在于：定理针对图灵完备级表达性，是否对当前 LLM 的受限语义直接适用存在解释空间（见 §争议 2）。
- **与他篇关系**：为整个子主题提供理论锚点——Jiang 的协作求真与 Sudhir 的 ASD 基准都可视为"在不可验证性墙下能走多远"的实证回答。与 Lovén & Tarkoma (2026) 互补：后者从机制设计角度证明校准报告的不可完全性，前者从可计算性角度证明安全认证的不可完全性，两者共同构成"对齐不可完全验证"的双重论证。

#### 4. The Endogeneity of Miscalibration: Impossibility and Escape in Scored Reporting
- **arXiv**: https://arxiv.org/abs/2605.07671 | **作者**: Lauri Lovén, Sasu Tarkoma | **年份**: 2026
- **批判摘要**：解决从自主代理引出真实报告这一可扩展监督的核心问题。证明一个不可能性：委托人的最优监督必然使用非仿射批准函数，使真实报告对代理次优——即"激励诚实"与"最优监督"内生冲突。给出逃逸条件：尖锐阈值（sharp thresholds）是校准保持设计，福利等价性对 Brier 评分唯一。其贡献是把 oversight 的机制设计难题形式化为一个可证明的不可能性，而非仅经验性困难。局限在于：结果在特定的评分族内成立，现实 oversight 是否落在该族内需逐案验证。
- **与他篇关系**：与 Gumbau Mezquita (2026) 构成不可验证性的"机制设计 + 可计算性"双支柱。它精确刻画了 Jiang 协作框架所欲绕开的激励冲突——但 Lovén 的定理暗示，协作求真若不改变评分结构，仍可能落入该不可能性。

### 子主题 B：机制可解释性（电路分析、SAE/稀疏自编码器、算术神经元、特征监督）

#### 5. Quantifying LLM Attention-Head Stability: Implications for Circuit Universality
- **arXiv**: https://arxiv.org/abs/2602.16740 | **作者**: Karan Bali, Jack Stanley | **年份**: 2026
- **批判摘要**：系统研究注意力头在独立初始化训练运行间的稳定性。发现中间层头部最不稳定但最具表征独特性，深层模型中不稳定头部功能更重要，权重衰减可显著改善稳定性。其关键贡献是把"电路跨实例鲁棒性"确立为可扩展白盒监督的前提——若电路不跨训练稳定，则从一个模型发现的电路不能用于监督另一个。局限在于：稳定性 ≠ 正确性，稳定的电路仍可能是错误归因。
- **与他篇关系**：为整个子主题奠定前提——CircuitKIT (Seth & Gosalia)、SAE 单义性 (Filus)、FADE (Puri) 都隐含假设电路/特征可迁移，而本文量化了该假设的脆弱性。它与 Naganna & Sijan (2026) 的算术神经元形成对照：后者发现跨格式共享的紧凑神经元，暗示部分电路确实跨实例稳定，与本文的"中间层不稳定"形成需解释的张力。

#### 6. CircuitKIT: Circuit Discovery, Evaluation, and Application Toolkit for Mechanistic Interpretability
- **arXiv**: https://arxiv.org/abs/2607.19317 | **作者**: Pratinav Seth, Hem Gosalia | **年份**: 2026
- **批判摘要**：提出连接电路分析工作流的源可用工具包，提供类型化可序列化表示，涵盖发现、声明式接口、诊断及下游应用（剪枝、编辑、转向、选择性微调）。其价值是回应机制可解释性方法碎片化、难以比较的现状，提供通用基础设施。局限在于：工具包的统一化可能预设了某种电路本体论，而该本体论本身（什么是"一个电路"）仍开放争论；且其下游应用（转向、编辑）的安全收益尚未在对抗性场景验证。
- **与他篇关系**：是 Bali & Stanley (2026) 稳定性研究的"消费者"——若稳定性不足，CircuitKIT 发现的电路跨模型可用性受限。与 OPIUM (Aravindan & Rastogi 2026) 互补：CircuitKIT 提供电路基础设施，OPIUM 提供转向向量的安全净化，两者共同构成"发现-编辑"工具链。

#### 7. OPIUM: Mitigating Steering Externalities and Over-Refusal via Dual Objective Latent Optimization
- **arXiv**: https://arxiv.org/abs/2607.19806 | **作者**: Kavin Aravindan, Arihant Rastogi | **年份**: 2026
- **批判摘要**：提出无需训练的方法，通过表示匹配净化转向向量。优化新转向向量以保留期望干预的下游表示，同时在原始向量失败的提示上匹配更安全的参考行为。被 ICML 2026 机制可解释性工作坊接收。关键贡献是直面转向的"外溢效应"——一个方向的转向可能破坏其他能力并造成过度拒绝。局限在于：表示匹配依赖一个"更安全的参考行为"的可用性，这在未知不安全行为上构成循环依赖。
- **与他篇关系**：填补 CircuitKIT (Seth & Gosalia 2026) 工具链中"安全转向"环节。与 Filus & Pokuciński (2026) 的 SAE 单义性形成前提关系——若转向向量所对应的潜在特征非单义，OPIUM 的"净化"可能只是转移而非消除副作用。

#### 8. Measuring Monosemanticity in Sparse Autoencoders via Latent Activation Coherence
- **arXiv**: https://arxiv.org/abs/2607.17770 | **作者**: Katarzyna Filus, Sebastian Pokuciński | **年份**: 2026
- **批判摘要**：提出 Tversky 单义性评分（TMS），一种无标签指标，将单义性操作化为二值化 SAE 潜在激活集的相干性。在 DINOv3、CLIP、BLIP2 特征上训练的 SAE 上评估，显示 TMS 比基于嵌入的替代方案更不受编码器各向异性影响。其贡献是给"单义性"这个机制可解释性的核心承诺一个可量化、可比较的度量。局限在于：TMS 度量的是激活模式的相干性，相干 ≠ 语义单义——一个稳定激活于多义特征的 SAE 潜在变量仍可得高分。
- **与他篇关系**：为 Puri et al. (2025) 的 FADE 提供"特征质量"的输入度量——FADE 评估特征-描述对齐，TMS 评估特征本身的单义性，两者构成"特征-描述"两端的评估栈。与 Bali & Stanley (2026) 的稳定性形成对比：稳定性是跨训练的，单义性是跨输入的，两者共同决定电路/特征的可监督性。

#### 9. Are Arithmetic Heuristic Neurons Form-Invariant? A Mechanistic Analysis of Symbols, Text, and Code in LLMs
- **arXiv**: https://arxiv.org/abs/2607.16693 | **作者**: Sharath Naganna, Tanvir Ahmed Sijan | **年份**: 2026
- **批判摘要**：研究算术启发式神经元在符号算术、自然语言应用题、Python 代码间是否形式不变。在三个 Llama-3 模型中发现一组紧凑神经元在三种格式间共享，跨格式激活迁移可恢复大多数错误预测，加减法准确率超 97%。关键发现是 LLM 算术处理存在跨模态电路共性，而非按格式分立。局限在于：仅覆盖加减法，乘除与更复杂运算的电路共性未证；且"形式不变"是在激活层面，权重层面的机制仍未解析。
- **与他篇关系**：提供"部分电路确实跨实例/跨格式稳定"的正面证据，与 Bali & Stanley (2026) 的"中间层不稳定"形成需调和的张力——可能解释是算术神经元属深层稳定头部。它是机制可解释性"特征监督"应用的具体靶点：若算术神经元可定位，则可对其做针对性监督。

### 子主题 C：Agent安全（间接注入、存储型 IPI、多智能体能力悖论、人主导框架）

#### 10. DualView: Preventing Indirect Prompt Injection in Personal AI Agents
- **arXiv**: https://arxiv.org/abs/2607.03821 | **作者**: Juhee Kim, Woohyuk Choi | **年份**: 2026
- **批判摘要**：揭示既往 Dual-LLM 防御（用符号替换不可信数据）的盲区——当 agent 将不可信数据写入文件系统后读回，它以"可信"身份返回，作者称之为"存储型间接注入（stored IPI）"。提出 DualView，将不可信数据追踪从 agent 上下文扩展到用户环境（文件系统/shell/网络/其他 agent），通过 AgentView（符号化）与 HumanView（原文）双视图，在 IPI 基准与 PinchBench 上阻断全部攻击含 stored IPI，且效用接近无防护基线。关键贡献是把"数据-指令分离"原则从上下文级提升到环境级。局限在于：双视图依赖工具钩子，对不经过钩子的旁路（如直接内存访问的恶意工具）无效；且部署为 OpenClaw 插件，跨框架可移植性未证。
- **与他篇关系**：是对经典 prompt injection 防御的实质性推进，直接更新 elective-e9/day-2 的 5 层防御（见 §6）。与 Liu & Holz (2026) 的能力悖论形成张力：DualView 假设"更细粒度的数据追踪=更安全"，但能力悖论表明在多智能体场景下更聪明的审计者反而降低安全性——DualView 的单 agent 防御在多 agent 组合下的失效模式未测。与 Weber & Taneja (2026) 的数字学徒框架互补：DualView 是技术防护层，数字学徒是自治权升级治理层。

#### 11. The Capability Paradox: How Smarter Auditors Make Multi-Agent Systems Less Secure
- **arXiv**: https://arxiv.org/abs/2605.17480 | **作者**: Qiqi Liu, Thorsten Holz | **年份**: 2026
- **批判摘要**：证明一个反直觉结果——在多智能体系统中，提升审计 agent 的能力反而降低系统整体安全性。机制是：更聪明的审计者能更好地区分"真实威胁"与"良性行为"，从而降低误报，但这同时让恶意 agent 的欺骗更难被察觉（因为审计者更倾向于"理性地"放过边界案例）。其贡献是把"安全=更聪明的检测"这一朴素信念证伪，揭示多智能体安全的 compositional 失效。局限在于：结果在特定审计博弈模型下成立，真实多智能体部署的审计博弈结构是否吻合需验证；且"能力"的操作化（更强 LLM）是否对应模型中的"理性"存疑。
- **与他篇关系**：直接挑战 DualView (Kim & Choi 2026) 的"更细追踪=更安全"假设在多智能体的延伸。与 Bowkis & Buhl (2026) 的"自动化对齐风险"形成共鸣——两者都指出"用更聪明的 AI 监督 AI"可能产生反效果，只是机制不同（能力悖论是博弈论，自动化对齐是优化压力集中错误）。

#### 12. The Digital Apprentice: A Framework for Human-Directed Agentic AI Development
- **arXiv**: https://arxiv.org/abs/2606.04321 | **作者**: Travis Weber, Rohit Taneja | **年份**: 2026
- **批判摘要**：提出实现可扩展、安全 AI 代理的框架，核心是"自治权是赢得的而非假设的"。三个组件：方法论捕获（内化人类隐性方法论）、授权（自治升级由明确人类批准门控）、持续对齐。数学建模质量框架并展示从数据漂移中恢复的能力。其贡献是把 agent 安全从"一次性对齐"重构为"渐进授权的治理过程"。局限在于：人类批准门控成为可扩展瓶颈——这正是可扩展监督欲解决的问题，框架未给出当人类审批能力不足时的逃逸路径。
- **与他篇关系**：为 DualView (Kim & Choi 2026) 的技术防护提供治理层封装。与 Lovén & Tarkoma (2026) 的校准不可能性形成直接张力——数字学徒的"持续对齐"依赖人类批准函数，而 Lovén 证明该函数的激励兼容性有内在极限。

### 子主题 D：对齐评估（自动化对齐风险、校准、机制可解释性驱动的评估）

#### 13. Automated alignment is harder than you think
- **arXiv**: https://arxiv.org/abs/2605.06390 | **作者**: Aleksandr Bowkis, Marie Davidsen Buhl | **年份**: 2026
- **批判摘要**：论证使用 AI 代理自动化对齐研究可能产生"令人信服但灾难性误导"的安全评估。识别三个核心风险：优化压力将错误集中在人类审查者最不可能发现的地方；代理产生非人类类错误（人类无法直觉识别）；共享权重使 AI 评估者之间的错误高度相关，比独立人类评估者更脆弱。其贡献是把"自动化对齐"的风险从"它可能做错"提升为"它的错会以人类最难发现的方式集中"。局限在于：论证偏概念性，未给出错误集中率的经验量化；且"非人类类错误"的可识别性可通过人机协作缓解，未充分讨论。
- **与他篇关系**：与 Liu & Holz (2026) 的能力悖论构成"自动化监督风险"的双证——一者证博弈论失效，一者证优化压力失效。它为 Gumbau Mezquita (2026) 的不可验证性提供了"即使自动化也无法逃逸"的工程注脚，并直接质疑 Sudhir et al. (2025) ASD 基准的自动化评估环节——若评估者自身错误高度相关，ASD 的可比较性被侵蚀。

#### 14. FADE: Why Bad Descriptions Happen to Good Features
- **arXiv**: https://arxiv.org/abs/2502.16994 | **作者**: Bruno Puri, Aakriti Jain | **年份**: 2025
- **批判摘要**：指出机制可解释性虽在自动化发现特征上进展显著，但缺乏标准化方法评估"特征-描述"对齐的有效性。提出 FADE（Feature Alignment to Description Evaluation），一个可扩展、模型无关的框架，通过 Clarity、Responsiveness、Purity、Faithfulness 四指标自动评估。关键发现：SAE 特征的描述生成比 MLP 神经元更难，揭示自动化可解释性管线的基础性挑战。其贡献是把"可解释性评估"本身变成可量化、可比较的实证科学。局限在于：四指标仍依赖外部 LLM 生成描述，描述质量本身成为混淆变量；且指标间的权衡（如 Purity vs Faithfulness）未给出聚合策略。
- **与他篇关系**：与 Filus & Pokuciński (2026) 的 TMS 构成"特征端-描述端"评估栈。它回应 Bowkis & Buhl (2026) 的"自动化对齐错误集中"担忧——FADE 提供了一种度量自动化可解释性管线失败模式的工具，使"错误在哪里集中"可被经验研究。与 Bali & Stanley (2026) 的稳定性研究互补：稳定性问"特征跨训练是否还在"，FADE 问"特征的描述是否还对"，两者共同决定可解释性发现的监督价值。

---

## cross_disciplinary_synthesis

本课题处于四个学科的交汇点——对齐（机器学习）、决策论/可计算性（逻辑与计算理论）、法律（AI 治理）、机制设计（微观经济学）——且这四者之间存在深层范式冲突，本深挖认为这些冲突是可发表研究的富矿。

**对齐的"证明安全"范式 vs 决策论的"不可能性"范式**。机器学习对齐的研究默认目标是"证明系统安全"——Constitutional AI、RLHF、机制可解释性都隐含一个承诺：通过更好的方法，安全可以被逼近甚至证明。但 Gumbau Mezquita (2026) 与 Lovén & Tarkoma (2026) 把决策论/可计算性的不可能性结果（Rice、Gödel、Trakhtenbrot）引入对齐，证明高表达性 AGI 的安全认证与激励兼容校准报告在一般情形下不可完全实现。范式冲突在于：ML 派把不可能性视为"工程可绕过的理想化"，理论派把它视为"必须改变问题表述的硬约束"。本深挖判断：对当前 LLM（受限语义、无自改写权重），定理的适用是部分的（见 §争议 2），但对"自主持续学习的 agent"——即 elective-e9/day-3 所讨论的 computer use 场景——定理开始咬合，因为此时系统语义在演化，落入动态不可验证范畴。

**机制设计的"激励兼容" vs 对齐的"价值内化"**。Lovén & Tarkoma 的不可能性本质是机制设计问题：委托人设计的批准函数无法同时最优监督与激励诚实报告。这与对齐的"价值内化"范式（让 agent 真正持有安全价值观）形成张力——机制设计接受 agent 可能欺骗并设计激励，对齐试图消除欺骗动机。Jiang & Chen (2026) 的协作求真是第三条路：既非纯激励也非纯内化，而是交互结构改造。但这三条路径的可扩展性排序尚无定论，且 Lovén 的定理暗示只要评分结构不变，协作也可能落入同一不可能性。

**法律的"过错责任" vs 对齐的"风险证明"**。EU AI Act（elective-e9/day-3 所教）采用基于风险分级的合规要求，高风险系统需"合格评定+CE 标志"——这隐含"安全可被认证"的法律预设。但 Gumbau Mezquita 的不可验证性定理直接挑战该预设：若 AGI 级系统的安全不可无误认证，CE 标志的法律意义何在？范式冲突在于：法律需要"可操作的合规断言"，而对齐理论给出"不可完全验证"。本深挖判断：解药在"分层可验证性"——对受限语义的子系统（如 NIST AI RMF 的 Measure 层度量）可给出有限保证，对整体行为只能给"尽力而为+持续监控"，这要求法律从"一次性认证"演进到"持续合规证据链"（这正是 Weber & Taneja 2026 数字学徒框架的治理直觉）。

**机制可解释性作为跨学科桥**。机制可解释性独特地连接 ML 与法律：它提供"白盒证据"，理论上可使安全认证从行为级（黑盒测试）深入到电路级（白盒审计）。Bali & Stanley (2026) 的稳定性研究、Puri et al. (2025) 的 FADE 都在为"白盒证据的可信度"建立度量。但若电路跨训练不稳定（Bali）且特征-描述对齐本身有系统偏差（FADE），则白盒证据的法律可采性受质疑。这是一个跨学科的开放问题：机制可解释性证据在 AI 治理合规中应占何种证据权重？该问题无法由单一学科回答——ML 提供证据，法律定义可采性标准，机制设计评估激励，决策论界定可知边界。

---

## controversies

### 争议 1：协作求真 vs 对抗辩论——哪条路径更可扩展？

- **正方（协作求真更可扩展）**：Jiang & Chen (2026) 的实证是硬证据——在同一判断任务上，协作分歧解决达 62.1% 而 standard debate 仅 49.2%，12.9 个百分点的差距是实质性的。理论上，协作框架降低了"说服裁判"的博弈负担，让模型聚焦于识别真实分歧点，符合人类专家共识形成的认知科学。支持者认为对抗辩论的"两个欺骗者+一个裁判"结构本质上是零和，难以扩展到 superhuman 能力区间（裁判能力不足时崩溃）。
- **反方（对抗辩论更可扩展）**：Sudhir et al. (2025) 的基准工作指出，单点实验不可泛化——Jiang 的判断任务可能恰好有利于协作结构。辩论范式的优势在于其激励兼容性有更形式化的基础（Irving 等人原工作的 debate truthfulness），且对抗压力天然暴露欺骗，而协作框架在存在一个策略性欺骗参与者时可能退化为"被协作利用"。更关键的是，Gumbau Mezquita (2026) 的不可验证性暗示：无论协作还是对抗，都不能逃逸形式化极限，因此"哪个更可扩展"可能是错误问题——两者都是"墙下能走多远"的局部优化。
- **本深挖判断**：证据当前略偏向正方，但以"可扩展性"裁决为时过早。Jiang 的 12.9 个百分点差距是真实的且值得追踪，但实验规模与任务多样性不足以支撑"协作普遍优于对抗"的强断言。博后级裁决应是：两条路径不是互斥而是互补——协作求真在"能力对等+诚实多数"场景占优，对抗辩论在"存在已知欺骗者"场景占优。可发表的研究方向是"混合协议"：在协作框架中引入对抗探针作为欺骗检测，用 ASD 指标（Sudhir）统一评估。把争议框定为"二选一"会遮蔽真正的可扩展性问题——即 Lovén & Tarkoma (2026) 的激励不可能性是否对两类协议同等约束。

### 争议 2：对齐不可验证性定理是否适用于当前 LLM？

- **正方（理论派，适用或即将适用）**：Gumbau Mezquita (2026) 的定理基于 Rice/Gödel/Trakhtenbrot，这些是计算理论的硬结果。虽然当前 LLM 是固定权重的推理机（不图灵完备），但一旦 LLM 被嵌入 agentic 框架（工具调用+持久记忆+自修改 prompt），系统整体的行为空间接近图灵完备。elective-e9/day-3 的 computer use 场景正是该情形。支持者认为，工程派"当前模型太小不必担心"的态度是能力外推的盲点——定理的价值在于界定"当我们逼近 AGI 时何处会撞墙"。
- **反方（工程派，当前不适用）**：当前 LLM 的语义是受限的——固定权重、有限上下文、无权重自修改。Rice 定理针对的是任意程序的语义性质不可判定，但 LLM 的"安全性质"是在一个有限权重空间上定义的，原则上可被一个足够强的认证器检查（尽管计算昂贵）。工程派认为理论派把"任意程序"的不可判定性误用到"特定受限系统"，制造了不必要的悲观。Bowkis & Buhl (2026) 的"自动化对齐风险"虽不否认定理，但把焦点转向"即使可验证，自动化也会集中错误"，暗示定理之争是次要的。
- **本深挖判断**：博后级裁决——双方各对一半，但反方对"当前 LLM"的论断更硬，正方对"agentic LLM"的论断更硬。关键区分是"静态认证 vs 动态认证"（Gumbau Mezquita 自己提出）：对固定权重 LLM，反方正确，定理是远虑不是近忧；对持续学习/自修改 agent，正方正确，定理已开始咬合。因此争议的真正价值不在"适用与否"的二元判断，而在迫使研究者明确"我认证的是静态系统还是动态系统"——这直接映射到 NIST AI RMF（elective-e9/day-3）的 Govern 层应区分"上线前静态认证"与"运行期动态监控"，前者可严，后者只能"尽力而为+持续可解释性监控"。把定理当作"设计约束"而非"悲观许可证"是研究者应有的姿态。

### 争议 3（补充）：自动化对齐是加速还是放大风险？

- **正方（加速派）**：自动化对齐（用 AI 代理做对齐研究）是人类对齐能力瓶颈的必要逃逸。Sudhir et al. (2025) 的 ASD 基准、Puri et al. (2025) 的 FADE 评估框架都依赖 LLM-as-judge，本质是自动化对齐工具。拒绝自动化等于放弃可扩展性。
- **反方（放大派）**：Bowkis & Buhl (2026) 给出三重风险——错误集中、非人类类错误、权重共享导致错误相关。Liu & Holz (2026) 的能力悖论是独立佐证：更聪明的自动化审计者反降安全性。两者共同暗示自动化对齐可能制造"看似可信实则系统性偏差"的安全剧场。
- **本深挖判断**：放大风险是真实的，但"拒绝自动化"不可行（人类瓶颈是硬约束）。博后级裁决：自动化对齐必须配"去相关化"——多个独立权重/架构的评估者集成（对抗 Bowkis 的相关性风险）、人类校准锚点嵌入（对抗非人类类错误）、显式标注自动化评估的不确定区间（对抗错误集中）。FADE 的四指标是"标注不确定区间"的雏形。这把争议从"是否自动化"推向"如何安全地自动化"，是更可发表的研究框架。

---

## research_roadmap

1. **近-可攻克：存储型 IPI 的多智能体扩展基准**。问题：DualView (Kim & Choi 2026) 在单 agent 验证了 stored IPI 防御，但多智能体场景下不可信数据经 agent 间消息传递的传播路径未基准化。为何重要：elective-e9/day-2 的 5 层防御假设单 agent，而产业部署多为多智能体。可行路径：扩展 PinchBench 到 2-N agent 拓扑，度量 DualView 在 agent 间消息链路的 stored IPI 拦截率，并与能力悖论（Liu & Holz）预测的"更聪明审计者更不安全"对照。6-9 个月可投稿应用安全会议。

2. **近-可攻克：SAE 特征-描述对齐的失败模式图谱**。问题：FADE (Puri 2025) 给出四指标，但特征类型（算术/情感/安全相关）与失败模式（Clarity 低 vs Faithfulness 低）的映射未系统化。为何重要：特征监督是机制可解释性落地对齐的桥梁，失败模式图谱直接指导 CircuitKIT (Seth & Gosalia) 的诊断模块。可行路径：在 Llama-3 与 Mistral 上对 SAE 特征按 FADE 四指标聚类，交叉 TMS 单义性（Filus），产出"特征类型×失败模式"矩阵。6 个月可投稿可解释性工作坊。

3. **中-可攻克：协作求真与对抗辩论的混合 oversight 协议**。问题：争议 1 指出协作与对抗各有所长，但无混合协议被形式化与基准化。为何重要：这是逃逸"二选一"争议的直接路径，且可扩展监督基准（Sudhir ASD）已提供评估底座。可行路径：设计"协作为主+对抗探针为欺骗检测"的协议，在 ASD 指标上与纯协作（Jiang）与纯对抗（debate）三向比较，理论侧分析 Lovén-Tarkoma 激励不可能性对混合协议的约束。12-15 个月可投稿 ICML/NeurIPS。

4. **中-可攻克：机制可解释性证据的 AI 治理合规证据权重**。问题：cross_disciplinary 综合指出，机制可解释性白盒证据在法律合规中应占何种证据权重无定论。为何重要：EU AI Act 高风险系统的"合格评定"需要证据链，白盒证据的纳入会改变合规实践。可行路径：联合法学研究者，构造"白盒证据+黑盒测试+红队"三源证据的贝叶斯融合框架，用 Bali 稳定性与 FADE 对齐质量量化白盒证据的先验可信度，产出跨学科框架论文。12-18 个月，适合 ML+Law 跨学科期刊。

5. **远-需突破：动态 AGI 的"分层可验证性"形式化**。问题：Gumbau Mezquita (2026) 证明动态 AGI 不可完全验证，但"哪些子性质可验证、哪些不可"的分层结构未形式化。为何重要：这是把不可验证性定理从"悲观许可证"转化为"设计约束"的关键一步，直接决定 NIST AI RMF Govern 层对动态 agent 的认证标准。可行路径：借鉴类型系统分层（强校验 vs 运行时检查），形式化"静态可认证子性质集合"与"动态仅可监控子性质集合"的分离定理，并给出后者的人工监督逃逸条件（连接 Weber-Taneja 数字学徒）。24-36 个月，需理论与工程双轨，适合博士论文级工作。

6. **远-需突破：自动化对齐的去相关化集成框架**。问题：争议 3 指出自动化对齐的错误相关性（Bowkis）与能力悖论（Liu）是放大风险根源，但"去相关化"无形式化框架。为何重要：人类对齐瓶颈是硬约束，自动化不可逆，去相关化是唯一可行方向。可行路径：形式化"评估者独立性"度量（权重不同+架构不同+训练数据不同的量化），构造集成评估者的错误相关性上界证明，并在 Sudhir ASD 基准上经验验证去相关化的 ASD 提升。24-30 个月。

---

## connection_to_curriculum

1. **elective-e9/day-1（价值对齐与 Constitutional AI）**：本深挖 § 争议 2 + § cross_disciplinary 更新该 Day 的关键认知锚点。Day-1 `notes.md` 已声明"对齐评估是发现问题的手段，不能证明已对齐"——本深挖把这句朴素声明升级为有形式化支撑的论断：Gumbau Mezquita (2026) 的不可验证性定理给出了"为何不能证明"的数学理由，Lovén & Tarkoma (2026) 给出了激励兼容的内在极限。更新点：(a) 在 `notes.md` 的"2026 前沿补充"节新增"对齐不可完全验证"小节，引用本深挖 § 争议 2，并修改 HHH 评估的定位表述——从"对齐评估不能证明已对齐"改为"对齐评估在静态系统给有限保证、在动态系统仅给监控信号（Gumbau Mezquita 静态/动态区分）"；(b) 把 Jiang & Chen (2026) 协作分歧解决作为"RLAIF 之后的 oversight 范式"加入 RLHF→CAI→DPO 演进表，新增"协作求真"列。

2. **elective-e9/day-2（Prompt Injection 与红队）**：本深挖 § paper_landscape 子主题 C 直接更新该 Day 的 5 层防御。Day-2 `notes.md` 的 5 层防御（L1 输入过滤 ~ L5 权限隔离）假设单 agent 且未覆盖 stored IPI。更新点：(a) 在 L1 与 L2 之间新增"L1.5 不可信数据环境级追踪"，引用 DualView (Kim & Choi 2026) 的 AgentView/HumanView 双视图，覆盖 stored IPI 攻击向量；(b) 在"5 层防御"后新增"多智能体失效模式"小节，引用能力悖论（Liu & Holz 2026），说明更聪明审计者反降安全，要求 5 层防御在多 agent 场景重新基准化；(c) 在红队工具链补充 PI-Hunter（He & Miculicich 2026，自动红队定位注入点）作为 garak/PyRIT 的补充；(d) `starter.ipynb` 的 TODO5（红队仿真）应加一个 stored IPI 攻击向量（agent 写入恶意内容后读回）。

3. **elective-e9/day-3（NIST AI RMF 与治理）**：本深挖 § cross_disciplinary + § 争议 2 更新该 Day 的治理框架。Day-3 `notes.md` 把 NIST Govern 层呈现为"组织保障"——本深挖补充 Govern 层的"可验证性分层"设计约束。更新点：(a) 在"关键回顾 1 NIST 四步循环"后新增"可验证性分层"小节，区分"上线前静态认证"（可严，Gumbau Mezquita 静态情形）与"运行期动态监控"（尽力而为，动态情形），并映射到 GOVERN-5 全生命周期治理；(b) 在 Measure 层新增"自动化对齐风险"（Bowkis & Buhl 2026），说明自动化评估的错误相关性侵蚀 ASD 可比性，要求 Measure 层用多独立评估者集成；(c) computer use 治理风险表新增"动态不可验证性"行，连接 Gumbau Mezquita 动态情形；(d) `solution.ipynb` 的 enterprise_security_check 加一个"可验证性分层"控制项。

4. **skill-5/day-3（Agent 评估与 Benchmarking）**：本深挖 § paper_landscape 子主题 A + § 争议 1 更新该 Day 的 LLM-as-a-judge 评估。Day-3 `notes.md` 的 GEval 假设单 judge——本深挖引入协作 vs 对抗的 oversight 协议选择。更新点：(a) 在"2026 前沿 LLM-as-a-judge"节新增"协作求真 vs 对抗辩论"小节，引用 Jiang & Chen (2026) 与 Sudhir et al. (2025) ASD 指标，说明 agent-as-judge 的协议结构（单 judge vs 协作 vs 对抗）是评估质量的关键变量；(b) 在六大指标表新增"第 7 指标：oversight 协议 ASD"，把协作/对抗的选择做成可度量决策；(c) 在 `tutorial.ipynb` 苏格拉底追问新增第 5 轮"你的 judge 协议是否在你的 agent 能力区间仍 truthful？"；(d) 在 `practice.md` 的 D1（GEval）drill 加"swap-positions 校准"以对齐位置偏差（呼应 LLM-as-judge 三大偏差）。

5. **skill-3/day-1（因果推断基础）**：本深挖 § cross_disciplinary 更新该 Day 的"因果阶梯与可知性"认知。Day-1 `notes.md` 的 Pearl 因果阶梯（L1 关联/L2 干预/L3 反事实）隐含"因果可识别"乐观——本深挖引入对齐的不可验证性作为"可知性的形式化极限"对照。更新点：(a) 在"关键回顾 1 因果阶梯"后新增"可知性的双重极限"小节——因果推断的极限是"混杂未阻断则不可识别"（后门准则），对齐的极限是"高表达性系统安全不可无误认证"（Gumbau Mezquita）。两者都是"我们能知道什么"的认识论问题，前者是统计的，后者是可计算的；(b) 说明机制可解释性（Bali 稳定性、FADE 对齐质量）是"在可知性极限内最大化白盒证据"的因果式努力——电路稳定性类比"估计量的方差"，FADE 对齐质量类比"估计量的偏差"；(c) 在 `reading.md` 补充 Gumbau Mezquita 2026 作为"因果可知性"的跨学科延伸阅读。

---

## teaching_seminar

### 研讨班 1（90分钟）：可扩展监督——协作求真、对抗辩论与不可验证性之墙

- **前置阅读**：(1) Jiang & Chen 2026 (2607.01251) 协作分歧解决；(2) Sudhir et al. 2025 (2504.03731) oversight 基准；(3) Gumbau Mezquita 2026 (2606.28639) 不可验证性定理（重点读 §1-3 静态/动态区分）。可选：Lovén & Tarkoma 2026 (2605.07671) 校准不可能性。
- **讨论问题**：(1) Jiang 的 62.1% vs 49.2% 差距，在何种任务结构下会反转？协作框架在存在一个策略性欺骗者时如何退化？(2) Sudhir 的 ASD 指标是否捕捉了"协议在 superhuman 能力区间的崩溃"？若否，应补什么维度？(3) Gumbau Mezquita 的静态/动态区分对当前 LLM（固定权重）与 agentic LLM（工具+记忆）分别意味着什么？(4) Lovén-Tarkoma 的激励不可能性对协作与对抗协议是否同等约束？(5) 若对齐不可完全验证，NIST AI RMF 的"合格评定"应如何重构？
- **活动**：前 45 分钟论文深读（Jiang 与 Gumbau Mezquita 对照阅读，提取"协作假设"与"可验证性假设"的隐性前提），中 30 分钟辩论（正方"协作求真更可扩展" vs 反方"不可验证性使协议之争次要"），后 15 分钟研究问题收敛。
- **产出**：1 页研究问题备忘，包含至少 2 个可发表 RQ（如"混合协议在 ASD 上的表现"、"静态/动态可验证性的形式化分层"），及对应的前置工作估计（近/中/远）。

### 研讨班 2（90分钟）：机制可解释性作为 Agent 安全基础设施——从电路稳定性到存储型注入

- **前置阅读**：(1) Bali & Stanley 2026 (2602.16740) 注意力头稳定性；(2) Kim & Choi 2026 (2607.03821) DualView 存储型 IPI；(3) Puri et al. 2025 (2502.16994) FADE 特征-描述评估。可选：Liu & Holz 2026 (2605.17480) 能力悖论；Bowkis & Buhl 2026 (2605.06390) 自动化对齐风险。
- **讨论问题**：(1) Bali 的"中间层头部最不稳定"对 CircuitKIT 的跨模型电路迁移意味着什么？机制可解释性作为"白盒监督"在何种稳定性阈值下可用？(2) DualView 的双视图防御在多智能体场景下，与能力悖论（Liu）的预测如何冲突？是否存在"更细追踪反降安全"的阈值？(3) FADE 的四指标中，哪个最可能被一个策略性欺骗的模型操纵？特征-描述评估的对抗鲁棒性如何？(4) 自动化对齐（Bowkis）的错误相关性与 LLM-as-judge 的自偏好如何叠加？多独立评估者集成能去相关到什么程度？(5) 机制可解释性证据在 AI 治理合规中应占何种证据权重？
- **活动**：前 40 分钟三篇论文的"前提-方法-局限"结构化速读，中 30 分钟小组活动（每组设计一个"机制可解释性驱动的 agent 安全监测器"草图，须指明用哪些电路/特征、如何应对稳定性不足、如何在多 agent 场景部署），后 20 分钟跨组互评。
- **产出**：1 页"机制可解释性安全监测器"设计草图，含稳定性假设、对抗鲁棒性分析、与 NIST AI RMF Measure 层的对接点；以及 2 个开放研究问题（如"SAE 特征作为 stored IPI 检测器的可行性"、"电路稳定性阈值下的白盒证据可采性"）。

---

## references

1. Bali, K., & Stanley, J. (2026). Quantifying LLM Attention-Head Stability: Implications for Circuit Universality. arXiv:2602.16740. https://arxiv.org/abs/2602.16740
2. Seth, P., & Gosalia, H. (2026). CircuitKIT: Circuit Discovery, Evaluation, and Application Toolkit for Mechanistic Interpretability. arXiv:2607.19317. https://arxiv.org/abs/2607.19317
3. Aravindan, K., & Rastogi, A. (2026). OPIUM: Mitigating Steering Externalities and Over-Refusal via Dual Objective Latent Optimization. arXiv:2607.19806. https://arxiv.org/abs/2607.19806
4. Filus, K., & Pokuciński, S. (2026). Measuring Monosemanticity in Sparse Autoencoders via Latent Activation Coherence. arXiv:2607.17770. https://arxiv.org/abs/2607.17770
5. Naganna, S., & Sijan, T. A. (2026). Are Arithmetic Heuristic Neurons Form-Invariant? A Mechanistic Analysis of Symbols, Text, and Code in LLMs. arXiv:2607.16693. https://arxiv.org/abs/2607.16693
6. Jiang, Y., & Chen, C. (2026). Collaborative Disagreement Resolution for Scalable Oversight. arXiv:2607.01251. https://arxiv.org/abs/2607.01251
7. Gumbau Mezquita, J. P. (2026). The Unverifiability of Artificial General Intelligence (AGI) Alignment, Static and Dynamic: From Trakhtenbrot's Wall to the Safety-Generality Tension. arXiv:2606.28639. https://arxiv.org/abs/2606.28639
8. Bowkis, A., & Davidsen Buhl, M. (2026). Automated alignment is harder than you think. arXiv:2605.06390. https://arxiv.org/abs/2605.06390
9. Weber, T., & Taneja, R. (2026). The Digital Apprentice: A Framework for Human-Directed Agentic AI Development. arXiv:2606.04321. https://arxiv.org/abs/2606.04321
10. Lovén, L., & Tarkoma, S. (2026). The Endogeneity of Miscalibration: Impossibility and Escape in Scored Reporting. arXiv:2605.07671. https://arxiv.org/abs/2605.07671
11. Sudhir, A. P., & Kaunismaa, J. (2025). A Benchmark for Scalable Oversight Protocols. arXiv:2504.03731. https://arxiv.org/abs/2504.03731
12. Kim, J., & Choi, W. (2026). DualView: Preventing Indirect Prompt Injection in Personal AI Agents. arXiv:2607.03821. https://arxiv.org/abs/2607.03821
13. Liu, Q., & Holz, T. (2026). The Capability Paradox: How Smarter Auditors Make Multi-Agent Systems Less Secure. arXiv:2605.17480. https://arxiv.org/abs/2605.17480
14. Puri, B., & Jain, A. (2025). FADE: Why Bad Descriptions Happen to Good Features. arXiv:2502.16994. https://arxiv.org/abs/2502.16994

---

*本文件由 v10.0 旗舰课题深挖层生成。14 篇论文中 10 篇来自 v9.0 `_frontier_corpus/elective-e9-ai-safety-alignment.md` 语料库（2 篇 verified + 8 篇 unverified），4 篇来自本深挖 arXiv 深研（3 篇经 abstract 页验证：2504.03731 / 2607.03821 / 2502.16994 + 1 篇搜索结果页确认：2605.17480）。所有 arXiv ID/标题/作者均经语料库或 WebFetch 真实搜索结果确认，无编造。面向博后/教授级研讨。*
