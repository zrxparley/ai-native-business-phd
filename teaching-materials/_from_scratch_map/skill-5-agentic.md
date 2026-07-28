# _from_scratch_map: skill-5-agentic (v11.0)

> skill-5 Agentic AI工程（7 Day）对应 rohitg00 P14 Agent / P15 Autonomous / P16 Multi-Agent / P17 Infra。最厚模块。wave agent 离线消费，链接必须从此文件取。

## 模块概述
- **对应 rohitg00 phase**: P14 Agent Engineering(主), P15 Autonomous(选), P16 Multi-Agent(选), P17 Infra(部署)
- **from-scratch 主题**: Agent 工程全栈 from-scratch（手写 ReAct/StateGraph/eval harness/注入防御/vLLM调度/观测/runtime）

## Day 映射

### day-1-agent-architecture: Agent架构
- **from-scratch 主题**: 手写 ReAct agent loop（thought-action-observation 循环）
- **rohitg00 链接**:
  - [P14/01 The Agent Loop](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/14-agent-engineering/01-the-agent-loop/README.md) - agent loop from scratch
  - [P14/06 Tool Use and Function Calling](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/14-agent-engineering/06-tool-use-and-function-calling/README.md) - 工具调用
- **核心算法**: ReAct 循环 + JSON 工具分发

### day-2-langgraph-orchestration: LangGraph编排
- **from-scratch 主题**: 手写 StateGraph 状态机 + 条件分支
- **rohitg00 链接**:
  - [P14/13 LangGraph Stateful Graphs](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/14-agent-engineering/13-langgraph-stateful-graphs/README.md) - 状态图
  - [P14/12 Anthropic Workflow Patterns](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/14-agent-engineering/12-anthropic-workflow-patterns/README.md) - 工作流模式
- **核心算法**: 有向图状态转移 + 条件路由

### day-3-agent-evaluation: Agent评估
- **from-scratch 主题**: 手写 Agent eval harness（任务 fixture + 通过率）
- **rohitg00 链接**:
  - [P14/19 Benchmarks SWE-bench GAIA](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/14-agent-engineering/19-benchmarks-swebench-gaia/README.md) - 基准测试
  - [P14/30 Eval Driven Agent Development](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/14-agent-engineering/30-eval-driven-agent-development/README.md) - 评估驱动开发
- **核心算法**: 任务通过率 + 轨迹评分

### day-4-security-adversarial: 安全防护与对抗
- **from-scratch 主题**: 手写 prompt injection 检测器 + 防御层
- **rohitg00 链接**:
  - [P14/27 Prompt Injection Defense](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/14-agent-engineering/27-prompt-injection-defense/README.md) - 注入防御
  - [P18/16 Red Team Tooling Garak LlamaGuard PyRIT](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/18-ethics-safety-alignment/16-red-team-tooling-garak-llamaguard-pyrit/README.md) - 红队工具
- **核心算法**: 模式匹配 + 输出分类器

### day-5-production-deployment: 生产部署与运维
- **from-scratch 主题**: 手写简易 vLLM 连续批处理调度骨架
- **rohitg00 链接**:
  - [P17/04 vLLM Serving Internals](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/17-infrastructure-and-production/04-vllm-serving-internals/README.md) - vLLM 内部
  - [P17/13 LLM Observability](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/17-infrastructure-and-production/13-llm-observability/README.md) - 可观测性
- **核心算法**: 连续批处理 + KV cache 复用

### day-6-imrad-writing: IMRaD论文写作
- **from-scratch 主题**: 手写实验追踪 logger（trace + span）
- **rohitg00 链接**:
  - [P14/24 Agent Observability Platforms](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/14-agent-engineering/24-agent-observability-platforms/README.md) - 可观测平台
  - [P14/23 OTel GenAI Conventions](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/14-agent-engineering/23-otel-genai-conventions/README.md) - OTel 语义约定
- **核心算法**: trace/span 结构化日志

### day-7-capstone-integration: Capstone整合
- **from-scratch 主题**: 手写端到端 Agent runtime（loop + tool + guardrail + obs）
- **rohitg00 链接**:
  - [P14/29 Production Runtimes](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/14-agent-engineering/29-production-runtimes/README.md) - 生产 runtime
  - [P17/23 SRE for AI](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/17-infrastructure-and-production/23-sre-for-ai/README.md) - AI SRE
- **核心算法**: runtime 四件套（loop/tool/guard/obs）组装
