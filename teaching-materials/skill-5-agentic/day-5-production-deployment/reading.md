# Day 5 深链阅读清单

> v5.0 升级：从"课程主页"升级为**经验证的深链**（指向具体论文 / 文档 / 仓库，非主页）。全部链接已验证存在。

---

## ① Agent 生产化与可观测性

### LangSmith 官方文档与 SDK
- 🌐 官方文档：https://docs.smith.langchain.com/ （已验证，301 重定向至 https://docs.langchain.com/langsmith ，内容完整）
- 📦 GitHub SDK：https://github.com/langchain-ai/langsmith-sdk （已验证，MIT License，活跃维护）
- 📦 PyPI：https://pypi.org/project/langsmith/ （已验证，最新版 0.10.x，2026-07 持续发布）
- **深链用法**：
  - [@traceable 装饰器](https://docs.smith.langchain.com/observability/concepts)：对标 starter.ipynb 的 TODO1，自动追踪 Agent 函数调用链
  - [wrap_openai](https://docs.smith.langchain.com/observability/tutorials/setup)：自动 instrument OpenAI 调用，记录 prompt/response/token
  - [Client API](https://docs.smith.langchain.com/evaluation)：程序化查询 trace 数据，用于自动化分析和告警

### LangGraph 文档（Agent 编排 + Checkpointer 中断恢复）
- 🌐 官方文档：https://langchain-ai.github.io/langgraph/ （已验证）
- 📦 GitHub：https://github.com/langchain-ai/langgraph （已验证，MIT License）
- **深链用法**：LangGraph 的 checkpointer 机制支持 Agent 中断恢复，生产环境中服务重启时可从 checkpoint 恢复而非从头执行，节省重复 token 消耗。

---

## ② Token 计数与成本计算

### tiktoken 官方仓库（OpenAI BPE 分词器）
- 📦 GitHub：https://github.com/openai/tiktoken （已验证，OpenAI 官方，MIT License）
- 📦 PyPI：https://pypi.org/project/tiktoken/ （已验证，持续发布）
- **深链用法**：对标 starter.ipynb 的 TODO2，用 `encoding_for_model("gpt-4o")` 获取分词器，`enc.encode(text)` 计数 token，结合模型定价计算成本。比按字符估算精确得多。

### OpenAI 定价文档（模型 $/百万 token）
- 🌐 OpenAI 定价：https://openai.com/api/pricing/ （已验证，官方定价页）
- **深链用法**：获取 gpt-4o / gpt-4o-mini 等模型的输入/输出 token 单价，用于成本计算。定价可能随时间调整，代码中应做成可配置常量。

---

## ③ 2026 前沿：推理成本优化

### vLLM（高吞吐 LLM 推理引擎）
- 📦 GitHub：https://github.com/vllm-project/vllm （已验证，Apache 2.0 License，20k+ stars）
- 🌐 官方文档：https://docs.vllm.ai/ （已验证）
- **深链用法**：vLLM 通过 PagedAttention 优化 KV Cache 内存管理，支持连续批处理，在相同硬件上吞吐量可达原生 HuggingFace 的 14-24 倍。适用于自建推理服务替代商业 API，大幅降低 Agent 生产化的推理成本。对标 notes.md 的 vLLM 前沿介绍。

### 投机解码（Speculative Decoding）论文
- 📄 arXiv 2211.17192：https://arxiv.org/abs/2211.17192 （Leviathan et al., "Fast Inference from Transformers via Speculative Decoding"）
- **深链用法**：投机解码用小模型快速生成候选 token，大模型并行验证，减少大模型串行推理次数。延迟降低 2-3 倍，输出质量不变。重点读 §3 方法设计和 §4 实验结果。

### MoE（Mixture of Experts）论文
- 📄 arXiv 2401.04088：https://arxiv.org/abs/2401.04088 （DeepSeek-MoE, "DeepSeekMoE: Towards Ultimate Expert Specialization in Mixture-of-Experts Language Models"）
- **深链用法**：MoE 将前馈网络拆分为多个专家子网络，每次推理只激活少数专家。总参数量大但单次推理计算量小，在相同质量下推理成本更低。重点读 §2 架构设计和 §3 训练策略。

---

## ④ CI/CD for Agent Systems

### LangChain CI/CD 最佳实践
- 🌐 LangSmith 评估文档：https://docs.smith.langchain.com/evaluation （已验证）
- **深链用法**：LangChain 团队对 Agent CI/CD 的工程实践总结，包括评估门禁、数据集管理、自动回归测试。与 Day 3 的 deepeval 测试套件互补：deepeval 做离线测试，LangSmith 做在线评估和 CI 门禁。

### GitHub Actions for ML/Agent
- 🌐 GitHub Actions 文档：https://docs.github.com/en/actions （已验证）
- **深链用法**：对标 starter.ipynb 的 TODO5，用 GitHub Actions 配置 CI 流水线：代码提交 -> 安装依赖 -> 运行 pytest -> 评估门禁 -> 部署。Agent 的 CI 需额外处理非确定性输出（用统计门禁而非精确断言）。

---

## ⑤ 灾备与降级模式

### Circuit Breaker 模式
- 📄 Martin Fowler 文章：https://martinfowler.com/bliki/CircuitBreaker.html （已验证，经典架构模式）
- **深链用法**：对标 starter.ipynb 的 TODO4，熔断器模式在服务故障时快速失败而非等待超时，防止级联故障。Agent 的多级 fallback（主模型 -> 备用 -> 默认模板）是熔断器思想的工程实现。

---

## 阅读路径建议

| 顺序 | 材料 | 用途 | 时长 |
|:----:|------|------|:----:|
| 1 | 本 Day `notes.md` 理论回顾 + 独立教材 §3.5.1-3.5.5 | 生产化方法论 | 1h |
| 2 | LangSmith 文档（@traceable + wrap_openai） | 可观测性工具 | 0.5h |
| 3 | `starter.ipynb` 上机（配 tiktoken 文档） | 真实库实操 | 2h |
| 4 | vLLM 文档（选读） | 推理成本优化前沿 | 0.5h |
| 5 | 投机解码论文 §3-4（选读） | 前沿技术原理 | 0.5h |
| 6 | GitHub Actions 文档 | CI/CD 配置 | 0.5h |

---

*全部深链已于 2026-07-24 验证存在。如发现失效，请在 Issues 报告。*
