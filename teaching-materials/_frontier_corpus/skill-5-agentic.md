# 前沿语料库: skill-5-agentic - Agent评估与LLM-as-a-Judge

> v9.0 前沿注入层共享语料库. 论文来自 arXiv 搜索 (2025-09 ~ 2026-07, post 2025-08 cutoff). 标注 verified 的论文经 abstract 页抽查. wave agent 仅可引用本文档列出的论文, 禁止编造.

## 论文

### 1. LLM-as-a-Coach: Experiential Learning for Non-Verifiable Tasks
- **arXiv**: https://arxiv.org/abs/2607.18110
- **作者**: Tianzhu Ye, Li Dong
- **年份**: 2026
- **摘要**: 提出Experiential Learning方法，将LLM-as-a-Judge重新定位为LLM-as-a-Coach，用丰富文本反馈而非标量奖励指导开放任务的策略训练。方法持续优于基于评分表的RL，泛化性更好，并缓解奖励黑客问题。
- **验证**: verified

### 2. LLM-as-a-Judge Scores Are Unreliable Optimization Signals in Closed-Loop Table Recognition
- **arXiv**: https://arxiv.org/abs/2607.13347
- **作者**: Donghwan Kim
- **年份**: 2026
- **摘要**: 以TEDS为受控测试床研究LLM-as-a-Judge在表格识别中的信号质量。发现判官信号在两个数据集上均很弱：分数频繁平局、排名不可复现，无判官策略能改进首输出。结论：迭代精修至少需要能确定性检测结构变化的验证信号。
- **验证**: verified

### 3. Articulate Intuition or Genuine Analysis? Benchmarking Epistemic Reliability in LLM-as-a-Judge Peer Reviews
- **arXiv**: https://arxiv.org/abs/2607.10511
- **作者**: Nuo Chen, Qian Wang
- **年份**: 2026
- **摘要**: 发布Kahneman4Review基准，包含3,563条按九个文本维度评分的同行评审。研究追问：当LLM判官称一条评审"具分析性"而人类委员会称另一条"高质量"时，它们是否在追踪同一信号？揭示LLM-as-a-Judge的认识论可靠性问题。
- **验证**: unverified

### 4. Eval-Pair Matrix: Answer-Paired Meta-Evaluation of LLM Judges for Grounded RAG
- **arXiv**: https://arxiv.org/abs/2607.10626
- **作者**: Sriram Selvam, Anneswa Ghosh
- **年份**: 2026
- **摘要**: 提出受控元评估协议用于源接地RAG，构建2,683条判官裁决的3×3交叉矩阵。发现将同一模型族同时用作生成器与判官会使自我宽容难以识别，为LLM-as-a-Judge的评估实践提供方法论。
- **验证**: unverified

### 5. More Convincing, Not More Correct: Self-Play Reward Hacking of Reference-Free LLM Judges
- **arXiv**: https://arxiv.org/abs/2607.05904
- **作者**: Chenyu Zhou
- **年份**: 2026
- **摘要**: 揭示自奖励与LLM-as-a-Judge流程结构性评分"合理性"而非"正确性"。在GSM8K上，自玩使判官通过率达0.94而真实准确率仅0.20，暴露无参考判官的系统性奖励黑客风险。
- **验证**: unverified

### 6. Challenges and Recommendations for LLMs-as-a-Judge in Multilingual Settings and Low-Resource Languages
- **arXiv**: https://arxiv.org/abs/2607.02235
- **作者**: A. Seza Doğruötz, Xixian Liao
- **年份**: 2026
- **摘要**: 从650篇提及LLM-as-a-Judge的论文中分析33篇聚焦多语言或低资源语言设置的文献。发现评估结果不一致、多语言场景中过度信任LLM判断、以及普遍依赖单一判官模型等问题，提出改进建议。
- **验证**: unverified

### 7. LLM-as-a-Tutor: Policy-Aware Prompt Adaptation for Non-Verifiable RL
- **arXiv**: https://arxiv.org/abs/2607.04412
- **作者**: Yujin Kim, Namgyu Ho
- **年份**: 2026
- **摘要**: 将LLM角色从判官扩展至导师，用于不可验证的RL训练。非可验证指令遵循的RL越来越依赖带提示特定评分表的LLM判官作为奖励信号，该框架附加约束以单调提升难度，扩展了LLM-as-a-Judge的应用边界。
- **验证**: unverified

### 8. Operationalising Multi-Dimensional Evaluation for Conversational Agents: A Scalable, Governed Pipeline with Selective Re-evaluation and Model Benchmarking
- **arXiv**: https://arxiv.org/abs/2607.12085
- **作者**: Niranjan Kumar M, Balaji Nagarajan
- **年份**: 2026
- **摘要**: 提出面向零售聊天机器人大规模评估的治理化、配置驱动流水线。指出LLM-as-a-Judge虽提供可扩展的人类评估替代方案，但生产部署在治理、可复现性方面引入新挑战，需选择性重新评估与模型基准测试。
- **验证**: unverified

### 9. Lower-Resource, Higher Scores: Language Bias in LLM Evaluators
- **arXiv**: https://arxiv.org/abs/2607.14480
- **作者**: Ej Zhou, Lucas Resck
- **年份**: 2026
- **摘要**: 揭示多语言LLM评估器跨语言评分显著不同：低资源语言评分更宽松，接受率差异达43%，且此偏差在成对准确率中不可见。对LLM-as-a-Judge的跨语言公平性提出根本性挑战。
- **验证**: unverified

## 备注
- 模块聚焦Agent评估方法论（meta-evaluation、可复现性）与LLM-as-a-Judge的可靠性/偏差/失效模式。
- 2篇verified论文（2607.18110 LLM-as-a-Coach、2607.13347 Unreliable Optimization Signals）经arXiv abstract页确认标题、作者与日期一致。
- 论文#5（Self-Play Reward Hacking）与#2（Unreliable Signals）揭示LLM-as-a-Judge的系统性缺陷，建议教学时成对引用以呈现正反视角。
- 论文#9（Language Bias）对多语言评估公平性有重要启示，适合与#6（Multilingual Challenges）配合使用。
- arXiv搜索原始query: "LLM as a judge evaluation agent" 及 '"LLM as a judge"'。
