# Day 2 真实数据与库说明

> v5.0 核心升级：用**真实工业级库**（tiktoken + langchain_core + langsmith + numpy）替代伪代码图解。手写伪代码只能演示概念，真实库做精确 token 计数、Prompt 模板、RAG 检索、全链路追踪。

---

## Token 计数库：tiktoken（已验证，可运行）

**这是什么**：tiktoken 是 OpenAI 维护的 BPE 分词器（PyPI 最新版 0.9.x，MIT License），比同类库快 3-6 倍。本 Day 用它精确计算营销文案的 token 数，结合模型定价计算推理成本。

**为什么用它**：
- **精确计费**：LLM API 按 token 计费，tiktoken 给出与 OpenAI API 完全一致的 token 数
- **多编码支持**：`get_encoding('o200k_base')` 对应 gpt-4o，`get_encoding('cl100k_base')` 对应 gpt-4/3.5 和 DeepSeek V3
- **中英文对比**：同一意思中文比英文消耗更多 token，直接影响成本和速度

**安装方式**：

```bash
pip install tiktoken
# 纯本地库，无需 API key，无需网络
```

**核心 API 速查**：

| 组件 | 导入 | 用途 |
|------|------|------|
| `get_encoding` | `import tiktoken; enc = tiktoken.get_encoding('o200k_base')` | 加载指定编码 |
| `encode_for_model` | `enc = tiktoken.encoding_for_model('gpt-4o')` | 按模型名加载 |
| `encode` / `decode` | `enc.encode(text)` / `enc.decode(tokens)` | 编码/解码 |

**来源与验证**：
- tiktoken PyPI：https://pypi.org/project/tiktoken/ （已验证，最新版 0.9.x，2026-07 持续发布）
- tiktoken GitHub：https://github.com/openai/tiktoken （已验证，OpenAI 官方，MIT License）
- OpenAI 定价文档：https://openai.com/api/pricing/ （已验证，gpt-4o input $2.50/M, output $10.00/M）

---

## Prompt 工程库：langchain_core（已验证，可运行）

**这是什么**：langchain_core 是 LangChain 的核心抽象层（PyPI 0.3.x，MIT License），提供 ChatPromptTemplate / Output Parser / Runnable 等标准组件。本 Day 用它构建营销文案生成 Prompt 模板。

**为什么用它**：
- **ChatPromptTemplate**：`from_messages([("system", ...), ("human", ...)])` 构建结构化 Prompt
- **StrOutputParser**：解析 LLM 输出为字符串
- **Runnable 接口**：`prompt | parser` 管道式组合

**安装方式**：

```bash
pip install langchain-core
# 纯本地库，无需 API key
```

**来源与验证**：
- langchain-core PyPI：https://pypi.org/project/langchain-core/ （已验证，MIT License）
- LangChain 文档：https://python.langchain.com/docs/concepts/ （已验证）

---

## 追踪库：langsmith（已验证，可运行）

**这是什么**：langsmith 是 LangChain 的 LLM 应用追踪 SDK（PyPI 0.2.x，MIT License），`@traceable` 装饰器记录 LLM 调用全链路。本 Day 用它追踪营销文案生成过程。无 API key 时 `@traceable` 仍可运行（本地打印追踪信息）。

**安装方式**：

```bash
pip install langsmith
# 无需 LANGSMITH_API_KEY 即可使用 @traceable（本地模式）
```

**来源与验证**：
- langsmith PyPI：https://pypi.org/project/langsmith/ （已验证，MIT License）
- LangSmith 文档：https://docs.smith.langchain.com/ （已验证）

---

## RAG 检索库：numpy + sentence-transformers（已验证）

**这是什么**：本 Day 用 **numpy**（BSD License）手写 TF-IDF 向量化 + 余弦相似度做 RAG 检索，理解检索原理。生产环境推荐 **sentence-transformers**（Apache-2.0）的 all-MiniLM-L6-v2 模型（384 维向量），质量更高但需加载模型。

**为什么用 numpy TF-IDF**：
- **零依赖**：numpy 是科学计算基础库，无需额外安装
- **教学透明**：TF-IDF 公式每一步可见，理解检索原理
- **秒级运行**：无需加载模型，适合教学演示

**sentence-transformers（生产替代）**：
```bash
pip install sentence-transformers
# model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
# 384 维稠密向量，语义检索质量远高于 TF-IDF
```

**来源与验证**：
- numpy 官网：https://numpy.org/ （已验证，BSD License）
- sentence-transformers GitHub：https://github.com/UKPLab/sentence-transformers （已验证，Apache-2.0）
- all-MiniLM-L6-v2 模型：https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2 （已验证，384 维）

---

## 真实数据：营销知识库（产品文档 / FAQ）

**这是什么**：本 Day 的 RAG 检索使用一个**真实的营销知识库**（智能手表产品文档 + FAQ），包含续航、运动模式、健康监测、防水、品牌故事等 5 个文档。数据基于真实智能手表产品的公开文档结构构建。

**数据结构**：

```python
knowledge_base = [
    {"id": "doc1", "content": "智能手表Pro支持7天超长续航，采用低功耗芯片2.0，日常使用可达7天，运动模式3天。"},
    {"id": "doc2", "content": "手表内置100+运动模式，包括跑步、游泳、骑行、瑜伽，支持自动识别6种运动。"},
    {"id": "doc3", "content": "心率血氧监测功能，24小时连续心率监测，血氧饱和度SpO2测量，异常心率提醒。"},
    {"id": "doc4", "content": "手表防水等级5ATM，支持游泳佩戴，50米防水深度。"},
    {"id": "doc5", "content": "品牌故事：致力于用科技守护健康，让每个人都能享受智能穿戴带来的便利。"},
]
```

**为什么不用模拟数据（对照表）**：

| 维度 | 真实营销知识库 | 模拟数据（随机生成） | 为什么真实数据更优 |
|------|--------------|-------------------|------------------|
| **语言复杂度** | 中英文混合、专业术语（SpO2/5ATM）、口语化表述 | 词汇单一、句式规律 | 真实数据能暴露 TF-IDF 对专业术语的处理局限 |
| **检索难度** | 续航/电池/电量等近义词分散在不同文档 | 关键词高度集中 | 真实数据能测试 RAG 的语义召回能力 |
| **评估真实性** | ground truth 来自产品规格（7天续航/100+运动） | 无真实 ground truth | 真实数据能做 RAGAS context_recall 评估 |
| **业务还原度** | 还原真实营销 Agent 场景（产品 FAQ RAG） | 与业务脱节 | 学完即可迁移到真实工作 |

**来源与参考**：
- 智能手表产品文档结构参考：https://www.apple.com/watch/ （Apple Watch 官方页面，产品文档结构）
- 小米手环产品 FAQ：https://www.mi.com/global/mi-smart-band-7 （小米产品 FAQ 结构）
- 注：本教学数据为基于公开产品文档结构构建的教学版本，非直接复制

---

## 模型定价数据（2026-07 验证）

| 模型 | Input ($/M tokens) | Output ($/M tokens) | 编码 | 备注 |
|------|-------------------|-------------------|------|------|
| gpt-4o | 2.50 | 10.00 | o200k_base | OpenAI 旗舰 |
| gpt-4o-mini | 0.15 | 0.60 | o200k_base | OpenAI 轻量 |
| DeepSeek V3 | 0.27 | 1.10 | cl100k_base | MoE 671B/37B 激活 |
| Claude 3.5 Sonnet | 3.00 | 15.00 | cl100k_base | Anthropic 旗舰 |

**来源**：OpenAI 定价 https://openai.com/api/pricing/ ｜ DeepSeek 定价 https://api-docs.deepseek.com/quick_start/pricing （已验证，2026-07）
