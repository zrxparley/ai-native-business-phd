# _from_scratch_map: capstone-ai-business-analytics (v11.0)

> Capstone 商业分析AI原生应用（6 Phase）对应 rohitg00 P19 Capstone。直接映射整合。wave agent 离线消费，链接必须从此文件取。

## 模块概述
- **对应 rohitg00 phase**: P19 Capstone Projects（autonomous research agent / plan-execute / paper-writer 等）
- **from-scratch 主题**: 端到端研究 pipeline from-scratch（手写文献检索/Plan-Execute/因果实验/蒙特卡洛估值/论文生成）

## Day 映射

### day-phase-1-problem-definition-lit-review: 问题定义+文献综述
- **from-scratch 主题**: 手写文献检索 Agent（query expansion + 排序）
- **rohitg00 链接**:
  - [P19/05 Autonomous Research Agent](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/19-capstone-projects/05-autonomous-research-agent/README.md) - 自主研究 agent
  - [P19/51 Literature Retrieval](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/19-capstone-projects/51-literature-retrieval/README.md) - 文献检索
- **核心算法**: query expansion + BM25 排序

### day-phase-2-data-representation-knowledge-graph: 数据表示+知识图谱
- **from-scratch 主题**: 手写 BPE tokenizer + KG 三元组构建
- **rohitg00 链接**:
  - [P19/30 BPE Tokenizer from Scratch](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/19-capstone-projects/30-bpe-tokenizer-from-scratch/README.md) - BPE 分词
  - [P19/50 Hypothesis Generator](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/19-capstone-projects/50-hypothesis-generator/README.md) - 假设生成
- **核心算法**: BPE 合并优先级 + 三元组抽取

### day-phase-3-agentic-system-architecture: Agentic系统架构
- **from-scratch 主题**: 手写 Plan-Execute agent + 验证门控
- **rohitg00 链接**:
  - [P19/24 Plan Execute Control Flow](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/19-capstone-projects/24-plan-execute-control-flow/README.md) - 计划-执行控制流
  - [P19/29 End to End Coding Task Demo](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/19-capstone-projects/29-end-to-end-coding-task-demo/README.md) - 端到端演示
- **核心算法**: Plan→Execute→Verify 三阶段 + 验证门控

### day-phase-4-causal-experiment-design: 因果实验设计
- **from-scratch 主题**: 手写 DML 因果估计 + 实验运行器
- **rohitg00 链接**:
  - [P19/52 Experiment Runner](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/19-capstone-projects/52-experiment-runner/README.md) - 实验运行
  - [P19/53 Result Evaluator](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/19-capstone-projects/53-result-evaluator/README.md) - 结果评估
- **核心算法**: DML 双重正交 + ATE 估计

### day-phase-5-business-model-valuation: 商业模式估值
- **from-scratch 主题**: 手写蒙特卡洛 NPV + 敏感性分析
- **rohitg00 链接**:
  - [P19/56 Iteration Scheduler](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/19-capstone-projects/56-iteration-scheduler/README.md) - 迭代调度
  - [P17/27 FinOps LLMs](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/17-infrastructure-and-production/27-finops-llms/README.md) - LLM FinOps
- **核心算法**: 蒙特卡洛 NPV + Bull/Base/Bear 情景

### day-phase-6-implementation-paper-writing: 实施+论文写作
- **from-scratch 主题**: 手写端到端研究 pipeline + 论文生成器
- **rohitg00 链接**:
  - [P19/57 End to End Research Demo](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/19-capstone-projects/57-end-to-end-research-demo/README.md) - 端到端研究演示
  - [P19/54 Paper Writer](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/19-capstone-projects/54-paper-writer/README.md) - 论文写作
- **核心算法**: pipeline 编排 + IMRaD 章节生成
