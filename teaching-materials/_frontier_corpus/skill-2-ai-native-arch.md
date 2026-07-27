# 前沿语料库: skill-2-ai-native-arch - 企业Agent编排与MCP/A2A协议

> v9.0 前沿注入层共享语料库. 论文来自 arXiv 搜索 (2025-09 ~ 2026-07, post 2025-08 cutoff). 标注 verified 的论文经 abstract 页抽查. wave agent 仅可引用本文档列出的论文, 禁止编造.

## 论文

### 1. Design and Implementation of Agentic Orchestrations and Orchestration of Agents
- **arXiv**: https://arxiv.org/abs/2606.31518
- **作者**: Stefanie Rinderle-Ma, Juergen Mangler
- **年份**: 2026
- **摘要**: 提供 agentic orchestration 选项的分类框架, 沿任务特异性、可追溯性、自主性、正确性保证等属性分类. 给出不同场景的定性决策标准和通过预测光感场景 agentic 实现评估的定量指标.
- **验证**: verified

### 2. Decoupled Intelligence: A Multi-Agent LLM Framework for Controllable Traffic Scenario Generation in SUMO
- **arXiv**: https://arxiv.org/abs/2605.27685
- **作者**: Shuyang Li, Ruimin Ke
- **年份**: 2026
- **摘要**: 多 agent 框架自动化 SUMO 交通仿真, 将流程解耦为专业化角色 (Planner, Builder, Demand, Runner, Analyst), 由状态持久化 Orchestrator 通过 MCP (Model Context Protocol) 协调. 角色消融研究表明任务成功率和参数准确率显著优于单 agent 基线.
- **验证**: verified

### 3. MAS-Lab: A Specification-Driven Validation Framework for Reliable Multi-Agent Systems
- **arXiv**: https://arxiv.org/abs/2606.30546
- **作者**: Jordan Augé, Giovanna Carofiglio
- **年份**: 2026
- **摘要**: 规格驱动框架, 包含三层: 声明式 agentic 规格层、有状态 MAS 操作系统、带可观测性工具的 lab overlay. 旨在将 MAS 从脚本集合转变为工程化分布式系统, 将语义意图与运维关注点分离.
- **验证**: unverified

### 4. Learning Latency-Aware Orchestration for Multi-Agent Systems
- **arXiv**: https://arxiv.org/abs/2607.13359
- **作者**: Xi Shi, Mengxin Zheng
- **年份**: 2026
- **摘要**: 提出延迟感知编排框架 LAMaS, 通过约束优化和关键路径感知信用分配学习执行图. 端到端延迟降低 50% 以上且保持竞争性准确率, 轻量推理时控制器消除冗余 agent 交互.
- **验证**: unverified

### 5. AgentFlow: Building Agent Dependency Graphs for Static Analysis of Agent Programs
- **arXiv**: https://arxiv.org/abs/2607.01640
- **作者**: Shenao Wang, Xinyi Hou
- **年份**: 2026
- **摘要**: 首个从 agent 程序中恢复和分析 agent 依赖关系的静态分析框架, 构建 Agent Dependency Graph (ADG) 作为框架无关表示. 在 5399 个真实 agent 程序上评估, 发现 238 个污点式 prompt-to-tool 风险并生成 Agent Bills of Materials.
- **验证**: unverified

### 6. ACE: Pluggable Adaptive Context Elasticizer across Agents
- **arXiv**: https://arxiv.org/abs/2606.31564
- **作者**: Ning Liao, Zihao Long
- **年份**: 2026
- **摘要**: 即插即用模块, 通过在每个决策步为每个步骤分配弹性类型 (raw/abstract/drop) 来弹性编排历史步骤信息到 agent 上下文. 适配 ReAct 和 DeepAgent 等四个 agent 框架无需训练, 持续优于截断和摘要基线.
- **验证**: unverified

### 7. Diagnosis-Driven Automatic Repair for Agentic Workflow via Symbolic Inference
- **arXiv**: https://arxiv.org/abs/2607.02882
- **作者**: Xuyan Ma, Yawen Wang
- **年份**: 2026
- **摘要**: 诊断驱动的自动修复框架 FlowFixer, 将执行转化为统一符号迹用于失败归因和根因分析. 在 Dify、Coze、n8n 平台的失败上达到 71.3% 修复成功率, 超越基线 11.9% 至 27.6%.
- **验证**: unverified

### 8. Agora: Enhancing LLM Agent Reasoning Via Auction-Based Task Allocation
- **arXiv**: https://arxiv.org/abs/2607.09600
- **作者**: Kaiji Zhou, Ales Leonardis
- **年份**: 2026
- **摘要**: 引入激励兼容拍卖机制, 将推理步骤视为可交易物品, 动态分配推理任务给专家模型. Agent 基于"校正能力"竞标, 确保关键逻辑路由到最有能力的求解器而非最过度自信的求解器.
- **验证**: unverified

### 9. Organize then Retrieve: Hierarchical Memory Navigation for Efficient Agents
- **arXiv**: https://arxiv.org/abs/2606.11680
- **作者**: Hao-Lun Hsu, Nikki Lijing Kuang
- **年份**: 2026
- **摘要**: 分层 organize-and-retrieve 记忆 agent HORMA, 将经验结构化为文件系统式层级, 链接摘要实体到原始轨迹. 使用 RL 训练的轻量 agent 进行最小上下文选择, 在长对话任务中最多仅需基线 22.17% 的 token 用量.
- **验证**: unverified

### 10. Glite ARF: Verifier-Driven Research with Parallel LLM Coding Agents
- **arXiv**: https://arxiv.org/abs/2606.27416
- **作者**: Vassili Philippov, Pavel Katunin
- **年份**: 2026
- **摘要**: 开源 Python 框架, 在研究仓库上并行运行多个 LLM 编码 agent, 使用确定性验证器脚本强制任务隔离与不可变性. 用于开发 BEA 2026 共享任务提交, 在 closed track 获得第一名, 包含 273 个跟踪任务.
- **验证**: unverified

## 备注
- 论文 2 (2605.27685) 是本批次中唯一直接提及 MCP (Model Context Protocol) 的论文, 已 verified. MCP 作为工业规范 (Anthropic 2024 提出), 在 arXiv 学术论文中的覆盖率仍较低, 大量 MCP 相关讨论存在于工程博客和 SDK 文档而非学术论文.
- 论文 1 (2606.31518) 提供 agentic orchestration 的系统分类框架, 对企业 Agent 编排架构设计有直接参考价值, 已 verified.
- arXiv 搜索查询: 原始查询 "model context protocol agent orchestration" 多次超时/断连, 改用 "agent framework LLM orchestration" 成功获取 39 篇可见论文 (页面显示共 591 结果), 全部在 2025-09 ~ 2026-07 范围内.
- A2A (Agent-to-Agent) 协议相关论文在本搜索中未出现, 该协议 (Google 2025 提出) 同样以工程文档为主, 学术论文稀缺. 建议教学材料中补充工业白皮书和 SDK 文档.
- 选材偏向: 编排架构/分类框架、延迟优化、静态分析/安全、上下文管理、工作流修复、多 agent 协作.
