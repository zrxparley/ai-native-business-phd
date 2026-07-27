# 技能5 · Day 5：生产部署与运维 · 讲义（v5.0 学习材料包版）

> **所属**：AI原生化商业博士 · 技能5 Agentic系统工程与落地 · Day 5
> **版本**：v5.0（从独立教材升级为学习材料包）
> **预计**：2h 讲义 + 2h 上机练习
> **核心命题**：Agent 从 PoC 走向生产--可靠性、成本、延迟、可观测性、灾备降级，如何系统化解决？
> **v5.0 升级点**：① 新增真实库上机（langsmith + tiktoken）② 新增 TODO 填空式起始笔记本 ③ Notebook 化 ④ 深链阅读 ⑤ 2026 前沿（LangSmith 可观测性 + vLLM 推理成本优化 + 投机解码 + MoE）

---

## 学习目标（学完你能做到）

1. 能解释 Agent 从 PoC 到生产的五大挑战（可靠性、成本控制、延迟优化、可观测性、安全合规），并说明为什么"PoC 能跑"不等于"生产能用"
2. 能用 **LangSmith**（`@traceable` 装饰器 + `wrap_openai`）为营销 Agent 配置端到端追踪，查看每步 LLM 调用的 token 消耗、延迟、工具调用链
3. 能用 **tiktoken** 精确统计 Agent 每次请求的输入/输出 token 数，结合模型定价计算单次成本和日均成本，识别成本瓶颈
4. 能设计**延迟监控**方案：为 Agent 各步骤（知识库检索 / LLM 推理 / 工具调用）分别计时，识别 P50/P95 瓶颈，用并行化/缓存/模型路由优化
5. 能实现**灾备降级策略**（多级 fallback：主模型 -> 备用模型 -> 缓存 -> 默认模板）和 **CI/CD 流水线**（pytest 回归测试 + 评估门禁 + GitHub Actions），保障生产可靠性

---

## 理论部分：精炼索引（详见独立教材）

> Day 5 的完整理论讲义见 [`../../AI原生化商业博士_独立教材_技能5_Agentic系统工程与落地.md` § Day 5](../../AI原生化商业博士_独立教材_技能5_Agentic系统工程与落地.md)（3.5.1–3.5.5 节，已包含 PoC 到生产挑战 / 可观测性设计 / 成本优化 / 灾备降级 / CI-CD）。本讲义不重复，仅做上机所需的关键回顾。

### 关键回顾 1：从 PoC 到生产的五大挑战

| 挑战 | PoC 阶段 | 生产环境要求 | 后果（不解决） |
|:----:|---------|-------------|---------------|
| 可靠性 | 偶尔出错可接受 | 99.9%+ 可用性 | 用户流失 |
| 成本控制 | 不在意 | 日均万次请求需可控 | 系统不可持续 |
| 延迟优化 | 等 30 秒可接受 | 5 秒内响应 | 用户体验差 |
| 可观测性 | 看日志 | 结构化监控/告警/诊断 | 出问题无法定位 |
| 安全合规 | 先跑起来 | 满足法规要求 | 法律风险 |

**核心洞察**：PoC 阶段的"能跑起来就行"思维是生产化的最大敌人。每个环节都需要容错、监控、降级机制。

### 关键回顾 2：三层可观测性设计

```
第一层：基础设施监控（Prometheus + Grafana）
  CPU/内存/网络/容器健康

第二层：应用性能监控 APM（LangSmith / Langfuse）
  LLM 调用延迟 P50/P95/P99 | Token 消耗 | 工具调用成功率 | 任务完成率

第三层：业务指标监控（自建 Dashboard + BI）
  用户采纳率 | 人工修改率 | 满意度评分 | 业务转化（CTR/转化率）
```

**LangSmith 的定位**：第二层 APM 的工程实现。通过 `@traceable` 装饰器自动记录 Agent 每次执行的完整调用链（LLM 调用输入输出、工具调用、延迟、token 消耗），存入云端 Dashboard 可视化查询。与 Day 3 的 deepeval（离线测试）互补：deepeval 防回归，LangSmith 防线上故障。

### 关键回顾 3：成本优化三大策略

| 策略 | 原理 | 工具 | 营销场景示例 |
|------|------|------|-------------|
| Token 管理 | 限制输出长度 + 简洁 prompt | `max_tokens` + prompt 设计 | 小红书文案限制 150 字 |
| 语义缓存 | 相似请求复用响应 | RedisSemanticCache | "给护肤品写文案" vs "给护肤品写个文案" |
| 模型路由 | 简单任务用小模型，复杂用大 | 自建路由函数 | 简单文案用 gpt-4o-mini，策略分析用 Claude Opus |

**成本计算基础**：用 **tiktoken** 精确计数 token（而非按字符估算），结合模型定价（$/百万 token）计算真实成本。

### 关键回顾 4：灾备降级与 CI/CD

**灾备降级**：当 LLM API 不可用时，系统需要优雅降级而非崩溃。多级 fallback 链：主模型 -> 备用模型 -> 缓存 -> 默认模板。

**CI/CD for Agent**：比传统软件更复杂，因为需要处理非确定性输出。核心是"评估门禁"：部署前自动运行测试集，检查任务完成率（>=90%）、幻觉率（<=5%）、安全违规率（=0%），不达标则阻止部署。

---

## 上机部分：用 LangSmith + tiktoken 生产化营销 Agent

> 📓 **配套笔记本**：[`starter.ipynb`](./starter.ipynb)（TODO 填空版，你来做）｜ [`solution.ipynb`](./solution.ipynb)（参考答案，gated，做完再看）
> 📊 **真实数据/库**：[`data/README.md`](./data/README.md)（langsmith + tiktoken 库 + 营销 Agent 运行日志样本）

### 为什么用真实库（langsmith + tiktoken）而非手写监控脚本

v4.0 的代码用"手写 `time.time()` 计时 + `print` 打日志"--手写监控只能做粗粒度计时和日志输出，无法做结构化 trace 追踪、无法精确计 token 成本、无法可视化调用链。v5.0 改用真实生产级工具：

- **LangSmith**（LangChain 出品，`pip install langsmith`）：`@traceable` 装饰器自动追踪函数调用链，记录每步的输入/输出/延迟/token；`Client` 查询 trace 数据做分析；`wrap_openai` 自动 instrument OpenAI 调用
- **tiktoken**（OpenAI 出品，`pip install tiktoken`）：BPE 分词器，精确计算文本的 token 数（3-6x 快于同类分词器），是成本计算的事实标准
- **concurrent.futures**（Python 标准库）：`ThreadPoolExecutor` 模拟并发请求，压测 Agent 在高负载下的表现

> **CI/CD 补充**：上机用 pytest 写 Agent 回归测试，模拟 GitHub Actions YAML 配置评估门禁。Day 3 的 deepeval 测试套件可直接嵌入此 CI 流水线。

### 营销映射（关键桥接）

本 Day 生产化一个"营销内容生成 Agent"（生成小红书种草文案/朋友圈广告），场景是把这个 Agent 从 PoC 推向生产：

| 生产化维度 | 营销场景 | 工具实现 |
|-----------|---------|---------|
| 可观测性 | 追踪 Agent 每步（搜索知识库 -> 生成文案）的 token 和延迟 | LangSmith `@traceable` |
| 成本控制 | 统计每次文案生成的 token 成本，日均万次请求的总成本 | tiktoken + 定价表 |
| 延迟优化 | 识别瓶颈步骤（知识库检索 vs LLM 推理），优化 P95 | `time.perf_counter` 分步计时 |
| 灾备降级 | 主模型（gpt-4o）故障时 fallback 到 gpt-4o-mini 或默认模板 | ResilientLLM 多级 fallback |
| CI/CD | 每次代码提交自动运行回归测试，防止 prompt 修改导致质量下降 | pytest + 评估门禁 |
| 压测 | 模拟 50 并发用户同时请求文案生成 | `ThreadPoolExecutor` |

### 上机任务（6 个 TODO，见 starter.ipynb）

1. **TODO1**：配置 LangSmith 追踪，用 `@traceable` 定义营销 Agent，运行并查看 trace 结构
2. **TODO2**：用 tiktoken 精确统计 token 数，结合模型定价计算单次请求成本和日均成本
3. **TODO3**：延迟监控--为 Agent 各步骤分步计时，识别瓶颈，计算 P50/P95
4. **TODO4**：灾备降级--实现 ResilientLLM 多级 fallback（主模型 -> 备用 -> 默认模板）
5. **TODO5**：CI/CD--用 pytest 写 Agent 回归测试，定义评估门禁，模拟 GitHub Actions YAML
6. **TODO6**：压测--用 ThreadPoolExecutor 模拟并发请求，观察延迟/成本/限流

---

## 2026 前沿补充：推理成本优化--vLLM / 投机解码 / MoE

> v5.0 新增前沿点。Agent 生产化的核心瓶颈是**推理成本**：每次请求调用 LLM 消耗 token，日均万次请求的成本可达数千美元。2026 年的趋势是用推理优化技术大幅降低单次推理成本。

**vLLM**（https://github.com/vllm-project/vllm）：高吞吐 LLM 推理引擎，通过 PagedAttention 优化 KV Cache 内存管理，支持连续批处理（continuous batching），在相同硬件上吞吐量可达原生 HuggingFace 的 14-24 倍。适用于自建推理服务替代商业 API，大幅降低成本。

**投机解码（Speculative Decoding）**：用一个小模型（draft model）快速生成候选 token，再用大模型并行验证。如果小模型猜对了，大模型只需一次前向传播即可接受多个 token，减少大模型的串行推理次数。延迟降低 2-3 倍，输出质量不变。

**MoE（Mixture of Experts）**：模型架构创新，将前馈网络拆分为多个"专家"子网络，每次推理只激活少数专家（如 Mixtral 8x7B 只激活 2/8 个专家）。总参数量大但单次推理计算量小，在相同质量下推理成本更低。DeepSeek-MoE、Mixtral 等模型已采用此架构。

**与 LangGraph 的协同**：LangGraph 的 checkpointer 机制支持 Agent 中断恢复--当 Agent 执行到第 3 步时服务重启，可从 checkpoint 恢复而非从头执行，节省重复 token 消耗。这是生产环境节省成本的另一关键机制。

> 🔗 深入阅读见 [`reading.md`](./reading.md) 的 vLLM / 投机解码 / MoE 条目。

---

## 与后续 Day 的衔接

- **Day 3**：Agent 评估与 Benchmarking--今天的 CI/CD 评估门禁直接复用 Day 3 的 deepeval 测试套件
- **Day 4**：安全防护与对抗--今天的安全合规检查（CI 门禁中的安全违规率=0%）是 Day 4 安全评估的生产化落地
- **Day 6**：IMRaD 论文写作--今天的生产化实践和监控数据是论文 Results 部分的素材来源

---

## 作业与评估

作业、5 分制量表、费曼演练、2 分钟话术、复盘自诊表--沿用独立教材 § Day 5 既有设计。本学习材料包不重复，仅新增上机交付物：

**新增交付物（v5.0）**：
- [ ] 完成的 `starter.ipynb`（6 个 TODO 全部填好，能跑通）
- [ ] 一段 300 字分析：你的营销 Agent 在压测中表现出什么瓶颈？（延迟飙升 / 成本超预算 / 限流？）根因是什么？
- [ ] （可选）设计一个 CI/CD 门禁规则（如"P95 延迟 > 10s 则阻止部署"），并说明如何用 LangSmith trace 数据自动判断

---

*本讲义由 v5.0 学习材料包升级生成。理论部分引用独立教材，上机部分用真实库（langsmith + tiktoken）+ TODO 脚手架。*
*最后更新：2026-07-24*

## 学习科学层 (v6.0)
本单元采用刻意练习(Ericsson)/间隔重复(FSRS-6,SM-2)/建构对齐(Biggs ILO↔TLA↔AT)/牛津tutorial LLM仿真(Socratic,Hattie四级反馈)。mastery 阈值与 Worked-Faded 示例见 practice.md 与 alignment.md。交叉练习(interleaving)促进迁移, 提取练习(retrieval practice)优于重读。

## 研究产出与产业链接层 (v7.0)
本单元产出可发表研究工件 (research.md: 研究问题+贡献声明+arXiv链接+IMRaD大纲+NeurIPS可复现清单+research-to-practice翻译) 与产业链接 (industry.md: >=3真实企业+部署场景+Imperial咨询项目+HBS教学案例+客座讲座+实习指针)。研究产出遵循IMRaD/DSR(Hevner)/OSF预注册/FAIR/可复现研究标准; 产业链接遵循Imperial MSc BA咨询项目(Burberry/Expedia/J&J)/HBS案例法/MIT Sloan行动学习模式。详见 research.md 与 industry.md。
