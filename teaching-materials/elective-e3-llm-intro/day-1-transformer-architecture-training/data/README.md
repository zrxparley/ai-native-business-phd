# Day 1 真实数据与库说明

> v5.0 核心升级：用**真实工业级库**（transformers + torch + tiktoken）替代伪代码图解。手写伪代码只能演示概念，真实库做精确 tokenization、架构分析、注意力计算。

---

## 架构分析库：transformers（已验证，可运行）

**这是什么**：transformers 是 HuggingFace 维护的 NLP 模型库（PyPI 最新版 4.57.x，Apache-2.0 License），提供 `AutoConfig` 读取模型架构参数、`AutoTokenizer` 加载分词器。本 Day 仅用 config + tokenizer，**不加载预训练权重**（避免下载 500MB+ 模型文件）。

**为什么用它**：
- **AutoConfig**：`AutoConfig.from_pretrained("gpt2")` 秒级加载 GPT-2 架构参数（n_layer=12, n_head=12, n_embd=768, vocab_size=50257），无需下载模型权重
- **AutoTokenizer**：`AutoTokenizer.from_pretrained("gpt2")` 加载真实 BPE 分词器，对营销文案做精确 tokenization
- **架构分析**：从 config 推算参数量（GPT-2 small ~124M），理解 Scale Law

**安装方式**：

```bash
pip install transformers
# 无需 API key，无需下载模型权重（仅用 config + tokenizer）
```

**核心 API 速查**：

| 组件 | 导入 | 用途 |
|------|------|------|
| `AutoConfig` | `from transformers import AutoConfig` | 读取模型架构参数 |
| `AutoTokenizer` | `from transformers import AutoTokenizer` | 加载分词器 |
| `GPT2Config` | `from transformers import GPT2Config` | GPT-2 专用 config |

**来源与验证**：
- transformers PyPI：https://pypi.org/project/transformers/ （已验证，最新版 4.57.x，2026-07 持续发布）
- transformers GitHub：https://github.com/huggingface/transformers （已验证，Apache-2.0 License，活跃维护）
- transformers 文档：https://huggingface.co/docs/transformers/ （已验证）

---

## 深度学习库：torch（已验证，可运行）

**这是什么**：torch（PyTorch）是 Meta 维护的深度学习框架（PyPI 2.6.x，BSD-style License），提供张量运算和自动微分。本 Day 用 torch 手写简化版 Self-Attention 和 Transformer Block。

**为什么用它**：
- **张量运算**：`torch.randn`、矩阵乘法 `@`、`F.softmax` -- 手写注意力公式的每一步
- **nn.Module**：用 `torch.nn.Linear`/`LayerNorm`/`Embedding` 组装 Transformer Block
- **教学版实现**：不调用 `transformers.GPT2Model`，而是手写 Q/K/V 计算流程，理解架构而非黑箱

**安装方式**：

```bash
pip install torch
# torch 是本地库，无需 API key，无需网络
```

**来源与验证**：
- PyTorch 官网：https://pytorch.org/ （已验证，BSD-style License）
- PyTorch GitHub：https://github.com/pytorch/pytorch （已验证，活跃维护）
- PyTorch 文档：https://docs.pytorch.org/ （已验证）

---

## Token 计数库：tiktoken（已验证，可运行）

**这是什么**：tiktoken 是 OpenAI 维护的 BPE 分词器（PyPI 0.12.x，MIT License），比同类分词器快 3-6 倍。它是计算 LLM token 消耗（进而计算推理成本）的事实标准。

**为什么用它**：
- **精确计数**：`enc.encode(text)` 返回精确的 token 列表，`len()` 即 token 数
- **BPE 可视化**：`enc.decode([token_id])` 可查看每个子词 token 的文本
- **成本计算**：token 数 × 模型定价 = 真实推理成本

**安装方式**：

```bash
pip install tiktoken
# tiktoken 是纯本地库，无需 API key，无需网络
```

**核心 API 速查**：

| 组件 | 导入 | 用途 |
|------|------|------|
| `get_encoding` | `import tiktoken; tiktoken.get_encoding('gpt2')` | 按编码名获取分词器 |
| `encoding_for_model` | `tiktoken.encoding_for_model('gpt-4o')` | 按模型名获取分词器 |
| `enc.encode` | `enc.encode('text')` | 文本 -> token 列表 |
| `enc.decode` | `enc.decode([tokens])` | token 列表 -> 文本 |

**来源与验证**：
- tiktoken GitHub：https://github.com/openai/tiktoken （已验证，OpenAI 官方，MIT License）
- tiktoken PyPI：https://pypi.org/project/tiktoken/ （已验证，持续发布）

---

## 运行数据：营销文案语料

本 Day 不使用外部数据集，而是用**预置的营销文案语料**作为分析对象。数据定义在 `starter.ipynb` 的初始化代码中，包含：

| 数据 | 内容 | 用途 |
|------|------|------|
| 英文营销 Brief | "Write a Xiaohongshu marketing copy..." | tokenization 对比（英文） |
| 中文营销 Brief | "为一款烟酰胺精华液写小红书种草文案..." | tokenization 对比（中文） |
| 英文产品描述 | "Niacinamide Brightening Serum 5%..." | 注意力可视化（英文） |
| 中文产品描述 | "烟酰胺亮肤精华液 5%烟酰胺..." | tokenization 对比（中文） |
| 模型定价表 | gpt-4o / gpt-4o-mini 的输入/输出单价 | tiktoken 计 token 后乘单价算成本 |

> 💡 **数据来源说明**：营销文案基于真实电商场景（烟酰胺精华液是真实护肤品类）。tiktoken 的 token 计数是真实的（非模拟），成本计算公式也是真实的。GPT-2 的 config 和 tokenizer 是真实加载的（仅 config + tokenizer，不加载权重）。

---

## 为什么不用模拟数据/伪代码（v4.0 做法）

| 维度 | 伪代码图解（v4.0） | 真实库 transformers+torch+tiktoken（v5.0） |
|------|--------------------------------|------------------------------|
| Tokenization | ❌ 伪代码示意 | ✅ tiktoken 精确 BPE 分词 |
| 架构参数 | ❌ 手写表格 | ✅ AutoConfig 读取真实 GPT-2 config |
| 注意力计算 | ❌ 伪代码公式 | ✅ torch 张量运算真实计算 |
| 参数量 | ❌ 文字描述 | ✅ 从 config 推算真实参数量 |
| 成本计算 | ❌ 按字符估算 | ✅ tiktoken 精确计数 × 真实定价 |
| 可执行性 | ❌ 无法运行 | ✅ 每步有真实输出 |

**真实即严谨**--用工业级库替代伪代码，是 v5.0 的哲学增量。
