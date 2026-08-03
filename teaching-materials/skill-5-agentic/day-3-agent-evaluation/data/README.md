# Day 3 真实数据与库说明

> v5.0 核心升级：用**真实评估库**（deepeval）+ **教学合成（synthetic）/人工策展（curated）的 Agent 轨迹样例**替代手写评估脚本。手写 if-else 只能做规则匹配，deepeval 能做 LLM-as-a-judge 语义评估。

---

## 主评估库：deepeval（已验证，可运行）

**这是什么**：deepeval 是 confident-ai 维护的开源 LLM 评估框架（17k★），提供测试用例定义（LLMTestCase）、内置指标（GEval/FaithfulnessMetric/AnswerRelevancyMetric）、自定义指标（BaseMetric）、批量运行（evaluate）和 CI 集成（`deepeval test run`）。它是 LLM-as-a-judge 范式的**可运行工程实现**。

**为什么用它**：
- **GEval**：给一段 criteria 描述，LLM 自动打分+给理由--可评估"内容质量""品牌调性"等语义维度（手写规则做不到）
- **FaithfulnessMetric**：自动检测幻觉（对比 actual_output 与 retrieval_context，逐条声明核查是否忠于知识库）
- **BaseMetric**：继承后实现 measure 方法，可自定义轨迹评估指标（如工具调用正确性）
- **assert_test / evaluate**：pytest 风格断言 + 批量运行，可纳入 CI/CD

**安装方式**：

```bash
pip install deepeval
# deepeval 默认使用 OpenAI 作为 judge 模型，需设置：
# export OPENAI_API_KEY=<your-openai-api-key>
# 也可指定其他模型（如本地 Ollama），见 deepeval 文档
```

**核心 API 速查**：

| 组件 | 导入 | 用途 |
|------|------|------|
| LLMTestCase | `from deepeval.test_case import LLMTestCase` | 定义测试用例（input/actual_output/expected_output/retrieval_context） |
| GEval | `from deepeval.metrics import GEval` | LLM-as-a-judge 自动评分（criteria 模式） |
| FaithfulnessMetric | `from deepeval.metrics import FaithfulnessMetric` | 幻觉检测（忠于知识库） |
| BaseMetric | `from deepeval.metrics import BaseMetric` | 自定义指标基类 |
| assert_test | `from deepeval import assert_test` | 单用例断言（pytest 风格） |
| evaluate | `from deepeval import evaluate` | 批量运行测试套件 |

**来源与验证**：
- deepeval GitHub：https://github.com/confident-ai/deepeval （17k★，MIT License，已验证存在，2026-07 活跃维护）
- deepeval 官方文档：https://docs.confident-ai.com/ （已验证，301 重定向至 https://deepeval.com/docs/ ，内容完整）
- PyPI：https://pypi.org/project/deepeval/ （已验证，持续发布）

---

## 数据真实性分级与泄漏控制

**证据复核日期：2026-08-03**

本 Day 把“评估库是否真实”和“测试轨迹是否来自生产”分开标注：

| 等级 | 定义 | 本单元状态 | 可用于 |
|---|---|---|---|
| 教学合成（synthetic） | 为覆盖好/坏/混合错误模式而人工构造的 brief、输出、知识库片段和轨迹 | 3 条上机样例属于此等级 | 教学、API 熟悉、离线 smoke test |
| 人工策展（curated） | 来自公开 demo、课堂项目或历史日志，经人工脱敏、去重、标注 expected_trace 后进入黄金集 | 本单元要求学生 Final 至少提交 10 条 curated case | judge 校准、回归测试 |
| 生产记录（recorded） | 从真实 Agent 线上 trace 采集，保留时间戳、模型版本、工具输入输出、token、成本、延迟，经隐私审查 | 本仓库不内置 recorded 数据 | 生产监控、上线门禁、A/B 后分析 |

泄漏控制：

- 训练集泄漏：生产记录（recorded）进入评估集前，必须检查 brief、参考文案、知识库片段是否曾用于 prompt 示例、微调数据或公开教程；已泄漏样例只能用于教学，不能进入黄金集。
- 答案泄漏：`solution.ipynb` 的 expected output、expected trace 和人工标签不得复制到 starter 答案区；学生提交的 curated case 需另附来源与脱敏说明。
- 隐私泄漏：recorded trace 不得含真实客户名、手机号、订单号、精准投放人群包、广告账户 ID；必要时只保留哈希化 trace id。
- 评审泄漏：LLM-as-a-judge 的 criteria 不得包含“用例1应通过、用例2应失败”等标签信息；人工黄金集标签单独保存。

---

## 评估对象：营销 Agent 轨迹测试用例

测试用例定义在 `starter.ipynb` TODO1 中，包含 3 条教学合成（synthetic）且由人工策展（curated）的营销场景轨迹，用于覆盖好/坏/混合三种错误模式：

| 用例 | 场景 | 轨迹质量 | 评估重点 |
|------|------|---------|---------|
| 用例1 | 小红书种草文案（烟酰胺精华液） | 好（工具正确、内容忠于知识库） | 端到端质量 + 幻觉检测应通过 |
| 用例2 | 朋友圈广告（新款口红） | 差（工具选错、虚构成分） | 工具调用准确率 + 幻觉率应报警 |
| 用例3 | 小红书种草文案（防晒霜） | 混合（工具正确但内容略有偏差） | 轨迹评估 vs 端到端评估的差异 |

每条测试用例包含：
- `input`：营销 Brief（产品+目标人群+渠道）
- `actual_output`：合成 Agent 输出内容；若替换为生产记录（recorded），必须标注 trace id、采集时间、模型版本和脱敏状态
- `expected_output`：人工专家写的参考文案
- `retrieval_context`：知识库检索到的产品资料（用于幻觉检测）
- `trajectory`：Agent 的工具调用轨迹（用于轨迹评估）
- `expected_trace`：人工黄金集标注的期望工具顺序、必填参数和冗余调用规则（用于防止直接信任 `correct=True`）

> 💡 **数据来源说明**：这些测试用例是 synthetic/curated 教学样例，模拟技能5 Day 2 营销 Agent 的典型输出。真实项目中应收集自己的 Agent 生产记录（recorded）或课堂项目人工策展（curated）样例，再用 deepeval 的 `EvaluationDataset` 从 JSON/CSV 批量导入。

---

## 可观测性补充：LangSmith / Langfuse

Agent 评估除了离线测试套件（deepeval），还需要**在线可观测性**（trace/eval/score）：

- **LangSmith**（LangChain 出品）：与 LangGraph/LangChain 深度集成的可观测性平台，自动记录 Agent 执行的完整调用链（每个 LLM 调用、工具调用的输入输出、延迟、token 消耗）。GitHub：https://github.com/langchain-ai/langgraph （已验证）
- **Langfuse**（开源）：开源 LLM 应用可观测性平台，提供 trace/eval/score 三大功能，支持 LLM-as-Judge 自动评估。详见独立教材 § 3.3.5。

> 本 Day 上机聚焦 deepeval（离线测试套件），LangSmith/Langfuse 属于在线可观测性，作为延伸阅读。

---

## 为什么不用手写评估脚本（v4.0 做法）

| 维度 | 手写 if-else（v4.0） | deepeval（v5.0） |
|------|---------------------|------------------|
| 规则匹配 | ✅ 字数/关键词/格式 | ✅ 同 |
| 语义评估 | ❌ 做不到 | ✅ GEval LLM-as-a-judge |
| 幻觉检测 | ❌ 做不到 | ✅ FaithfulnessMetric |
| 轨迹评估 | ❌ 需手写大量逻辑 | ✅ BaseMetric 自定义 |
| CI 集成 | ❌ 需自己搭 | ✅ `deepeval test run` |
| 可复现 | ❌ 评分主观 | ✅ 结构化 score + reason |

**真实即严谨**--用工程化框架替代手写脚本，是 v5.0 的哲学增量。
