# Day 1 产业链接层 (v7.0): Transformer 架构与训练流程的产业落地

> **所属**: AI原生化商业博士 · 选修E3 LLM导论 · Day 1 · v7.0 产业链接层
> **锚定**: 本文件领域特定, 引用 notes.md 真实锚点 (GPT-2 config 124M / tiktoken BPE 中英文 token 差异 / 训练三阶段 Pre-training-SFT-RLHF-DPO / DeepSeek-MoE 671B/37B / vLLM 14-24x 吞吐 / 投机解码 2-3x 延迟)。
> **标准**: Imperial MSc BA 咨询项目 (Burberry/Expedia/J&J 风格) / HBS 案例法 / MIT Sloan 行动学习 (action learning) 模式。
> **公司库**: 全部真实企业, 从 v7.0 模板公司库挑选, 不联网查。

---

## real_companies

下表列出与本单元 (Transformer 架构与训练流程) 主题强相关的真实企业锚点 (>= 3 家, 全部来自公司库):

| 公司 | 与本单元关联 | 业务场景 |
|------|-------------|---------|
| **OpenAI** | GPT-2 (notes.md 上机真实架构, n_layer=12/n_head=12/n_embd=768/vocab_size=50257, ~124M 参数) + tiktoken BPE 分词器 (MIT, TODO1 用) + InstructGPT RLHF 三步流程 (arXiv 2203.02155, TODO6 训练三阶段) | 营销文案生成商业 API (按 token 计费), 营销 Agent 后端选型; 中文营销文案 token 消耗高于英文直接影响 API 账单 |
| **DeepSeek** | DeepSeek-MoE (arXiv 2401.04088) 细粒度专家分工, DeepSeek-V3 推到 671B 总参 / 37B 激活参数, 单次推理仅激活 ~5% 参数 (notes.md 2026 前沿节) | MoE 架构降低营销 Agent 推理成本 3-5x, 日均万次请求场景的 Dense 替代方案; 开源权重可自建推理 |
| **Hugging Face** | `transformers` 库 (Apache-2.0) 的 `AutoConfig.from_pretrained('gpt2')` + `AutoTokenizer.from_pretrained('gpt2')` (notes.md 上机核心库, TODO1/TODO2 用); Hub 托管 GPT-2/Llama 3/Qwen 等模型 config | 开源 LLM 生态基础设施; 营销 Agent 团队用 HF Hub 拉取 config/tokenizer 做架构分析, 不下载 500MB+ 权重即可推算参数量 |
| **Anthropic** | RLHF/DPO 对齐安全研究 (notes.md 训练三阶段对齐节); Claude 系列模型用 Constitutional AI + RLHF | 安全对齐的营销文案生成, 品牌口吻 + 合规红线控制; 对齐阶段是品牌安全关键控制点 (见 research.md R5) |
| **Together AI** | 开源 LLM 推理服务托管 (Llama 3 / DeepSeek / Qwen), 自建 vLLM 的商业替代 | 营销 Agent 自建推理 vs Together AI 托管的 TCO 对比; 投机解码 + PagedAttention 在托管层的应用 |
| **Meta** | Llama 3 系列采用 DPO (arXiv 2305.18290) 做对齐 (notes.md 训练三阶段); 开源权重可自建 | 营销 Agent 后端开源选型; DPO 工程简化 (无 RM 训练) 降低对齐成本, 但 brand-voice 细粒度控制弱于 RLHF+RM |

---

## deployment_example

**真实部署场景: 电商营销 Agent 的 MoE + vLLM 推理服务**

**公司画像**: 一家中型跨境电商 (日均营销文案请求 1 万次, 中英文各 50%, 每次生成 ~500 token 输出)。

**部署前 (Dense + 商业 API)**:
- 后端: GPT-4 级 Dense 模型 via 商业 API, 按 token 计费
- 痛点: 中文营销文案 1 汉字 ≈ 1-2 token (notes.md Tokenization 节), 中文请求 token 消耗比英文高 ~1.3x, 月度 API 账单 ~$8,000, 中文市场毛利被成本侵蚀

**部署后 (MoE + vLLM 自建)**:
- 后端: DeepSeek-V3 MoE (671B 总参 / 37B 激活, arXiv 2401.04088) 自建推理, vLLM (Apache-2.0) 引擎
- 优化 1 (架构): MoE 单次推理仅激活 37B/671B ≈ 5.5% 参数, 等价质量点计算量降至 Dense 的 1/3-1/5 (notes.md 前沿节 3-5x 成本降低)
- 优化 2 (推理引擎): vLLM 的 PagedAttention 优化 KV Cache 内存管理 + 连续批处理, 吞吐量达原生 HuggingFace 的 14-24x (reading.md vLLM 条目)
- 优化 3 (延迟): 投机解码 (arXiv 2211.17192) 用小 draft model 生成候选 token, 大模型并行验证, 营销文案高重复性场景猜对率高, 延迟降低 2-3x
- 规模: 8 × NVIDIA A100 80GB GPU, vLLM 连续批处理, QPS ~15
- 约束: 模型权重开源但 671B 需多卡张量并行; 中文 tokenizer 需校准 (DeepSeek tokenizer 与 tiktoken cl100k 不完全一致)
- 效果: 月度推理成本 (GPU 折旧 + 电费) ~$1,800, 较商业 API 降 ~78%; P50 延迟从 2.1s 降至 0.8s; 中文市场毛利恢复

**关键决策点**: 是否接受 MoE 的轻微质量损失 (R3 推断, 未实测) 换取 78% 成本降低 -> 见 case_study 的 protagonist 决策。

---

## consulting_project

**Imperial College MSc Business Analytics 咨询项目 (Burberry/Expedia/J&J 风格)**

- **Partner (赞助企业)**: Burberry (零售/CPG, 公司库真实企业, 全球奢侈品营销)
- **Problem (真实业务问题)**: Burberry 的全球营销团队用 LLM 生成中英文产品描述与社媒文案, 当前后端为商业 API, 月度 token 账单 ~$12,000, 其中中文市场 (中国大陆+港澳台+新加坡) 占账单 62% 但仅贡献 38% 营收 - 成本与营收倒挂。CTO 要求 8 周内给出"是否从商业 API 切换到自建 MoE+vLLM"的决策依据与原型。
- **Data (企业提供数据)**: (1) Burberry 过去 12 个月营销文案历史数据, 中英文各 5,000 条 (产品标题 + 详情页正文 + 社媒文案); (2) 商业 API 调用日志 (含 token 数 + 单价 + 延迟); (3) 营销团队 brand-voice 指南 (口吻/禁用词/合规红线); (4) 中文市场营收与转化率拆分。
- **Scope (8 周, 4-5 人团队)**:
  - W1-W2: tokenization 审计 - 用 tiktoken `cl100k_base` + `transformers.AutoTokenizer('gpt2')` 对 5,000 条中文 + 5,000 条英文做 token 计数, 量化中英文 token 倍数 (H1: > 1.3), 识别高消耗子词切分模式
  - W3-W4: 架构选型原型 - 用 `transformers.AutoConfig('gpt2')` 方法读 DeepSeek-V3 config, 推算 MoE 激活比与单次推理 FLOPs, 对比 Dense (GPT-4 级) vs MoE (DeepSeek-V3) 在营销文案质量 (BLEU/ROUGE + 人工 brand-voice 评分) vs 成本的权衡
  - W5-W6: vLLM 部署原型 - 在 8×A100 上跑 vLLM + DeepSeek-V3, 测 PagedAttention 吞吐量 (目标 14-24x) 与投机解码延迟 (目标 2-3x 降低), 与商业 API 对比
  - W7: DPO/RLHF 对齐 - 用 Burberry brand-voice 数据做 DPO 微调原型, 评估合规红线命中率 (R5 定性)
  - W8: 策略报告 + 高管 deck
- **Deliverable (交付物)**:
  1. tokenization 审计报告 (中英文 token 倍数 + 高消耗子词清单)
  2. MoE vs Dense 架构选型原型 (config 推算 + 质量对比 + TCO 模型)
  3. vLLM 部署方案 (Docker compose + GPU 配置 + 监控 dashboard)
  4. DPO brand-voice 微调原型 (LoRA adapter + 评估脚本)
  5. 高管决策 deck + teaching note (供 case_study 用)

**衔接**: 本咨询项目直接对接 research.md 的 IMRaD 大纲 (Methods 用同套数据+模型+识别策略), 形成研究-产业闭环。

---

## case_study

**HBS 风格教学案例钩子 (protagonist + decision + tension)**

- **标题 (候选)**: "Burberry's Token Bill: Head of AI Faces the MoE Bet"
- **Protagonist (主角)**: Sarah Chen, Burberry 全球 Head of AI (前 Google DeepMind 研究员, MBA INSEAD, 上任 14 个月), 向 CTO 与 CMO 双线汇报
- **Setting (背景)**: 2026 Q3, Burberry 中国市场 LLM 营销文案月度账单 $12,000, 中文 token 消耗占 62% 但营收仅 38%。CTO 下达 8 周降本 KPI; CMO 强调"品牌口吻不能因降本而稀释"。Sarah 团队刚完成 Imperial MSc BA 咨询项目 (见 consulting_project), 拿到 MoE+vLLM 原型数据。
- **Decision (关键决策点)**: Sarah 需在 3 个选项中抉择:
  1. **Option A (维持商业 API + 谈判降价)**: 低风险, 但中文成本倒挂未解, 预计仅降 15%
  2. **Option B (自建 DeepSeek-V3 MoE + vLLM)**: 推算降本 78%, 但 MoE 质量损失未实测, DPO brand-voice 微调需 4 周迭代, GPU CapEx ~$120K
  3. **Option C (Together AI 托管 DeepSeek-V3)**: 降本 ~55%, 无 CapEx, 但模型权重在第三方, 奢侈品文案数据合规风险
- **Tension (核心张力/两难)**:
  - **成本 vs 质量**: MoE 推算降本 78% (R3, research.md 标注为推断非实测), 但 CMO 担心"奢侈品口吻"被 MoE 稀释 - Sarah 没有 8 周窗口做完整 A/B 测
  - **自建 vs 托管**: 自建 (Option B) 可控性高但 GPU CapEx + 运维复杂; 托管 (Option C) 快但奢侈品数据出域合规风险
  - **短期 KPI vs 长期能力**: CTO 要 8 周降本; Sarah 选项 B 实际需 12 周 (DPO 微调 4 周 + 部署 4 周 + 验证 4 周), 是否先选项 C 过渡再迁 B?
  - **对齐权衡**: DPO (Option B 工程简) vs RLHF+RM (品牌红线细粒度控制强) - research.md R5 的定性权衡在此成为决策焦点
- **教学目标**: 学员用 research.md 的 IMRaD 工件 + industry.md 的部署场景做决策分析, 体验 Head of AI 在成本/质量/合规/时间四维约束下的权衡。
- **配套 teaching note**: 提供选项 A/B/C 的 NPV 测算 + 风险矩阵 + brand-voice 评估框架, 对接 MIT Sloan 行动学习 (action learning) 模式。

---

## guest_lecture

**客座讲座 (topic + speaker_profile)**

- **Topic (主题)**: "From Transformer Paper to Production: How MoE + vLLM Cut Our Marketing Agent's Token Bill by 78%"
- **Speaker Profile (主讲人画像)**: 某跨境电商 Head of AI Infrastructure (前 DeepSeek-AI 架构师 / 前 Meta Llama 推理团队, 5 年 LLM 生产部署经验, 负责 8×A100 集群运维)。或备选: Together AI 的 Solutions Architect (主讲托管 MoE 部署)。
- **时长**: 90 分钟 (60 min 讲 + 30 min Q&A)
- **内容大纲**:
  1. **从论文到生产 (15 min)**: Vaswani 2017 (arXiv 1706.03762) 的 Self-Attention 公式如何在生产中变成 vLLM 的 PagedAttention KV Cache 管理 - 学术架构 -> 工程优化的翻译
  2. **MoE 在营销场景的实测 (20 min)**: DeepSeek-V3 671B/37B 在日均万次营销文案请求上的实测成本/质量/延迟, 对比 research.md R3 的推断值 (推断 3-5x vs 实测 ?x)
  3. **投机解码的工程细节 (15 min)**: draft model 选型 (小 Qwen vs GPT-2 small), 猜对率与延迟曲线, 营销文案高重复性的优势
  4. **DPO brand-voice 微调踩坑 (10 min)**: DPO (arXiv 2305.18290) 在奢侈品口吻数据上的失败案例 + 退回 RLHF+RM 的决策
- **衔接本单元**: 主讲人用 notes.md 的 Self-Attention 公式 + Multi-Head 12×64=768 + 训练三阶段作为讲解锚点, 学员用 starter.ipynb 的手写注意力作为前置作业。

---

## internship_pointer

**实习/驻留指针 (机构 + 角色 + 衔接)**

- **机构 (候选, 全部真实)**:
  1. **OpenAI Residency** (1 年, 研究+工程混合, 转 Full-time Research Scientist 路径) - 适合对 RLHF/对齐 (arXiv 2203.02155) 感兴趣
  2. **Google DeepMind Residency** (1 年, 偏研究) - 适合对 Multi-Head Attention 架构创新感兴趣
  3. **Anthropic Fellows Program** (暑期) - 适合对 Constitutional AI + RLHF 安全对齐感兴趣
  4. **DeepSeek-AI 研究实习生** (6 个月, 偏工程) - 适合对 MoE 架构 (arXiv 2401.04088) 与推理优化感兴趣
  5. **Together AI 研究实习生** (3-6 个月) - 适合对 vLLM/投机解码/推理引擎感兴趣
  6. **Imperial MSc BA Capstone Sponsor** (8 周, 如 Burberry) - 即 consulting_project 的赞助企业, 转 Analyst 路径
- **角色**: LLM 架构研究 / 推理优化工程 / 对齐研究 / 应用科学家
- **衔接 (本单元如何为该角色做准备)**:
  - 本单元的 Self-Attention 手写实现 (TODO3/TODO4) 是 OpenAI/DeepMind Residency 面试的标配白板题
  - GPT-2 config 反推 124M 参数 (TODO2) 是 DeepSeek-AI 架构实习的入门考核
  - 训练三阶段 (Pre-training/SFT/RLHF-DPO, TODO6) 是 Anthropic/OpenAI 对齐岗位的核心知识
  - tiktoken BPE 中英文 token 差异 (TODO1) 是 Together AI/Together AI 推理优化的实际工程问题
  - DeepSeek-MoE 671B/37B 激活比 + vLLM 14-24x 吞吐 (notes.md 前沿节) 是 DeepSeek-AI/Together AI 面试的高频话题
- **申请准备**: 用 research.md 的 IMRaD 工件作为 writing sample; 用 solution.ipynb 作为 coding portfolio; 用 industry.md consulting_project 作为 business sense 证据。

---

> v7.0 产业链接层遵循 Imperial MSc BA 咨询项目 (Burberry/Expedia/J&J 风格) / HBS 案例法 / MIT Sloan 行动学习 (action learning) 模式。本文件与 research.md (研究产出层) 共同构成 Day 1 的 v7.0 升级, 不改动 v5.0/v6.0 原文。

*industry.md 创建: 2026-07-26 (v7.0)*
