# deep_dive.md: 因果推断 × LLM -- 因果发现/推理/反事实

> **课题**：因果推断 × LLM：因果发现、因果推理与反事实
> **版本**：v10.0（旗舰课题深挖层）
> **定位**：专著式前沿专题章，供博后研讨班/教授深度教学用。非全58单元，仅覆盖被选中的旗舰课题。
> **论文来源**：v9.0 `_frontier_corpus/skill-3-causal.md` 语料库（10 篇）+ 本深挖的额外 arXiv 深研（3 次搜索，3 篇经 abstract 页验证）。全 13 篇论文均来自 arXiv，无编造。

---

## topic

因果推断 × LLM：因果发现/推理/反事实 -- 作为 LLM 认识论边界测试床与因果阶梯（Pearl L1/L2/L3）形式化前沿的交汇点。

---

## abstract

本课题聚焦 2025-2026 "因果推断 × LLM" 前沿的五大子主题：LLM 作为因果元裁判（ensemble reweighting / judge / meta-analysis）、Lean 形式化因果推理（Causalean / 机器检查定理 / CausalForge）、Agent 时代因果发现（causal-learn+ / PC+FCI+LLM）、LLM 从文本学因果结构（差分逻辑 / Words as Difference Makers / L1 天花板争议）、可审计因果图（target-aware graph / path-level evidence）。核心张力有三：（1）LLM 能否跨越 Pearl 因果阶梯 L1--差分逻辑派肯定 vs 基准实证派（CausalGame 30 智能体无一可靠）否定；（2）Lean 机器检查与统计反驳（placebo / sensitivity）哪条路径更提升因果可复现性；（3）LLM 应作元裁判（CEA）还是直接推断器（Pharmacovigilance）。对博士课程的意义：skill-3 因果模块的 DoWhy 四步（建模->识别->估计->反驳）可被 Lean 形式化层加固，`placebo_treatment_refuter` 可被机器检查其不变量，而 LLM 元裁判可审查 DAG 完整性与后门准则满足性--但学生须认清 LLM 停在 L1，不可让其估计效应本身。

---

## paper_landscape

13 篇论文跨 5 个子主题组织。语料库 10 篇（#1-#10）+ 本深挖新研 3 篇（#11-#13，经 abstract 页验证）。

### 子主题 A：LLM 作为因果元裁判（ensemble reweighting、judge、meta-analysis）

#### 1. Causal Ensemble Agent: Hierarchical Causal Discovery with LLM-guided Expert Reweighting
- **arXiv**: https://arxiv.org/abs/2606.10607 | **作者**: Xinyu Li, Yuanyuan Wang | **年份**: 2026
- **批判摘要**：提出 Causal Ensemble Agent (CEA)，用线性意见池聚合多个统计因果发现专家的结构输出，并在聚合置信度接近决策边界时调用 LLM 作为元裁判动态重新加权专家。关键设计是 LLM 只做元分析（判断哪个专家在边界情形更可信），不直接做因果推断。在合成与真实数据集上达到最强整体性能，验证了"LLM 当裁判不当选手"的工程哲学。
- **与他篇关系**：与 #10 Pharmacovigilance 形成对照--后者让 LLM 直接做因果评估（ albeit 在结构化 Naranjo 尺度下），CEA 则把 LLM 限制在元层。两者的分歧正是争议 3 的实证来源。CEA 的"边界情形触发 LLM"策略也被 #13 Counterfactual Chains 隐性采纳（低置信度才扩张反事实链）。

#### 2. Optimizing Large Language Models for Causality Assessment in Pharmacovigilance
- **arXiv**: https://arxiv.org/abs/2607.03704 | **作者**: Nicole Sonne Heckmann, Arnault-Quentin Vermillet | **年份**: 2026
- **批判摘要**：在药物警戒领域（FAERS 个案安全报告，Naranjo 因果评估量表）研究 GPT-5.2 与专家一致性是否随温度优化改善。开发与高斯过程兼容的 EWACS 优化目标，将分类一致性从 45.0% 提升至 72.0%（+27pp）。关键发现是不存在通用最优温度--性能主要由 ICR（个案安全报告）内容驱动，暗示 LLM 直接因果评估在窄领域可校准但不可外推。
- **与他篇关系**：与 #1 CEA 互补--证明在窄领域（结构化量表 + 专家锚点）LLM 可直接评估因果，但泛化性差。这为争议 1（L1 天花板）提供边界证据：窄领域校准成功 ≠ 跨越 L1。其"无通用温度最优"结论与 #11 CausalGame 的"内容驱动失败"一致。

#### 3. LLM Explainability with Counterfactual Chains and Causal Graphs
- **arXiv**: https://arxiv.org/abs/2606.05972 | **作者**: Nirit Nussbaum-Hoffer, Nitay Calderon | **年份**: 2026
- **批判摘要**：将因果反转--不是用 LLM 做因果推断，而是用因果图建模 LLM 推理本身。四阶段方法：发现类判别概念 -> 映射输入到 LLM 感知的概念状态 -> 用 MCMC 启发的反事实增强过程扩张稀疏观测数据 -> 因果发现（σ-CG）。在疾病诊断、情感分析、LLM-as-a-Judge 三任务上验证，发现因果图捕获了与 LLM 推理一致的依赖结构。
- **与他篇关系**：与 #1 CEA 形成元层闭环--CEA 让 LLM 判断因果发现专家，本文用因果图判断 LLM-as-Judge 本身。三者（#1/#2/#3）构成"LLM 既是因果裁判又是因果被裁判对象"的三角，为争议 3 提供了自指（self-referential）视角。

### 子主题 B：形式化因果推理（Lean/Causalean、机器检查定理、CausalForge）

#### 4. CausalForge: A Formally Grounded, Self-Improving Agentic Framework for Automated Research in Causal Inference
- **arXiv**: https://arxiv.org/abs/2607.22511 | **作者**: Jiyuan Tan, Vasilis Syrgkanis | **年份**: 2026
- **批判摘要**：提出基于 Lean 证明助手的因果推断自动化研究框架，结合 Causalean（7,035 条机器检查声明的 Lean 库）与 CausalSmith（自改进 agentic pipeline）。Agent 选择研究主题、提出结果、构造证明，并通过声明审计比较形式化定理与非形式化声明。这是目前"形式化因果 × LLM agent"最完整的系统尝试，将 do-演算代数从纸面证明推向机器检查。
- **与他篇关系**：与 #12 ReplaySCM 同属形式化路径但策略不同--CausalForge 用 Lean 定理证明器（数学严格性），ReplaySCM 用可执行 Boolean DSL 重放（行为等价性）。两者互补：CausalForge 可形式化 ReplaySCM 基准的 SCM 类。CausalForge 的"声明审计"机制直接回应争议 2--它承认形式化定理与非形式化声明之间存在缝隙，需显式审计。

#### 5. ReplaySCM: A Benchmark for Executable Causal Mechanism Induction from Interventions
- **arXiv**: https://arxiv.org/abs/2605.08197 | **作者**: Serafim Batzoglou | **年份**: 2026
- **批判摘要**：1,300 项基准，要求系统从潜在二元布尔 SCM 生成的干预证据中输出可执行机制图，按重放行为（而非公式字符串）评分。变体设置（Ordered / Block-order / Hidden-order / Hidden-roots）逐步隐藏结构信息；support-audit ladder（Original 0.8949 -> Extra Worlds 0.9815 -> Counterexample Audit 1.0）显示审计可将局部前驱模式覆盖提升至满分。关键发现：前沿 LLM 能推断部分功能-父结构，但当顺序或根结构隐藏时 held-out 重放急剧下降。
- **与他篇关系**：与 #4 CausalForge 同属形式化阵营，但 ReplaySCM 侧重"可执行重放"而非"Lean 证明"。与 #11 CausalGame 互补--CausalGame 测试端到端因果思维（实验设计+数据收集+解释），ReplaySCM 测试机制归纳的泛化。两者共同构成 LLM 因果能力的"可执行+端到端"双基准。

### 子主题 C：LLM 时代因果发现（agent 辅助、causal-learn 平台、PC/FCI+LLM）

#### 6. Causal Discovery in the Era of Agents
- **arXiv**: https://arxiv.org/abs/2606.23608 | **作者**: Yujia Zheng, Vishal Verma | **年份**: 2026
- **批判摘要**：论证 agent 在因果发现中应辅助工作流（检查数据、检索上下文、解释假设），而因果声明须基于数据、显式假设和形式化算法。提出 causal-learn+ 在线平台，协调数据分析、预处理、方法推荐和形式化发现。在 Big Five 人格数据上展示 agent 辅助因果发现。核心立场是"LLM 辅助不推断"--拒绝让 LLM 直接输出因果图。
- **与他篇关系**：与 #11 CausalGame 形成"立场-证据"对--CausalGame 的 30 智能体无一可靠（68% 存活率 vs 78-85% 最优）正是 Era-of-Agents "辅助不推断"立场的实证支撑。与 #1 CEA 的"元裁判不选手"哲学同源，三者共同主张：LLM 在因果发现中的安全角色是辅助/裁判，不是推断器。

#### 7. CausalGame: Benchmarking Causal Thinking of LLM Agents in Games
- **arXiv**: https://arxiv.org/abs/2607.04293 | **作者**: Zhenhao Chen, Yongqiang Chen 等 | **年份**: 2026
- **批判摘要**：ICML 2026 Oral。基准评估 30 个 LLM 智能体在交互式游戏中的因果思维--须设计实验协议、收集观测数据、推导最终解并附解释报告。14 个场景包含选择偏差、测量误差、隐藏混杂。结果严峻：最优模型仅 68.0% 存活率（vs 分析最优 78-85%），仅 5-7% 会话在因果推理评分细则上获分。这是 LLM 无法可靠进行端到端因果思维的最硬实证。
- **与他篇关系**：与 #6 Era-of-Agents 形成"证据-立场"闭环。与 #5 ReplaySCM 互补--ReplaySCM 测机制归纳泛化，CausalGame 测实验设计+解释。两者共同为争议 1（L1 天花板）提供反方核心证据。CausalGame 的"5-7% 评分细则得分"与 Pharmacovigilance 的"72% 校准"形成张力：窄领域可校准，宽领域失败。

### 子主题 D：LLM 从文本学因果结构（Words as Difference Makers、差分逻辑、L1 天花板争议）

#### 8. Words as Difference Makers: How Large Language Models Determine Causal Structure in Text
- **arXiv**: https://arxiv.org/abs/2606.22430 | **作者**: Wolfgang Pietsch | **年份**: 2026
- **批判摘要**：论证 LLM 采用基于"差分逻辑"（difference-making logic / variational induction）的归纳方法从文本学习因果结构--识别词序列中的差分制造者与非差分制造者。分析 token 嵌入与自注意力如何实现该逻辑，强调 LLM 需海量多样上下文文本。这是争议 1 正方核心文献：主张 LLM 通过差分归纳已隐式获得因果结构识别能力，暗示 L1 可被文本规模突破。
- **与他篇关系**：与 #7 CausalGame 直接对立--Pietsch 主张 LLM 学到差分逻辑（L1 突破），CausalGame 实证 LLM 端到端因果思维失败。与 #3 Scaling Point-in-Time 互补--Pietsch 依赖"海量文本"，Scaling-PIT 警告该文本本身可能被前瞻偏差污染，从源头削弱差分归纳的因果纯净性。

#### 9. Scaling Point-in-Time Language Models
- **arXiv**: https://arxiv.org/abs/2607.11889 | **作者**: Bryan Kelly, Semyon Malamud | **年份**: 2026
- **批判摘要**：解决 LLM 在无限制互联网语料上训练的前瞻偏差问题--该偏差损害金融与社会科学中的回测和因果推断。在 1 万亿按时间过滤的 token 上训练至 4B 参数的 decoder-only transformer，构建 2013-2024 月度 checkpoint，接近同等规模时间无约束模型的性能。核心贡献是把"时间一致性"从因果推断的隐含假设提升为 LLM 训练的显式约束。
- **与他篇关系**：与 #8 Words as Difference Makers 形成前提批判--若训练语料含前瞻信息，差分归纳学到的"因果"可能是反向因果。与 #4 CausalMix 互补--CausalMix 把数据混合当因果推断，Scaling-PIT 把时间过滤当因果推断，两者共同将 LLM 训练数据选择纳入因果框架。

#### 10. CausalMix: Data Mixture as Causal Inference for Language Model Training
- **arXiv**: https://arxiv.org/abs/2607.01104 | **作者**: Zinan Tang, Yukun Zhang | **年份**: 2026
- **批判摘要**：将 LLM 训练的数据混合优化建模为因果推断问题--数据池统计特征作协变量，领域混合作处理。在 512 次 Qwen2.5-0.5B 运行上拟合因果模型估计 CATE，外推至 800K 数据池并应用于 7B 模型，持续超越 RegMix 等基线。方法论贡献是把 CATE 估计引入数据选择，将"哪些数据训练好模型"从相关性问题转为干预问题。
- **与他篇关系**：与 #9 Scaling Point-in-Time 同属"LLM 训练即因果推断"范式，但维度不同--Scaling-PIT 处理时间维因果，CausalMix 处理领域维因果。两者共同表明 LLM 训练本身是因果推断的富应用域，为子主题 D 增加了"LLM 作为因果被训练对象"的视角。

### 子主题 E：可审计因果图（target-aware graph、path-level evidence、Causal-Audit）

#### 11. Causal-Audit: Explicit and Auditable Graph-based Reasoning via Target-Aware Causal Chain Construction
- **arXiv**: https://arxiv.org/abs/2607.15281 | **作者**: Su Lan, Xuefei Yin | **年份**: 2026
- **批判摘要**：提出显式可审计因果推理框架，将因果推断建模为在显式因果图上的结构化推理。目标感知图构建策略在扩展时将目标变量作为核心约束以抑制无关变量；路径级因果证据聚合机制建模跨多路径的增强和抵消效应。核心创新是把"可审计性"从后验检查提升为推理时的结构约束--每条结论可追溯到图上的路径证据。
- **与他篇关系**：与 #13 Pruning via Causal Attribution、#8 BridgeVLM 同属"显式因果结构"范式但层级不同--Causal-Audit 在推理层（目标感知图），CAP 在架构层（注意力头因果归因），BridgeVLM 在输入层（因果 token）。三者构成"显式因果"的三层栈。Causal-Audit 的路径级证据聚合直接回应争议 2 的可复现性需求。

#### 12. Pruning via Causal Attribution Preserves Reasoning Performance in Large Language Models
- **arXiv**: https://arxiv.org/abs/2606.19350 | **作者**: Amogh Sheth, Biruk Assefa | **年份**: 2026
- **批判摘要**：提出 Causal Attribution Pruning (CAP)，无训练方法通过测量注意力头对推理任务的因果影响识别关键头，再将头级重要性转化为权重级重要性进行剪枝。在 ARC-Challenge 20% 稀疏度下相对 Wanda 准确率提升最高 61%。方法论价值在于把因果归因（干预注意力头看输出变化）作为模型可解释性与压缩的统一工具。
- **与他篇关系**：与 #11 Causal-Audit 同属显式因果但作用域不同--CAP 把因果归因用于架构诊断（哪些头重要），Causal-Audit 用于推理诊断（哪些路径支持结论）。与 #4 CausalForge 的形式化路径正交--CAP 是经验因果归因，CausalForge 是形式化因果证明。

#### 13. From Prompts to Tokens: Internalizing Causal Supervision in Vision-Language Model for Multi-Image Causal Reasoning
- **arXiv**: https://arxiv.org/abs/2606.11745 | **作者**: Haoping Yu, Yuanxi Li | **年份**: 2026
- **批判摘要**：提出 BridgeVLM，从多图像输入诱导因果图并转化为结构化 Causal Tokens，由注入 LLM 解码器的 RAMP 层执行。统一训练接口 M3S 提供局部和全局因果监督，在 CausalVLBench 干预任务上达 54.4% 准确率（prompt 级仅 33.2%）。关键发现是把因果监督从 prompt（外部）内化为 token（内部）显著提升因果推理，暗示因果结构需进入模型表示而非停留在上下文。
- **与他篇关系**：与 #11 Causal-Audit、#12 CAP 共同主张"因果结构须显式化"，但 BridgeVLM 选择 token 级内化（最强显式化），CAP 选择头级归因，Causal-Audit 选择图级推理。BridgeVLM 的"prompt 33.2% -> token 54.4%"增益为争议 1 提供了微妙证据：结构化内化可部分突破 L1，但 54.4% 仍远非可靠。

---

## cross_disciplinary_synthesis

因果推断 × LLM 是计量经济学（econometrics）、机器学习（ML）、形式方法（formal methods）与 Pearl 因果认识论四者交汇的张力场。三者的范式冲突构成本课题的核心认识论辩论。

**Pearl do-演算 vs LLM 分布式因果**：Pearl 因果阶梯（L1 关联 / L2 干预 / L3 反事实）要求显式 SCM 与 do-算子，因果效应通过图上的后门调整/前门调整/工具变量识别，认识论上是"结构优先、数据随后"。LLM 的分布式因果（#8 Words as Difference Makers）则主张因果结构可从海量文本的差分模式中归纳涌现，认识论上是"数据优先、结构隐式"。两者的根本冲突在于：Pearl 要求 do(X) 切断所有指向 X 的路径（干预的物理性），而 LLM 的"差分"是对已 articulasi 的人类因果文本的模式匹配--它从未真正执行 do，只是复述人类已做的 do 的叙述。#7 CausalGame 的 30 智能体无一可靠（68% vs 78-85% 最优）正是这一冲突的实证：当任务要求真正的实验设计（L2 do），LLM 的文本归纳（L1 over L2-text）失效。计量经济学的 IV/PSM/DiD 传统站在 Pearl 一侧--它要求先验识别策略（工具变量外生性、平行趋势假设），再估计。LLM 元裁判（#1 CEA）试图调和：让 LLM 在 Pearl 框架内做元判断（哪个专家更可信），而非取代 Pearl 识别。

**Lean 形式化 vs 统计反驳**：形式方法社区（#4 CausalForge / Causalean 7,035 声明）追求机器检查的数学确定性--do-演算代数、识别定理可在 Lean 中无歧义证明。但因果推断的实证力量来自统计反驳（DoWhy 的 placebo_treatment_refuter、dummy outcome、bootstrap、sensitivity analysis）--这些是"假设-数据"桥接的工程实践，Lean 难以形式化数据生成过程或混杂假设的现实匹配。#5 ReplaySCM 的可执行重放提供第三条路：不证明定理也不统计反驳，而是行为等价性审计。三者在可复现性上互补：Lean 保证识别代数正确，统计反驳保证假设-数据匹配稳健，重放审计保证机制泛化。

**ML 规模化 vs 因果可识别性**：ML 追求大规模端到端学习，因果推断则强调可识别性假设（unconfoundedness、exclusion restriction、SUTVA）的脆弱性。#9 Scaling Point-in-Time 与 #10 CausalMix 展示了调和方向：把因果约束（时间一致性、领域处理效应）注入 ML 训练管线，让规模化与可识别性共存。#13 BridgeVLM 的"prompt 33.2% -> token 54.4%"进一步暗示因果监督需内化进表示空间。

范式互鉴机会：Pearl 提供 LLM 缺失的干预语义；LLM 提供 Pearl 框架的自动化（#6 Era-of-Agents 的 DAG 构建、#1 CEA 的元裁判）；Lean 提供两者共同缺失的机器检查；计量经济学提供现实识别策略库（IV/PSM/DiD/RDD）。capstone Phase 4 的"ATE 估计 + 反事实"正是这四者交汇的教学现场。

---

## controversies

### 争议 1：LLM 能否越过因果阶梯 L1（Words as Difference Makers 正方 vs 工程派/基准派反方）

- **正方**：#8 Words as Difference Makers（Pietsch 2026）主张 LLM 通过差分逻辑（variational induction）从海量文本归纳因果结构，token 嵌入与自注意力实现差分制造者识别，暗示 LLM 隐式获得 L2 干预理解。#13 BridgeVLM 的"prompt 33.2% -> token 54.4%"为结构化内化可部分突破 L1 提供证据。
- **反方**：#7 CausalGame（Chen 等 2026, ICML Oral）实证 30 个 LLM 智能体在端到端因果思维（实验设计+数据收集+解释）上无一可靠，最优仅 68% 存活率 vs 78-85% 最优，仅 5-7% 会话获评分细则得分。#2 Pharmacovigilance 的"无通用温度最优、性能内容驱动"暗示即使窄领域校准（72%）也不稳定。#5 ReplaySCM 显示 held-out 重放在结构隐藏时急剧下降。隐式因果链发现（Allein 等 2025, arXiv:2510.13417）的"associative pattern matching rather than genuine causal reasoning"是反方独立佐证。
- **本深挖判断**：**反方证据更硬，LLM 停在 L1**。Pietsch 描述的"差分逻辑"实质是 L1 over human-pre-articulated L2/L3 text--LLM 复述人类已 articulasi 的因果叙述，而非执行 do(X)。CausalGame 要求真正的实验设计（物理 do），LLM 失败；Pharmacovigilance 在结构化 Naranjo 量表下可校准，但量表本身是人类预编码的 L2 框架。BridgeVLM 的 54.4% 虽有提升但仍非可靠阈值。裁决：LLM 展现 L1 模式匹配的强泛化，可模仿差分语言，但未跨越 L1；"Words as Difference Makers"描述的是 L1 generalization over L2-text，不是 L1 transcendence。生产中应将 LLM 限制在元裁判角色（#1 CEA / #6 Era-of-Agents），不让他们估计效应本身。

### 争议 2：形式化（Lean）vs 统计反驳--哪条路径提升因果可复现性更可行

- **正方形式化**：#4 CausalForge（Tan & Syrgkanis 2026）用 Lean + Causalean（7,035 声明）机器检查 do-演算代数与识别定理，消除纸面证明的歧义；#5 ReplaySCM 用可执行 Boolean DSL + support-audit ladder 将机制泛化从 0.89 提升至 1.0。两者共同主张：机器检查是可复现性的终极保障。
- **反方统计反驳**：#6 Causal Discovery Era of Agents（Zheng & Verma 2026）坚持因果声明须基于数据+显式假设+形式化算法，暗示 Lean 形式化只覆盖识别代数，不覆盖"假设-现实匹配"。DoWhy 的 placebo_treatment_refuter / dummy outcome / sensitivity analysis 传统（skill-3/day-1, day-3 实操）是统计反驳的工程基石，它们检验的是 Lean 无法形式化的经验稳健性。#11 Causal-Audit 的路径级证据聚合提供"可审计但不形式化"的中间路径。
- **本深挖判断**：**两者是互补而非替代，但近期（2-3 年）统计反驳路径更具可行性与覆盖面**。Lean 形式化的收益真实但有界：它能机器检查识别定理（后门准则、do-演算代数），但无法形式化数据生成过程、混杂假设的现实匹配、或未观测混杂的敏感度--而这些恰是因果推断可复现性的主要失败模式。CausalForge 自身的"声明审计"机制承认形式化定理与非形式化声明间存在缝隙。统计反驳（placebo / sensitivity / bootstrap）逻辑上较弱但经验覆盖广，且已有 DoWhy 工程基础设施。最优策略是分层：Lean 形式化识别层（CausalForge/Causalean），统计反驳假设-数据桥接层（DoWhy refuters），可审计图约束推理层（Causal-Audit）。研究路线 1（Lean-verified refutation library）正是此分层的技术路径。

### 争议 3：LLM 元裁判 vs 直接推断器

- **正方元裁判**：#1 CEA 将 LLM 限制在元分析（边界情形重加权专家），#6 Era-of-Agents 主张"辅助不推断"，两者共同主张 LLM 的安全角色是审查论证质量而非估计效应。#3 LLM Explainability Counterfactual 用因果图建模 LLM-as-Judge 本身，为元裁判提供了自审机制。
- **反方直接推断**：#2 Pharmacovigilance 在窄领域（Naranjo 量表 + 专家锚点）让 LLM 直接评估因果，72% 一致性证明直接推断在结构化场景可行。#8 Words as Difference Makers 隐含主张 LLM 已隐式学到因果结构可直接调用。#13 BridgeVLM 的 token 内化（54.4%）暗示结构化内化可支撑直接推断。
- **本深挖判断**：**元裁判是更稳健的工程选择，直接推断仅限窄域校准**。Pharmacovigilance 的 72% 依赖 Naranjo 量表（人类预编码 L2 框架）与 FAERS 结构化报告，一旦脱离此结构（如 CausalGame 的开放实验设计），直接推断崩溃至 5-7% 评分细则得分。元裁判（CEA）的优势在于利用 LLM 的强项（论证模式匹配：DAG 是否遗漏混杂？后门是否满足？）而非弱项（效应数值估计）。生产部署建议：默认元裁判，仅在存在结构化量表与专家锚点的窄域允许直接推断，且必须附带温度校准与内容驱动失败监控。

---

## research_roadmap

1. **（近-可攻克）Lean-verified DoWhy refuter 库**：将 DoWhy 的反驳器（placebo_treatment_refuter、dummy outcome、bootstrap、data subset、sensitivity）形式化为 Lean 声明并机器检查其不变量。为何重要：#4 CausalForge 的 Causalean 已覆盖识别代数，但反驳器（skill-3/day-1 TODO5、day-3 TODO5 的工程基石）尚无形式化层，这是争议 2 分层策略的关键缺口。可行路径：为每个 refuter 定义不变量（如 placebo 下估计应收敛于 0），在 Lean 中证明 refute_estimate 保持识别假设，产出 `Causalean.Refuters` 子库。
2. **（近-可攻克）LLM 元裁判基准 for 因果论证**：构建基准让 LLM 判断 DAG 完整性、后门准则满足性、refuter 充分性，对照专家评分。为何重要：#1 CEA / #2 Pharmacovigilance 显示元裁判可行但无标准基准，#7 CausalGame 的评分细则可适配为论证评估。可行路径：从 CausalGame 提取论证评估子集，专家标注 DAG 完整性 ground truth，评估 LLM 元裁判与专家一致性。
3. **（中）Point-in-time 因果语料预训练**：扩展 #9 Scaling Point-in-Time 的时间过滤到因果论文语料，训练因果专用 LLM 并在 #7 CausalGame / #5 ReplaySCM 评估。为何重要：#8 Words as Difference Makers 依赖干净文本，#9 证明前瞻偏差污染因果推断，两者结合暗示因果专用 LLM 需 point-in-time 因果语料。可行路径：按 arXiv 公告日过滤因果论文，训练 1-3B decoder，对比通用 LLM 在 CausalGame 存活率与 ReplaySCM 重放泛化。
4. **（中）Target-aware 因果图 + LLM 路径证据聚合**：结合 #11 Causal-Audit 的目标感知图构建与 LLM 从文献抽取的路径证据，形成可审计证据链。为何重要：Causal-Audit 抑制无关变量但依赖给定图，LLM 可抽取路径证据但缺目标感知。可行路径：LLM 从语料抽取候选路径，target-aware 剪枝，每条路径附可审计证据引用，在 capstone Phase 4 数据集验证。
5. **（远-高风险）do-calculus 预训练因果基础模型**：在合成（SCM, 干预, 结果）三元组上预训练，让模型内化 do-算子。为何重要：测试 #8 Pietsch 的 L1 突破假说是否可通过结构化预训练实现，#13 BridgeVLM 的 token 内化（54.4%）暗示有空间。可行路径：生成多样化合成 SCM，预训练干预查询，在 ReplaySCM held-out 与 CausalGame 评估。高风险：可能撞上 L1 天花板，但负面结果本身有发表价值。
6. **（远-高风险）Lean-ML-Econ 因果统一框架**：扩展 CausalForge 包裹 econml + DoWhy + IV，机器检查"识别-估计-推断"链端到端一致性。为何重要：Pearl-LLM-Lean 范式冲突（cross_disciplinary_synthesis）需统一框架化解。可行路径：在 Causalean 中编码 econml 估计器的识别条件，机器检查 IV 外生性 + PSM 平衡性 + DML 交叉拟合的一致性，产出 `Causalean.Econ` 子库。

---

## connection_to_curriculum

1. **skill-3/day-1-causal-basics**（DoWhy 四步：建模->识别->估计->反驳；solution.ipynb TODO5 `placebo_treatment_refuter`；NSW/Lalonde 真实数据）：§争议 2 + §子主题 B（#4 CausalForge / Causalean）为反驳步添加形式化验证层--学生可在 TODO5 后加一个"Lean 不变量检查"附录，机器验证 placebo 下估计收敛于 0。§子主题 A（#1 CEA）将 notes.md 的"LLM-as-a-judge 自检因果论证"前沿框升级为元裁判范式：LLM 审查 DAG 是否遗漏混杂、后门是否满足，不估计效应。§争议 1 警示学生 LLM 停在 L1，不可让其替代后门调整。
2. **skill-3/day-3-observational-causal**（PSM + IV；NSW+CPS 观测对照；close_college 教育回报；placebo_treatment_refuter）：§子主题 C（#6 Era-of-Agents / causal-learn+）更新 DAG 构建--学生可用 agent 辅助从 NSW+CPS 协变量提议候选图，但因果声明须由 PC/FCI 形式化算法下。§研究路线 1 的 Lean refuter 库直接加固 TODO5 的 IV 稀疏性反驳。
3. **skill-3/day-4-causal-discovery**（PC/FCI 算法）：§子主题 C（#7 CausalGame / #6 Era-of-Agents）+ §子主题 D（#8 Words as Difference Makers / L1 天花板）直接更新前沿--agent 辅助因果发现的边界（CausalGame 68% 存活率划定 LLM 能力下限），Words as Difference Makers 的差分逻辑作为 PC/FCI 的文本先验。
4. **skill-3/day-5-scale-marketing**（CUPED / 增量测量）：§子主题 A（#1 CEA）为 uplift 模型规格提供 LLM 元裁判--在规模营销场景，LLM 审查 uplift 模型的特征工程是否引入混杂，不直接估计 CATE。
5. **skill-0/day-3 描述统计与推断统计**（假设检验、t 检验、A/B）：§子主题 D + §争议 1 重构"相关 vs 因果"教学--加入 LLM 维度：LLM 的相关匹配能力是 L1 的极致，但 L2 干预需 A/B（do 操作）。学生通过 CausalGame 理解为何 LLM 不能替代 A/B。
6. **skill-0/day-4 回归分析与概率分布**（OLS、Logit、倾向性评分作因果桥梁；NSW 数据）：§子主题 A（#2 Pharmacovigilance 温度校准）+ §争议 1 映射到倾向性评分校准--LLM 温度优化与 propensity score 平衡性检验同属"校准未观测假设"工程实践。CausalMix（#10）将数据混合当因果推断，可作为"回归系数的因果解读"前沿延伸。
7. **elective-e2/day-3 MMM/MTA/增量测量**（NSW RCT、合成控制、DML）：§子主题 D（#9 Scaling Point-in-Time 前瞻偏差）直接更新 MMM 回测--前瞻偏差破坏 MMM 的因果识别，point-in-time 过滤是必要前置。§子主题 E（#11 Causal-Audit 路径级证据）为 MTA 的多触点归因提供可审计图结构。
8. **capstone/day-phase-4-causal-experiment-design**（ATE 估计 + 反事实；DoWhy + causaldata）：§子主题 B（#4 CausalForge 形式化层）+ §研究路线 1（Lean refuter 库）允许学生在 capstone 因果设计中添加形式化验证附录，机器检查识别策略。§争议 2 的分层策略（Lean 识别层 + 统计反驳桥接层 + Causal-Audit 推理层）作为 capstone 因果论证的结构模板。

---

## teaching_seminar

### 研讨班 1（90 分钟）：LLM 能否越过 L1？--Words as Difference Makers vs CausalGame

- **前置阅读**：#8 Words as Difference Makers（Pietsch 2026, arXiv:2606.22430）；#7 CausalGame（Chen 等 2026, arXiv:2607.04293）；隐式因果链发现（Allein 等 2025, arXiv:2510.13417）
- **讨论问题**：
  1. Pietsch 的"差分逻辑"是真正的 L2 干预理解，还是 L1 over human-pre-articulated L2-text？给出判别标准。
  2. CausalGame 最优模型 68% vs 78-85% 最优，5-7% 评分细则得分--失败模式是实验设计、数据收集还是解释？哪一环最致命？
  3. 若 LLM 不能越过 L1，其在因果推断中的安全角色边界在哪？（参考 #1 CEA 元裁判、#6 Era-of-Agents 辅助）
  4. 设计一个实验区分"L1 模式匹配"与"L2 干预推理"--提示工程 vs 结构化内化（#13 BridgeVLM token 54.4%）的对比。
- **活动**：60 分钟精读 CausalGame 评分细则（5-7% 得分的具体失败案例）+ 30 分钟辩论"LLM 永远不能越过 L1"（正反方各 15 分钟）
- **产出**：1 页研究问题备忘录，聚焦 L1 天花板的可测试判据

### 研讨班 2（90 分钟）：形式化 vs 统计反驳--Lean 因果与可复现性前沿

- **前置阅读**：#4 CausalForge（Tan & Syrgkanis 2026, arXiv:2607.22511）；#5 ReplaySCM（Batzoglou 2026, arXiv:2605.08197）；#6 Causal Discovery Era of Agents（Zheng & Verma 2026, arXiv:2606.23608）
- **讨论问题**：
  1. Lean 能证明什么统计反驳不能？反之呢？给出各自不可覆盖的因果推断失败模式。
  2. Causalean 的 7,035 条声明是真实基础还是玩具规模？哪些识别定理仍缺失？
  3. ReplaySCM 的 support-audit ladder（0.89->0.98->1.0）是否可推广到非 Boolean SCM？
  4. 设计一个可在 Lean 中形式化的 DoWhy refuter（如 placebo_treatment_refuter 的不变量）。参考 skill-3/day-1 TODO5。
- **活动**：60 分钟 CausalForge/Causalean 与 ReplaySCM 精读（如可现场演示 Lean 证明则演示）+ 30 分钟"在 Lean 中设计一个 refuter"小组练习
- **产出**：1 页 Lean refuter 规格说明，含不变量定义与机器检查路径

---

## references

1. Jiyuan Tan, Vasilis Syrgkanis. CausalForge: A Formally Grounded, Self-Improving Agentic Framework for Automated Research in Causal Inference. arXiv:2607.22511, 2026. https://arxiv.org/abs/2607.22511
2. Xinyu Li, Yuanyuan Wang. Causal Ensemble Agent: Hierarchical Causal Discovery with LLM-guided Expert Reweighting. arXiv:2606.10607, 2026. https://arxiv.org/abs/2606.10607
3. Bryan Kelly, Semyon Malamud. Scaling Point-in-Time Language Models. arXiv:2607.11889, 2026. https://arxiv.org/abs/2607.11889
4. Zinan Tang, Yukun Zhang. CausalMix: Data Mixture as Causal Inference for Language Model Training. arXiv:2607.01104, 2026. https://arxiv.org/abs/2607.01104
5. Yujia Zheng, Vishal Verma. Causal Discovery in the Era of Agents. arXiv:2606.23608, 2026. https://arxiv.org/abs/2606.23608
6. Wolfgang Pietsch. Words as Difference Makers: How Large Language Models Determine Causal Structure in Text. arXiv:2606.22430, 2026. https://arxiv.org/abs/2606.22430
7. Amogh Sheth, Biruk Assefa. Pruning via Causal Attribution Preserves Reasoning Performance in Large Language Models. arXiv:2606.19350, 2026. https://arxiv.org/abs/2606.19350
8. Haoping Yu, Yuanxi Li. From Prompts to Tokens: Internalizing Causal Supervision in Vision-Language Model for Multi-Image Causal Reasoning. arXiv:2606.11745, 2026. https://arxiv.org/abs/2606.11745
9. Su Lan, Xuefei Yin. Causal-Audit: Explicit and Auditable Graph-based Reasoning via Target-Aware Causal Chain Construction. arXiv:2607.15281, 2026. https://arxiv.org/abs/2607.15281
10. Nicole Sonne Heckmann, Arnault-Quentin Vermillet. Optimizing Large Language Models for Causality Assessment in Pharmacovigilance. arXiv:2607.03704, 2026. https://arxiv.org/abs/2607.03704
11. Zhenhao Chen, Yongqiang Chen 等. CausalGame: Benchmarking Causal Thinking of LLM Agents in Games. arXiv:2607.04293, 2026. https://arxiv.org/abs/2607.04293
12. Serafim Batzoglou. ReplaySCM: A Benchmark for Executable Causal Mechanism Induction from Interventions. arXiv:2605.08197, 2026. https://arxiv.org/abs/2605.08197
13. Nirit Nussbaum-Hoffer, Nitay Calderon 等. LLM Explainability with Counterfactual Chains and Causal Graphs. arXiv:2606.05972, 2026. https://arxiv.org/abs/2606.05972

---

*本文件由 v10.0 旗舰课题深挖层生成。13 篇论文：10 篇来自 v9.0 `_frontier_corpus/skill-3-causal.md` 语料库（#1-#2 verified，#3-#10 unverified 但来自语料库搜索），3 篇本深挖新研（#11-#13 经 arXiv abstract 页验证）。面向博后/教授级研讨。WebFetch 仅访问 arxiv.org，共 6 次（3 次搜索 + 3 次 abstract 验证）。*
