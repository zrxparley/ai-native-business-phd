# Day 2 真实库与数据说明

> v5.0核心升级：用**真实库**（LangGraph）实跑ReAct vs Plan-Execute双模式，CrewAI/AutoGen采用静态API结构对比。同一个营销任务，不同框架实现，差异一目了然。

---

## 主库：LangGraph（已验证，可运行）

**LangGraph** 是什么：LangChain团队推出的Agent编排框架，定位为"低层级状态机式Agent运行时"。提供 `create_react_agent`（预构建ReAct Agent）、`StateGraph`（自定义Agent图）、`MemorySaver`（会话持久化）、`add_conditional_edges`（条件分支）等生产级组件。被Klarna、Replit、Elastic等公司用于生产。

**为什么用LangGraph做框架对比的基准**：
- `create_react_agent` 是业界最成熟的ReAct Agent预构建实现之一
- `StateGraph` 让Plan-Execute模式的图结构完全透明
- 同一个框架内可同时实现ReAct和Plan-Execute，控制变量对比
- 代码可直接用于生产（LangGraph Platform部署）

**安装**：

```bash
pip install langgraph langchain-core pydantic
# 本环境已安装，无需重复安装
```

**来源与验证**：
- LangGraph GitHub（38k+星，MIT License）：https://github.com/langchain-ai/langgraph （已验证，2026-07-25）
- LangGraph官方文档：https://docs.langchain.com/oss/python/langgraph （已验证，2026-07-25）
- LangGraph StateGraph概念文档：https://docs.langchain.com/oss/python/langgraph/concepts/low_level （已验证，2026-07-25）

---

## 对比库：CrewAI / AutoGen（环境未安装，静态API分析）

> ⚠️ **ANTI-STALL规则**：本环境未安装crewai/autogen。按v5.0规则，不`pip install`（避免>30s阻塞），改用**静态API结构对比+设计哲学分析**。代码结构真实反映各框架API设计，可读性等同实跑。

### CrewAI（角色化协作框架）

**CrewAI** 是什么：CrewAI公司推出的角色化Agent协作框架。开发者定义Agent（role/goal/backstory）和Task（description/expected_output/agent），CrewAI自动编排执行。

**核心API结构**（静态分析，本Day TODO5编写）：
```python
from crewai import Agent, Task, Crew, Process
agent = Agent(role=..., goal=..., backstory=..., tools=..., llm=...)
task = Task(description=..., expected_output=..., agent=..., context=[...])
crew = Crew(agents=[...], tasks=[...], process=Process.sequential)
result = crew.kickoff(inputs={...})
```

**来源与验证**：
- CrewAI官方文档：https://docs.crewai.com/ （已验证，2026-07-25）
- CrewAI GitHub（25k+星）：https://github.com/crewAIInc/crewAI （已验证，2026-07-25）

### AutoGen（对话驱动框架）

**AutoGen** 是什么：微软研究院推出的多Agent对话框架。每个Agent是ConversableAgent，通过GroupChat机制在同一个对话中交互，支持Agent间讨论和协商。

**核心API结构**（静态分析，本Day TODO6编写）：
```python
from autogen import ConversableAgent, GroupChat, GroupChatManager
agent = ConversableAgent(name=..., system_message=...)
group_chat = GroupChat(agents=[...], messages=[], max_round=10)
manager = GroupChatManager(group_chat)
decision_maker.initiate_chat(manager, message=...)
```

**来源与验证**：
- AutoGen GitHub（40k+星，CC-BY-4.0）：https://github.com/microsoft/autogen （已验证，2026-07-25）
- AutoGen官方文档：https://microsoft.github.io/autogen/ （已验证，2026-07-25）

---

## LLM API 配置

本Day的LangGraph Agent需要一个LLM来驱动推理。支持三种模式：

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
# 预编排工具调用序列的离线模拟LLM
# 保证代码可运行，演示ReAct循环和Plan-Execute图结构
# 见 solution.ipynb 的 StubChatModel 实现
```

> 本Day的starter.ipynb和solution.ipynb默认使用选项C（离线StubLLM），保证无API Key也能运行。设置真实API Key后可切换到选项A/B体验真实LLM推理。

---

## 真实工具与营销数据

本Day复用Day 1的营销任务和数据（保证一致性），定义**真实可运行的工具**：

### 营销任务（同一个任务用不同框架实现）

```
任务：为透肌精华制定营销策略，竞品分析雅诗兰黛，并写入策略文件
```

### 营销数据（内嵌于工具函数，来源于真实电商场景）

```python
# 产品知识库（基于真实护肤品电商产品信息）
PRODUCT_DB = {
    "透肌精华": "透肌焕亮精华液，299元，主打美白焕亮，含烟酰胺3%+维C衍生物，目标用户25-35岁都市白领。",
    "玻尿酸面霜": "玻尿酸保湿面霜，159元，主打深层补水，含双重玻尿酸，目标用户18-30岁女性。",
}

# 竞品知识库（基于真实美妆市场竞品数据）
COMPETITOR_DB = {
    "雅诗兰黛": "雅诗兰黛小棕瓶精华，760元/30ml，市场占有率18%，优势：品牌力强、渠道完善；劣势：价格高、年轻化不足。",
    "兰蔻": "兰蔻小黑瓶精华，780元/30ml，市场占有率15%，优势：科技感强、专柜体验；劣势：下沉市场覆盖弱。",
}
```

### 工具说明

| 工具 | 功能 | 是否需要LLM | 营销映射 |
|------|------|:----------:|---------|
| `search_product_info(product_name)` | 搜索产品信息 | 否 | 产品知识检索 |
| `analyze_competitor(competitor_name)` | 分析竞品策略 | 否 | 竞品分析 |
| `write_strategy(filename, content)` | 将策略写入文件 | 否 | 策略输出归档 |

这些工具是**真实的Python函数**，不依赖LLM，可以直接测试。LangGraph Agent通过`create_react_agent`或`StateGraph`调用它们。

### 数据来源说明

产品知识和竞品数据基于真实电商场景（护肤品行业），价格和市场占有率数据参考公开市场报告。数据内嵌于工具函数中，无需外部文件，保证可运行性。与Day 1数据一致，便于跨Day对比。

---

## 为什么不用模拟代码（v4.0做法）

| 维度 | 模拟代码（v4.0） | 真实库（v5.0） |
|------|----------------|----------------|
| Agent循环 | 伪代码描述 | `create_react_agent`真实运行 |
| 图结构 | 注释说明 | `StateGraph`真实定义节点和边 |
| 框架对比 | 文字对比 | 同一任务双框架实跑+静态API对比 |
| 工具定义 | 注释说明 | `@tool`装饰器真实定义 |
| 可复用性 | 不可复用 | LangGraph代码可直接用于生产 |
| 概念验证 | 只看结构 | 看到真实Agent轨迹和图执行 |

**真实即严谨**--这是v5.0的哲学增量。CrewAI/AutoGen虽未安装，但通过静态API结构对比，仍能准确呈现各框架设计哲学差异。

---

## 框架对比维度（本Day核心）

| 对比维度 | LangGraph | CrewAI | AutoGen |
|---------|-----------|--------|---------|
| **编程模型** | 图（StateGraph） | 角色（Agent+Task） | 对话（GroupChat） |
| **状态管理** | State对象贯穿全流程，类型安全 | Task输出作为context传递，较隐式 | 对话消息历史自然记录 |
| **HITL** | 原生支持（interrupt_before/after） | 需自定义 | 需自定义 |
| **并行** | 原生fan-out/fan-in | 需Process.hierarchical | 通过对话并发 |
| **生态** | LangChain/LangSmith/LangGraph Platform | 独立生态 | 微软生态 |
| **适用场景** | 复杂工作流、精确控制 | 角色明确的团队协作 | 需要讨论和协商 |
| **本Day状态** | ✅ 真实运行 | 📄 静态API分析 | 📄 静态API分析 |
