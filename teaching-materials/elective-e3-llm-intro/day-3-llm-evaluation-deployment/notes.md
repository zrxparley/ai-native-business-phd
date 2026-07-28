# 选修E3 · Day 3：LLM 评估与部署 · 讲义（v5.0 学习材料包版）

> **所属**：AI原生化商业博士 · 选修E3 LLM导论 · Day 3
> **版本**：v5.0（从独立教材升级为学习材料包）
> **预计**：2h 讲义 + 2h 上机练习
> **核心命题**：LLM 上线不是终点而是起点--用 deepeval 自动化评估质量、用 LangSmith 追踪部署后调用、用 tiktoken 监控推理成本、用 vLLM/投机解码/MoE 优化推理架构
> **v5.0 升级点**：① 新增真实库上机（deepeval + langsmith + tiktoken）② 新增 TODO 填空式起始笔记本 ③ Notebook 化 ④ 深链阅读 ⑤ 2026 前沿（LLM-as-a-Judge / deepeval / vLLM / 投机解码 / MoE / AgentBench）

---

## 学习目标（学完你能做到）

1. 能阐述 LLM 评估的三层框架（通用能力 MMLU/HumanEval/AgentBench 基准 / 任务能力领域评测集 / 系统效果 A/B 测试），并说明"标准基准用于模型选型初筛，但最终评估必须在真实业务数据上进行"的工程原则
2. 能用 **deepeval**（Confident AI，MIT）自定义 `BaseMetric` + `LLMTestCase`，对营销文案做四维度质量评估（准确性 / 相关性 / 无害性 / 忠实性），理解 LLM-as-a-Judge 的自动化评估范式
3. 能用 **langsmith**（LangChain，MIT）的 `@traceable` 装饰器为部署后的营销 LLM 配置端到端追踪，监控每次调用的延迟、token 消耗、成本，理解"没有可观测性的 LLM 应用等于黑箱"
4. 能用 **tiktoken**（OpenAI，MIT）精确统计部署后 LLM 的输入/输出 token，结合 2026 年主流模型定价（gpt-4o / DeepSeek V3）计算日均万次请求的推理成本，识别成本瓶颈
5. 能解释 **vLLM / 投机解码 / MoE** 三大推理优化技术的原理与适用场景，理解 2026 年 LLM 部署从"能跑"到"低成本高吞吐"的架构演进，并能说明为什么 DeepSeek V3 能用 1/10 的成本逼近 GPT-4o 质量

---

## 理论部分：精炼索引（详见独立教材）

> Day 3 的完整理论讲义见 [`../../AI原生化商业博士_独立教材_选修E3_LLM导论.md` § Day 3](../../AI原生化商业博士_独立教材_选修E3_LLM导论.md)（一至四节，已包含 LLM 评估基准 / 模型选择决策框架 / LLM 部署架构 / 可观测性）。本讲义不重复，仅做上机所需的关键回顾。

### 关键回顾 1：LLM 评估三层框架

| 层次 | 评估对象 | 方法 | 目的 |
|:----:|---------|------|------|
| **通用能力** | 模型基础能力 | MMLU、HumanEval、GSM8K、AgentBench 等标准基准 | 模型选型初筛 |
| **任务能力** | 特定任务表现 | 自建评测集 + 人工/LLM-as-Judge 评分 | 确认模型适合具体任务 |
| **系统效果** | 端到端应用效果 | A/B 测试 + 用户反馈 + 业务转化 | 验证业务价值 |

**工程原则**：标准基准（MMLU 等）用于模型选型初筛，但不要过度依赖。一个模型在 MMLU 上高 5 分，不代表它在你的营销任务上更好。构建一个包含 100-500 条标注数据的领域评测集，比任何标准基准都有参考价值。

### 关键回顾 2：主流评估基准

| 基准 | 评估维度 | 测试方法 | 适用场景 |
|------|---------|---------|---------|
| **MMLU** | 多领域知识 | 多选题 | 评估模型的知识广度 |
| **HumanEval** | 代码生成 | 函数级编程题 | 评估代码能力 |
| **GSM8K** | 数学推理 | 小学数学应用题 | 评估推理能力 |
| **MT-Bench** | 多轮对话 | 人工+LLM 评分 | 评估对话质量 |
| **LLM-as-Judge** | 通用 | 用强 LLM 评判弱 LLM 输出 | 快速自动评估 |
| **RAGAS** | RAG 系统 | 检索准确率+生成忠实度 | RAG 专用评估 |
| **AgentBench** | Agent 能力 | 多轮工具调用+任务完成 | 评估 Agent 系统 |

### 关键回顾 3：LLM 评估四维度（营销场景映射）

| 维度 | 定义 | 营销场景示例 | 失败后果 |
|------|------|-------------|---------|
| **准确性 Accuracy** | 输出事实是否正确 | 产品参数/价格/规格不能编造 | 误导消费者，法律风险 |
| **相关性 Relevance** | 输出是否切题 | 用户要小红书文案，不能给学术论文 | 用户流失 |
| **无害性 Harmlessness** | 输出是否含歧视/违规 | 不能有性别/种族/地域歧视 | 品牌危机 |
| **忠实性 Faithfulness** | 输出是否忠于检索上下文（防幻觉） | RAG 文案只能用知识库信息，不能编造 | 虚假宣传 |

### 关键回顾 4：模型选择决策框架

```
数据能否出域（发送到 API）？
├── 不能 -> 开源模型本地部署
│   ├── 有 GPU 服务器（>=2 张 A100）-> Llama 3 70B / Qwen 2.5 72B
│   ├── 有限 GPU（1 张 A100/4090）-> Llama 3 8B / Qwen 2.5 7B + 量化
│   └── 无 GPU -> 小模型（1-3B）或 API 方案重新评估
└── 可以 -> API 模型
    ├── 任务复杂度高（推理/代码/多步分析）-> Claude 3.5 Sonnet / GPT-4o
    ├── 任务简单（分类/摘要/翻译）-> Claude 3 Haiku / GPT-4o-mini
    └── 超长文档处理 -> 长 Context Window 模型
```

**选型策略**：先用最强模型做原型开发和评测集建立，然后在评测集上测试更便宜的模型，如果质量差距在可接受范围内（如总分差 <10%），切换到便宜模型。这是"先求质量，再降成本"的策略。

### 关键回顾 5：推理优化五大技术

| 技术 | 原理 | 效果 | 适用场景 |
|------|------|------|---------|
| **Quantization（量化）** | FP16 权重压缩为 INT8/INT4 | 显存减少 50-75% | 几乎所有场景 |
| **KV Cache** | 缓存已计算的 Key-Value 对 | 减少重复计算 | 对话场景 |
| **PagedAttention** | 分页管理 KV Cache 显存 | 提高显存利用率 | vLLM 的核心技术 |
| **Speculative Decoding（投机解码）** | 小模型先生成草稿，大模型验证 | 2-3 倍推理加速 | 有配对大小模型时 |
| **Batching** | 合并多个请求批量处理 | 提高吞吐量 | 高并发场景 |

---

## 上机部分：用真实库构建 LLM 评估与监控管道

> 📓 **配套笔记本**：[`starter.ipynb`](./starter.ipynb)（TODO 填空版，你来做）｜ [`solution.ipynb`](./solution.ipynb)（参考答案，gated，做完再看）
> 📊 **真实数据/库**：[`data/README.md`](./data/README.md)（deepeval + langsmith + tiktoken 库 + 营销文案评估集）

### 为什么用真实库而非手写脚本

v4.0 的代码用"手写 print 评分 + time.time() 计时"演示概念。v5.0 改用工业级真实库：

- **deepeval**（Confident AI，MIT）：自定义 `BaseMetric` + `LLMTestCase`，评估营销文案质量。无 API key 时用规则 GEval fallback（关键词匹配/长度/CTA 检测），理解 LLM-as-a-Judge 的评估指标设计原理
- **langsmith**（LangChain，MIT）：`@traceable` 装饰器为部署后 LLM 调用配置端到端追踪，监控延迟/token/成本。无 API key 时本地模式可运行
- **tiktoken**（OpenAI，MIT）：精确统计营销文案的输入/输出 token，结合模型定价计算日均成本，是 LLM 成本监控的事实标准
- **transformers AutoConfig/AutoTokenizer**（HuggingFace，Apache-2.0）：秒级加载模型配置和 tokenizer（不加载权重），理解部署前的模型探测

### 营销映射（关键桥接）

LLM 评估与部署的核心场景：营销 LLM 上线后，怎么评估质量、监控成本、优化推理。

| 上机任务 | 营销场景 | 真实库实现 |
|---------|---------|-----------|
| 评测集构建 | 营销文案评估集（真实文案+评估标准） | dataclass + 真实文案样本 |
| 质量评估 | 营销文案四维度评分（准确/相关/无害/忠实） | deepeval 自定义 BaseMetric |
| 评估运行 | 批量评估营销文案集 + 评分矩阵输出 | deepeval `evaluate` |
| 部署追踪 | 营销 LLM 调用全链路追踪（延迟/token） | langsmith `@traceable` |
| 成本监控 | 日均万次营销文案生成的 token 成本 | tiktoken + 定价表 |
| LLM-as-Judge | 规则近似自动评分（无 API） | 规则实现 GEval fallback |

### 上机任务（6 个 TODO，见 starter.ipynb）

1. **TODO1**：构建营销领域评测集（EvalExample dataclass + 5 条真实营销文案 + 评估标准）
2. **TODO2**：用 deepeval 自定义 `MarketingQualityMetric`（继承 `BaseMetric`），实现四维度规则评分
3. **TODO3**：用 deepeval `evaluate` 批量评估营销文案集，输出评分矩阵
4. **TODO4**：用 langsmith `@traceable` 追踪部署后营销 LLM 调用（mock LLM），记录延迟/token
5. **TODO5**：用 tiktoken 监控日均万次营销文案生成的 token 成本（gpt-4o vs DeepSeek V3）
6. **TODO6**：用 LLM-as-a-Judge 规则近似实现自动评分（无 API，关键词/长度/CTA 检测）

---

## 2026 前沿补充：LLM-as-a-Judge / deepeval / vLLM / 投机解码 / MoE

> v5.0 新增前沿点。LLM 评估与部署在 2026 年的核心趋势是**评估自动化 + 推理成本革命 + 部署架构优化**。

### LLM-as-a-Judge：自动化评估范式

LLM-as-a-Judge（arXiv 2306.05685）用强 LLM（如 GPT-4）评判弱 LLM 的输出质量，是 2026 年 LLM 评估的事实标准。deepeval 的 `GEval` 指标内置 LLM-as-a-Judge 实现，支持自定义评估维度（准确性/相关性/无害性/忠实性）。对营销场景，LLM-as-a-Judge 可自动评估文案是否符合品牌调性、是否含违规内容、是否忠于产品知识库。

### deepeval：LLM 评估的 pytest

deepeval（Confident AI，MIT）是 LLM 评估框架，把评估指标封装为 `BaseMetric`，用 `LLMTestCase` 包装评估样本，用 `evaluate` 批量运行。2026 年的趋势是把 deepeval 评估集成到 CI/CD 流水线，每次 LLM 应用更新（prompt/模型/检索策略变更）都自动跑评估，质量回归即阻断部署。

### vLLM：高吞吐推理引擎

vLLM（https://github.com/vllm-project/vllm）通过 PagedAttention 优化 KV Cache 内存管理，支持连续批处理（continuous batching），在相同硬件上吞吐量可达原生 HuggingFace 的 14-24 倍。适用于自建推理服务替代商业 API，大幅降低成本。本 Day 只做概念讲解，不实装（需 GPU+权重）。

### 投机解码（Speculative Decoding）

用小模型（draft model）快速生成候选 token，再用大模型并行验证。如果小模型猜对了，大模型只需一次前向传播即可接受多个 token，减少串行推理次数。延迟降低 2-3 倍，输出质量不变。2026 年已成为低成本高延迟场景的标配技术。

### MoE（Mixture of Experts）

模型架构创新，将前馈网络拆分为多个"专家"子网络，每次推理只激活少数专家（如 Mixtral 8x7B 只激活 2/8 个专家）。总参数量大但单次推理计算量小，在相同质量下推理成本更低。DeepSeek V3 用 MoE 架构（671B 总参数 / 37B 激活参数）实现接近 GPT-4o 的质量，但 API 定价仅 gpt-4o 的 1/10。

### AgentBench：Agent 能力评估

AgentBench（arXiv 2308.03688）是评估 LLM Agent 能力的基准，测试多轮工具调用、任务完成、环境交互等能力。2026 年随着 Agent 系统普及，AgentBench 已成为模型选型的关键参考。

> 🔗 深入阅读见 [`reading.md`](./reading.md) 的 LLM-as-a-Judge / deepeval / vLLM / 投机解码 / MoE / AgentBench 条目。

---

## 与后续 Day 的衔接

- **Day 1**（已学）：Transformer 架构与训练流程--理解模型底层
- **Day 2**（已学）：LLM 应用工程--RAG / Prompt / Function Calling 已构建应用
- **Day 3**（今天）：LLM 评估与部署--应用上线后怎么评估质量、监控成本、优化推理
- **后续**：选修 E3 结业--从模型到应用到评估部署的完整 LLM 工程闭环

---

## 作业与评估

作业、5 分制量表、费曼演练、2 分钟话术、复盘自诊表--沿用独立教材 § Day 3 既有设计。本学习材料包不重复，仅新增上机交付物：

**新增交付物（v5.0）**：
- [ ] 完成的 `starter.ipynb`（6 个 TODO 全部填好，能跑通）
- [ ] 一段 300 字分析：gpt-4o vs DeepSeek V3 在日均万次营销文案生成场景的成本差异有多大？对模型选型和部署架构有什么启示？
- [ ] （可选）用 deepeval 自定义指标评估自己构建的营销文案，准确性/相关性/无害性/忠实性各是多少？

---

*本讲义由 v5.0 学习材料包升级生成。理论部分引用独立教材，上机部分用真实库（deepeval + langsmith + tiktoken）+ TODO 脚手架。*
*最后更新：2026-07-25*

---

## 学习科学层 (v6.0)

本单元采用刻意练习 (Ericsson deliberate practice, 3 个 drill 各含 Worked-Faded 三阶段) / 间隔重复 (FSRS-6, SM-2 backup, 6 张卡片 due 1-3-8-21-60-180) / 建构对齐 (Biggs ILO↔TLA↔AT, 5 行对齐矩阵含 mastery threshold >=80%) / 牛津 tutorial LLM 仿真 (Socratic 4 轮静态 if/else, Hattie 4 级反馈 [TASK]/[PROCESS]/[SELF-REG]/[FEED-FORWARD], 避 Self 级表扬)。mastery 阈值与 Worked-Faded 示例见 practice.md 与 alignment.md。交叉练习 (interleaving A1B1C1...B2C2A2...C3A3B3) 促进迁移, 提取练习 (retrieval practice, tutorial pre-tutorial essay) 优于重读。间隔重复卡片 (schedule.json) 覆盖本单元 6 个核心概念 (LLM 评估三层框架 / deepeval BaseMetric / 评估四维度 / langsmith @traceable / vLLM+投机解码+MoE / 模型选择决策框架), 配合 FSRS-6 算法在 1-3-8-21-60-180 天节点复习, request_retention=0.9。

## 研究产出与产业链接层 (v7.0)
本单元产出可发表研究工件 (research.md: 研究问题+贡献声明+arXiv链接+IMRaD大纲+NeurIPS可复现清单+research-to-practice翻译) 与产业链接 (industry.md: >=3真实企业+部署场景+Imperial咨询项目+HBS教学案例+客座讲座+实习指针)。研究产出遵循IMRaD/DSR(Hevner)/OSF预注册/FAIR/可复现研究标准; 产业链接遵循Imperial MSc BA咨询项目(Burberry/Expedia/J&J)/HBS案例法/MIT Sloan行动学习模式。详见 research.md 与 industry.md。

---

## 学术前沿层 (v9.0)

本单元新增 `frontier.md`：注入 2025-2026 最新学术前沿（N 篇真实 arXiv 论文 + 批判性综述 + delta_to_unit + ≥3 开放研究问题 + 方法论批评）。论文来自 `_frontier_corpus/elective-e3-llm-intro.md` 共享语料库（arXiv 搜索 + abstract 页抽查验证），覆盖前沿课题：LLM推理经济 × 推理模型 × 高效推理。面向博后/教授级读者：批判性综述非罗列，delta_to_unit 显式指出前沿如何更新本单元所教，开放问题为可发表研究方向。详见 `frontier.md`。

---

## AI工程从零构建层 (v11.0)

> v11.0 新增 [`from_scratch.md`](./from_scratch.md)：AI工程从零构建（旗舰模块），与本单元 deepeval BaseMetric 规则评分 + tiktoken API 成本形成"信息论指标 + 量化降本"对照。
> - **从零构建主题**：手写 INT8 对称量化（矩阵分解 + 反量化误差）+ 手写 perplexity 计算 + 手写 greedy/beam search（LLM eval + deployment from scratch）
> - **核心算法**：INT8 对称量化 $\text{scale}=\max(|W|)/127$ + round + 反量化误差 + perplexity $=\exp(-\text{mean}(\text{NLL}))$（含数学推导 + LaTeX）
> - **code_artifact**：手写 numpy/math 骨架（≤50行），imports ⊆ 白名单 {numpy, math}，附 verification_property
> - **延伸阅读**：rohitg00 AI工程 from scratch P11/10 Evaluation + P17/04 vLLM Serving Internals（ai-engineering-from-scratch 仓库）
> - **手写实现要点**：用 from-scratch INT8 量化而非 deepeval/vLLM 黑箱，理解量化误差到数学层；notes.md 标注"不实装"被 from-scratch 打破
> - **verification_property**：INT8 范围 $[-127,127]$；反量化相对 L2 误差 $<5\%$；均匀分布 PPL $= V$（词表大小）
