# 前沿语料库: elective-e3-llm-intro - LLM推理经济与高效推理

> v9.0 前沿注入层共享语料库. 论文来自 arXiv 搜索 (2025-09 ~ 2026-07, post 2025-08 cutoff). 标注 verified 的论文经 abstract 页抽查. wave agent 仅可引用本文档列出的论文, 禁止编造.

## 论文

### 1. Towards Trustworthy and Cost-Efficient Data Integration: From Naive RAG to Agentic RAG
- **arXiv**: https://arxiv.org/abs/2607.22319
- **作者**: Chuangtao Ma, Arijit Khan
- **年份**: 2026
- **摘要**: 展望通过知识锚定 LLM 和 Agent 实现"可信、可扩展、成本高效"的数据集成. 追溯从经典 RAG 到 Agentic RAG 的演进, 涉及 LLM 推理在企业环境中的精度与成本权衡.
- **验证**: verified

### 2. Scaling Native Multimodal Pre-Training From Scratch
- **arXiv**: https://arxiv.org/abs/2607.22043
- **作者**: Haoyuan Wu, Aoqi Wu
- **年份**: 2026
- **摘要**: 研究在固定计算预算下训练视觉语言模型的最优模型规模和 token 数量. 发现语言和多模态目标呈现不同的缩放行为, 为多模态 LLM 的高效预训练提供指导.
- **验证**: unverified

### 3. Learning as Reasoning Unfolds: Progressive Rollout Allocation for Efficient Reinforcement Learning
- **arXiv**: https://arxiv.org/abs/2607.22002
- **作者**: Heyang Jiang, Henry Liu
- **年份**: 2026
- **摘要**: 提出 VIGOR, 迭代地将 rollout 分配给组奖励方差最高的样本. 在数学任务上以最多 2.3 倍更少的 rollout 达到目标精度, 显著提升推理模型训练效率.
- **验证**: unverified

### 4. Three-Body Alignment: Aligning Chess Agent with Human Reasoning through Reranked Rationale
- **arXiv**: https://arxiv.org/abs/2607.21993
- **作者**: Jaymari Chua, Chen Wang
- **年份**: 2026
- **摘要**: 分析人类专家、引擎辅助评论员和 LLM 在国际象棋中生成的理由之间的语义差异. 证明重排序可提升人类对齐度, 但存在战术性能权衡, 为推理对齐提供见解.
- **验证**: unverified

### 5. Coupled Hierarchical Search over Topology and Execution for Agentic Workflow Synthesis
- **arXiv**: https://arxiv.org/abs/2607.21609
- **作者**: Dong Li, Yanchi Liu
- **年份**: 2026
- **摘要**: 引入 HierFlow, 无训练层次搜索架构, 通过反馈引导的拓扑调整和 MCTS 启发的树搜索自动化 Agent 工作流设计. 展示了高效推理工作流合成的方法论.
- **验证**: unverified

### 6. SHIFT: Self-reconstruction Harnesses Implicit Fine-grained Thinking for Retrieval
- **arXiv**: https://arxiv.org/abs/2607.21333
- **作者**: Yuxiao Luo, Da Li
- **年份**: 2026
- **摘要**: 提出检索训练框架, 将 LLM 转化为"推理高效检索器", 使用残差投影和基于细粒度下一 token 预测的重建. 直接优化推理效率与检索质量.
- **验证**: unverified

### 7. Multi-turn RL with Structural and Performance Aware Rewards for CUDA Kernel Generation
- **arXiv**: https://arxiv.org/abs/2607.20908
- **作者**: Quazi Ishtiaque Mahmud, Nesreen K. Ahmed
- **年份**: 2026
- **摘要**: 提出 CudaPerf, 反思 RL 框架, 结合可验证执行奖励和结构化代码感知奖励. 实现最高 5 倍和 3.32 倍加速改进, 展示了结构感知奖励在推理效率优化中的作用.
- **验证**: unverified

### 8. Profiling Lightweight Large Language Models
- **arXiv**: https://arxiv.org/abs/2607.20806
- **作者**: Tomohiro Harada, Enrique Alba
- **年份**: 2026
- **摘要**: 提出 PTME 框架, 联合测量轻量级 LLM 推理的精度、时间、内存和能耗. 发现没有单一模型在所有 PTME 维度上占优, 为高效推理部署提供系统化评估方法.
- **验证**: verified

### 9. MiniCache: Reusable Program Caching with Small Model Interfaces for Efficient LLM Inference
- **arXiv**: https://arxiv.org/abs/2607.20507
- **作者**: Jingquan Chen, Jinghua Piao
- **年份**: 2026
- **摘要**: 提出可复用程序缓存框架, 使用小模型作为接口模型实现程序缓存. 达到 3.1 倍更低延迟和 2.8 倍更高吞吐, 直接优化 LLM 推理经济性.
- **验证**: unverified

### 10. AISE-Bench: A Full-Cycle Curated Benchmark for Information Seeking on Academic Knowledge Graphs
- **arXiv**: https://arxiv.org/abs/2607.20498
- **作者**: Fanjin Zhang, Zhengyang Wang
- **年份**: 2026
- **摘要**: 引入包含 1,133 个 QA 对的基准, 评估 LLM Agent 在学术知识图谱上的信息检索能力, 包括 API 规划正确性和执行成功率. 为推理系统的端到端评估提供标准化工具.
- **验证**: unverified

## 备注
- 论文来自 arXiv "large language model reasoning efficient inference" 与 "LLM efficient reasoning" 两次搜索合并去重.
- 10 篇论文全部位于 2026-06 至 2026-07, 反映该领域当前高度活跃.
- 覆盖高效推理的多个维度: 成本高效集成 (#1), 缩放效率 (#2), 高效 RL (#3), 推理对齐 (#4), 工作流合成 (#5), 推理高效检索 (#6), 结构感知奖励 (#7), 推理 profiling (#8), 缓存加速 (#9), 推理评估 (#10).
- verified 论文: #1 (Agentic RAG) 和 #8 (Profiling Lightweight LLMs) 经 arXiv abstract 页确认存在且标题匹配.
