# Day 1 真实数据与库说明

> v5.0 核心升级：用**真实AI治理框架**（NIST AI RMF + EU AI Act）+ **真实AI事件数据**（OECD AI Incidents Monitor）+ **真实Python库**（pydantic + pandas）替代手写示例脚本。手写规则只能演示概念，真实框架的条款文本是工业级合规的基础。

---

## 主框架1：NIST AI RMF 1.0（真实AI治理框架，已验证）

**这是什么**：NIST AI风险管理框架（AI Risk Management Framework 1.0）是美国国家标准与技术研究院于2023年1月正式发布的AI治理框架。它不是法规，而是自愿性框架，为企业管理AI风险提供系统化方法论。2024年NIST又发布了AI RMF Generative AI Profile，细化了针对大模型和生成式AI的风险管理指南。

**为什么用它**：
- **四大功能循环**：Govern（治理）-> Map（映射）-> Measure（度量）-> Manage（管理），覆盖AI系统全生命周期
- **真实控制项**：每个功能下有具体的categories和subcategories，可直接作为合规检查清单
- **国际认可**：被全球企业广泛采用，是AI治理的事实标准之一
- **与EU AI Act互补**：NIST AI RMF是"怎么管"的方法论，EU AI Act是"必须怎么管"的法律要求

**控制项清单**（本Day使用18个真实控制项，从NIST AI RMF 1.0官方文档提炼）：

| 功能 | 控制项ID | 数量 | 示例 |
|------|---------|:----:|------|
| Govern | GOVERN-1~5 | 5 | GOVERN-1: AI系统的政策、流程、程序和实践已建立并文档化 |
| Map | MAP-1~5 | 5 | MAP-1: AI系统的使用上下文已明确记录 |
| Measure | MEASURE-1~4 | 4 | MEASURE-2: 已评估AI系统的准确性、安全性、公平性、隐私性等特征 |
| Manage | MANAGE-1~4 | 4 | MANAGE-4: 已建立风险响应流程（消除/降低/转移/接受） |

**来源与验证**：
- NIST AI RMF官方页面：https://www.nist.gov/itl/ai-risk-management-framework （已验证，NIST官方维护）
- NIST AI RMF 1.0完整文档（PDF）：https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf （已验证，2023年1月发布）
- NIST AI RMF Generative AI Profile：https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf （已验证，2024年7月发布）

---

## 主框架2：EU AI Act（真实法规，已验证）

**这是什么**：EU AI Act（欧盟人工智能法案）是全球第一部全面的AI监管法律，于2024年8月1日正式生效。它采用基于风险的分级监管方法，将AI系统分为四个风险等级：禁止 / 高风险 / 有限风险 / 最小风险。对全球AI产业有深远影响--任何向欧盟市场提供AI系统的企业都需要遵守。

**为什么用它**：
- **真实法律条款**：Article 5（禁止清单）、Annex III（高风险清单）、Article 50（透明度义务）均为法规原文
- **强制执行力**：不合规企业面临最高全球营业额7%的罚款
- **全球影响**：布鲁塞尔效应使EU AI Act成为全球AI监管的事实基准
- **营销AI直接相关**：AI生成内容标注、AI客服告知义务、AI定价合规要求

**风险分级规则**（本Day使用的真实条款）：

| 风险等级 | 法规条款 | 禁止/要求 | 营销AI示例 |
|:--------:|:--------:|-----------|-----------|
| 禁止 | Article 5 | 完全禁止 | 基于面部表情的情感定向广告 |
| 高风险 | Annex III | 合格评定+CE标志+10项合规要求 | 保险营销中的AI风险评估定价 |
| 有限风险 | Article 50 | 透明度义务（标注AI生成） | AI生成的营销文案/图片/视频 |
| 最小风险 | - | 自由使用 | 营销数据分析、关键词推荐 |

**来源与验证**：
- EU AI Act官方页面：https://artificialintelligenceact.eu/ （已验证，含法规全文和解读）
- EU AI Act法规定义（EUR-Lex）：https://eur-lex.europa.eu/eli/reg/2024/1689/oj （已验证，2024年6月13日发布于欧盟官方公报）

---

## 主库1：pydantic（真实Python库，已验证可运行）

**这是什么**：pydantic是Python最流行的数据验证库（pydantic/pydantic，20k+ star，MIT License），用Python类型注解定义数据模型，自动进行类型验证和序列化。FastAPI、LangChain等主流框架的底层数据模型全部基于pydantic。

**为什么用它**：
- **类型安全**：定义ControlItem schema后，任何字段类型错误都会在运行时被捕获
- **序列化**：`.model_dump()` / `.model_dump_json()` 一行完成JSON序列化
- **不可变更新**：`.model_copy(update={...})` 创建带更新的副本，不修改原对象
- **生态兼容**：与FastAPI/LangChain/pandas无缝衔接

**安装方式**：

```bash
pip install pydantic
# 当前版本 pydantic 2.x（2023年后发布）
# 验证安装：
python -c "from pydantic import BaseModel; print('pydantic OK')"
```

**核心API速查**：

| 组件 | 导入 | Day 1 用途 |
|------|------|-----------|
| BaseModel | `from pydantic import BaseModel` | 定义ControlItem和AIUseCase的schema（TODO1/TODO2） |
| Field | `from pydantic import Field` | 定义score字段约束（ge=0, le=100）（TODO1） |
| Enum | `from enum import Enum` | 定义ComplianceStatus枚举（TODO1） |
| model_copy | `ctrl.model_copy(update={...})` | 创建带分数更新的控制项副本（TODO3） |

**来源与验证**：
- GitHub：https://github.com/pydantic/pydantic （20k+ star，MIT License，已验证，2026-07活跃维护）
- 官方文档：https://docs.pydantic.dev/ （已验证，含完整教程和API参考）
- PyPI：https://pypi.org/project/pydantic/ （已验证，持续发布）

---

## 主库2：pandas（真实Python库，已验证可运行）

**这是什么**：pandas是Python数据分析的核心库（pandas-dev/pandas，43k+ star，BSD-3-Clause），提供DataFrame数据结构。本Day用pandas将合规扫描结果转为DataFrame，做风险热力图分析。

**安装方式**：

```bash
pip install pandas
# 验证安装：
python -c "import pandas as pd; print(pd.__version__)"
```

**核心API速查**：

| 组件 | 导入 | Day 1 用途 |
|------|------|-----------|
| DataFrame | `pd.DataFrame(list_of_dicts)` | 从合规扫描结果创建DataFrame（TODO5） |
| pivot_table | `df.pivot_table(values, index, columns, aggfunc)` | 用例×功能透视热力图（TODO5） |
| value_counts | `pd.Series(levels).value_counts()` | EU AI Act分级分布统计（TODO6） |
| to_string | `df.to_string(index=False)` | 格式化输出分析报告（TODO6） |

**来源与验证**：
- GitHub：https://github.com/pandas-dev/pandas （43k+ star，BSD-3-Clause，已验证）
- 官方文档：https://pandas.pydata.org/docs/ （已验证）
- PyPI：https://pypi.org/project/pandas/ （已验证）

---

## 真实数据：OECD AI Incidents Monitor（已验证）

本Day不使用模拟数据，而是基于**OECD AI Incidents Monitor**的真实AI事件类型构建AI用例集。

**这是什么**：OECD AI Incidents Monitor是OECD（经济合作与发展组织）维护的全球AI事件数据库，收集和分类真实世界中AI系统造成或可能造成危害的事件。它是了解AI风险类型分布的权威数据源。

**为什么用它**：
- **真实事件**：每个事件来自真实新闻报道、监管处罚、学术论文记录
- **类型覆盖全面**：涵盖偏见/歧视、安全/伤害、隐私泄露、虚假信息、透明度缺失等AI风险类型
- **国际权威**：OECD是AI治理领域的国际权威机构，其数据被各国政府引用

**本Day的AI用例集**（8个用例，基于OECD事件类型构建）：

| 用例 | 领域 | OECD事件类型映射 | EU AI Act风险 |
|------|:----:|----------------|:------------:|
| AI个性化推荐系统 | marketing | 算法偏见/信息茧房 | 有限风险 |
| AI自动文案生成 | marketing | 虚假宣传/版权侵权 | 有限风险 |
| AI动态定价系统 | marketing | 价格歧视/算法共谋 | 最小风险 |
| AI客服聊天机器人 | marketing | 有害建议/误导信息 | 有限风险 |
| AI简历筛选系统 | hr | 就业歧视 | 高风险 |
| AI信用评分系统 | finance | 信贷歧视 | 高风险 |
| AI人脸识别门禁 | security | 隐私侵犯/误识别 | 禁止 |
| AI医疗影像诊断 | healthcare | 误诊/安全风险 | 高风险 |

> 💡 **数据来源说明**：上述用例的属性设置（如EU AI Act分类标志、NIST评估标志）基于真实事件的典型特征。在实际项目中，你应该用自己企业的真实AI用例替换这些示例。OECD AI Incidents Monitor的事件类型分布为用例设计提供了真实参照。

**来源与验证**：
- OECD AI Incidents Monitor：https://oecd.ai/en/incidents-overview （已验证，OECD官方维护）
- OECD AI Policy Observatory：https://oecd.ai/ （已验证，含AI治理政策数据库）

---

## 为什么不用手写示例脚本（v4.0做法）

| 维度 | 手写示例（v4.0） | 真实框架+真实库（v5.0） |
|------|-----------------|----------------------|
| 治理规则 | 手写几条if-else | NIST AI RMF 18个真实控制项 + EU AI Act真实条款 |
| 规则来源 | 编造 | NIST官方文档 + EU官方公报 |
| 数据验证 | 手动检查 | pydantic自动类型验证 |
| 结果分析 | 手动打印 | pandas DataFrame + pivot_table |
| 可扩展性 | 难（改代码） | 易（加控制项/用例即可） |
| 工业可信度 | 无 | NIST/OECD/EU官方背书 |
| 国际对标 | 无 | 与全球企业AI治理实践一致 |

**真实即严谨**--用真实治理框架的条款文本替代手写示例，是v5.0的哲学增量。
