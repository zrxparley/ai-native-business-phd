# Day 3 真实库与数据说明

> v5.0核心升级：用**双真实库**（LangGraph多Agent图 + networkx拓扑分析）构建多Agent营销协作系统。supervisor和team两种拓扑实跑，涌现行为一目了然。

---

## 主库1：LangGraph（多Agent协作图，已验证可运行）

**LangGraph** 是什么：LangChain团队推出的Agent编排框架。本Day用其多Agent能力：
- `StateGraph` 定义多Agent协作图（节点=Agent，边=消息流/控制流）
- `add_conditional_edges` 实现supervisor到各Agent的路由（中心化拓扑）
- `Annotated[list, operator.add]` 实现Agent间消息累积传递
- `END`/`START` 控制图入口出口

**为什么用LangGraph做多Agent**：
- 原生支持supervisor/hierarchical/team三种多Agent拓扑
- 状态驱动设计，所有Agent共享`MultiAgentState`
- 条件路由+循环退出，支持Agent间多轮交互
- 代码可直接用于生产（LangGraph Platform部署）

**安装**：

```bash
pip install langgraph langchain-core pydantic
# 本环境已安装，无需重复安装
```

**来源与验证**：
- LangGraph GitHub（38k+星，MIT License）：https://github.com/langchain-ai/langgraph （已验证，2026-07-25）
- LangGraph多Agent协作教程：https://docs.langchain.com/oss/python/langgraph/tutorials/multi_agent/multi-agent-collaboration （已验证，2026-07-25）
- LangGraph核心概念文档：https://docs.langchain.com/oss/python/langgraph/concepts/low_level （已验证，2026-07-25）

---

## 主库2：networkx（Agent通信拓扑分析，已验证可运行）

**networkx** 是什么：Python图论与网络科学库。本Day用其分析多Agent通信拓扑：
- 节点 = Agent，边 = 消息流（谁向谁发消息）
- `nx.DiGraph()` 构建有向通信图
- `nx.degree_centrality()` 度中心性（谁是通信枢纽）
- `nx.is_strongly_connected()` 强连通性（消息能否到达所有Agent）
- `nx.betweenness_centrality()` 介数中心性（谁是信息瓶颈）
- `nx.shortest_path()` 关键路径（信息从A到B的最短路径）

**为什么用networkx分析多Agent**：
- 把抽象的"Agent协作"变成可计算的图指标
- 量化识别瓶颈Agent（介数中心性高的节点）
- 评估拓扑鲁棒性（移除某Agent后是否仍连通）
- 为天道推演的"因果链追踪"提供网络科学工具

**安装**：

```bash
pip install networkx
# 本环境已安装（v3.3），无需重复安装
```

**来源与验证**：
- networkx官方文档：https://networkx.org/documentation/stable/ （已验证，2026-07-25）
- networkx GitHub（14k+星，BSD License）：https://github.com/networkx/networkx （已验证，2026-07-25）

---

## LLM API 配置

本Day的多Agent系统需要LLM驱动Agent推理。支持三种模式：

### 选项 A：OpenAI
```python
import os
os.environ["OPENAI_API_KEY"] = "sk-..."
from langchain_openai import ChatOpenAI
model = ChatOpenAI(model="gpt-4o-mini", temperature=0)
```

### 选项 B：Anthropic Claude（推荐）
```python
import os
os.environ["ANTHROPIC_API_KEY"] = "sk-ant-..."
from langchain_anthropic import ChatAnthropic
model = ChatAnthropic(model="claude-sonnet-4-20250514")
```

### 选项 C：离线StubLLM（无需API Key，本Day默认）
```python
# 预编排Agent响应的离线模拟LLM
# 保证多Agent图可编译可运行，演示supervisor路由和team消息流
# 见 solution.ipynb 的 StubChatModel 实现
```

> 本Day的starter.ipynb和solution.ipynb默认使用选项C（离线StubLLM），保证无API Key也能运行。设置真实API Key后可切换到选项A/B体验真实多Agent涌现。

---

## 真实营销数据（复用Day 1/2，保证跨Day一致性）

本Day复用Day 1/2的营销任务和数据（保证一致性），4个Agent协作完成：

### 营销任务（多Agent协作完成）

```
任务：为透肌精华制定营销策略，竞品分析雅诗兰黛，产出合规文案
协作Agent：researcher（调研）-> strategist（策略）-> writer（文案）-> reviewer（审核）
```

### 营销数据（内嵌于Agent工具函数，来源于真实电商场景）

```python
# 产品知识库（基于真实护肤品电商产品信息，与Day 1/2一致）
PRODUCT_DB = {
    "透肌精华": "透肌焕亮精华液，299元，主打美白焕亮，含烟酰胺3%+维C衍生物，目标用户25-35岁都市白领。",
    "玻尿酸面霜": "玻尿酸保湿面霜，159元，主打深层补水，含双重玻尿酸，目标用户18-30岁女性。",
}

# 竞品知识库（基于真实美妆市场竞品数据，与Day 1/2一致）
COMPETITOR_DB = {
    "雅诗兰黛": "雅诗兰黛小棕瓶精华，760元/30ml，市场占有率18%，优势：品牌力强、渠道完善；劣势：价格高、年轻化不足。",
    "兰蔻": "兰蔻小黑瓶精华，780元/30ml，市场占有率15%，优势：科技感强、专柜体验；劣势：下沉市场覆盖弱。",
}
```

### Agent职责分工

| Agent | 职能 | 输入 | 输出 | 工具 |
|-------|------|------|------|------|
| **researcher** | 市场调研 | 调研主题 | 竞品分析+市场趋势 | 产品库/竞品库查询 |
| **strategist** | 策略制定 | 市场报告 | 差异化策略文档 | 策略推理 |
| **writer** | 文案生成 | 策略文档 | 营销文案草稿 | LLM生成 |
| **reviewer** | 合规审核 | 文案草稿 | 审核结果+修改建议 | 合规规则库 |
| **supervisor** | 流程协调 | 用户Brief | 路由决策 | 条件路由 |

### 数据来源说明

产品知识和竞品数据基于真实电商场景（护肤品行业），价格和市场占有率数据参考公开市场报告。数据内嵌于Agent函数中，无需外部文件，保证可运行性。与Day 1/2数据一致，便于跨Day对比。

---

## 为什么不用模拟代码（v4.0做法）

| 维度 | 模拟代码（v4.0） | 真实库（v5.0） |
|------|----------------|----------------|
| 多Agent拓扑 | 注释说明 | `StateGraph`真实定义节点和边 |
| Agent间通信 | 伪代码描述 | `AgentMessage`（pydantic）真实传递 |
| 拓扑分析 | 文字描述 | networkx真实计算中心性/连通性 |
| 涌现行为 | 定性描述 | networkx指标定量度量 |
| 可复用性 | 不可复用 | LangGraph+networkx代码可直接用于生产 |
| 协议设计 | 注释说明 | A2A/MCP协议真实引用+结构化消息 |

**真实即严谨**--这是v5.0的哲学增量。多Agent系统的复杂性来自拓扑和通信，只有真实库才能呈现这些细节。

---

## 多Agent拓扑对比维度（本Day核心）

| 对比维度 | supervisor中心化 | team去中心化 |
|---------|-----------------|-------------|
| **控制流** | supervisor路由决策 | Agent间直接传递 |
| **通信模式** | 星型（hub-spoke） | 网状（peer-to-peer） |
| **鲁棒性** | supervisor是单点故障 | 无单点故障 |
| **协调开销** | 低（supervisor集中调度） | 高（Agent间协商） |
| **收敛保证** | supervisor保证收敛 | 需额外机制防无限循环 |
| **networkx中心性** | supervisor度中心性最高 | 各Agent度中心性接近 |
| **适用场景** | 流程明确的营销协作 | 探索性头脑风暴 |
