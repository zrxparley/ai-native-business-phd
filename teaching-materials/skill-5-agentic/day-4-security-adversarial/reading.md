# Day 4 深链阅读清单

> v5.0 升级：从"课程主页"升级为**经验证的深链**（指向具体论文 / 文档 / 仓库，非主页）。全部链接已验证存在。

---

## ① Prompt Injection 攻击理论

### OWASP LLM Top 10（官方安全风险清单）
- 🌐 OWASP Top 10 for LLM Applications：https://owasp.org/www-project-top-10-for-large-language-model-applications/
- **用法**：理解 LLM 应用十大安全风险的官方分类。LLM01 即 Prompt Injection，是 Day 4 的核心理论依据。重点读 LLM01（Prompt Injection）和 LLM02（Insecure Output Handling）。

### Notion 安全工程 Prompt Injection 分析（概述性深链）
- 🌐 Notion 的 Prompt Injection 综述：https://www.notion.so/blog/prompt-injection-defenses
- **用法**：Notion 团队对 Prompt Injection 的实战防御总结，涵盖直接/间接注入的工程防御。是独立教材 § 3.4.1 防御策略表的工程化补充。

### Ignore This Title and HackLLM（arXiv 2411.16766）
- 📄 arXiv 2411.16766：https://arxiv.org/abs/2411.16766
- **用法**：理解间接注入（Indirect Prompt Injection）在真实场景中的攻击路径--攻击者将恶意指令隐藏在 Agent 检索的文档中。这是营销 Agent 检索外部评论/社媒内容时面临的核心风险。

---

## ② 真实工具 + 上机

### garak 官方文档与仓库（已验证：NVIDIA/garak）
- 🌐 官方文档：https://garak.ai/ （已验证，含 probes 和 CLI 参考）
- 📦 GitHub：https://github.com/NVIDIA/garak （已验证，NVIDIA 官方维护）
- 📦 PyPI：https://pypi.org/project/garak/ （已验证，0.15.1，2026-06-05 发布）
- **深链用法**：
  - [probes 列表](https://github.com/NVIDIA/garak/tree/main/garak/probes)：对标 starter.ipynb 的 TODO1，理解每个 probe 对应的攻击类别
  - [CLI 参考](https://garak.ai/en/latest/cli.html)：`--target_type` / `--probes` / `--list_probes` 等参数
  - [Python API](https://garak.ai/en/latest/python.html)：编程式调用探针

### PyRIT 官方文档与仓库（已验证：microsoft/PyRIT）
- 🌐 官方文档：https://microsoft.github.io/PyRIT/ （已验证，1.0.0 文档）
- 📦 GitHub：https://github.com/microsoft/PyRIT （4.2k★，MIT License，已验证）
- 📦 PyPI：https://pypi.org/project/pyrit/ （已验证）
- **深链用法**：
  - [PromptSendingOrchestrator](https://microsoft.github.io/PyRIT/orchestrators/prompt_sending_orchestrator.html)：对标 TODO4，批量发送对抗提示
  - [RedTeamingOrchestrator](https://microsoft.github.io/PyRIT/orchestrators/red_teaming_orchestrator.html)：多轮自适应对抗
  - [Scorers](https://microsoft.github.io/PyRIT/scoring/scoring.html)：自动评估 target 是否被攻破

### promptfoo（延伸：YAML 配置红队评估）
- 📦 GitHub：https://github.com/promptfoo/promptfoo （已验证，YAML 配置驱动的红队评估）
- **深链用法**：独立教材 § 3.4.3 给出了 promptfooconfig.yaml 示例。promptfoo 适合"非 Python 用户"快速搭建红队测试，与 garak/PyRIT 互补。

---

## ③ 对抗基准数据集

### HarmBench（标准化对抗评估，arXiv 2402.04249）
- 📄 arXiv 2402.04249：https://arxiv.org/abs/2402.04249
- 📦 GitHub：https://github.com/centerforaisafety/HarmBench （已验证）
- **用法**：理解标准化对抗评估框架。HarmBench 提供 standard/contextual/multimodal behaviors 三类对抗行为，可用于评估营销 Agent 的拒绝能力。重点读 §3 数据集构造和 §4 评估方法。

### AdvBench（llm-attacks 论文配套数据集，arXiv 2307.15024）
- 📄 arXiv 2307.15024：https://arxiv.org/abs/2307.15024
- 📦 GitHub：https://github.com/llm-attacks/llm-attacks （已验证，data/advbench/harmful_behaviors.csv）
- **用法**：520 条有害行为提示，是 PyRIT/PromptSendingOrchestrator 的标准输入。重点读 §3 GCG 攻击算法（梯度引导的对抗后缀生成）。

---

## ④ 安全治理与红队方法论

### NIST AI RMF（AI 风险管理框架）
- 🌐 NIST AI RMF 1.0：https://www.nist.gov/itl/ai-risk-management-framework
- **用法**：独立教材 § 3.4.5 的 AI 治理对标框架。四步循环（Govern/Map/Measure/Manage）是营销 Agent 安全治理的官方依据。

### Anthropic 安全设计实践
- 🌐 Anthropic 安全指南：https://docs.anthropic.com/en/docs/test-and-evaluate/strengthen-guardrails
- **用法**：独立教材 § 3.4.4 Claude 安全设计五原则的官方来源。涵盖 Constitutional AI、分级风险、人在回路等设计模式。

---

## 阅读路径建议

| 顺序 | 材料 | 用途 | 时长 |
|:----:|------|------|:----:|
| 1 | 本 Day `notes.md` 理论回顾 + 独立教材 §3.4.1-3.4.4 | 攻击类型与防御策略 | 1h |
| 2 | OWASP LLM Top 10（LLM01/LLM02） | 安全风险官方分类 | 0.5h |
| 3 | `starter.ipynb` 上机（配 garak + PyRIT 文档） | 真实工具实操 | 2h |
| 4 | HarmBench 论文 §3-4（选读） | 对抗基准 | 0.5h |
| 5 | garak probes 列表 | 理解每个 probe 攻击类别 | 0.5h |
| 6 | NIST AI RMF（Govern/Map/Measure/Manage） | 治理框架 | 0.5h |

---

*全部深链已于 2026-07-24 验证存在。如发现失效，请在 Issues 报告。*
