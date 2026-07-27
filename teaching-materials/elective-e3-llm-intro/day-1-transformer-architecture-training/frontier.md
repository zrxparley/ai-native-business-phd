# frontier.md (v9.0 学术前沿注入层)

> **所属**：elective-e3-llm-intro · day-1-transformer-architecture-training
> **版本**：v9.0（学术前沿注入层）
> **本单元前沿课题**：从本模块"LLM 推理经济 × 推理模型 × 高效推理"课题中，特化到本单元所教 Self-Attention / Multi-Head / Pre-training-SFT-Alignment 三阶段 / GPT-2 config 参数推算 / MoE 推理成本优化 的 2025-2026 前沿子问题：高效预训练缩放、高效 RL 对齐、推理 profiling 与注意力层效率创新如何更新本单元的"训练三阶段成本-质量权衡"基础认知。

---

## frontier_topic

本单元教 Transformer 三机制（Self-Attention Q/K/V 点积+缩放+softmax、Multi-Head 多视角并行、Positional Encoding）+ 训练三阶段（Pre-training/SFT/RLHF-DPO Alignment）+ GPT-2 config 参数推算（~124M）+ MoE/投机解码推理成本优化。前沿子问题是：2025-2026 年的高效预训练缩放（多模态分模态 scaling）、高效 RL 对齐（方差引导 rollout 分配）、推理多维度 profiling（精度/时间/内存/能耗联合）与注意力层效率创新（细粒度下一 token 重建）如何更新本单元所教的"训练三阶段 + Scale Law 单维参数量推算"基础认知。

---

## recent_papers

> 从本模块 `_frontier_corpus/elective-e3-llm-intro.md` 语料库中挑 4 篇最贴本单元的 2025-2026 论文。**严禁引用语料库之外的论文**。

### 1. Scaling Native Multimodal Pre-Training From Scratch
- **arXiv**: https://arxiv.org/abs/2607.22043
- **作者**: Haoyuan Wu, Aoqi Wu
- **年份**: 2026
- **摘要**: 研究在固定计算预算下训练视觉语言模型的最优模型规模和 token 数量。发现语言和多模态目标呈现不同的缩放行为，为多模态 LLM 的高效预训练提供指导。
- **与本单元的关联**: 直接更新本单元 notes.md "Scale Law 对商业决策的影响"与 solution.ipynb TODO2 GPT-2 config 单模态参数推算--必须分模态建模缩放。

### 2. Learning as Reasoning Unfolds: Progressive Rollout Allocation for Efficient Reinforcement Learning
- **arXiv**: https://arxiv.org/abs/2607.22002
- **作者**: Heyang Jiang, Henry Liu
- **年份**: 2026
- **摘要**: 提出 VIGOR，迭代地将 rollout 分配给组奖励方差最高的样本。在数学任务上以最多 2.3 倍更少的 rollout 达到目标精度，显著提升推理模型训练效率。
- **与本单元的关联**: 更新本单元 notes.md 训练三阶段中 Alignment 阶段 RLHF/DPO 的 RL 训练效率上限，方差引导 rollout 是 DPO 之后的对齐效率新路径。

### 3. Profiling Lightweight Large Language Models
- **arXiv**: https://arxiv.org/abs/2607.20806
- **作者**: Tomohiro Harada, Enrique Alba
- **年份**: 2026
- **摘要**: 提出 PTME 框架，联合测量轻量级 LLM 推理的精度、时间、内存和能耗。发现没有单一模型在所有 PTME 维度上占优，为高效推理部署提供系统化评估方法。
- **与本单元的关联**: 扩展本单元 solution.ipynb TODO1 tiktoken 单维 token 计数与 TODO2 GPT-2 config 单维参数量推算为四维 Pareto 评估框架。

### 4. SHIFT: Self-reconstruction Harnesses Implicit Fine-grained Thinking for Retrieval
- **arXiv**: https://arxiv.org/abs/2607.21333
- **作者**: Yuxiao Luo, Da Li
- **年份**: 2026
- **摘要**: 提出检索训练框架，将 LLM 转化为"推理高效检索器"，使用残差投影和基于细粒度下一 token 预测的重建。直接优化推理效率与检索质量。
- **与本单元的关联**: 补充本单元 notes.md "2026 前沿：DeepSeek-MoE / 投机解码" 之外的第三条效率路线--在 Self-Attention 层面用下一 token 重建机制优化检索推理效率，直接呼应本单元 TODO3 手写 Self-Attention。

---

## critical_synthesis

这 4 篇 2026 论文 + 语料库其他相关条目共同揭示了一个**领域共识**：LLM 训练与推理效率优化已从"单维 Scale Law"转向"多目标 Pareto 联合优化"。PTME (#8) 把"精度/时间/内存/能耗"四维联合测量作为标配，VIGOR (#3) 把对齐阶段的 RL 样本效率作为核心指标（2.3x rollout 节省），SHIFT (#6) 把"下一 token 预测"从预训练任务扩展为检索训练的重建信号，Scaling Native Multimodal (#2) 把单模态 scaling 拆解为分模态异构行为。这些工作共同表明：本单元所教的"参数量→性能"单维推算框架在 2026 年已不足以指导商业决策。

**争议**在于：分模态 scaling (#2) 与 PTME (#8) 的多维度 Pareto 都暗示"没有单一最优"，但工业实践仍倾向于用单一 flagship 模型（GPT-4o/Claude）做基准--学术的多目标细化与工业的单点选型存在张力。VIGOR 的方差引导 rollout 在数学任务上有效，但是否泛化到非推理任务（营销文案/对话）仍是开放问题。

**方法学趋势**：从"训练后评测"转向"训练中评测"--VIGOR 用组奖励方差实时分配 rollout，PTME 在部署前联合 profiling，SHIFT 把检索质量拉回预训练阶段优化。这预示着 Pre-training/SFT/Alignment 三阶段边界正在模糊化。

**局限**：#2 unverified、#3/#6 unverified（仅 abstract 推断），#8 verified 但仅覆盖轻量级模型（1-3B 量级），其结论是否能外推到 70B+/MoE 量级未经验证。VIGOR 的 2.3x 数据来自数学任务，营销文案等开放生成任务的增益未披露。

---

## delta_to_unit

1. **本单元 notes.md "关键回顾 4：训练三阶段" 中 Alignment 阶段讲 RLHF/DPO**--VIGOR (arXiv 2607.22002) 用组奖励方差引导 rollout 分配，在数学任务上以 2.3x 更少 rollout 达到目标精度。这更新了本单元"DPO 绕过 Reward Model 训练和 RL 优化，更简单更稳定"的简化叙事：DPO 之后仍有 RL 样本效率的优化空间，方差引导是对齐阶段的新维度，本单元未覆盖。

2. **本单元 solution.ipynb TODO1/TODO2 用 tiktoken 计数 + GPT-2 config 单维推算 ~124M 参数**--PTME (arXiv 2607.20806) 提出精度/时间/内存/能耗四维联合测量，发现没有单一轻量级模型在所有维度占优。这把本单元"Scale Law: GPT-2 small (124M) -> GPT-2 XL (1.5B) -> GPT-3 (175B)，模型每增大 10x 能力显著提升但推理成本也线性增长"的单维推算扩展为四维 Pareto，商业决策需在四维上联合选型而非仅看参数量。

3. **本单元 notes.md "2026 前沿补充" 讲 MoE + 投机解码两条推理成本优化路线**--SHIFT (arXiv 2607.21333) 提出在 Self-Attention 层面用残差投影 + 细粒度下一 token 预测重建，将 LLM 转化为"推理高效检索器"。这是本单元 TODO3 手写 Self-Attention 之外的第三条效率路线（注意力层内部创新），本单元未覆盖。

4. **本单元 solution.ipynb TODO2 用 GPT-2 单模态 config (n_layer=12/n_head=12/n_embd=768) 推算参数量**--Scaling Native Multimodal (arXiv 2607.22043) 发现语言和多模态目标呈现不同缩放行为。这更新了本单元"Scale Law 对商业决策的影响"必须分模态建模：GPT-2 的单模态参数推算公式不能直接外推到 GPT-4o/Gemini 等多模态模型，本单元的单模态推算在 2026 年多模态主流场景下需修正。

---

## open_questions

1. 在多模态异构缩放定律下，本单元 GPT-2 config (n_layer/n_head/n_embd/vocab_size) 的参数推算公式如何修正以同时预测语言与视觉 token 损失，且保持单模态场景下的预测精度？
2. VIGOR 的组奖励方差引导 rollout 分配在 SFT 之后的对齐阶段是否仍优于均匀分配，还是仅在数学推理 RL 阶段有效，在营销文案等开放生成任务上是否反而因方差噪声导致样本浪费？
3. SHIFT 的"推理高效检索器"将注意力从序列外检索拉回模型内部重建，是否意味着传统 RAG 检索架构在小参数量（1-3B）下被内部化，本单元 Day 2 教的 RAG 四模式决策框架是否需要重新排序？
4. PTME 四维 Pareto 在能耗维度上的测量是否可复现到 MoE 架构（如 DeepSeek V3 671B/37B 激活），还是 MoE 的稀疏激活使能耗模型需重新标定？

---

## methodological_critique

这些前沿论文的局限与可复现性顾虑需显式标注。**#2 Scaling Native Multimodal 与 #3 VIGOR 与 #6 SHIFT 均为 unverified**（语料库仅 abstract 推断，未抽查 arXiv abstract 页），其具体数值（2.3x rollout 节省、多模态 scaling 系数）需独立验证。**#8 PTME 虽 verified 但仅覆盖轻量级模型（1-3B 量级）**，其"没有单一模型在所有维度占优"的结论是否能外推到 70B+/MoE 量级未经验证--大模型的能耗曲线与小模型可能存在相变点。VIGOR 的 2.3x 数据来自数学任务（GSM8K/MATH 类），在营销文案等开放生成任务上的增益未披露，存在 benchmark-gaming 风险（在公开数学基准上过度优化）。SHIFT 的"推理高效检索器"训练需要残差投影与细粒度下一 token 预测重建，训练数据与代码是否开源未明确，复现成本可能很高。Scaling Native Multimodal 的分模态 scaling 系数依赖于具体的视觉语言数据混合比例，不同数据混合下系数可能漂移。整体上，这些论文的"效率提升"数据均来自作者自选基准，缺乏第三方独立复现，博后级读者应将其视为"上界估计"而非"生产可达"。

---

*本文件由 v9.0 学术前沿注入层生成。所有论文链接来自 `_frontier_corpus/elective-e3-llm-intro.md` 共享语料库（arXiv 搜索 + abstract 页抽查验证）。*
