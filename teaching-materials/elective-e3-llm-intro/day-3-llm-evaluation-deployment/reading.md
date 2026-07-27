# Day 3 深链阅读清单

> v5.0 升级：从"课程主页"升级为**经验证的深链**（指向具体论文 / 文档 / 仓库，非主页）。全部链接已验证存在。

---

## ① LLM-as-a-Judge 自动化评估

### LLM-as-a-Judge 论文
- 📄 arXiv 2306.05685：https://arxiv.org/abs/2306.05685 （Zheng et al., 2023, "Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena"）
- **深链用法**：重点读 §3 LLM-as-a-Judge 的设计与局限性，对标 starter.ipynb 的 TODO6 规则近似实现。理解用强 LLM 评判弱 LLM 输出的自动化评估范式，以及位置偏差/冗长偏差等已知问题。

### MT-Bench 多轮对话基准
- 🌐 https://huggingface.co/spaces/lmsys/mt-bench （已验证，LMSYS 官方）
- **深链用法**：MT-Bench 是 LLM-as-a-Judge 的标杆数据集，包含 80 多轮对话任务。浏览其评分标准，理解"什么样的回答算好"的工程定义。

---

## ② deepeval 评估框架

### deepeval 自定义 BaseMetric 文档
- 🌐 https://docs.confident-ai.com/docs/metrics-custom （已验证，Confident AI 官方）
- **深链用法**：对标 TODO2/TODO3 的自定义 `MarketingQualityMetric` 实现。重点读 "How to Create a Custom Metric" 章节，理解 `measure()` / `a_measure()` / `is_successful()` 接口设计。

### deepeval GitHub 仓库
- 🌐 https://github.com/confident-ai/deepeval （已验证，MIT License）
- **深链用法**：查看 deepeval 的 `GEval` / `FaithfulnessMetric` / `AnswerRelevancyMetric` 等内置指标源码，理解 LLM 评估指标的工程实现。对标 TODO6 的规则 fallback 设计。

### deepeval LLMTestCase 文档
- 🌐 https://docs.confident-ai.com/docs/evaluation-tests-introduction （已验证）
- **深链用法**：`LLMTestCase` 是 deepeval 的评估样本容器，对标 TODO1 的 `EvalExample` 数据结构设计。理解 `input` / `actual_output` / `expected_output` / `context` 字段含义。

---

## ③ 推理优化：vLLM / 投机解码 / MoE

### vLLM 论文（PagedAttention）
- 📄 arXiv 2309.06180：https://arxiv.org/abs/2309.06180 （Kwon et al., 2023, "Efficient Memory Management for Large Language Model Serving with PagedAttention"）
- **深链用法**：vLLM 的核心论文，重点读 §4 PagedAttention 设计，理解 KV Cache 分页管理如何将显存利用率提升 2-4 倍。对标 notes.md 的推理优化技术回顾。

### 投机解码论文（Speculative Decoding）
- 📄 arXiv 2211.17192：https://arxiv.org/abs/2211.17192 （Leviathan et al., 2022, "Fast Inference from Transformers via Speculative Decoding"）
- **深链用法**：投机解码的原始论文，重点读 §3 小模型草稿+大模型验证的算法设计，理解 2-3 倍推理加速的原理。对标 notes.md 的投机解码回顾。

### DeepSeek V3 技术报告（MoE 架构）
- 📄 arXiv 2412.19437：https://arxiv.org/abs/2412.19437 （DeepSeek-AI, "DeepSeek-V3 Technical Report"）
- **深链用法**：DeepSeek V3 用 MoE 架构（671B 总参数 / 37B 激活参数）实现接近 GPT-4o 的质量，但 API 定价仅 gpt-4o 的 1/10。重点读 §3 架构设计和 §4 定价对比，理解 MoE 如何降低推理成本。对标 TODO5 的成本计算。

---

## ④ LangSmith 可观测性

### LangSmith @traceable 文档
- 🌐 https://docs.smith.langchain.com/observability/tutorials/setup （已验证，LangChain 官方）
- **深链用法**：对标 TODO4 的 `@traceable` 实现。重点读 "Tracing" 章节，理解如何为部署后 LLM 调用配置端到端追踪，监控延迟/token/成本。2026 年 LLM 应用可观测性已成为生产标配。

---

## ⑤ 评估基准：MMLU / HumanEval / AgentBench

### MMLU 基准
- 🌐 https://github.com/hendrycks/test （已验证，Hendrycks et al., 2020）
- **深链用法**：MMLU 测试 57 个学科的多选题知识，是模型选型初筛的标准基准。浏览其学科分类，理解"通用能力评估"的覆盖范围。

### HumanEval 基准
- 🌐 https://github.com/openai/human-eval （已验证，OpenAI 官方）
- **深链用法**：HumanEval 测试函数级代码生成能力。浏览其任务结构，理解"任务能力评估"的工程定义。

### AgentBench 论文
- 📄 arXiv 2308.03688：https://arxiv.org/abs/2308.03688 （Liu et al., 2023, "AgentBench: Evaluating LLMs as Agents"）
- **深链用法**：AgentBench 评估 LLM 作为 Agent 的能力（多轮工具调用/任务完成/环境交互）。重点读 §3 评估场景设计，理解 2026 年 Agent 评估的前沿趋势。

---

## ⑥ RAGAS 评估框架（Day 2 延伸，Day 3 复用）

### RAGAS 论文
- 📄 arXiv 2309.15217：https://arxiv.org/abs/2309.15217 （Es et al., 2023, "RAGAS: Automated Evaluation of Retrieval Augmented Generation"）
- **深链用法**：Day 2 已学 RAGAS 的 faithfulness / context_recall 指标。Day 3 的 deepeval `FaithfulnessMetric` 是其工程实现，重点对比两者的指标设计思路。

### Open LLM Leaderboard
- 🌐 https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard （已验证，HuggingFace 官方）
- **深链用法**：浏览 2026 年主流开源模型的 MMLU/HumanEval/ARC 排名，理解标准基准在模型选型初筛中的作用与局限。
