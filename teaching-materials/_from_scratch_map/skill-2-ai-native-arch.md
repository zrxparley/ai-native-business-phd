# _from_scratch_map: skill-2-ai-native-arch (v11.0)

> skill-2 AI原生企业架构（4 Day）对应 rohitg00 P13 Tools & Protocols / P14 Agent / P17 Infra。wave agent 离线消费，链接必须从此文件取。

## 模块概述
- **对应 rohitg00 phase**: P13 Tools & Protocols, P14 Agent(orchestration), P17 Infra(lite)
- **from-scratch 主题**: 企业 Agent 编排的 from-scratch 实现（手写 MCP server/StateGraph/HITL/编排拓扑）

## Day 映射

### day-1-process-intelligence-ai-governance: 流程智能驱动+AI治理框架
- **from-scratch 主题**: 手写 MCP server 骨架 + 工具接口
- **rohitg00 链接**:
  - [P13/06 MCP Fundamentals](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/13-tools-and-protocols/06-mcp-fundamentals/README.md) - MCP 基础
  - [P13/07 Building an MCP Server](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/13-tools-and-protocols/07-building-an-mcp-server/README.md) - 构建 MCP server
  - [P13/01 The Tool Interface](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/13-tools-and-protocols/01-the-tool-interface/README.md) - 工具接口
- **核心算法**: JSON-RPC 工具调度

### day-2-agent-orchestration-langgraph: Agent编排架构+LangGraph
- **from-scratch 主题**: 手写 StateGraph 状态机 + 条件分支
- **rohitg00 链接**:
  - [P14/13 LangGraph Stateful Graphs](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/14-agent-engineering/13-langgraph-stateful-graphs/README.md) - LangGraph 状态图
  - [P11/16 LangGraph State Machines](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/11-llm-engineering/16-langgraph-state-machines/README.md) - LLM 工程中的状态机
- **核心算法**: 有向图状态转移 + interrupt

### day-3-human-ai-collaboration-org-change: 人机协作治理+组织变革
- **from-scratch 主题**: 手写 HITL interrupt 工作流 + 审批循环
- **rohitg00 链接**:
  - [P14/12 Anthropic Workflow Patterns](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/14-agent-engineering/12-anthropic-workflow-patterns/README.md) - 工作流模式
  - [P14/02 REWOO Plan and Execute](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/14-agent-engineering/02-rewoo-plan-and-execute/README.md) - Plan-Execute
- **核心算法**: interrupt_before + 人工审批门控

### day-4-enterprise-arch-action-research: 企业级架构+行动研究
- **from-scratch 主题**: 手写企业 Agent 编排拓扑 + 依赖图
- **rohitg00 链接**:
  - [P17/01 Managed LLM Platforms](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/17-infrastructure-and-production/01-managed-llm-platforms/README.md) - 托管 LLM 平台
  - [P14/28 Orchestration Patterns](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/14-agent-engineering/28-orchestration-patterns/README.md) - 编排模式
- **核心算法**: TOGAF 四层依赖图 + 行动研究 KPI 追踪
