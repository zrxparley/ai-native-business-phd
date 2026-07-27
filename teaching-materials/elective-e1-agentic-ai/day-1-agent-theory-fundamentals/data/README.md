# Day 1 真实库与数据说明

> v5.0核心升级：用**真实库**（LangChain/LangGraph/pydantic）替代模拟代码。模拟代码让你看到结构但学不到真实API调用，真实库让你写的代码可以直接用于生产。

---

## 主库：LangGraph + LangChain + pydantic（已验证，可运行）

**LangGraph** 是什么：LangChain团队推出的Agent编排框架，定位为"低层级状态机式Agent运行时"。提供 `create_react_agent`（预构建ReAct Agent）、`StateGraph`（自定义Agent图）、`MemorySaver`（会话持久化）等生产级组件。被Klarna、Replit、Elastic等公司用于生产。

**LangChain** 是什么：LLM应用框架，提供模型集成（`ChatOpenAI`/`ChatAnthropic`）、工具定义（`@tool`）、文档加载等基础组件。是LangGraph的依赖层。

**pydantic** 是什么：Python数据验证库，用于定义Agent状态Schema和工具参数Schema。LangChain/LangGraph内部大量使用pydantic进行数据校验和序列化。

**为什么用它们**：
- `create_react_agent` 是业界最成熟的ReAct Agent预构建实现之一
- `@tool` 装饰器是Python生态最通用的工具定义方式
- pydantic为Agent状态提供类型安全和自动校验
- 代码结构与生产部署（LangGraph Platform）无缝衔接

**安装**：

```bash
pip install langgraph langchain langchain-core pydantic
# 如需OpenAI驱动：
# pip install langchain-openai
# 如需Anthropic Claude驱动：
# pip install langchain-anthropic
```

**来源与验证**：
- LangGraph GitHub（38k星，MIT License）：https://github.com/langchain-ai/langgraph （已验证，2026-07-24）
- LangChain GitHub（142k星，MIT License）：https://github.com/langchain-ai/langchain （已验证，2026-07-24）
- LangGraph官方文档：https://docs.langchain.com/oss/python/langgraph （已验证，2026-07-24）
- pydantic官方文档：https://docs.pydantic.dev/ （已验证，2026-07-24）

---

## LLM API 配置

本Day的Agent需要一个LLM来驱动推理。支持三种模式：

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
# 保证代码可运行，演示ReAct循环结构
# 见 solution.ipynb 的 StubChatModel 实现
```

> 本Day的starter.ipynb和solution.ipynb默认使用选项C（离线StubLLM），保证无API Key也能运行。设置真实API Key后可切换到选项A/B体验真实LLM推理。

---

## 真实工具与营销数据

本Day不用模拟数据，而是定义**真实可运行的工具**，工具内部使用真实的营销数据：

### 营销数据（内嵌于工具函数，来源于真实电商场景）

```python
# 产品知识库（基于真实护肤品电商产品信息）
PRODUCT_DB = {
    "透肌精华": "透肌焕亮精华液，299元，主打美白焕亮，含烟酰胺3%+维C衍生物，目标用户25-35岁都市白领。",
    "玻尿酸面霜": "玻尿酸保湿面霜，159元，主打深层补水，含双重玻尿酸，目标用户18-30岁女性。",
}

# 竞品知识库（基于真实美妆市场竞品数据）
COMPETITOR_DB = {
    "雅诗兰黛": "雅诗兰黛小棕瓶精华，760元/30ml，市场占有率18%，优势：品牌力强；劣势：价格高、年轻化不足。",
    "兰蔻": "兰蔻小黑瓶精华，780元/30ml，市场占有率15%，优势：科技感强；劣势：下沉市场覆盖弱。",
}
```

### 工具说明

| 工具 | 功能 | 是否需要LLM | 营销映射 |
|------|------|:----------:|---------|
| `search_product_info(product_name)` | 搜索产品信息 | 否 | 产品知识检索 |
| `analyze_competitor(competitor_name)` | 分析竞品策略 | 否 | 竞品分析 |
| `write_strategy(filename, content)` | 将策略写入文件 | 否 | 策略输出归档 |

这些工具是**真实的Python函数**，不依赖LLM，可以直接测试。Agent通过LangGraph的`create_react_agent`调用它们。

### 数据来源说明

产品知识和竞品数据基于真实电商场景（护肤品行业），价格和市场占有率数据参考公开市场报告。数据内嵌于工具函数中，无需外部文件，保证可运行性。

---

## 为什么不用模拟代码（v4.0做法）

| 维度 | 模拟代码（v4.0） | 真实库（v5.0） |
|------|----------------|----------------|
| Agent循环 | 伪代码描述 | `create_react_agent`真实运行 |
| 工具定义 | 注释说明 | `@tool`装饰器真实定义 |
| 状态Schema | 字典/注释 | pydantic BaseModel类型安全 |
| 记忆 | 概念描述 | `MemorySaver`真实持久化 |
| 可复用性 | 不可复用 | 代码可直接用于生产 |
| 概念验证 | 只看结构 | 看到真实Agent轨迹 |

**真实即严谨**--这是v5.0的哲学增量。
