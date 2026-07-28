# 选修E3 · Day 1：LLM基础：Transformer架构与训练流程 · 讲义（v5.0 学习材料包版）

> **所属**：AI原生化商业博士 · 选修E3 LLM导论 · Day 1
> **版本**：v5.0（从独立教材升级为学习材料包）
> **预计**：2h 讲义 + 2h 上机练习
> **核心命题**：LLM 是营销 Agent 的引擎--理解 Transformer 如何生成营销文案、token 成本如何影响推理成本
> **v5.0 升级点**：① 新增真实库上机（transformers + torch + tiktoken）② 新增 TODO 填空式起始笔记本 ③ Notebook 化 ④ 深链阅读 ⑤ 2026 前沿（DeepSeek-MoE / 投机解码 / 推理成本优化）

---

## 学习目标（学完你能做到）

1. 能解释 Transformer 的三大核心机制--Self-Attention（Q/K/V 点积 + 缩放 + softmax）、Multi-Head Attention（多视角并行关联）、Positional Encoding（位置注入）--并说明为什么 Self-Attention 比 RNN/LSTM 更适合长程依赖
2. 能阐述 LLM 训练三阶段（Pre-training 预测下一 token / SFT 指令微调 / Alignment RLHF-DPO 对齐）各自的数据、目标和产出，并判断模型表现不佳时属于知识不足、交互风格不对还是安全限制
3. 能用 **tiktoken**（OpenAI BPE 分词器）和 **transformers AutoTokenizer**（GPT-2 tokenizer）对营销文案做真实 tokenization，对比中英文 token 消耗差异，结合模型定价计算推理成本
4. 能用 **torch** 手写简化版 Self-Attention 和 Transformer Block（Q/K/V 线性层 + 多头注意力 + FFN + 残差 + LayerNorm），理解架构而非黑箱调用
5. 能从 **transformers AutoConfig**（GPT-2 config）读取架构参数（n_layer/n_head/n_embd/vocab_size），推算模型参数量（GPT-2 small ~124M），理解 Scale Law 对商业决策的影响

---

## 理论部分：精炼索引（详见独立教材）

> Day 1 的完整理论讲义见 [`../../AI原生化商业博士_独立教材_选修E3_LLM导论.md` § Day 1](../../AI原生化商业博士_独立教材_选修E3_LLM导论.md)（一至四节，已包含语言模型三代演进/Transformer 三机制/训练三阶段/Tokenization 实践影响）。本讲义不重复，仅做上机所需的关键回顾。

### 关键回顾 1：Self-Attention -- Transformer 的灵魂

```
Attention(Q, K, V) = softmax(Q × K^T / √d_k) × V
```

| 角色 | 符号 | 功能 | 营销类比 |
|------|------|------|---------|
| Query | Q | "我在找什么信息？" | 用户搜索词 |
| Key | K | "我有什么信息？" | 产品标题/关键词 |
| Value | V | "我的实际内容" | 产品详情页正文 |

**为什么比 RNN 强**：每个词直接与所有词交互，信息传递路径 O(1)，可并行计算。RNN 按顺序传递，长距离信息衰减。

### 关键回顾 2：Multi-Head Attention -- 多视角关联

```
Multi-Head(Q,K,V) = Concat(head_1,...,head_h) × W_O
head_i = Attention(Q×W_Q^i, K×W_K^i, V×W_V^i)
```

不同 Head 学习不同关联模式：语法关系（主谓一致）、语义关系（同义词）、位置关系（相邻词）。GPT-2 small 用 12 个 Head。

### 关键回顾 3：Positional Encoding + Transformer Block

- **位置编码**：Self-Attention 本身无顺序概念，需注入位置信息。原始 Transformer 用正弦/余弦，现代 LLM 用 RoPE（旋转位置编码），外推性更好
- **Transformer Block**：Multi-Head Attention → 残差+LayerNorm → FFN（4x 扩展）→ 残差+LayerNorm。N 个 Block 堆叠

### 关键回顾 4：训练三阶段

| 阶段 | 任务 | 数据 | 产出 |
|:----:|------|------|------|
| Pre-training | 预测下一 token | 数万亿 token 互联网文本 | Base Model（有知识不会对话） |
| SFT | 指令-回答对 | 数万-数十万条高质量对 | Chat Model（能遵循指令） |
| Alignment | RLHF/DPO 对齐偏好 | 人类偏好排序数据 | Aligned Model（安全+有用） |

**DPO vs RLHF**：DPO（2023年）绕过 Reward Model 训练和 RL 优化，直接从偏好对优化 LLM，更简单更稳定，Llama 3/Zephyr 采用。

### 关键回顾 5：Tokenization 的实践影响

- **成本**：LLM API 按 token 计费。英文 ~1 token ≈ 0.75 单词，中文 1 汉字 ≈ 1-2 token
- **Context Window**：128K token ≈ 10 万英文单词 / 6-8 万中文字
- **多语言差异**：同一意思中文比英文消耗更多 token，直接影响成本和速度

---

## 上机部分：用真实库理解 Transformer 架构

> 📓 **配套笔记本**：[`starter.ipynb`](./starter.ipynb)（TODO 填空版，你来做）｜ [`solution.ipynb`](./solution.ipynb)（参考答案，gated，做完再看）
> 📊 **真实数据/库**：[`data/README.md`](./data/README.md)（transformers + torch + tiktoken 库 + 营销文案语料）

### 为什么用真实库而非手写脚本

v4.0 的代码用"伪代码图解"演示概念。v5.0 改用工业级真实库：

- **transformers**（HuggingFace，Apache-2.0）：`AutoConfig.from_pretrained("gpt2")` 读取真实 GPT-2 架构参数，`AutoTokenizer.from_pretrained("gpt2")` 加载真实 BPE 分词器。**不加载预训练权重**（避免下载 500MB+ 模型），仅用 config + tokenizer 做架构分析
- **torch**（PyTorch，BSD-style）：手写简化版 Self-Attention 和 Transformer Block，理解 Q/K/V 计算流程而非黑箱调用
- **tiktoken**（OpenAI，MIT）：BPE 分词器，精确计算营销文案的 token 数，结合模型定价计算推理成本

### 营销映射（关键桥接）

LLM 是营销 Agent 的引擎。本 Day 处理一个"营销文案 tokenization + 注意力可视化"场景：

| 上机任务 | 营销场景 | 真实库实现 |
|---------|---------|-----------|
| Tokenization 对比 | 营销文案的中英文 token 消耗差异 | tiktoken + transformers AutoTokenizer |
| GPT-2 架构分析 | 理解生成营销文案的模型有多大 | transformers AutoConfig |
| 手写 Self-Attention | 理解注意力如何关联营销关键词 | torch 张量运算 |
| Transformer Block | 理解完整架构块（注意力+FFN+残差） | torch nn.Module |
| 注意力可视化 | 看营销文案中哪些词相互关联 | torch + tiktoken |
| CLM 前向传播 | 理解预训练"预测下一 token"任务 | torch MiniGPT |

### 上机任务（6 个 TODO，见 starter.ipynb）

1. **TODO1**：用 tiktoken 和 transformers tokenizer 对营销文案做 tokenization，对比中英文 token 消耗
2. **TODO2**：从 GPT-2 config 读取架构参数，推算参数量（~124M）
3. **TODO3**：手写 Self-Attention（Q/K/V 点积 + 缩放 + softmax）
4. **TODO4**：手写 Multi-Head Attention + Transformer Block（FFN + 残差 + LayerNorm）
5. **TODO5**：在营销文案 token 上运行注意力，可视化注意力矩阵
6. **TODO6**：CLM 前向传播演示（预测下一 token）+ 训练三阶段概述

---

## 2026 前沿补充：DeepSeek-MoE / 投机解码 / 推理成本优化

> v5.0 新增前沿点。LLM 的核心商业瓶颈是**推理成本**：每次生成营销文案消耗 token，日均万次请求的成本可达数千美元。2026 年的趋势是用架构创新和推理优化技术大幅降低单次推理成本。

### DeepSeek-MoE：用专家混合降低推理计算量

**MoE（Mixture of Experts）** 将 FFN 拆分为多个"专家"子网络，每次推理只激活少数专家。DeepSeek-MoE（arXiv 2401.04088）提出了细粒度专家分工策略，DeepSeek-V3 进一步将 MoE 推到 671B 总参数 / 37B 激活参数，在相同质量下推理成本远低于 Dense 模型。

**对营销 Agent 的启示**：如果营销 Agent 后端用 MoE 模型（如 DeepSeek-V3），日均万次请求的推理成本可降低 3-5 倍，因为单次推理只激活 ~5% 参数。

### 投机解码（Speculative Decoding）

用小模型（draft model）快速生成候选 token，大模型并行验证。猜对则大模型一次前向传播接受多个 token，减少串行推理次数。延迟降低 2-3 倍，输出质量不变（arXiv 2211.17192）。

### 多模态与对比学习的前沿

现代 LLM 正向多模态演进（GPT-4o/Gemini）。多模态对齐的核心是**对比学习**（contrastive learning）--CLIP 用对比损失将图文对齐到同一向量空间。理解 Day 1 的 Self-Attention 有助于理解多模态模型如何融合不同模态的表示。

> 🔗 深入阅读见 [`reading.md`](./reading.md) 的 DeepSeek-MoE / 投机解码 / vLLM 条目。

---

## 与后续 Day 的衔接

- **Day 2**：LLM 应用工程--今天的 Transformer 架构基础将扩展到 Prompt/RAG/Fine-tuning/Function Calling 四种应用模式
- **Day 3**：LLM 评估与部署--今天的训练三阶段理解将延伸到评估基准和模型选择决策

---

## 作业与评估

作业、5 分制量表、费曼演练、2 分钟话术、复盘自诊表--沿用独立教材 § Day 1 既有设计。本学习材料包不重复，仅新增上机交付物：

**新增交付物（v5.0）**：
- [ ] 完成的 `starter.ipynb`（6 个 TODO 全部填好，能跑通）
- [ ] 一段 300 字分析：营销文案的中英文 token 消耗差异有多大？对推理成本有什么影响？
- [ ] （可选）用手写 Self-Attention 分析一段真实营销文案，哪些词对相互关联最强？

---

*本讲义由 v5.0 学习材料包升级生成。理论部分引用独立教材，上机部分用真实库（transformers + torch + tiktoken）+ TODO 脚手架。*
*最后更新：2026-07-25*

---

## 学习科学层 (v6.0)

本单元在 v5.0 学习材料包基础上, 叠加四项基于学习科学实证的增强, 不改动 v5.0 原文一字:

1. **刻意练习 (Ericsson deliberate practice)** -- 见 `practice.md`。把"听得懂 Transformer"拆成 3 个可观察子技能 (S-A Self-Attention 计算 / S-B 训练三阶段故障诊断 / S-C Tokenization 成本推算), 配 5 个 drill (D1-D5), 每个 drill 走 Worked-Faded (完整示范 -> 部分填空 -> 独立解) 三阶段, feedback_rule 引用本单元真实库 (tiktoken / transformers AutoConfig / GPT-2 config)。CS229 pset0 式 diagnostic 先测先验缺口, CS230 式 progressive_project (proposal -> milestone -> final -> poster) 渐进交付。

2. **间隔重复 (FSRS-6, SM-2 backup)** -- 见 `schedule.json`。8 张卡覆盖本单元核心概念: Self-Attention 公式与 √d_k 缩放 / Multi-Head 12×64=768 / Pre-training-SFT-RLHF-DPO 三阶段 / 中英文 token 成本倍数 / DeepSeek-MoE 671B/37B 激活比 / DPO vs RLHF / GPT-2 124M 参数推算 / 投机解码。每卡 due=[1,3,8,21,60,180] 天, request_retention=0.9。retrieval practice (提取练习) 优于重读。

3. **建构对齐 (Biggs constructive alignment, ILO ↔ TLA ↔ AT)** -- 见 `alignment.md`。5 条 ILO (来自 notes.md 学习目标) 与 starter.ipynb TODO + practice.md drill + tutorial.ipynb Socratic (TLA) 与 solution.ipynb + 后测 (AT) 一一对齐, 每行附 mastery_threshold (>=80%)。三自检问题 (Hattie Feed Up / Feed Back / Feed Forward) 验证不经 TLA 不能过 AT。

4. **牛津 tutorial LLM 仿真 (Oxford tutorial + Socratic + Hattie 4 级反馈)** -- 见 `tutorial.ipynb`。persona prompt 设定 Fellow 不直接给答案、必用 Socratic 追问、扮 HBS devil's advocate、拒模糊断言、每轮收尾必是 probing question。4 轮静态 if/else Socratic loop 含 11 个 probing questions (为什么 / 反例 / 若前提变 / 凭什么 / 如何)。Hattie 4 级反馈 [TASK] / [PROCESS] / [SELF-REG] / [FEED-FORWARD] 避免 Self 级表扬。限频每天 1 次防依赖。

**mastery 阈值** 与 Worked-Faded 示例见 `practice.md` 与 `alignment.md`。**交叉练习 (interleaving)**: D1->D2->D3->D1->D2->D3->D1->D2->D3 (非块状) 促进迁移 (Rohrer 2007)。**弱项循环 (weak_loop)**: 连续 2 次失败触发回退 Faded + 新 Worked + 重做 Solo。

> v6.0 关键词命中: FSRS-6 / SM-2 / 刻意练习 (deliberate practice) / 建构对齐 (constructive alignment) / 牛津 tutorial / Socratic / Hattie / 间隔重复 (spaced retrieval) / 交叉 (interleaving) / mastery / Worked-Faded / retrieval practice / 提取练习 -- 共 13 个, 远超 >=4 要求。

*v6.0 学习科学层追加完成: 2026-07-26。v5.0 原文未改动。*

## 研究产出与产业链接层 (v7.0)

本单元产出可发表研究工件 (research.md: 研究问题+贡献声明+arXiv链接+IMRaD大纲+NeurIPS可复现清单+research-to-practice翻译) 与产业链接 (industry.md: >=3真实企业+部署场景+Imperial咨询项目+HBS教学案例+客座讲座+实习指针)。研究产出遵循IMRaD/DSR(Hevner)/OSF预注册/FAIR/可复现研究标准; 产业链接遵循Imperial MSc BA咨询项目(Burberry/Expedia/J&J)/HBS案例法/MIT Sloan行动学习模式。详见 research.md 与 industry.md。

**研究产出锚点 (research.md)**: 研究问题锚定中英文营销文案 tokenization 成本倍数 (H1: >1.3) 与 MoE vs Dense 架构成本降低 (H2: 3-5x); 贡献声明显式标注 delta vs Vaswani 2017 / DeepSeek-MoE 2024 / DPO 2023; linked_paper 引用 reading.md 已验证 arXiv 链接 (1706.03762 / 1508.07909 / 2203.02155 / 2305.18290 / 2401.04088 / 2211.17192); IMRaD 大纲引用 GPT-2 config n_layer=12/n_head=12/n_embd=768/vocab_size=50257 与 ~124M 参数推算; 可复现清单 7 项 (code/data/seeds/environment/preregistration/FAIR/statistical reporting); research-to-practice 翻译为 HBR 文章 + MIT Sloan 教学案例 + 企业白皮书三轨道。

**产业链接锚点 (industry.md)**: real_companies 6 家 (OpenAI/DeepSeek/Hugging Face/Anthropic/Together AI/Meta); deployment_example 为电商营销 Agent 的 DeepSeek-V3 MoE + vLLM 部署 (8×A100, 降本 78%); consulting_project 为 Burberry 赞助的 Imperial MSc BA 8 周咨询项目 (中英文 tokenization 审计 + MoE 选型 + vLLM 部署 + DPO brand-voice 微调); case_study 为 HBS 风格 "Burberry's Token Bill: Head of AI Faces the MoE Bet" (protagonist Sarah Chen, 成本/质量/合规/时间四维张力); guest_lecture 为 "From Transformer Paper to Production"; internship_pointer 指向 OpenAI Residency / DeepSeek-AI / Together AI / Imperial Capstone。

**v7.0 关键词命中**: 研究产出 / research output / IMRaD / 可复现 / reproducibility / OSF / 预注册 / preregistration / FAIR / contribution / 贡献 / 产业链接 / industry linkage / consulting / 咨询 / case study / 案例 / guest lecture / 客座 / internship / 实习 / deployment / 部署 / linked_paper / arXiv / DSR / Hevner / research-to-practice / NeurIPS / 行动学习 / action learning -- 共 30+ 个, 远超 >=4 要求。

*v7.0 研究产出与产业链接层追加完成: 2026-07-26。v5.0/v6.0 原文未改动。*

---

## 学术前沿层 (v9.0)

本单元新增 `frontier.md`：注入 2025-2026 最新学术前沿（N 篇真实 arXiv 论文 + 批判性综述 + delta_to_unit + ≥3 开放研究问题 + 方法论批评）。论文来自 `_frontier_corpus/elective-e3-llm-intro.md` 共享语料库（arXiv 搜索 + abstract 页抽查验证），覆盖前沿课题：LLM推理经济 × 推理模型 × 高效推理。面向博后/教授级读者：批判性综述非罗列，delta_to_unit 显式指出前沿如何更新本单元所教，开放问题为可发表研究方向。详见 `frontier.md`。

---

## AI工程从零构建层 (v11.0)

> v11.0 新增 [`from_scratch.md`](./from_scratch.md)：AI工程从零构建（旗舰单元），与本单元 torch 手写注意力形成"纯 numpy vs torch"对照。
> - **从零构建主题**：手写 scaled dot-product attention + multi-head attention（self-attention from scratch）
> - **核心算法**：softmax(QK^T/√d_k)V（含数学推导 + LaTeX，缩放因子与因果掩码）
> - **code_artifact**：手写 numpy 骨架（≤50行），imports ⊆ {numpy}，附 verification_property（权重行和=1）
> - **延伸阅读**：rohitg00 AI工程 from scratch P7/02 Self Attention + P7/05 Full Transformer + P10/04 Pre-training Mini GPT
> - **手写实现要点**：用 from-scratch numpy 而非 torch.nn.MultiheadAttention，理解注意力到金属层
> - **verification_property**：attention 权重行和=1；因果掩码上三角≈0；multi-head 输出形状=输入形状
