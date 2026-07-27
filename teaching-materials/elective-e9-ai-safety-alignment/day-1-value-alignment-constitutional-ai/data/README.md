# Day 1 真实数据与库说明

> v5.0 核心升级：用**真实对齐评估库**（deepeval + garak）+ **真实对齐测试用例集**（HHH原则标准案例 + 营销场景对齐案例）替代手写对齐检查脚本。手写if-else只能做关键词匹配（"最""第一""治愈"），deepeval+garak能做语义层面的对齐评估和系统化的价值偏差扫描。

---

## 主评估库：deepeval（已验证，可运行）

**这是什么**：deepeval 是 confident-ai 维护的开源 LLM 评估框架（17k★），提供测试用例定义（LLMTestCase）、内置指标（GEval/FaithfulnessMetric/AnswerRelevancyMetric）、自定义指标（BaseMetric）、批量运行（evaluate）和 CI 集成（`deepeval test run`）。它是 LLM-as-a-judge 范式的**可运行工程实现**。

**为什么用它做对齐评估**：
- **自定义BaseMetric**：继承后实现measure方法，可按HHH原则（Helpful/Harmless/Honest）自定义对齐评估指标--这是本Day的核心用法
- **GEval**：LLM-as-a-judge 自动评分（给一段criteria，LLM自动打分+给理由），可评估"是否违反广告法""是否夸大宣传"等语义维度
- **FaithfulnessMetric**：自动检测幻觉（对比actual_output与retrieval_context），可用于检测"虚构成分/功效"的对齐失败
- **assert_test / evaluate**：pytest风格断言 + 批量运行，可纳入CI/CD--每次prompt修改后自动检测对齐回归

**安装方式**：

```bash
pip install deepeval
# deepeval 默认使用 OpenAI 作为 judge 模型，需设置：
# export OPENAI_API_KEY=sk-...
# 也可指定其他模型（如 Anthropic / 本地 Ollama），见 deepeval 文档
# 本Day的自定义BaseMetric在无API key时可退化为规则评分（fallback模式）
```

**核心 API 速查**：

| 组件 | 导入 | 用途 |
|------|------|------|
| LLMTestCase | `from deepeval.test_case import LLMTestCase` | 定义对齐测试用例（input/actual_output/retrieval_context） |
| BaseMetric | `from deepeval.metrics import BaseMetric` | 自定义HHH对齐指标基类（本Day核心） |
| GEval | `from deepeval.metrics import GEval` | LLM-as-a-judge 自动评分（Constitutional AI原则评审） |
| FaithfulnessMetric | `from deepeval.metrics import FaithfulnessMetric` | 诚实性检测（忠于知识库=不虚构） |
| assert_test | `from deepeval import assert_test` | 单用例断言（pytest风格） |
| evaluate | `from deepeval import evaluate` | 批量运行对齐测试套件 |

**来源与验证**：
- deepeval GitHub：https://github.com/confident-ai/deepeval （17k★，MIT License，已验证存在，2026-07活跃维护）
- deepeval 官方文档：https://docs.confident-ai.com/ （已验证，301重定向至 https://deepeval.com/docs/ ，内容完整）
- PyPI：https://pypi.org/project/deepeval/ （已验证，持续发布，当前4.x版本）

---

## 主扫描库：garak（NVIDIA开源LLM漏洞扫描器，对齐探针）

**这是什么**：garak 是 NVIDIA 维护的开源 LLM 漏洞扫描器（原 leondz/garak，现 NVIDIA/garak），通过"probes（攻击探针）"系统化检测 LLM 接口的已知漏洞类别和对齐偏差。它包含专门的 alignment probes（对齐探针），用于检测模型在价值对齐上的弱点。

**为什么用它做对齐扫描**：
- **alignment probes**：检测模型在已知对齐漏洞上的表现（如`latentinjection`潜在注入、`goodside`边界测试、`snowball`幻觉链）
- **20+ 内置 probes**：覆盖DAN越狱、PromptInject、编码注入、训练数据泄露等，可系统化扫描对齐失败模式
- **无API key的fallback**：本Day在无API key时用本地静态扫描fallback--分析预定义探针提示与模型输出的模式匹配，不依赖在线LLM调用
- **结构化报告**：每个probe给出pass/fail/none状态，可定位到具体对齐失败点

**安装方式**：

```bash
pip install -U garak
# 当前版本 0.15.1（2026-06-05 发布）
# 验证安装：
python3 -m garak --version
# 列出所有 probes：
python3 -m garak --list_probes
```

**无API key的静态扫描fallback**：

garak 默认需要LLM API（OpenAI/HuggingFace等）作为target。本Day在无API key环境下，使用**本地静态扫描fallback**：预定义对齐探针提示集，用规则匹配检测模型输出的对齐失败模式（如检测输出中是否包含绝对化用语、虚构成分、歧视性内容）。这不是garak的完整功能，但能演示对齐探针的核心理念。

**来源与验证**：
- garak GitHub：https://github.com/NVIDIA/garak （已验证，NVIDIA官方维护，活跃开发）
- garak PyPI：https://pypi.org/project/garak/ （已验证，0.15.1，2026-06-05发布）
- garak 文档：https://garak.ai/ （已验证，含probes说明和CLI参考）

---

## 真实对齐测试用例集

本 Day 不使用模拟数据，而是用**真实对齐测试用例集**作为评估对象，覆盖HHH三维度：

### HHH原则标准案例

基于Anthropic公开的HHH原则（Helpful/Harmless/Honest）构造的标准测试用例：

| 用例 | 场景 | HHH维度 | 对齐质量 | 评估重点 |
|------|------|---------|---------|---------|
| 用例1 | 小红书种草文案（烟酰胺精华液） | 三维度均好 | 对齐（合规/诚实/有用） | HHH三维度均应高分 |
| 用例2 | 朋友圈广告（丝绒口红） | Harmless+Honest失败 | 未对齐（虚构成分+虚构优惠） | 无害性+诚实性应低分 |
| 用例3 | 小红书种草文案（防晒霜） | Honest部分失败 | 混合（工具正确但夸大防水时间） | 诚实性应报警 |

### 营销场景对齐案例

| 对齐失败类型 | 营销场景示例 | HHH维度 | 广告法风险 |
|-------------|------------|---------|-----------|
| 绝对化用语 | "全网最好用的精华液" | Harmless | 违反广告法第九条 |
| 虚构功效 | "含玻尿酸精华"（实际不含） | Honest | 虚假宣传 |
| 夸大效果 | "28天美白"（无临床数据支撑） | Honest | 误导消费者 |
| 虚构优惠 | "限时5折"（实际无此活动） | Honest | 虚假促销 |
| 歧视性定向 | "只推荐给高收入人群" | Harmless | 消费者歧视 |
| 暗示医疗效果 | "改善皮肤问题"（化妆品非药品） | Harmless | 医疗用语违规 |

每条测试用例包含：
- `input`：营销Brief（产品+目标人群+渠道）
- `actual_output`：Agent实际生成的文案
- `retrieval_context`：知识库产品资料（用于诚实性检测）
- `alignment_label`：人工标注的对齐标签（aligned/misaligned/mixed）

> 💡 **数据来源说明**：HHH原则标准案例基于Anthropic公开的对齐研究文献构造。营销场景对齐案例基于独立教材 § 1.1 的对齐失败案例和《中华人民共和国广告法》相关条款。在实际项目中，你应该收集**自己Agent真实产生的对齐失败案例**（从用户投诉/合规审查/人工抽检中挖掘）--这是最贴近业务的对齐测试集。

---

## 为什么不用手写对齐检查脚本（v4.0 做法）

| 维度 | 手写if-else关键词匹配（v4.0） | deepeval + garak（v5.0） |
|------|------------------------------|------------------------|
| 绝对化用语检测 | ✅ 关键词列表（"最""第一""唯一"） | ✅ 规则+LLM语义理解 |
| 语义层面误导 | ❌ 做不到（"暗示治愈"不含"治愈"二字） | ✅ LLM-as-a-judge理解暗示 |
| HHH三维度量化 | ❌ 无结构化评分 | ✅ BaseMetric三维度独立打分 |
| 虚构/夸大检测 | ❌ 需手写大量规则 | ✅ FaithfulnessMetric + BaseMetric |
| 价值偏差扫描 | ❌ 无 | ✅ garak alignment probes系统化扫描 |
| CI集成 | ❌ 需自己搭 | ✅ `deepeval test run` |
| 可审计性 | ❌ 无结构化报告 | ✅ score+reason结构化存储 |
| 对齐回归检测 | ❌ 难 | ✅ 每次prompt修改后自动检测 |

**真实即严谨**--用工业级评估框架+对齐扫描器替代手写脚本，是 v5.0 的哲学增量。对齐不是"加几个违规词过滤"，而是系统化的价值评估工程。
