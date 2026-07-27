# Day 1 真实库与工具说明

> v5.0 核心升级：用**真实库**（LangChain/LangGraph）替代模拟代码。模拟代码让你看到结构但学不到真实 API 调用，真实库让你写的代码可以直接用于生产。

---

## 主库：LangGraph + LangChain（已验证，可运行）

**LangGraph** 是什么：LangChain 团队推出的 Agent 编排框架，定位为"低层级状态机式 Agent 运行时"。提供 `create_react_agent`（预构建 ReAct Agent）、`StateGraph`（自定义 Agent 图）、`MemorySaver`（会话持久化）等生产级组件。被 Klarna、Replit、Elastic 等公司用于生产。

**LangChain** 是什么：LLM 应用框架，提供模型集成（`ChatOpenAI`/`ChatAnthropic`）、工具定义（`@tool`）、文档加载等基础组件。是 LangGraph 的依赖层。

**为什么用它们**：
- `create_react_agent` 是业界最成熟的 ReAct Agent 预构建实现之一
- `@tool` 装饰器是 Python 生态最通用的工具定义方式
- 代码结构与生产部署（LangGraph Platform）无缝衔接
- 文档完善、社区活跃、Star 数高（LangGraph 38k 星，LangChain 142k 星）

**安装**：

```bash
pip install langgraph langchain langchain-openai
# 或使用 Anthropic Claude：
# pip install langgraph langchain langchain-anthropic
```

**来源与验证**：
- LangGraph GitHub（38k 星，MIT License，"Build resilient agents"）：https://github.com/langchain-ai/langgraph （已验证，2026-07-24）
- LangChain GitHub（142k 星，MIT License）：https://github.com/langchain-ai/langchain （已验证，2026-07-24）
- LangGraph 官方文档（新址）：https://docs.langchain.com/oss/python/langgraph （已验证，2026-07-24，"LangGraph overview"）
- LangChain 官方文档：https://python.langchain.com/docs/ （已验证）

---

## LLM API 配置

本 Day 的 Agent 需要一个 LLM 来驱动推理。支持两种选项：

### 选项 A：OpenAI（默认）
```python
import os
os.environ["OPENAI_API_KEY"] = "sk-..."  # 替换为你的 key
from langchain_openai import ChatOpenAI
model = ChatOpenAI(model="gpt-4o-mini", temperature=0)
```

### 选项 B：Anthropic Claude（推荐用于本课程）
```python
import os
os.environ["ANTHROPIC_API_KEY"] = "sk-ant-..."  # 替换为你的 key
from langchain_anthropic import ChatAnthropic
model = ChatAnthropic(model="claude-sonnet-4-20250514")
```

> ⚠️ 没有 API Key 也能完成 TODO1（定义工具并直接测试），但 TODO2-6 的 Agent 调用需要 LLM API。

---

## 真实工具（本 Day Lab 使用）

本 Day 不用模拟数据，而是定义**真实可运行的工具**：

| 工具 | 功能 | 是否需要 LLM | 营销映射 |
|------|------|:----------:|---------|
| `calculate_roi(revenue, cost)` | 计算投资回报率 | 否 | 投入产出分析 |
| `analyze_sentiment(text)` | 分析文本情感倾向（基于关键词） | 否 | 用户评价分析 |
| `write_strategy(filename, content)` | 将策略写入文件 | 否 | 策略输出归档 |

这些工具是**真实的 Python 函数**，不依赖 LLM，可以直接测试。Agent 通过 LangGraph 的 `create_react_agent` 调用它们。

### 营销任务数据（内嵌于笔记本）

笔记本中的营销任务使用以下真实场景数据（内嵌为 Python 变量，无需外部文件）：

```python
# 产品信息
product = {
    "name": "透肌焕亮精华液",
    "category": "护肤品",
    "price": 299,
    "cost": 80,
}

# 用户评价样本（用于情感分析工具）
reviews = [
    "这款精华液效果好，用完皮肤很光滑，推荐！",
    "价格太贵了，效果一般，不太满意。",
    "用了两周，美白效果明显，会回购。",
    "包装很劣质，配送也慢，失望。",
]
```

---

## 为什么不用模拟代码（v4.0 做法）

| 维度 | 模拟代码（v4.0） | 真实库（v5.0） |
|------|----------------|----------------|
| Agent 循环 | 伪代码描述 | `create_react_agent` 真实运行 |
| 工具定义 | 注释说明 | `@tool` 装饰器真实定义 |
| 记忆 | 概念描述 | `MemorySaver` 真实持久化 |
| 可复用性 | 不可复用 | 代码可直接用于生产 |
| 概念验证 | 只看结构 | 看到真实 LLM 推理过程 |

**真实即严谨**--这是 v5.0 的哲学增量。
