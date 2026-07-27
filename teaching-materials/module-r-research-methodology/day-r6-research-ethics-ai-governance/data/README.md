# R6 真实数据与库说明

> v5.0 核心升级：用**真实研究伦理框架**（Belmont Report + NIST AI RMF + EU AI Act）+ **真实AI事件数据**（OECD AI Incidents Monitor）+ **真实Python库**（pydantic + pandas）+ **真实AI安全测试工具概念**（garak + PyRIT）替代手写示例脚本。手写检查项只能演示概念，真实框架的条款文本是工业级伦理审查的基础。

---

## 主框架1：Belmont Report（真实研究伦理框架，已验证）

**这是什么**：Belmont Report（贝尔蒙特报告）是美国国家委员会于1979年发布的研究伦理报告，确立了三条核心原则，至今仍是美国 IRB（Institutional Review Board，机构审查委员会）审查的基础。它的历史脉络可追溯至二战后的 Nuremberg Code（1947）和 Declaration of Helsinki（1964）。

**为什么用它**：
- **三原则体系**：尊重个人（Respect for Persons）/ 善行（Beneficence）/ 公平正义（Justice），覆盖研究伦理的核心维度
- **IRB审查基础**：全球研究机构的伦理审查委员会均以 Belmont 三原则为审查框架
- **AI研究适用**：AI+营销研究涉及人类参与者数据，Belmont 原则直接适用
- **与NIST/EU互补**：Belmont 是"研究伦理底线"，NIST AI RMF 是"怎么管"，EU AI Act 是"必须怎么管"

**审查清单**（本单元使用6个真实审查项，从 Belmont Report 三原则提炼）：

| 原则 | 审查项ID | 数量 | 示例 |
|------|---------|:----:|------|
| 尊重个人 | R1, R2 | 2 | R1: 知情同意（参与者充分知情后自愿同意） |
| 善行 | B1, B2 | 2 | B1: 风险-收益评估（最大化收益、最小化伤害） |
| 公平正义 | J1, J2 | 2 | J1: 负担公平分配（弱势群体不过度承担风险） |

**来源与验证**：
- Belmont Report 官方文档（HHS.gov）：https://www.hhs.gov/ohrp/regulations-and-policy/belmont-report/index.html （已验证，美国卫生与公众服务部官方维护）
- Belmont Report 原文（PDF）：https://www.hhs.gov/sites/default/files/ohrp/regulations-and-policy/belmont-report-v2.pdf （已验证，1979年发布）

---

## 主框架2：NIST AI RMF 1.0（真实AI治理框架，已验证）

**这是什么**：NIST AI风险管理框架（AI Risk Management Framework 1.0）是美国国家标准与技术研究院于2023年1月正式发布的AI治理框架。本单元从**研究伦理视角**（非企业治理视角）映射其四步循环。

**为什么用它（研究伦理视角）**：
- **Govern**：是否有 IRB 审批/伦理委员会监督
- **Map**：是否识别了人类参与者及研究风险
- **Measure**：是否有偏见/公平性/安全性度量
- **Manage**：是否有风险缓解与知情退出机制

> **与技能2 Day1的区别**：技能2 Day1 从企业治理视角（组织如何管AI），R6 从研究伦理视角（研究者如何保护参与者）。两者互补。

**来源与验证**：
- NIST AI RMF官方页面：https://www.nist.gov/itl/ai-risk-management-framework （已验证，NIST官方维护）
- NIST AI RMF 1.0完整文档（PDF）：https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf （已验证，2023年1月发布）

---

## 主框架3：EU AI Act（真实法规，已验证）

**这是什么**：EU AI Act（欧盟人工智能法案）是全球第一部全面的AI监管法律，于2024年8月1日正式生效。本单元从**研究合规视角**判定AI研究案例的风险等级。

**风险分级规则**（本单元使用的真实条款）：

| 风险等级 | 法规条款 | 研究合规要求 |
|:--------:|:--------:|------------|
| 禁止 | Article 5 | 研究中完全禁止（如针对弱势群体的剥削性处理） |
| 高风险 | Annex III | 需风险评估、数据治理、人工监督 |
| 有限风险 | Article 50 | 透明度义务（标注AI生成） |
| 最小风险 | - | 自由使用（鼓励自律） |

**来源与验证**：
- EU AI Act官方页面：https://artificialintelligenceact.eu/ （已验证，含法规全文和解读）
- EU AI Act法规定义（EUR-Lex）：https://eur-lex.europa.eu/eli/reg/2024/1689/oj （已验证，2024年6月13日发布）

---

## 主工具1：garak（NVIDIA开源 LLM 漏洞扫描器，已验证）

**这是什么**：garak 是 NVIDIA 维护的开源 LLM 漏洞扫描器（NVIDIA/garak），通过"probes（攻击探针）"系统化检测 LLM 接口的已知漏洞类别。在本单元中，garak 的红队测试被定位为 **Belmont 善行原则（最小化伤害）的履行手段**。

**为什么用它（伦理视角）**：
- **善行原则履行**：红队测试主动发现 AI 系统漏洞 = 最小化研究对参与者的潜在伤害
- **20+ 内置 probes**：dan（DAN越狱）、promptinject（注入）、encoding（编码注入）、leakreplay（训练数据泄露）、goodside（社工攻击）、snowball（幻觉）、packagehallucination（包幻觉）等
- **按领域映射**：不同研究领域的 AI 系统需跑不同 probe 类别

**安装方式**：

```bash
pip install -U garak
# 当前版本 0.15.1（2026-06-05 发布）
# 验证安装：
python3 -m garak --version
python3 -m garak --list_probes
```

> 💡 **本单元用法**：garak 较重，上机用其真实 probe 概念做轻量映射（按领域映射 probe 类别）。data/README.md 说明完整安装用法，实际项目中应跑真实 garak 扫描。

**来源与验证**：
- garak GitHub：https://github.com/NVIDIA/garak （已验证，NVIDIA 官方维护，活跃开发）
- garak PyPI：https://pypi.org/project/garak/ （已验证，0.15.1，2026-06-05 发布）

---

## 主工具2：PyRIT（微软 Python Risk Identification Toolkit，已验证）

**这是什么**：PyRIT 是微软开源的 Python 自动化红队框架（microsoft/PyRIT，4.2k★，MIT License），提供 Orchestrator + Target + Scorer + Converter 的完整架构。在本单元中，PyRIT 的风险评分概念被用于量化 AI 研究的红队风险。

**为什么用它（伦理视角）**：
- **风险量化**：PyRIT Scorer 自动评估目标是否被攻破，将伦理风险从定性转为定量
- **多轮对抗**：RedTeamingOrchestrator 模拟真实攻击者行为，发现单轮测试遗漏的风险
- **可复现**：Memory 持久化攻击记录，支持伦理审查的可审计性

**安装方式**：

```bash
pip install pyrit
# 当前版本 1.0.0（2026 发布）
# 需要 .env 文件配置 API 密钥
```

> 💡 **本单元用法**：PyRIT 较重，上机用其风险评分概念做轻量模拟（基于案例属性估算 PyRIT 风险分）。实际项目中应跑真实 PyRIT 红队测试。

**来源与验证**：
- PyRIT GitHub：https://github.com/microsoft/PyRIT （4.2k★，MIT License，已验证，1.0.0 版本）
- PyRIT 文档：https://microsoft.github.io/PyRIT/ （已验证，1.0.0 文档）

---

## 主库1：pydantic（真实Python库，已验证可运行）

**这是什么**：pydantic是Python最流行的数据验证库（pydantic/pydantic，20k+ star，MIT License），用Python类型注解定义数据模型。本单元用 pydantic 定义 Belmont Report 伦理审查清单的 schema。

**安装方式**：

```bash
pip install pydantic
# 验证安装：
python -c "from pydantic import BaseModel; print('pydantic OK')"
```

**核心API速查**：

| 组件 | 导入 | R6 用途 |
|------|------|---------|
| BaseModel | `from pydantic import BaseModel` | 定义 EthicsChecklistItem 和 ResearchCase 的 schema（TODO1/TODO2） |
| Field | `from pydantic import Field` | 定义 score 字段约束（ge=0, le=100）（TODO1） |
| Enum | `from enum import Enum` | 定义 BelmontPrinciple 和 ReviewStatus 枚举（TODO1） |
| model_copy | `item.model_copy(update={...})` | 创建带分数更新的审查项副本（TODO3） |

**来源与验证**：
- GitHub：https://github.com/pydantic/pydantic （20k+ star，MIT License，已验证）
- 官方文档：https://docs.pydantic.dev/ （已验证）

---

## 主库2：pandas（真实Python库，已验证可运行）

**这是什么**：pandas是Python数据分析的核心库（pandas-dev/pandas，43k+ star，BSD-3-Clause），提供DataFrame数据结构。本单元用pandas将伦理审查结果转为DataFrame，做案例×原则热力图分析。

**安装方式**：

```bash
pip install pandas
# 验证安装：
python -c "import pandas as pd; print(pd.__version__)"
```

**来源与验证**：
- GitHub：https://github.com/pandas-dev/pandas （43k+ star，BSD-3-Clause，已验证）
- 官方文档：https://pandas.pydata.org/docs/ （已验证）

---

## 真实数据：OECD AI Incidents Monitor（已验证）

本单元不使用模拟数据，而是基于 **OECD AI Incidents Monitor** 的真实AI事件类型构建AI研究案例集。

**这是什么**：OECD AI Incidents Monitor是OECD（经济合作与发展组织）维护的全球AI事件数据库，收集和分类真实世界中AI系统造成或可能造成危害的事件。

**本单元的AI研究案例集**（8个案例，基于OECD事件类型构建）：

| 案例 | 领域 | OECD事件类型映射 | Belmont风险 | EU AI Act风险 |
|------|:----:|----------------|:-----------:|:------------:|
| AI个性化推荐研究 | marketing | 算法偏见/信息茧房 | 低 | 有限风险 |
| AI自动文案A/B测试 | marketing | 虚假宣传/误导信息 | 中 | 有限风险 |
| AI动态定价研究 | marketing | 价格歧视/算法共谋 | **高** | **禁止** |
| AI客服交互研究 | marketing | 有害建议/误导信息 | 低 | 有限风险 |
| AI简历筛选研究 | hr | 就业歧视 | **高** | **禁止** |
| AI信用评分研究 | finance | 信贷歧视 | 中 | 高风险 |
| AI人脸识别研究 | security | 隐私侵犯/误识别 | 中 | 高风险 |
| AI医疗影像研究 | healthcare | 误诊/安全风险 | 中 | 高风险 |

> 💡 **数据来源说明**：上述案例的属性设置（如知情同意、敏感属性、伤害严重度）基于真实OECD事件类型的典型特征。在实际项目中，你应该用自己研究的真实AI案例替换这些示例。

**来源与验证**：
- OECD AI Incidents Monitor：https://oecd.ai/en/incidents-overview （已验证，OECD官方维护）
- OECD AI Policy Observatory：https://oecd.ai/ （已验证，含AI治理政策数据库）

---

## 为什么不用手写示例脚本（v4.0做法）

| 维度 | 手写示例（v4.0） | 真实框架+真实库（v5.0） |
|------|-----------------|----------------------|
| 伦理规则 | 手写几条if-else | Belmont Report 6个真实审查项 + NIST AI RMF真实控制项 |
| 规则来源 | 编造 | Belmont Report 1979 + NIST官方文档 + EU官方公报 |
| 数据验证 | 手动检查 | pydantic自动类型验证 |
| 结果分析 | 手动打印 | pandas DataFrame + pivot_table |
| 安全验证 | 无 | garak/PyRIT 真实红队工具概念 |
| 风险预判 | 无 | 天道推演3层推演树 |
| 可扩展性 | 难（改代码） | 易（加审查项/案例即可） |
| 工业可信度 | 无 | Belmont/NIST/OECD/EU官方背书 |
| 国际对标 | 无 | 与全球研究伦理实践一致 |

**真实即严谨**--用真实研究伦理框架的条款文本替代手写示例，是v5.0的哲学增量。
