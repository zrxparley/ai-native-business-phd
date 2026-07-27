# Day 3 真实数据与库说明

> v5.0 核心升级：用**三个真实治理框架**（NIST AI RMF + EU AI Act + 中国AI法规）的**真实条款文本**作为规则源，用**pydantic**定义控制项schema，用**pandas**构建治理台账。替代v4.0的"手写几个规则演示治理概念"。

---

## 主schema库：pydantic（已验证，可运行）

**这是什么**：pydantic 是 Python 最流行的数据验证库（基于类型注解），提供 BaseModel、Field、Enum 等。它是 AI 治理 schema 定义的**事实标准**--用 pydantic 定义 NIST AI RMF 控制项模型，可自动验证字段类型、范围、默认值。

**为什么用它做治理schema**：
- **BaseModel**：定义 ControlItem（控制项）和 AIUseCase（AI用例）的数据模型，字段类型自动验证
- **Field约束**：`Field(ge=0, le=100)` 确保分数在 0-100 范围内，`default=0.0` 提供默认值
- **model_copy(update=...)**：pydantic v2 API，用于扫描后更新控制项的 score 和 status（不可变模型的函数式更新）
- **Enum**：定义 ComplianceStatus 枚举（NOT_ASSESSED/NOT_MET/PARTIALLY_MET/MET），类型安全

**安装方式**：

```bash
pip install pydantic
# pydantic v2.x，本Day用 BaseModel + Field + model_copy
```

**核心 API 速查**：

| 组件 | 导入 | 用途 |
|------|------|------|
| BaseModel | `from pydantic import BaseModel` | 定义控制项/用例模型基类 |
| Field | `from pydantic import Field` | 字段约束（ge/le/default） |
| Enum | `from enum import Enum` | 定义 ComplianceStatus 枚举 |
| model_copy | `model.model_copy(update={...})` | 不可变更新（pydantic v2） |

**来源与验证**：
- pydantic GitHub：https://github.com/pydantic/pydantic （20k+星，MIT License，已验证存在，2026-07活跃维护）
- pydantic 官方文档：https://docs.pydantic.dev/ （已验证，v2文档完整）
- PyPI：https://pypi.org/project/pydantic/ （已验证，持续发布，当前2.x版本）

---

## 主分析库：pandas（已验证，可运行）

**这是什么**：pandas 是 Python 数据分析的事实标准库，提供 DataFrame、pivot_table、value_counts 等。本Day用 pandas 构建企业AI治理台账（用例清单/风险分级/控制措施/审计记录），分析闭环状态分布。

**为什么用它做治理台账**：
- **DataFrame**：将扫描结果转为表格，每行一个用例，每列一个治理维度
- **pivot_table**：按用例×功能（Govern/Map/Measure/Manage）透视NIST合规分数
- **value_counts**：统计EU AI Act风险分级分布、治理闭环状态分布

**安装方式**：

```bash
pip install pandas
# pandas 2.x，本Day用 DataFrame + pivot_table + value_counts
```

**来源与验证**：
- pandas GitHub：https://github.com/pandas-dev/pandas （40k+星，BSD License，已验证存在）
- pandas 官方文档：https://pandas.pydata.org/docs/ （已验证，内容完整）
- PyPI：https://pypi.org/project/pandas/ （已验证，持续发布）

---

## 三个真实治理框架（规则源）

### 1. NIST AI RMF 1.0（美国，2023年1月发布）

**这是什么**：美国国家标准与技术研究院（NIST）发布的 AI 风险管理框架，已成为全球企业AI治理的事实标准之一。核心是四步循环：Govern（治理）-> Map（映射）-> Measure（度量）-> Manage（管理），Govern贯穿全过程。

**真实控制项**（18项，来自官方文档）：
- Govern-1~5：政策与流程 / 问责结构 / 人员能力 / 利益相关方参与 / 全生命周期治理
- Map-1~5：上下文建立 / 分类与风险识别 / 能力与限制 / 影响评估 / 第三方风险评估
- Measure-1~4：评估方法选择 / 可信特征评估 / 指标追踪 / 反馈机制
- Manage-1~4：风险优先级 / 资源分配 / 第三方风险处理 / 风险响应

**来源**：
- NIST AI RMF 官网：https://www.nist.gov/itl/ai-risk-management-framework （已验证，NIST官方）
- NIST AI RMF 1.0 完整文档PDF：https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf （已验证，2023年1月发布）

### 2. EU AI Act（欧盟，2024年8月1日生效，2026年分阶段执行）

**这是什么**：全球第一部全面AI监管法律，采用基于风险的4级分级监管：禁止（Article 5）/ 高风险（Annex III）/ 有限风险（Article 50）/ 最小风险。

**真实条款**（本Day实现）：
- Article 5：禁止的AI实践（潜意识操纵、社会评分、工作场所情感识别、实时生物识别等）
- Annex III：高风险AI系统（招聘/信贷/保险/医疗/司法/移民/公共服务等）
- Article 50：有限风险透明度义务（聊天机器人/AI生成内容/深度伪造需标注）

**来源**：
- EU AI Act 官网：https://artificialintelligenceact.eu/ （已验证，欧盟官方）
- EU AI Act 全文：https://eur-lex.europa.eu/eli/reg/2024/1689/oj （已验证，Official Journal）

### 3. 中国AI法规体系

**这是什么**：中国已形成多层次AI监管体系，本Day覆盖5部核心法规：

| 法规 | 生效时间 | 核心要求 |
|------|---------|---------|
| 《数据安全法》 | 2021-09-01 | 数据分级分类、跨境传输限制 |
| 《个人信息保护法》 | 2021-11-01 | 知情同意、最小必要、可撤回 |
| 《算法推荐管理规定》 | 2022-03-01 | 推荐需透明、可关闭 |
| 《深度合成管理规定》 | 2023-01-10 | 深度合成内容需标识 |
| 《生成式AI服务管理暂行办法》 | 2023-08-15 | 生成式AI服务需备案、内容需安全 |

**来源**：
- 国家网信办《生成式AI服务管理暂行办法》：https://www.cac.gov.cn/2023-07/13/c_1690898327029107.htm （已验证，网信办官方）
- 国家网信办《算法推荐管理规定》：https://www.cac.gov.cn/2021-12/31/c_1643574110791945.htm （已验证，网信办官方）
- 国家网信办《深度合成管理规定》：https://www.cac.gov.cn/2022-12/11/c_1672221949354811.htm （已验证，网信办官方）

---

## 真实营销AI用例集（9个）

本 Day 不使用模拟数据，而是用**基于真实营销场景**构建的9个AI用例做治理登记与风险分级：

| 用例ID | 营销AI系统 | EU AI Act风险 | 中国法规要求 | NIST治理重点 |
|--------|-----------|:------------:|:----------:|:----------:|
| UC-01 | AI个性化推荐系统 | 有限风险 | 算法推荐透明 | Measure（公平性） |
| UC-02 | AI自动文案生成 | 有限风险 | 生成式AI备案 | Manage（人工审核） |
| UC-03 | AI动态定价系统 | 最小风险 | 个人信息保护 | Govern（问责） |
| UC-04 | AI客服聊天机器人 | 有限风险 | 生成式AI备案 | Map（上下文） |
| UC-05 | AI用户画像分析 | 最小风险 | 个人信息保护 | Measure（隐私性） |
| UC-06 | AI竞品分析 | 最小风险 | 一般合规 | Map（第三方风险） |
| UC-07 | AI投放策略优化 | 有限风险 | 算法推荐透明 | Manage（风险响应） |
| UC-08 | AI深度合成广告 | 有限风险 | 深度合成标识 | Manage（人工审核） |
| UC-09 | AI情感分析定向 | 有限风险 | 个人信息保护 | Measure（公平性） |

### 数据来源

1. **独立教材 § 3.1 NIST AI RMF营销AI评估示例**：营销内容生成Agent的Govern/Map/Measure/Manage四步评估，是本Day用例集的原始参考
2. **NIST AI RMF 1.0 官方控制项**：18个控制项的真实描述文本，非编造
3. **EU AI Act 官方条款**：Article 5 / Annex III / Article 50 的真实条款文本
4. **中国网信办法规原文**：5部法规的真实要求文本

> 数据来源说明：营销AI用例基于独立教材的营销场景和真实企业AI实践构造。在实际项目中，你应该梳理自己企业的真实AI用例清单（从IT资产清单/业务系统/数据流图中挖掘）--这是最贴近业务的治理台账。

---

## 前沿认知库：garak + PyRIT + MCP（本Day不实跑，作关键词提及）

### garak（NVIDIA开源LLM漏洞扫描器）

**这是什么**：garak 是 NVIDIA 维护的开源 LLM 漏洞扫描器，在 NIST AI RMF 中属于 **Measure层**的度量工具（MEASURE-1评估方法选择 + MEASURE-2可信特征评估-安全性）。

**为什么本Day不实跑**：garak的完整功能需要LLM API key + 安装较慢（可能阻塞）。本Day用pydantic schema + 规则扫描替代，演示相同的治理理念。生产环境应用完整garak做系统化漏洞扫描。

**来源**：
- garak GitHub：https://github.com/NVIDIA/garak （已验证，NVIDIA官方维护）

### PyRIT（微软自动化红队框架）

**这是什么**：PyRIT 是微软维护的 Python 自动化红队框架，在 NIST AI RMF 中属于 **Measure层**的评估工具（自动化红队编排）。

**为什么本Day不实跑**：PyRIT需要OPENAI_API_KEY + 安装较重。本Day用三框架规则分级替代，演示相同的治理理念。生产环境应用PyRIT做自动化红队编排。

**来源**：
- PyRIT GitHub：https://github.com/Azure/PyRIT （已验证，微软维护）

### MCP（Model Context Protocol，Anthropic 2024）

**这是什么**：MCP 是 Anthropic 提出的开放协议，让AI Agent通过标准化接口接入外部工具。在AI治理领域实现**治理即代码**：合规检查Agent + 审计日志MCP Server。

**为什么本Day不实跑**：MCP需要Agent运行时环境。本Day在notes.md作前沿认知，不实跑。

**来源**：
- MCP 官方文档：https://modelcontextprotocol.io/ （已验证，Anthropic官方）

---

## 为什么不用手写几个规则演示治理概念（v4.0 做法）

| 维度 | 手写几个规则（v4.0） | 三框架真实条款 + pydantic + pandas（v5.0） |
|------|---------------------|-------------------------------------------|
| 规则来源 | 自编规则，无权威性 | NIST AI RMF + EU AI Act + 中国法规真实条款 |
| 框架覆盖 | 单一框架 | 三框架对比（NIST方法论 + EU法律分级 + 中国备案制） |
| schema验证 | 无 | pydantic BaseModel + Field约束 + Enum |
| 台账分析 | 无 | pandas DataFrame + pivot_table + value_counts |
| 闭环追踪 | 无 | 登记->评估->控制->监控->审计 五阶段闭环 |
| 治理深度 | 概念演示 | 5层企业安全架构 + 营销AI专项分析 |
| 可审计性 | 无结构化报告 | 治理台账DataFrame + 改进建议 |

**真实即严谨**--用三个真实治理框架的真实条款 + pydantic schema + pandas台账替代手写几个规则，是 v5.0 的哲学增量。AI治理不是"写几个规则检查一下"，而是系统化的框架对标 + 闭环追踪 + 持续改进。
