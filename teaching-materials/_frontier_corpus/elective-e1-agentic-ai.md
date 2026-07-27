# 前沿语料库: elective-e1-agentic-ai - 多Agent框架与协作拓扑

> v9.0 前沿注入层共享语料库. 论文来自 arXiv 搜索 (2025-09 ~ 2026-07, post 2025-08 cutoff). 标注 verified 的论文经 abstract 页抽查. wave agent 仅可引用本文档列出的论文, 禁止编造.

## 论文

### 1. IDSTune: A Multi-Agent Collaborative Framework for Integrated Database System Tuning
- **arXiv**: https://arxiv.org/abs/2607.22031
- **作者**: Yiyan Li, Guanli Liu
- **年份**: 2026
- **摘要**: 提出 IDSTune 框架, 通过 LLM 驱动的多 Agent 协作联合优化数据库系统的多个配置组件 (knobs, indexes, materialized views). 在性能上实现最高 38% 提升, 调优速度提升 57%, 证明了多 Agent 协作在复杂系统优化中的有效性.
- **验证**: verified

### 2. A Knowledge-Grounded Behavioral Reasoning Framework for Training-Free Urban Healthcare OD Prediction
- **arXiv**: https://arxiv.org/abs/2607.21906
- **作者**: Linzhen Yang, Xueliang Liu
- **年份**: 2026
- **摘要**: 提出无需训练的城市医疗 OD 预测框架, 利用多 Agent 推理管道对结构化城市知识进行协作推理. 在 Top-K 指标上超越深度学习基线, 展示了知识驱动的多 Agent 协作在空间预测任务中的潜力.
- **验证**: unverified

### 3. LLMs Get Lost in Evolving User Intent
- **arXiv**: https://arxiv.org/abs/2607.20734
- **作者**: Jihoon Tack, Philippe Laban
- **年份**: 2026
- **摘要**: 引入一个将静态任务转化为多轮对话的框架, 其中用户意图动态演变. 研究发现静态设置下的强劲性能无法迁移到意图演变设置, 揭示了多 Agent/多轮协作场景中的关键挑战.
- **验证**: unverified

### 4. Small, Free, and Effective: Orchestrating Open-Weight Small Language Models to Outperform Single LLM for Malware Analysis
- **arXiv**: https://arxiv.org/abs/2607.20216
- **作者**: Adel ElZemity, Shujun Li
- **年份**: 2026
- **摘要**: 评估四种小模型编排架构, 混合系统结合证据锚定管道与对抗辩论推理, 实现 35.30% 准确率. 展示了通过编排多个开源小模型超越单一 LLM 的协作策略.
- **验证**: unverified

### 5. ETPDesigner: Multi-Agent Orchestration for Interactive Multimodal Electronic Theater Program
- **arXiv**: https://arxiv.org/abs/2607.19947
- **作者**: Mengtian Li, Xinruo Guo
- **年份**: 2026
- **摘要**: 提出 ETPDesigner 协作多 Agent 框架, 从戏剧脚本合成电子剧场节目. 使用"全局风格锚定机制"保证跨页面视觉一致性, 展示了多 Agent 编排在多模态创意任务中的应用.
- **验证**: unverified

### 6. Oracle Gap and Signal Fidelity: A Fixed-Pool Diagnostic for Test-Time Collaboration
- **arXiv**: https://arxiv.org/abs/2607.17531
- **作者**: Jie Hu
- **年份**: 2026
- **摘要**: 将测试时协作重新定义为候选选择问题而非多 Agent 拓扑的内在属性. 提出 oracle gap 和 signal fidelity 两个诊断指标, 为多 Agent 协作拓扑的部署前评估提供实用工具.
- **验证**: unverified

### 7. Debate-on-Graph: Reliable and Adaptive Reasoning of Large Language Model on Uncertain Knowledge Graph
- **arXiv**: https://arxiv.org/abs/2607.17266
- **作者**: Peiji Yu, Xin Chen
- **年份**: 2026
- **摘要**: 提出 DoG 框架, 通过多 Agent 辩论机制使 LLM 与不确定知识图谱自适应协作推理. 在四个 QA 基准上达到 SOTA, 证明了辩论式协作拓扑在可靠推理中的价值.
- **验证**: verified

### 8. DevicesWorld: Benchmarking Cross-Device Agents in Heterogeneous Environments
- **arXiv**: https://arxiv.org/abs/2607.13465
- **作者**: Huatao Li, Xinwei Geng
- **年份**: 2026
- **摘要**: 提出 DevicesWorld 大规模基准, 包含 6,140 个跨设备协作操作任务. 最强的前沿 LLM-Agent 系统成功率仅达 12.5%, 揭示了异构环境下多 Agent 协作的巨大挑战.
- **验证**: unverified

### 9. MetaInfer: A Knowledge Only LLM Inference Engine Generator SKILL Toolbox
- **arXiv**: https://arxiv.org/abs/2607.12875
- **作者**: Zhenwen Miao, Honglin Wang
- **年份**: 2026
- **摘要**: 提出 MetaInfer, 采用"LLM-as-Compiler"方法, 通过 LLM 驱动的多 Agent 协作系统从运行时约束自动生成定制化推理框架. 展示了多 Agent 协作在系统生成中的应用.
- **验证**: unverified

### 10. Communication-Efficient Digital-Twin Coordination for Heterogeneous LLM Embodied Agents over Computing Power Networks
- **arXiv**: https://arxiv.org/abs/2607.09330
- **作者**: Nuocheng Yang, Sihua Wang
- **年份**: 2026
- **摘要**: 提出 LDT-Coord 网络化协调框架, 使用轻量级数字孪生将协调性能与自然语言推理能力解耦. 通信开销降低 70 倍以上, 展示了高效的多 Agent 通信协作拓扑.
- **验证**: unverified

## 备注
- 论文均来自 arXiv "multi-agent LLM collaboration framework" 搜索, 按 announced_date 降序排列.
- 10 篇论文全部位于 2026-07, 反映该领域当前高度活跃.
- 覆盖多 Agent 协作的多个维度: 框架设计 (IDSTune, ETPDesigner), 协作拓扑诊断 (Oracle Gap), 辩论式协作 (DoG), 跨设备协作 (DevicesWorld), 通信效率 (LDT-Coord), 编排策略 (Small Free Effective).
- verified 论文: #1 (IDSTune) 和 #7 (Debate-on-Graph) 经 arXiv abstract 页确认存在且标题匹配.
