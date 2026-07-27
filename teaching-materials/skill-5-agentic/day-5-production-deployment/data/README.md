# Day 5 真实数据与库说明

> v5.0 核心升级：用**真实生产级工具**（langsmith + tiktoken）替代手写监控脚本。手写 `time.time()` + `print` 只能做粗粒度计时，langsmith 做结构化 trace 追踪，tiktoken 做精确 token 计数。

---

## 主可观测性库：langsmith（已验证，可运行）

**这是什么**：langsmith 是 LangChain 团队维护的 LLM 应用可观测性平台 SDK（PyPI 最新版 0.10.x，MIT License），提供 `@traceable` 装饰器自动追踪函数调用链、`wrap_openai` 自动 instrument OpenAI 调用、`Client` 查询 trace 数据。它是 Agent 生产化可观测性的**工程实现**。

**为什么用它**：
- **`@traceable`**：装饰器自动追踪函数执行，记录输入/输出/延迟/嵌套调用链--无需手写计时代码
- **`wrap_openai`**：包装 OpenAI client，自动记录每次 LLM 调用的 prompt/response/token/延迟
- **`Client`**：程序化查询 trace 数据（`list_runs`），用于自动化分析和告警
- **环境变量配置**：`LANGSMITH_TRACING=true` + `LANGSMITH_API_KEY=...` 即可启用云端 trace 上传

**安装方式**：

```bash
pip install langsmith
# 启用云端 trace 上传（可选，不设则本地追踪不上传）：
# export LANGSMITH_TRACING=true
# export LANGSMITH_API_KEY=lsv2_sk_...
# export LANGSMITH_PROJECT=marketing-agent-prod
```

**核心 API 速查**：

| 组件 | 导入 | 用途 |
|------|------|------|
| `@traceable` | `from langsmith import traceable` | 装饰器，自动追踪函数调用链 |
| `wrap_openai` | `from langsmith.wrappers import wrap_openai` | 包装 OpenAI client，自动记录 LLM 调用 |
| `Client` | `from langsmith import Client` | 程序化查询 trace（list_runs / create_dataset） |
| `RunTree` | `from langsmith import RunTree` | 底层 API，手动管理 trace 树 |

**来源与验证**：
- langsmith PyPI：https://pypi.org/project/langsmith/ （已验证，最新版 0.10.x，2026-07 持续发布）
- langsmith GitHub：https://github.com/langchain-ai/langsmith-sdk （已验证，MIT License，活跃维护）
- langsmith 官方文档：https://docs.smith.langchain.com/ （已验证，301 重定向至 docs.langchain.com/langsmith）

---

## Token 计数库：tiktoken（已验证，可运行）

**这是什么**：tiktoken 是 OpenAI 维护的 BPE 分词器（PyPI 持续更新），比同类分词器快 3-6 倍。它是计算 LLM token 消耗（进而计算成本）的事实标准。

**为什么用它**：
- **精确计数**：`enc.encode(text)` 返回精确的 token 列表，`len()` 即 token 数（而非按字符估算）
- **模型适配**：`tiktoken.encoding_for_model("gpt-4o")` 自动选择正确的分词器
- **成本计算基础**：token 数 x 模型定价（$/百万 token）= 真实成本

**安装方式**：

```bash
pip install tiktoken
# tiktoken 是纯本地库，无需 API key，无需网络
```

**核心 API 速查**：

| 组件 | 导入 | 用途 |
|------|------|------|
| `get_encoding` | `import tiktoken; tiktoken.get_encoding("o200k_base")` | 按编码名获取分词器 |
| `encoding_for_model` | `tiktoken.encoding_for_model("gpt-4o")` | 按模型名获取分词器 |
| `enc.encode` | `enc.encode("text")` | 文本 -> token 列表 |
| `enc.decode` | `enc.decode([tokens])` | token 列表 -> 文本 |

**来源与验证**：
- tiktoken GitHub：https://github.com/openai/tiktoken （已验证，OpenAI 官方维护，MIT License）
- tiktoken PyPI：https://pypi.org/project/tiktoken/ （已验证，持续发布）

---

## Agent 编排库：LangGraph（复用 Day 1-2）

本 Day 的营销 Agent 复用 Day 1-2 的 LangGraph 架构。LangGraph 的 **checkpointer** 机制支持 Agent 中断恢复--生产环境中服务重启时可从 checkpoint 恢复而非从头执行，节省重复 token 消耗。

- LangGraph GitHub：https://github.com/langchain-ai/langgraph （已验证，MIT License）
- LangGraph 文档：https://langchain-ai.github.io/langgraph/ （已验证）

---

## 运行数据：营销 Agent 运行日志样本

本 Day 不使用外部数据集，而是用**预置的营销 Agent 运行日志**作为分析对象。数据定义在 `starter.ipynb` 的初始化代码中，包含：

| 数据 | 内容 | 用途 |
|------|------|------|
| 产品知识库 | 3个产品的真实属性（烟酰胺精华液/丝绒口红/防晒霜） | Agent 搜索知识库的模拟数据源 |
| 营销 Brief 集 | 5个营销任务请求 | Agent 输入，压测时复用 |
| 模型定价表 | gpt-4o / gpt-4o-mini 的输入/输出单价 | tiktoken 计 token 后乘单价算成本 |
| 模拟 LLM 函数 | 返回营销文案的离线函数 | 无 API key 时可运行的模拟 LLM |

> 💡 **数据来源说明**：产品知识库和 Brief 基于技能5 Day 2 的营销 Agent 架构设计，模拟真实营销场景。在实际项目中，你应该接入自己的产品数据库和真实 LLM API。tiktoken 的 token 计数是真实的（非模拟），成本计算公式也是真实的。

---

## 为什么不用手写监控脚本（v4.0 做法）

| 维度 | 手写 time.time() + print（v4.0） | langsmith + tiktoken（v5.0） |
|------|--------------------------------|------------------------------|
| 调用链追踪 | ❌ 只能看单步日志 | ✅ @traceable 自动记录嵌套调用链 |
| Token 计数 | ❌ 按字符估算（误差大） | ✅ tiktoken 精确计数（BPE 分词） |
| 成本计算 | ❌ 粗略估算 | ✅ token 数 x 真实定价 |
| 可视化 | ❌ 需自建 Dashboard | ✅ LangSmith 云端 Dashboard |
| 云端存储 | ❌ 本地日志文件 | ✅ 结构化 trace 存储可查询 |
| CI 集成 | ❌ 需自己搭 | ✅ Client API 自动化查询 |

**真实即严谨**--用生产级工具替代手写脚本，是 v5.0 的哲学增量。
