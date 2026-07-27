# AI原生化商业博士 · 独立教材：选修E3 Introduction to Large Language Models

> **修读者**：aha.gare  
> **导师系统**：Claude / 天道推演 + 系统觉醒 + 学位对标融合 + 牛津自然学习法 + 全球七校对标  
> **版本**：v4.0 | **日期**：2026-07-16  
> **学时**：6h + 英语平行轨道2h = 8h | 建议节奏：3天集中学习  
> **对标课程**：Stanford CS224N NLP与深度学习（2025 LLM更新版）+ Imperial College London Deep Learning & Generative AI + Princeton COS 597G Understanding LLMs + Berkeley CS182 Deep Learning  
> **对应技能**：技能2（AI原生企业架构）+ 技能5（Agentic系统工程）基础  
> **英语轨道**：Stanford CS224N 2025版讲义（Lecture 17-20 LLM应用层）+ Anthropic官方文档 + HuggingFace Course（i+1难度：⭐⭐⭐）  
> **前置条件**：完成技能2核心课程（AI原生企业架构），具备基本Python编程能力  
> **定位**：为非CS背景的AI商业博士提供LLM的技术底座理解，从"会用LLM API"升级到"理解LLM原理并能做架构决策"

---

## 课程概述

### 核心命题

**LLM是如何从"统计语言模型"进化为"通用推理引擎"的？理解LLM的内部机制如何指导我们做出更好的应用工程决策？**

Large Language Models是AI原生时代的核心基础设施。技能2让你理解了"企业如何被AI重写"（原生架构），技能5让你掌握了"如何用Agent编排业务流程"。但这些能力都建立在一个前提上：你对LLM本身有足够深入的理解。本选修课补齐这个技术底座。

这不是一门纯粹的NLP理论课--我们不推导Transformer的数学公式，不实现反向传播算法。这是一门面向AI商业分析师的LLM工程课：理解LLM的工作原理到足够做出架构决策的程度，理解LLM的能力边界到足够避免"幻觉式方案设计"的程度，理解LLM的评估方法到足够科学选择模型的程度。

对于售前解决方案产品经理而言，LLM理解力直接决定了方案的技术可信度。当客户问"为什么用GPT而不是开源模型"、"RAG和Fine-tuning该选哪个"、"这个应用场景需要多大的模型"时，你需要能给出基于原理的分析，而不是"因为大家都这么做"。

### 学习目标

完成本课程后，你将能够：

1. **原理层**：解释Transformer架构的核心机制（Self-Attention、Multi-Head Attention、Positional Encoding），理解预训练-微调-对齐三阶段训练流程
2. **应用层**：掌握Prompt Engineering、RAG、Fine-tuning、Function Calling四种LLM应用模式，理解各自的适用场景和工程实现
3. **评估层**：使用主流评估基准（MMLU、HumanEval、BLEU、ROUGE等）评估LLM能力，设计特定场景的评估方案
4. **部署层**：理解LLM部署的关键架构选择（API vs 本地、量化、蒸馏、推理优化），能做成本-性能权衡分析
5. **研究层**：阅读Stanford CS224N讲义和LLM论文，跟踪LLM前沿发展趋势

### 前置条件

学习本选修课前，你应当已经：
- 完成技能2核心课程，理解AI原生企业架构的三层模型
- 具备Python编程能力（能阅读和编写基本脚本）
- 理解基本的机器学习概念（训练、测试、过拟合）
- 使用过至少一个LLM API（OpenAI、Anthropic或其他）

---

## 学习计划表（3天）

| 天次 | 主题 | 时长 | 核心产出 | 英语轨道材料 |
|:---:|------|:----:|---------|-------------|
| **Day 1** | LLM基础：Transformer架构与训练流程 | 2h | Transformer架构图解 + 三阶段训练流程文档 | CS224N Lecture 1 & 17 讲义 + "Attention is All You Need"论文摘要 |
| **Day 2** | LLM应用工程：Prompt/RAG/Fine-tuning/Function Calling | 2h | RAG系统完整代码 + 四种应用模式对比矩阵 | HuggingFace RAG教程 + Anthropic Prompt Engineering文档 |
| **Day 3** | LLM评估与部署：评估基准、模型选择、部署架构 | 2h | 模型选择决策矩阵 + 部署架构设计文档 | CS224N Lecture 18-19讲义 + HuggingFace Model Hub浏览 |

> **英语轨道（2h）**：分散在3天中。核心材料为Stanford CS224N 2025版讲义（重点Lecture 1, 17-19）。遵循牛津自然学习法：先读中文概念讲解，再对照英文讲义，目标理解70%即可。

---

## 详细学习内容

---

### Day 1：LLM基础：Transformer架构与训练流程

> 🌐 **英语轨道（i+1）**：读Stanford CS224N 2025版Lecture 1讲义（https://web.stanford.edu/class/cs224n/）。这是课程导论，用英文解释了NLP和深度学习的基本概念。先快速浏览，遇到专业术语标注但不查字典。同时读"Attention is All You Need"论文（arXiv 1706.03762）的摘要和引言。

#### 一、从语言模型到Large Language Model

**语言模型的本质**非常简单：给定前面的词，预测下一个词的概率分布。

```
P(w_t | w_1, w_2, ..., w_{t-1})
```

这个看似简单的任务蕴含了深刻的能力。要准确预测下一个词，模型必须理解语法、语义、常识、推理、世界知识。这就是为什么"预测下一个词"这个简单目标能训练出如此强大的模型。

**语言模型的三代演进**：

| 代际 | 代表模型 | 核心架构 | 参数规模 | 能力特点 |
|:----:|---------|---------|:--------:|---------|
| 第一代 | N-gram模型 | 统计计数 | <1M | 仅能捕获局部n-1个词的上下文 |
| 第二代 | Word2Vec/LSTM | 神经网络 | 1M-1B | 连续表示+序列建模，但长程依赖弱 |
| 第三代 | GPT/BERT/Llama | Transformer | 1B-1T+ | 并行计算+长程依赖+涌现能力 |

**Scale Law（规模法则）**是理解LLM的关键。OpenAI在2020年发现（Kaplan et al.），模型性能随参数量、数据量和计算量的增加而可预测地提升。更重要的是，DeepMind在2022年（Hoffmann et al., "Chinchilla"论文）发现，**模型规模和数据量需要按比例增长**才能达到最优性能--之前业界过度关注模型变大而忽视了数据量的同步增长。

> 💡 **商业洞察**：Scale Law意味着LLM的能力提升是可预测的。这对商业决策有直接影响：如果你知道某个能力需要多大的模型规模才能达到，你就可以提前规划基础设施和成本。反之，如果一个能力即使在最大规模下仍未出现（如真正的逻辑推理），可能需要架构创新而非单纯放大。

#### 二、Transformer架构核心解析

Transformer是2017年Google在"Attention is All You Need"论文中提出的架构，是所有现代LLM的基础。理解Transformer不需要深入每个数学细节，但需要掌握三个核心机制。

**机制1：Self-Attention（自注意力）**

Self-Attention是Transformer的灵魂。它的核心思想是：**对于序列中的每个词，计算它与其他所有词的关联程度，用这个关联程度加权聚合信息。**

用三个角色来理解Self-Attention：

| 角色 | 符号 | 功能 | 类比 |
|------|------|------|------|
| **Query（查询）** | Q | "我在找什么信息？" | 搜索查询词 |
| **Key（键）** | K | "我有什么信息？" | 网页标题/关键词 |
| **Value（值）** | V | "我的实际内容是什么？" | 网页正文内容 |

Self-Attention的计算过程：

```
Attention(Q, K, V) = softmax(Q × K^T / √d_k) × V
```

用语言解释这个公式：
1. **Q × K^T**：计算每个词的Query与所有词的Key的点积，得到"关联度矩阵"
2. **/ √d_k**：缩放，防止点积值过大导致softmax梯度消失
3. **softmax**：将关联度归一化为概率分布（加和为1）
4. **× V**：用归一化的关联度加权聚合所有词的Value

**为什么Self-Attention比RNN/LSTM强大？**

RNN/LSTM按顺序处理词，信息需要经过每一步的传递，长距离信息会逐渐衰减。Self-Attention让每个词直接与所有其他词交互，无论距离多远，信息传递路径长度始终为O(1)。这解决了长程依赖问题，也使模型可以并行计算（不需要等待前一步完成）。

**机制2：Multi-Head Attention（多头注意力）**

一个Attention Head只能学习一种关联模式。Multi-Head Attention将Q/K/V分成多组，每组独立计算Attention，然后拼接结果。

```
Multi-Head(Q, K, V) = Concat(head_1, head_2, ..., head_h) × W_O

其中 head_i = Attention(Q × W_Q^i, K × W_K^i, V × W_V^i)
```

不同的Head可以学习不同的关联模式：有的Head关注语法关系（主谓一致），有的关注语义关系（同义词），有的关注位置关系（相邻词）。这让模型能同时从多个角度理解语言。

**机制3：Positional Encoding（位置编码）**

Self-Attention本身没有顺序概念--它把输入看作"词的集合"而非"词的序列"。为了让模型知道词的顺序，需要加入位置编码。

```
输入表示 = 词嵌入（Word Embedding） + 位置编码（Positional Encoding）
```

原始Transformer使用正弦/余弦函数生成位置编码。现代LLM使用了更先进的位置编码方案，如RoPE（Rotary Position Embedding，旋转位置编码），它对长文本的外推性更好。

> 💡 **实践意义**：理解Positional Encoding有助于理解LLM的Context Window限制。LLM的"记忆"不是无限的--位置编码和Attention计算复杂度都随序列长度增长。这就是为什么Context Window是LLM的关键指标，以及为什么需要RAG（将外部信息检索到Context Window内）而非简单地把所有信息塞进Prompt。

**Transformer Block的完整结构**：

```
输入
  |
  ├─ Multi-Head Self-Attention
  |      |
  |      └─ 残差连接 + Layer Normalization
  |
  ├─ Feed-Forward Network (FFN)
  |      |
  |      └─ 残差连接 + Layer Normalization
  |
输出

（N个这样的Block堆叠 = Transformer Encoder或Decoder）
```

两个关键设计：
- **残差连接（Residual Connection）**：将输入直接加到输出上（output = input + f(input)），解决深层网络的梯度消失问题
- **Layer Normalization**：对每一层的输出做归一化，稳定训练

**Encoder vs Decoder**：

| 类型 | 功能 | 代表模型 | 典型用途 |
|------|------|---------|---------|
| **Encoder-only** | 理解输入，输出上下文化表示 | BERT | 文本分类、NER、语义搜索 |
| **Decoder-only** | 自回归生成下一个Token | GPT系列、Llama | 文本生成、对话、推理 |
| **Encoder-Decoder** | 先编码输入，再解码输出 | T5、BART | 翻译、摘要 |

当前主流LLM（GPT-4、Claude、Llama）几乎都是Decoder-only架构。原因是Decoder-only的生成能力和Scale Law表现更好。

#### 三、LLM训练三阶段

LLM的训练不是一步到位的，而是经历三个阶段，每个阶段有不同的目标和数据。

**阶段1：Pre-training（预训练）**

预训练是LLM能力的根基。在这个阶段，模型在海量文本数据（通常数万亿Token）上训练"预测下一个Token"任务。

```
输入：The cat sat on the
目标：mat
```

预训练的关键特征：
- **数据**：互联网爬取的网页、书籍、论文、代码等（Common Crawl、Wikipedia、GitHub等）
- **规模**：数千亿到数万亿Token，数百亿到数千亿参数
- **成本**：极其昂贵（GPT-4预训练估计成本超过1亿美元）
- **产出**：一个具有语言理解、世界知识、基础推理能力的Base Model

预训练后，模型已经"知道"了很多东西，但它还不会"对话"--给它一个问题，它可能继续补全问题而非回答。这就是为什么需要下一阶段。

**阶段2：Supervised Fine-Tuning（SFT，监督微调）**

SFT让模型学会"遵循指令"。在预训练模型的基础上，用高质量的"指令-回答"对来微调。

```
输入（指令）：请解释什么是营销归因。
输出（回答）：营销归因是指...
```

SFT的关键特征：
- **数据**：人工编写或筛选的高质量指令-回答对（数万到数十万条）
- **规模**：比预训练小得多
- **成本**：远低于预训练
- **产出**：一个能遵循指令、进行对话的Chat Model

**阶段3：Alignment（对齐）**

对齐让模型的回答更符合人类价值观和偏好。即使SFT后的模型能回答问题，它的回答可能不准确、有害或不符合用户期望。对齐阶段通过人类反馈来"矫正"模型行为。

主流对齐方法：

| 方法 | 全称 | 核心思想 | 代表应用 |
|------|------|---------|---------|
| **RLHF** | Reinforcement Learning from Human Feedback | 训练奖励模型，用RL优化模型输出 | GPT-3.5/4 |
| **DPO** | Direct Preference Optimization | 直接从偏好对优化模型，不需要奖励模型 | Llama 3, Zephyr |
| **RLAIF** | Reinforcement Learning from AI Feedback | 用AI代替人类提供反馈 | Constitutional AI (Anthropic) |
| **Constitutional AI** | - | 让模型根据"宪法"原则自我批评和改进 | Claude |

RLHF的三步流程：
1. 训练Reward Model：人类标注员对模型输出的多个版本进行排序，训练一个能预测人类偏好的Reward Model
2. 强化学习优化：用PPO算法优化LLM，使其输出最大化Reward Model的分数
3. 迭代：重复以上过程

DPO是2023年出现的简化方案，它绕过了Reward Model训练和RL优化，直接从偏好数据对中优化LLM。DPO更简单、更稳定，在开源社区中比RLHF更受欢迎。

> 💡 **实践意义**：理解训练三阶段有助于理解LLM的行为特征。预训练决定了模型的"知识上限"，SFT决定了模型的"交互风格"，对齐决定了模型的"安全边界"。当模型在某个任务上表现不好时，需要判断是知识不足（需要RAG或Fine-tuning）、还是交互风格不对（需要更好的Prompt）、还是安全限制过严（需要调整系统Prompt或换模型）。

#### 四、Tokenization：LLM看到的不是"词"

LLM处理的不是人类理解的"词"，而是Token。Tokenization是将文本切分为Token的过程。

```
文本：Marketing analytics is important
Token化：[Marketing] [ analytics] [ is] [ important]
Token ID：[48329] [ 91284] [ 318] [ 1292]
```

主流Tokenization方法是BPE（Byte Pair Encoding），它根据频率将文本切分为子词单元。高频词是一个完整的Token，低频词被拆分为多个子词Token。

**Tokenization的实践影响**：

1. **成本计算**：LLM API按Token计费，不是按词或字符。英文约1 Token ≈ 0.75个单词，中文约1个汉字 ≈ 1-2个Token。
2. **Context Window**：Context Window以Token为单位。128K Context Window约能容纳10万英文单词或6-8万中文字。
3. **多语言差异**：同一个意思，中文比英文消耗更多Token，这直接影响成本和响应速度。

```python
# Tokenization示例
from transformers import AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("gpt2")
# GPT-2的tokenizer（注意GPT-2对中文支持不好）

text_en = "Marketing analytics is important"
text_zh = "营销分析很重要"

tokens_en = tokenizer.encode(text_en)
tokens_zh = tokenizer.encode(text_zh)

print(f"英文: {len(tokens_en)} tokens -> {tokens_en}")
print(f"中文: {len(tokens_zh)} tokens -> {tokens_zh}")
# 中文往往被拆成更多Token，因为BPE主要在英文数据上训练

# 使用支持多语言的tokenizer
tokenizer_multi = AutoTokenizer.from_pretrained("meta-llama/Llama-2-7b")
# Llama系列的tokenizer对中文支持更好
```

---

### Day 2：LLM应用工程

> 🌐 **英语轨道（i+1）**：读HuggingFace的RAG教程（https://huggingface.co/learn/nlp-course）和Anthropic的Prompt Engineering文档（https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview）。这些是LLM应用工程的实践指南，用简洁的英文写成。

#### 一、LLM应用的四种模式

构建LLM应用有四种核心模式，它们不是互斥的，而是可以根据场景组合使用。

| 模式 | 核心思想 | 适用场景 | 成本 | 灵活性 |
|------|---------|---------|------|--------|
| **Prompt Engineering** | 通过设计Prompt引导LLM行为 | 快速原型、简单任务 | 极低 | 极高 |
| **RAG** | 检索外部知识增强LLM | 知识密集型问答 | 中 | 高 |
| **Fine-tuning** | 用领域数据微调LLM | 特定领域、风格统一 | 高 | 中 |
| **Function Calling** | 让LLM调用外部工具 | 需要与外部系统交互 | 低 | 高 |

**决策框架**：

```
问题是否需要最新知识或私有知识？
├── 是 -> 用 RAG
│   └── 还需要特定输出格式/风格？
│       └── 是 -> RAG + Fine-tuning
└── 否 -> 用 Prompt Engineering
    └── 需要调用外部工具/API？
        ├── 是 -> Function Calling
        └── 否 -> 纯Prompt Engineering
```

> 💡 **关键原则**：先尝试Prompt Engineering，不够再上RAG，还不够才考虑Fine-tuning。Fine-tuning应该是最后手段，因为它成本高、灵活性低、且可能"遗忘"预训练知识（灾难性遗忘）。

#### 二、Prompt Engineering进阶

Prompt Engineering不是"写一句话"，而是一套系统化的Prompt设计方法论。

**Prompt的层次结构**：

```
System Prompt（系统提示）
├── 角色定义：你是一个营销分析专家...
├── 行为约束：只基于提供的数据回答，不要编造...
├── 输出格式：以JSON格式返回，包含以下字段...
└── 示例（Few-shot）：输入->输出示例

User Prompt（用户提示）
└── 具体任务和上下文
```

**五种核心Prompt技术**：

1. **Zero-shot**：直接给任务描述，不提供示例。适用于LLM已有能力的任务。

```
请将以下营销文案翻译成英文：[文案]
```

2. **Few-shot**：提供少量示例，引导LLM的输出模式。适用于需要特定格式或风格的任务。

```
示例1：
输入：这款手机续航很强
输出：{"sentiment": "positive", "aspect": "battery"}

示例2：
输入：屏幕太暗了
输出：{"sentiment": "negative", "aspect": "screen"}

现在请分析：
输入：[用户输入]
输出：
```

3. **Chain-of-Thought (CoT)**：要求LLM展示推理过程，提升复杂推理任务的准确性。

```
问题：某品牌上月投放了10万元广告，获得500个线索，转化率为20%，
客单价为2000元。请计算ROAS。

请一步一步思考：
Step 1: 计算转化客户数 = 500 × 20% = 100人
Step 2: 计算总收入 = 100 × 2000 = 20万元
Step 3: 计算ROAS = 20万 / 10万 = 2.0
```

4. **Self-Consistency**：让LLM对同一问题生成多个回答，取多数结果。减少随机性影响。

5. **Structured Output**：要求LLM输出结构化格式（JSON/XML），便于程序解析。

```python
# 结构化输出示例
prompt = """
分析以下营销文案的情感和关键要素，以JSON格式返回：

文案：{content}

返回格式：
{{
    "sentiment": "positive/negative/neutral",
    "key_elements": ["要素1", "要素2", ...],
    "target_audience": "目标受众描述",
    "call_to_action": "CTA描述或null",
    "confidence": 0.0-1.0
}}
"""
```

#### 三、RAG系统详解

RAG（Retrieval-Augmented Generation）是LLM应用工程中最核心的技术。它解决了一个根本问题：**LLM的知识是静态的（训练数据截止日期），且无法访问企业私有数据。**

**RAG的工作流程**：

```
用户提问
    |
    v
[Query处理] -> 将问题转化为检索query
    |
    v
[检索] -> 从向量数据库中检索相关文档
    |
    v
[重排序] -> 对检索结果按相关性重排序
    |
    v
[生成] -> 将检索到的文档和问题一起送入LLM生成回答
    |
    v
回答
```

**RAG系统的完整实现**：

```python
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_openai import ChatOpenAI
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate

class MarketingKnowledgeRAG:
    """企业营销知识库RAG系统"""
    
    def __init__(self, openai_api_key):
        # 初始化组件
        self.embeddings = OpenAIEmbeddings(
            model="text-embedding-3-small",
            openai_api_key=openai_api_key
        )
        self.llm = ChatOpenAI(
            model="gpt-4",
            temperature=0,  # RAG场景用低temperature保证准确性
            openai_api_key=openai_api_key
        )
        self.vectorstore = None
        self.qa_chain = None
    
    def ingest_documents(self, documents):
        """文档摄入和处理"""
        # Step 1: 文档分块（Chunking）
        # 分块策略对RAG质量影响极大
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=500,        # 每块约500字符
            chunk_overlap=50,      # 块间重叠50字符（保证上下文连续性）
            separators=["\n\n", "\n", "。", "！", "？", "，", " ", ""]
            # 中文友好的分隔符
        )
        chunks = text_splitter.split_documents(documents)
        
        # Step 2: 向量化并存储
        self.vectorstore = Chroma.from_documents(
            documents=chunks,
            embedding=self.embeddings,
            persist_directory="./chroma_db"  # 持久化存储
        )
        
        # Step 3: 构建QA链
        # 自定义Prompt模板
        prompt_template = """
        你是一个营销知识助手。请基于以下检索到的上下文回答问题。
        如果上下文中没有相关信息，请明确说"根据现有资料，我无法回答这个问题"。
        不要编造信息。
        
        上下文：
        {context}
        
        问题：{question}
        
        回答（请引用上下文中的具体内容）：
        """
        
        prompt = PromptTemplate(
            template=prompt_template,
            input_variables=["context", "question"]
        )
        
        self.qa_chain = RetrievalQA.from_chain_type(
            llm=self.llm,
            chain_type="stuff",  # 将所有检索结果"塞入"Prompt
            retriever=self.vectorstore.as_retriever(
                search_type="similarity",
                search_kwargs={"k": 5}  # 检索top-5相关文档
            ),
            chain_type_kwargs={"prompt": prompt},
            return_source_documents=True  # 返回来源文档（可溯源）
        )
    
    def ask(self, question):
        """提问"""
        result = self.qa_chain.invoke({"query": question})
        
        return {
            "answer": result["result"],
            "sources": [
                {
                    "content": doc.page_content[:200],
                    "metadata": doc.metadata
                }
                for doc in result["source_documents"]
            ]
        }

# 使用示例
rag = MarketingKnowledgeRAG(openai_api_key="your-key")

# 摄入营销知识文档
from langchain_community.document_loaders import DirectoryLoader
loader = DirectoryLoader("./marketing_docs", glob="**/*.md")
documents = loader.load()
rag.ingest_documents(documents)

# 提问
result = rag.ask("我们品牌在2025年Q4的社媒投放策略是什么？")
print(f"回答: {result['answer']}")
print(f"来源: {result['sources']}")
```

**RAG质量优化的关键维度**：

| 维度 | 问题 | 优化方法 |
|------|------|---------|
| **分块策略** | 块太大：检索不精确；太小：丢失上下文 | 语义分块（按段落/主题分），重叠窗口 |
| **Embedding模型** | 通用embedding对垂直领域效果差 | 领域微调embedding或选择多语言embedding |
| **检索策略** | 纯向量检索可能遗漏关键词匹配 | 混合检索：向量检索 + BM25关键词检索 |
| **重排序** | 检索top-k中相关度排序不准 | Cross-encoder重排序模型 |
| **Prompt设计** | LLM可能忽略检索结果或编造信息 | 强约束Prompt + Few-shot引导 |
| **评估** | 难以量化RAG质量 | RAGAS框架：检索准确率+生成准确率+忠实度 |

> 💡 **工程实践**：RAG不是"搭起来就行"的。一个可用的RAG系统需要持续的评估和优化。最常见的RAG质量问题是：检索不到相关文档（检索召回率低）、检索到了但LLM没用（生成忠实度低）、LLM编造了检索结果中没有的信息（幻觉）。每个问题都有对应的优化手段，但首先需要能度量这些问题。

#### 四、Fine-tuning：何时用，怎么用

Fine-tuning是用领域数据进一步训练LLM，使其在特定任务上表现更好。

**Fine-tuning的三种方法**：

| 方法 | 数据需求 | 计算成本 | 效果 | 适用场景 |
|------|---------|---------|------|---------|
| **Full Fine-tuning** | 大量标注数据 | 极高 | 最好，但有过拟合风险 | 大企业、有GPU集群 |
| **LoRA（Low-Rank Adaptation）** | 中等数据 | 中低 | 接近Full FT | 最流行的PEFT方法 |
| **QLoRA** | 中等数据 | 低 | 略低于LoRA | 消费级GPU可用 |

**LoRA的原理**（直觉理解）：不全量更新模型的所有参数，而是冻结原始模型，只训练一个小的"低秩适配器"。这个适配器只有原始参数量的0.1%-1%，但能达到接近Full Fine-tuning的效果。

**什么时候需要Fine-tuning？**

| 场景 | 需要Fine-tuning吗？ | 替代方案 |
|------|:------------------:|---------|
| 需要最新知识 | ❌ | RAG |
| 需要私有数据 | ❌ | RAG |
| 需要特定输出格式 | ❌ | Prompt Engineering |
| 需要特定写作风格 | ✅ | Few-shot可能够用 |
| 需要特定领域推理能力 | ✅ | 大模型+Prompt可能够用 |
| 需要降低成本（用小模型替代大模型） | ✅ | - |

```python
# LoRA Fine-tuning示例（使用HuggingFace PEFT）
from peft import LoraConfig, get_peft_model, TaskType
from transformers import AutoModelForCausalLM, TrainingArguments
from trl import SFTTrainer

# 加载基础模型
model = AutoModelForCausalLM.from_pretrained(
    "meta-llama/Llama-2-7b-chat",
    load_in_4bit=True,  # 4-bit量化，降低显存需求
    device_map="auto"
)

# 配置LoRA
lora_config = LoraConfig(
    task_type=TaskType.CAUSAL_LM,
    r=8,              # LoRA秩（常用4-16）
    lora_alpha=32,    # 缩放因子
    lora_dropout=0.1,
    target_modules=["q_proj", "v_proj"]  # 只对Attention的Q和V做LoRA
)

model = get_peft_model(model, lora_config)

# 准备训练数据（指令-回答对）
train_data = [
    {"instruction": "分析这款产品的目标用户", "input": "产品描述...", "output": "分析结果..."},
    # ... 更多营销领域数据
]

# 训练
trainer = SFTTrainer(
    model=model,
    train_dataset=train_data,
    args=TrainingArguments(
        output_dir="./lora_marketing",
        num_train_epochs=3,
        per_device_train_batch_size=4,
        learning_rate=2e-4,
        save_steps=100,
    ),
    peft_config=lora_config
)

trainer.train()

# 保存LoRA适配器（只有几十MB，而非基础模型的几十GB）
model.save_pretrained("./lora_marketing_adapter")
```

> 💡 **成本对比**：Fine-tuning一个7B模型用LoRA，单GPU（A100 80G）约需4-8小时，成本约50-100美元。而使用GPT-4 API做同样任务的推理成本可能在每次调用0.01-0.06美元。如果任务量大（如每天10万次调用），Fine-tuning小模型可能更经济。但如果任务量小，直接用API更划算。

#### 五、Function Calling：LLM与外部世界的桥梁

Function Calling让LLM能调用外部工具（API、数据库、计算器等），是Agent系统的基础能力。

```python
# Function Calling完整示例
import json
from openai import OpenAI

client = OpenAI(api_key="your-key")

# 定义可用工具
tools = [
    {
        "type": "function",
        "function": {
            "name": "get_marketing_metrics",
            "description": "获取指定渠道的营销指标数据",
            "parameters": {
                "type": "object",
                "properties": {
                    "channel": {
                        "type": "string",
                        "enum": ["search", "social", "email", "display"],
                        "description": "营销渠道名称"
                    },
                    "date_range": {
                        "type": "string",
                        "description": "日期范围，格式：YYYY-MM-DD到YYYY-MM-DD"
                    },
                    "metrics": {
                        "type": "array",
                        "items": {"type": "string"},
                        "description": "要查询的指标列表，如impressions, clicks, conversions"
                    }
                },
                "required": ["channel", "date_range"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "calculate_roas",
            "description": "计算ROAS（广告支出回报率）",
            "parameters": {
                "type": "object",
                "properties": {
                    "revenue": {"type": "number", "description": "总收入"},
                    "spend": {"type": "number", "description": "总广告支出"}
                },
                "required": ["revenue", "spend"]
            }
        }
    }
]

# 工具实现
def execute_tool(tool_name, arguments):
    """执行工具调用"""
    if tool_name == "get_marketing_metrics":
        # 实际场景中查询数据库或API
        return json.dumps({
            "channel": arguments["channel"],
            "impressions": 1500000,
            "clicks": 45000,
            "conversions": 1200,
            "spend": 50000,
            "revenue": 120000
        })
    elif tool_name == "calculate_roas":
        roas = arguments["revenue"] / arguments["spend"]
        return json.dumps({"roas": roas})

# 对话循环
messages = [
    {"role": "system", "content": "你是一个营销数据分析助手。你可以查询营销数据并进行分析。"},
    {"role": "user", "content": "帮我查看搜索广告渠道上个月的营销数据，并计算ROAS。"}
]

# Step 1: LLM决定调用什么工具
response = client.chat.completions.create(
    model="gpt-4",
    messages=messages,
    tools=tools,
    tool_choice="auto"
)

# Step 2: 执行工具调用
if response.choices[0].message.tool_calls:
    messages.append(response.choices[0].message)
    
    for tool_call in response.choices[0].message.tool_calls:
        function_name = tool_call.function.name
        arguments = json.loads(tool_call.function.arguments)
        
        # 执行工具
        result = execute_tool(function_name, arguments)
        
        # 将结果返回给LLM
        messages.append({
            "role": "tool",
            "tool_call_id": tool_call.id,
            "content": result
        })
    
    # Step 3: LLM基于工具结果生成最终回答
    final_response = client.chat.completions.create(
        model="gpt-4",
        messages=messages,
        tools=tools
    )
    
    print(final_response.choices[0].message.content)
    # 输出类似："搜索广告渠道上月的数据如下：
    # 曝光量150万，点击量4.5万，转化量1200，广告支出5万元，收入12万元。
    # ROAS为2.4，表现良好。"
```

> 💡 **Function Calling vs RAG的协作**：Function Calling和RAG不是竞争关系，而是互补。RAG适合"检索知识"（文档、FAQ、案例），Function Calling适合"执行操作"（查询数据库、调用API、发送邮件）。在实际Agent系统中，两者经常同时使用：RAG提供知识背景，Function Calling提供操作能力。

---

### Day 3：LLM评估与部署

> 🌐 **英语轨道（i+1）**：浏览HuggingFace Model Hub（https://huggingface.co/models）和Open LLM Leaderboard（https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard）。这些是LLM生态的核心入口。先浏览模型排名，理解评估基准的含义。

#### 一、LLM评估基准

LLM评估是当前AI工程中最具挑战性的问题之一。传统软件有明确的输入输出，可以精确测试。LLM的输出是非确定性的，同一输入可能产生不同输出，且"好坏"往往是主观的。

**主流评估基准**：

| 基准 | 评估维度 | 测试方法 | 适用场景 |
|------|---------|---------|---------|
| **MMLU** | 多领域知识 | 多选题 | 评估模型的知识广度 |
| **HumanEval** | 代码生成 | 函数级编程题 | 评估代码能力 |
| **GSM8K** | 数学推理 | 小学数学应用题 | 评估推理能力 |
| **MT-Bench** | 多轮对话 | 人工+LLM评分 | 评估对话质量 |
| **AlpacaEval** | 指令遵循 | LLM自动评分 | 评估输出质量 |
| **LLM-as-Judge** | 通用 | 用强LLM评判弱LLM输出 | 快速自动评估 |
| **RAGAS** | RAG系统 | 检索准确率+生成忠实度 | RAG专用评估 |

**评估的三层框架**：

| 层次 | 评估对象 | 方法 | 目的 |
|:----:|---------|------|------|
| **通用能力** | 模型基础能力 | MMLU、HumanEval等标准基准 | 模型选型初筛 |
| **任务能力** | 特定任务表现 | 自建评测集 + 人工/LLM评分 | 确认模型适合具体任务 |
| **系统效果** | 端到端应用效果 | A/B测试 + 用户反馈 | 验证业务价值 |

> 💡 **实践建议**：标准基准（MMLU等）用于模型选型初筛，但不要过度依赖。一个模型在MMLU上高5分，不代表它在你的营销任务上更好。最终评估必须在你的实际任务数据上进行。构建一个包含100-500条标注数据的领域评测集，比任何标准基准都有参考价值。

**构建领域评测集的方法**：

```python
# 营销领域评测集构建示例
from dataclasses import dataclass
from typing import List

@dataclass
class EvalExample:
    """评估样本"""
    input: str           # 输入
    reference: str       # 参考答案（标准答案）
    criteria: List[str]  # 评估标准
    category: str        # 任务类别

# 营销评测集示例
marketing_eval_set = [
    EvalExample(
        input="分析以下竞品信息并生成SWOT分析：[竞品数据]",
        reference="[参考SWOT分析]",
        criteria=["结构完整", "分析有数据支撑", "建议可操作"],
        category="竞品分析"
    ),
    EvalExample(
        input="为以下产品撰写小红书种草文案：[产品信息]",
        reference="[参考文案]",
        criteria=["符合小红书风格", "包含产品卖点", "有CTA"],
        category="内容生成"
    ),
    # ... 100-500条样本
]

# LLM-as-Judge评估
def evaluate_with_llm_judge(model_output, eval_example, judge_model="gpt-4"):
    """用LLM作为评判者"""
    prompt = f"""
    请评估以下AI生成的营销内容的质量。
    
    任务类别：{eval_example.category}
    输入：{eval_example.input}
    参考答案：{eval_example.reference}
    AI输出：{model_output}
    
    评估标准：{', '.join(eval_example.criteria)}
    
    请对每个标准打分（1-5分），并给出理由。
    最后给出总分和是否通过（总分>=12分为通过）。
    
    返回JSON格式：
    {{
        "scores": {{"标准1": 分数, "标准2": 分数, ...}},
        "total_score": 总分,
        "passed": true/false,
        "reasoning": "评价理由"
    }}
    """
    # 调用评判模型
    result = llm.invoke(prompt)
    return result
```

#### 二、模型选择决策框架

面对数百个开源和闭源LLM，如何选择适合自己场景的模型？

**模型选择的核心维度**：

| 维度 | 考量因素 | 权重建议 |
|------|---------|---------|
| **能力** | 在目标任务上的表现 | 最高 |
| **成本** | API调用成本或部署成本 | 高 |
| **延迟** | 响应速度 | 中（取决于实时性要求） |
| **Context Window** | 能处理的上下文长度 | 中（取决于文档长度） |
| **隐私/合规** | 数据是否可出域 | 高（企业场景必须考虑） |
| **生态** | 工具链、社区支持 | 中 |
| **许可** | 开源协议是否允许商用 | 高（商用必须确认） |

**2026年模型选择决策树**：

```
数据能否出域（发送到API）？
├── 不能 -> 开源模型本地部署
│   ├── 有GPU服务器（>=2张A100）-> Llama 3 70B / Qwen 2.5 72B
│   ├── 有限GPU（1张A100/4090）-> Llama 3 8B / Qwen 2.5 7B + 量化
│   └── 无GPU -> 小模型（1-3B）或API方案重新评估
└── 可以 -> API模型
    ├── 任务复杂度高（推理/代码/多步分析）-> Claude 3.5 Sonnet / GPT-4o
    ├── 任务简单（分类/摘要/翻译）-> Claude 3 Haiku / GPT-4o-mini
    └── 超长文档处理 -> 长Context Window模型（Gemini 1.5 Pro 2M）
```

**成本估算模型**：

```python
def estimate_llm_cost(model, avg_input_tokens, avg_output_tokens, 
                      daily_calls, days_per_month=30):
    """估算LLM月度成本"""
    # 2026年主流模型定价（美元/百万Token）
    pricing = {
        "gpt-4o": {"input": 2.50, "output": 10.00},
        "gpt-4o-mini": {"input": 0.15, "output": 0.60},
        "claude-3.5-sonnet": {"input": 3.00, "output": 15.00},
        "claude-3-haiku": {"input": 0.25, "output": 1.25},
        "llama-3-70b-local": {"input": 0, "output": 0, "infra": 2000},  # GPU月租
        "llama-3-8b-local": {"input": 0, "output": 0, "infra": 400},
    }
    
    p = pricing.get(model, {"input": 0, "output": 0})
    
    if "local" in model:
        return p.get("infra", 0)  # 本地部署只算基础设施成本
    
    monthly_input = avg_input_tokens * daily_calls * days_per_month
    monthly_output = avg_output_tokens * daily_calls * days_per_month
    
    cost = (monthly_input / 1_000_000 * p["input"] + 
            monthly_output / 1_000_000 * p["output"])
    
    return cost

# 示例：营销内容生成场景
# 假设每天1000次调用，平均输入2000 Token，输出500 Token
scenarios = [
    ("GPT-4o", estimate_llm_cost("gpt-4o", 2000, 500, 1000)),
    ("GPT-4o-mini", estimate_llm_cost("gpt-4o-mini", 2000, 500, 1000)),
    ("Claude 3.5 Sonnet", estimate_llm_cost("claude-3.5-sonnet", 2000, 500, 1000)),
    ("Claude 3 Haiku", estimate_llm_cost("claude-3-haiku", 2000, 500, 1000)),
    ("Llama 3 70B 本地", estimate_llm_cost("llama-3-70b-local", 2000, 500, 1000)),
]

for name, cost in scenarios:
    print(f"{name}: ${cost:.0f}/月")

# 输出类似：
# GPT-4o: $300/月
# GPT-4o-mini: $18/月
# Claude 3.5 Sonnet: $375/月
# Claude 3 Haiku: $31/月
# Llama 3 70B 本地: $2000/月（但有隐私优势和无Token限制）
```

> 💡 **选型策略**：先用最强模型（如Claude 3.5 Sonnet）做原型开发和评测集建立。然后在评测集上测试更便宜的模型（如Haiku或GPT-4o-mini），如果质量差距在可接受范围内（如总分差<10%），切换到便宜模型。这是"先求质量，再降成本"的策略。

#### 三、LLM部署架构

当选择本地部署开源LLM时，需要设计部署架构。

**部署架构的核心组件**：

```
┌───────────────────────────────────────────────────┐
│                  用户请求                          │
│                    │                               │
│           ┌────────▼────────┐                      │
│           │  API Gateway    │  (FastAPI / vLLM)   │
│           │  负载均衡 + 认证 │                      │
│           └────────┬────────┘                      │
│                    │                               │
│           ┌────────▼────────┐                      │
│           │  推理引擎        │                      │
│           │  (vLLM/TGI)     │  GPU推理             │
│           └────────┬────────┘                      │
│                    │                               │
│    ┌───────────────┼───────────────┐              │
│    │               │               │              │
│ ┌──▼──┐      ┌────▼────┐    ┌────▼────┐         │
│ │模型1 │      │模型2    │    │模型3    │         │
│ │7B   │      │13B     │    │70B量化  │         │
│ └─────┘      └─────────┘    └─────────┘         │
│                                                  │
│ ┌──────────────────────────────────────────────┐ │
│ │           可观测性层                          │ │
│ │  Langfuse (Tracing + Cost + Quality)        │ │
│ └──────────────────────────────────────────────┘ │
└───────────────────────────────────────────────────┘
```

**推理优化技术**：

| 技术 | 原理 | 效果 | 适用场景 |
|------|------|------|---------|
| **Quantization（量化）** | 将FP16权重压缩为INT8/INT4 | 显存减少50-75%，速度提升 | 几乎所有场景 |
| **KV Cache** | 缓存已计算的Key-Value对 | 减少重复计算 | 对话场景 |
| **PagedAttention** | 分页管理KV Cache显存 | 提高显存利用率，支持更多并发 | vLLM的核心技术 |
| **Speculative Decoding** | 小模型先生成草稿，大模型验证 | 2-3倍推理加速 | 有配对大小模型时 |
| **Batching** | 合并多个请求批量处理 | 提高吞吐量 | 高并发场景 |

**vLLM部署示例**：

```python
# vLLM是当前最流行的开源LLM推理引擎
# 安装：pip install vllm

# 命令行启动vLLM服务
# vllm serve meta-llama/Llama-2-7b-chat \
#   --tensor-parallel-size 1 \
#   --quantization awq \
#   --max-model-len 4096 \
#   --port 8000

# Python中使用vLLM
from vllm import LLM, SamplingParams

llm = LLM(
    model="meta-llama/Llama-2-7b-chat",
    quantization="awq",              # AWQ量化
    tensor_parallel_size=1,          # GPU数量
    max_model_len=4096,              # 最大上下文长度
    gpu_memory_utilization=0.9,      # GPU显存利用率
)

sampling_params = SamplingParams(
    temperature=0.7,
    top_p=0.9,
    max_tokens=500,
)

# 批量推理（vLLM的强项）
prompts = [
    "为以下产品撰写营销文案：[产品A]",
    "分析以下竞品的定价策略：[竞品B]",
    "生成5个社媒广告标题：[主题C]",
]

outputs = llm.generate(prompts, sampling_params)
for output in outputs:
    print(output.outputs[0].text)
```

#### 四、LLM应用的可观测性

生产级LLM应用需要完整的可观测性体系。Langfuse是当前最流行的开源LLM可观测性工具。

**可观测性的三个维度**：

| 维度 | 监控内容 | 工具 | 告警阈值 |
|------|---------|------|---------|
| **性能** | 延迟、吞吐量、错误率 | Langfuse + Prometheus | P99延迟>5s |
| **成本** | Token消耗、API费用 | Langfuse Cost Tracking | 日成本超预算120% |
| **质量** | 输出质量评分、用户反馈 | LLM-as-Judge + 用户评分 | 质量分<阈值 |

```python
# Langfuse集成示例
from langfuse import Langfuse
from langfuse.decorators import observe

langfuse = Langfuse()

@observe()  # 自动记录Tracing
def marketing_content_agent(brief):
    """营销内容Agent，自动追踪每一步"""
    
    # 记录输入
    langfuse.trace(
        name="marketing_content_generation",
        input={"brief": brief}
    )
    
    # Step 1: 分析Brief
    analysis = llm.invoke(f"分析以下营销Brief的关键要素：{brief}")
    
    # Step 2: 生成内容
    content = llm.invoke(f"基于以下分析生成营销文案：{analysis}")
    
    # Step 3: 质量检查
    quality_check = llm.invoke(f"评估以下文案的质量：{content}")
    
    return {
        "content": content,
        "quality_score": quality_check.score,
        "analysis": analysis
    }

# Langfuse Dashboard自动展示：
# - 每次调用的完整Trace（输入->中间步骤->输出）
# - Token消耗和成本
# - 延迟分布
# - 质量评分趋势
```

> 💡 **售前洞察**：可观测性是区分"Demo级AI系统"和"生产级AI系统"的关键。当客户问"你们的AI系统怎么保证质量"时，展示Langfuse的Tracing和质量监控Dashboard，比任何口头承诺都有说服力。可观测性也是持续优化的基础--没有度量就没有优化。

---

## 知识问答

| # | 问题 | 参考答案要点 | 难度 |
|:--:|------|------------|:----:|
| Q1 | Self-Attention中Q、K、V分别代表什么？为什么需要三个而不是一个？ | Q=查询（我在找什么），K=键（我有什么），V=值（我的内容）。三个角色让模型能区分"我想知道的"和"我能提供的"，实现更灵活的信息匹配。如果只有一个，模型无法区分查询意图和被查询内容。 | ⭐⭐ |
| Q2 | Decoder-only架构为什么在生成任务上比Encoder-only更受欢迎？ | Decoder-only通过自回归方式生成文本，天然适合开放式生成任务。Encoder-only（如BERT）擅长理解任务但生成能力弱。Scale Law表明Decoder-only在规模放大时生成能力提升更显著。 | ⭐⭐ |
| Q3 | LLM训练三阶段（预训练-SFT-对齐）各自解决什么问题？如果跳过对齐阶段会怎样？ | 预训练建立知识和语言能力，SFT学会遵循指令，对齐使输出符合人类偏好。跳过对齐会导致模型输出可能有害、不准确或不符合用户期望，虽然有知识但"不会好好说话"。 | ⭐⭐ |
| Q4 | RAG和Fine-tuning的核心区别是什么？什么时候应该选哪个？ | RAG是推理时注入外部知识（动态、可更新、无遗忘），Fine-tuning是训练时注入领域能力（静态、需重训、有遗忘风险）。需要最新/私有知识选RAG，需要特定风格/推理模式选Fine-tuning。两者可组合。 | ⭐⭐⭐ |
| Q5 | 为什么RAG的文档分块策略对系统质量影响很大？过大和过小各有什么问题？ | 分块过大：检索不精确（一个块包含太多主题，向量化后语义模糊）；过小：丢失上下文（一个块可能只有半句话，LLM无法理解）。需要根据文档类型选择合适的chunk_size和overlap。 | ⭐⭐⭐ |
| Q6 | Tokenization为什么影响LLM的成本和多语言能力？中文和英文在Token效率上的差异是什么？ | LLM按Token计费和计算。英文约1 Token=0.75词，中文1字=1-2 Token。同样内容中文消耗更多Token，成本更高、Context Window消耗更快。选择多语言优化好的tokenizer可缓解。 | ⭐⭐ |
| Q7 | MMLU等标准评估基准的局限是什么？为什么需要构建领域评测集？ | MMLU测试通用知识，不反映特定任务表现。模型在MMLU高5分不代表在营销任务上更好。领域评测集使用真实业务数据，评估模型在具体场景的实际能力，更有参考价值。 | ⭐⭐⭐ |
| Q8 | 量化（Quantization）如何减少LLM的显存需求？有什么代价？ | 将FP16权重压缩为INT8/INT4，显存减少50-75%。代价是精度损失（通常质量下降1-3%）。AWQ和GPTQ是当前主流量化方法，在4-bit量化下仍能保持接近原模型的性能。 | ⭐⭐⭐ |
| Q9 | Function Calling和RAG在LLM应用中分别扮演什么角色？它们如何协作？ | Function Calling是"执行操作"（调用API、查询数据库），RAG是"检索知识"（查找文档）。协作方式：RAG提供知识背景和上下文，Function Calling执行基于知识的操作。Agent系统通常同时使用两者。 | ⭐⭐ |
| Q10 | 如果你为一个企业客户设计LLM部署方案，需要考虑哪些关键因素？如何平衡成本和质量？ | 核心因素：数据隐私（能否出域）、任务复杂度、调用量、延迟要求、预算。策略：先用强API模型建原型和评测集，在评测集上测试更便宜模型，如质量可接受则切换。高隐私需求用本地部署+量化。 | ⭐⭐⭐ |

---

## 作业设计

### 必做作业：构建营销知识库RAG系统

**任务**：使用LangChain和OpenAI API（或开源替代），构建一个营销知识库RAG系统：

1. 准备至少10个营销相关文档（可以是产品文档、营销策略、竞品分析等）
2. 实现文档摄入（分块、向量化、存储）
3. 实现检索和生成（含自定义Prompt模板）
4. 实现5个测试问答，记录RAG的回答和来源
5. 写一份500字的系统设计说明，包含架构选择理由和优化方向

**评分标准**：

| 维度 | 优秀（9-10分） | 良好（7-8分） | 合格（5-6分） | 不合格（<5分） |
|------|-------------|------------|------------|-------------|
| 功能完整性 | 系统可运行、回答准确、来源可追溯 | 基本可运行 | 部分功能可用 | 无法运行 |
| 代码质量 | 结构清晰、有注释、有错误处理 | 基本清晰 | 可读但粗糙 | 混乱 |
| 设计说明 | 深入分析架构选择和优化方向 | 说明基本合理 | 表面描述 | 缺失 |

### 挑战作业：LLM模型选型与部署方案设计

**任务**：为一个虚拟企业场景设计LLM部署方案：

**场景**：一家中型电商企业，日均10万次营销内容生成请求，数据不可出域（隐私合规要求），需要支持中文营销文案生成和客服对话。

1. 比较至少3个候选模型（含开源和闭源）
2. 分析每个模型在成本、能力、合规、延迟上的表现
3. 推荐最终方案并给出理由
4. 设计部署架构（含推理优化策略）
5. 设计可观测性方案
6. 总字数1500-2000字

**评分标准**：重点考察选型分析的全面性（是否覆盖所有关键维度）、推荐的合理性（理由是否充分）、部署架构的可行性（是否考虑了推理优化和可观测性）。

---

## 推荐资源清单

### 核心论文与文档（必读）
- 📄 **"Attention is All You Need"**（Transformer原论文, arXiv 1706.03762）: https://arxiv.org/abs/1706.03762
- 📄 **"Language Models are Few-Shot Learners"**（GPT-3论文, arXiv 2005.14165）: https://arxiv.org/abs/2005.14165
- 📄 **LoRA论文**（arXiv 2106.09685）: https://arxiv.org/abs/2106.09685
- 📄 **DPO论文**（arXiv 2305.18290）: https://arxiv.org/abs/2305.18290
- 🌐 **Anthropic Prompt Engineering文档**: https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview

### 开源工具（必读）
- 🌐 **HuggingFace Transformers**: https://huggingface.co/docs/transformers
- 🌐 **HuggingFace Course（免费）**: https://huggingface.co/learn/nlp-course
- 🌐 **LangChain文档**: https://python.langchain.com/docs/
- 🌐 **vLLM（推理引擎）**: https://github.com/vllm-project/vllm
- 🌐 **PEFT（参数高效微调）**: https://github.com/huggingface/peft
- 🌐 **Langfuse（可观测性）**: https://langfuse.com/docs/

### 对标课程
- 🌐 **Stanford CS224N NLP与深度学习**: https://web.stanford.edu/class/cs224n/
- 🌐 **Imperial Deep Learning & GenAI**: https://www.imperial.ac.uk/business-school/programmes/msc-business-analytics/
- 🌐 **Princeton COS 597G Understanding LLMs**: https://www.cs.princeton.edu/courses/archive/fall23/cos597G/
- 🌐 **Berkeley CS182 Deep Learning**: https://cs182sp24.github.io/
- 🌐 **Andrej Karpathy "Let's build GPT" 视频**: https://www.youtube.com/watch?v=kCc8FmEb1nY

### 模型与基准（推荐）
- 🌐 **Open LLM Leaderboard**: https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard
- 🌐 **HuggingFace Model Hub**: https://huggingface.co/models
- 🌐 **MMLU基准**: https://github.com/hendrycks/test
- 🌐 **HumanEval基准**: https://github.com/openai/human-eval
- 🌐 **RAGAS（RAG评估框架）**: https://github.com/explodinggradients/ragas

### 进阶阅读（可选）
- 📄 **RAG综述论文**（arXiv 2401.15884）: https://arxiv.org/abs/2401.15884
- 📄 **Constitutional AI论文**（Anthropic）: https://arxiv.org/abs/2212.08073
- 📄 **Scaling Laws论文**（OpenAI）: https://arxiv.org/abs/2001.08361
- 📄 **Chinchilla论文**（DeepMind）: https://arxiv.org/abs/2203.15556
- 🌐 **The Illustrated Transformer**（Jay Alammar可视化教程）: https://jalammar.github.io/illustrated-transformer/

---

> 💡 **英语轨道总结**：本选修课的英语轨道核心材料是Stanford CS224N 2025版讲义。建议在Day 1读Lecture 1（课程导论）和Lecture 17（LLM应用层RAG），Day 2读HuggingFace RAG教程和Anthropic Prompt Engineering文档，Day 3读Lecture 18-19（LLM评估与安全）。遵循i+1原则：先读中文概念讲解建立框架，再对照英文讲义深化理解，目标是能用自己的话解释LLM的核心概念和工程决策。
