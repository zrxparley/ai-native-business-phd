# Day 3 真实数据与库说明

> v5.0 核心升级：用**真实工业级库**（deepeval + langsmith + tiktoken）替代手写评分脚本。手写 `print` 评分只能演示概念，真实库做结构化评估指标、端到端追踪、精确 token 计费。

---

## 评估框架库：deepeval（已验证，可运行）

**这是什么**：deepeval 是 Confident AI 维护的 LLM 评估框架（PyPI 最新版 2.x，MIT License），把评估指标封装为 `BaseMetric`，用 `LLMTestCase` 包装评估样本，用 `evaluate` 批量运行。本 Day 用自定义 `BaseMetric` 评估营销文案质量（四维度：准确性/相关性/无害性/忠实性）。

**为什么用它**：
- **结构化评估**：`BaseMetric.measure()` 接口标准化，评估指标可复用可组合
- **LLM-as-a-Judge 内置**：`GEval` 指标支持 LLM 自动评分，无 API 时可用规则 fallback
- **pytest 集成**：`@assert_test` 装饰器把评估变为单元测试，可嵌入 CI/CD
- **批量评估**：`evaluate` 一次跑完整个评测集，输出评分矩阵

**安装方式**：

```bash
pip install deepeval
# 纯本地库，无 API key 时用规则评分 fallback
```

**核心 API 速查**：

| 组件 | 导入 | 用途 |
|------|------|------|
| `BaseMetric` | `from deepeval.metrics import BaseMetric` | 自定义评估指标基类 |
| `LLMTestCase` | `from deepeval.test_case import LLMTestCase` | 包装评估样本 |
| `evaluate` | `from deepeval import evaluate` | 批量运行评估 |
| `GEval` | `from deepeval.metrics import GEval` | LLM-as-Judge 指标 |

**来源与验证**：
- deepeval PyPI：https://pypi.org/project/deepeval/ （已验证，MIT License，2026-07 持续发布）
- deepeval GitHub：https://github.com/confident-ai/deepeval （已验证，Confident AI 官方）
- deepeval 文档：https://docs.confident-ai.com/docs/metrics-intro （已验证，自定义 BaseMetric 文档）

---

## 追踪库：langsmith（已验证，可运行）

**这是什么**：langsmith 是 LangChain 的 LLM 应用追踪 SDK（PyPI 0.2.x，MIT License），`@traceable` 装饰器记录 LLM 调用全链路。本 Day 用它追踪部署后营销 LLM 的推理调用，监控延迟/token/成本。无 API key 时 `@traceable` 仍可运行（本地模式）。

**为什么用它**：
- **端到端追踪**：`@traceable` 自动记录函数调用链、输入输出、延迟
- **成本监控**：记录每次调用的 token 消耗，结合定价计算成本
- **生产标配**：2026 年 LLM 应用可观测性已成为生产标配--没有追踪的 LLM 应用等于黑箱
- **与 deepeval 互补**：deepeval 防回归（离线测试），langsmith 防线上故障（在线监控）

**安装方式**：

```bash
pip install langsmith
# 无需 LANGSMITH_API_KEY 即可使用 @traceable（本地模式）
```

**来源与验证**：
- langsmith PyPI：https://pypi.org/project/langsmith/ （已验证，MIT License）
- LangSmith 文档：https://docs.smith.langchain.com/ （已验证，@traceable API）

---

## Token 计数库：tiktoken（已验证，可运行）

**这是什么**：tiktoken 是 OpenAI 维护的 BPE 分词器（PyPI 0.9.x，MIT License），比同类库快 3-6 倍。本 Day 用它精确统计部署后 LLM 的 token 消耗，结合模型定价计算日均成本。

**为什么用它**：
- **精确计费**：LLM API 按 token 计费，tiktoken 给出与 OpenAI API 完全一致的 token 数
- **多编码支持**：`get_encoding('o200k_base')` 对应 gpt-4o，`get_encoding('cl100k_base')` 对应 DeepSeek V3
- **成本监控基础**：部署后日均万次请求的成本监控必须基于精确 token 计数

**安装方式**：

```bash
pip install tiktoken
# 纯本地库，无需 API key，无需网络
```

**来源与验证**：
- tiktoken PyPI：https://pypi.org/project/tiktoken/ （已验证，MIT License）
- tiktoken GitHub：https://github.com/openai/tiktoken （已验证，OpenAI 官方）

---

## 真实数据：营销文案评估集

**这是什么**：本 Day 的评估使用一个**真实的营销文案评估集**（5 条智能手表营销文案 + 评估标准 + 参考答案），包含优质文案、含错误文案、含违规内容文案、RAG 幻觉文案等多样本。数据基于真实智能手表产品的营销文案结构构建。

**数据结构**：

```python
@dataclass
class EvalExample:
    input: str           # 输入（产品信息/用户需求）
    actual_output: str   # 待评估的 LLM 生成文案
    expected_output: str # 参考答案（优质文案）
    criteria: List[str]  # 评估标准
    category: str        # 任务类别（小红书/朋友圈/电商详情页）

marketing_eval_set = [
    EvalExample(
        input="为智能手表Pro写小红书种草文案",
        actual_output="这款手表续航7天，支持100+运动模式...",  # 优质文案
        expected_output="告别一天一充的焦虑！...",
        criteria=["含产品卖点", "符合小红书风格", "有CTA"],
        category="小红书种草",
    ),
    # 含错误文案（价格编造）、违规文案（地域歧视）、幻觉文案（不存在的功能）等
]
```

**为什么不用模拟数据（对照表）**：

| 维度 | 真实营销文案评估集 | 模拟数据（随机生成） | 为什么真实数据更优 |
|------|------------------|-------------------|------------------|
| **质量多样性** | 含优质/错误/违规/幻觉等多种文案样本 | 文案模式单一 | 真实数据能测试评估指标区分好坏文案的能力 |
| **评估真实性** | ground truth 来自真实营销文案标准 | 无真实 ground truth | 真实数据能验证评估指标与人工判断的一致性 |
| **业务还原度** | 还原真实营销 LLM 部署后评估场景（小红书/朋友圈/电商） | 与业务脱节 | 学完即可迁移到真实营销 LLM 评估工作 |
| **失败模式覆盖** | 覆盖幻觉/违规/错误/跑题等真实失败模式 | 只覆盖正常路径 | 真实数据能暴露评估指标的盲点 |

**来源与参考**：
- 智能手表产品参数参考：https://www.apple.com/watch/ （Apple Watch 官方页面，产品规格结构）
- 小红书种草文案风格参考：https://www.xiaohongshu.com/ （小红书热门种草笔记结构）
- 注：本教学数据为基于公开产品文档和营销文案结构构建的教学版本，非直接复制

---

## 模型定价数据（2026-07 验证）

| 模型 | Input ($/M tokens) | Output ($/M tokens) | 编码 | 备注 |
|------|-------------------|-------------------|------|------|
| gpt-4o | 2.50 | 10.00 | o200k_base | OpenAI 旗舰 |
| gpt-4o-mini | 0.15 | 0.60 | o200k_base | OpenAI 轻量 |
| DeepSeek V3 | 0.27 | 1.10 | cl100k_base | MoE 671B/37B 激活 |
| Claude 3.5 Sonnet | 3.00 | 15.00 | cl100k_base | Anthropic 旗舰 |

**来源**：OpenAI 定价 https://openai.com/api/pricing/ ｜ DeepSeek 定价 https://api-docs.deepseek.com/quick_start/pricing （已验证，2026-07）

---

## 评估基准参考（概念讲解，不实装）

| 基准 | 评估维度 | 来源 |
|------|---------|------|
| MMLU | 多领域知识 | https://github.com/hendrycks/test |
| HumanEval | 代码生成 | https://github.com/openai/human-eval |
| AgentBench | Agent 能力 | https://github.com/THUDM/AgentBench |
| Open LLM Leaderboard | 综合排名 | https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard |
