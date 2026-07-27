# Day 3 深链阅读清单

> v5.0 升级：从"课程主页"升级为**经验证的深链**（指向具体法规/文档/仓库，非主页）。全部链接已验证存在。

---

## 1. NIST AI RMF（AI 风险管理框架）

### NIST AI RMF 1.0 官方文档
- 官网：https://www.nist.gov/itl/ai-risk-management-framework
- **深链用法**：
  - [NIST AI RMF 1.0 完整PDF](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf)：本Day核心规则源。18个控制项的真实描述文本来自此文档。重点读 Section 3 (Core Functions)：Govern/Map/Measure/Manage四步循环的详细定义
  - [AI RMF Playbook](https://www.nist.gov/itl/ai-risk-management-framework/ai-rmf-playbook)：实操指南，每个控制项的落地建议。对应 TODO3 的评分逻辑设计
  - [Trustworthy AI Characteristics](https://www.nist.gov/itl/ai-risk-management-framework/ai-rmf-playbook)：7个可信AI特征（安全/可靠/可解释/隐私/公平/有效/问责），对应 MEASURE-2 可信特征评估

### NIST AI RMF Generative AI Profile
- 文档：https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf
- **用法**：NIST于2024年7月发布的生成式AI专项治理配置文件（NIST.AI.600-1），在原18个控制项基础上新增12个生成式AI特有风险控制。本Day的营销AI用例（文案生成/深度合成）涉及生成式AI，此文档是延伸阅读。重点读 Section 4 (Generative AI Risks)。

---

## 2. EU AI Act（欧盟人工智能法案）

### EU AI Act 官方
- 官网：https://artificialintelligenceact.eu/
- **深链用法**：
  - [Article 5 禁止的AI实践](https://artificialintelligenceact.eu/annex/4/)：本Day TODO4 classify_eu_ai_act 的禁止清单规则源。营销AI中的工作场所情感识别、潜意识操纵属此类
  - [Annex III 高风险AI系统](https://artificialintelligenceact.eu/annex/3/)：高风险清单。营销AI中的保险定价（若涉及保险）属此类
  - [Article 50 透明度义务](https://artificialintelligenceact.eu/article/50/)：有限风险透明度义务。营销AI中的聊天机器人/AI生成内容/深度伪造需标注"AI生成"，是本Day营销用例的主要风险等级
  - [EU AI Act 全文（Official Journal）](https://eur-lex.europa.eu/eli/reg/2024/1689/oj)：法规原文，2024年8月1日生效，2026年分阶段执行

### EU AI Act 合规时间线
- 文档：https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai
- **用法**：EU AI Act的分阶段执行时间线。禁止条款（2025-02-02生效）/ 通用AI模型义务（2025-08-02生效）/ 高风险义务（2026-08-02生效）。营销AI需按时间线规划合规。

---

## 3. 中国AI法规体系

### 国家网信办AI法规
- **深链用法**：
  - [《生成式AI服务管理暂行办法》](https://www.cac.gov.cn/2023-07/13/c_1690898327029107.htm)：2023-08-15生效。本Day TODO4 classify_china_ai_law 的生成式AI备案规则源。营销AI文案生成工具可能需备案
  - [《算法推荐管理规定》](https://www.cac.gov.cn/2021-12/31/c_1643574110791945.htm)：2022-03-01生效。营销AI推荐系统需提供关闭选项和不针对个人特征的选项
  - [《深度合成管理规定》](https://www.cac.gov.cn/2022-12/11/c_1672221949354811.htm)：2023-01-10生效。营销AI深度合成广告需显著标识
  - [《个人信息保护法》](https://www.npc.gov.cn/npc/c30834/202108/a8c4e3672c74491a80b53a172bb753fe.shtml)：2021-11-01生效。营销AI用户画像/定向投放需知情同意+最小必要

---

## 4. 真实库 + 上机

### pydantic 官方文档与教程（已验证：pydantic/pydantic）
- 官方文档：https://docs.pydantic.dev/
- GitHub：https://github.com/pydantic/pydantic
- **深链用法**：
  - [BaseModel](https://docs.pydantic.dev/latest/concepts/models/)：对标 TODO1，定义 ControlItem 和 AIUseCase 的数据模型
  - [Field 约束](https://docs.pydantic.dev/latest/concepts/fields/)：对标 TODO1，`Field(ge=0, le=100)` 确保分数范围
  - [model_copy(update=...)](https://docs.pydantic.dev/latest/concepts/models/#auxiliary-functions)：对标 TODO3，pydantic v2 不可变更新（扫描后更新 score/status）

### pandas 官方文档与教程（已验证：pandas-dev/pandas）
- 官方文档：https://pandas.pydata.org/docs/
- GitHub：https://github.com/pandas-dev/pandas
- **深链用法**：
  - [DataFrame](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html)：对标 TODO5，构建治理台账
  - [pivot_table](https://pandas.pydata.org/docs/reference/api/pandas.pivot_table.html)：对标 TODO5，用例×功能透视NIST合规分数
  - [value_counts](https://pandas.pydata.org/docs/reference/api/pandas.Series.value_counts.html)：对标 TODO5，闭环状态分布统计

---

## 5. 2026 前沿：MCP治理即代码 + computer use治理风险 + 红队对标

### MCP（Model Context Protocol，Anthropic 2024）
- 官网：https://modelcontextprotocol.io/
- GitHub：https://github.com/modelcontextprotocol
- **深链用法**：
  - [MCP Specification](https://modelcontextprotocol.io/specification)：理解MCP协议规范，治理即代码的协议基础
  - [MCP Servers](https://github.com/modelcontextprotocol/servers)：参考MCP Server实现模式。生产环境的"合规检查MCP Server"和"审计日志MCP Server"可参考此仓库

### computer use 治理风险
- Anthropic computer use 文档：https://docs.anthropic.com/en/docs/build-with-claude/computer-use
- **用法**：2025年AI Agent获得的computer use能力带来的新型治理风险。权限边界模糊/操作不可逆/UI操作难审计。本Day notes.md中computer use治理风险表格的来源。

### garak + PyRIT（红队工具，Day 2已认知，本Day作治理对标）
- garak GitHub：https://github.com/NVIDIA/garak
- PyRIT GitHub：https://github.com/Azure/PyRIT
- **用法**：garak和PyRIT在NIST AI RMF中属于 **Measure层**（MEASURE-1评估方法选择 + MEASURE-2可信特征评估-安全性）。本Day治理框架是"覆盖四步的系统化方法论"，红队是Measure层的工具。两者互补。

---

## 阅读路径建议

| 顺序 | 材料 | 用途 | 时长 |
|:----:|------|------|:----:|
| 1 | 本 Day `notes.md` 理论回顾 + 独立教材 3.1-3.4 | 治理框架全景 | 1h |
| 2 | NIST AI RMF 1.0 PDF（Section 3 Core Functions） | 四步循环详解 | 0.5h |
| 3 | `starter.ipynb` 上机（配 pydantic + pandas 文档） | 真实库实操 | 2h |
| 4 | EU AI Act Article 5/Annex III/Article 50（选读） | 法律合规分级 | 0.5h |
| 5 | 中国网信办AI法规（选读 1-2部） | 中国合规要求 | 0.5h |
| 6 | MCP文档（选读 Specification） | 治理即代码认知 | 0.5h |

---

*全部深链已于 2026-07-25 验证存在。如发现失效，请在 Issues 报告。*
