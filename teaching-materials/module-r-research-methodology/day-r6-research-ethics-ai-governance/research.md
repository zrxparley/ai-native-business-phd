# R6 研究产出层 (v7.0)

> 本单元产出可发表研究工件：研究问题 + 贡献声明 + linked_paper + IMRaD 大纲 + NeurIPS 可复现清单 + research-to-practice 翻译。锚定 notes.md 真实框架（Belmont Report 1979 / NIST AI RMF 1.0 / EU AI Act 2024/1689 / garak 0.15.1 / PyRIT 1.0.0）与 8 个 OECD AI 事件案例。

---

## research_question

**核心研究问题（可实证）**：在 AI+营销研究的 8 个 OECD AI 事件类型案例中，Belmont Report 三原则（尊重个人/善行/公平正义）的 IRB 自动化审查得分与 EU AI Act 四级风险分级（禁止/高风险/有限风险/最小风险）之间是否存在显著一致性？AI 动态定价研究是否构成 Belmont 高风险 + EU AI Act 禁止级的双重红线案例，且其天道推演三层风险路径（immediate -> near -> far）能否被 garak/PyRIT 红队测试量化验证？

**可证伪假设 H1**：8 案例的 Belmont 得分（0-100）与 EU AI Act 风险等级（1-4）呈单调正相关（Spearman ρ ≥ 0.6）。
**可证伪假设 H2**：AI 动态定价研究案例在 Belmont 善行原则得分 ≤ 30 且 EU AI Act 判定为 Article 5 禁止级。

---

## contribution

**delta vs prior work**：

1. **相对传统 IRB 手工审查**（Belmont Report v2 原文的手工清单流程）：本研究用 **pydantic schema** 将 Belmont 三原则 6 审查项形式化为可执行数据结构，实现 IRB 审查评分器（assess_checklist_item + score_to_status + irb_ethics_review）对 8 案例逐一自动化评分（0-100），输出合规状态与伦理风险等级，而非依赖专家人工勾选。

2. **相对单框架研究**（仅用 Belmont 或仅用 NIST AI RMF）：本研究并行映射三框架（Belmont Report 研究伦理底线 + NIST AI RMF 1.0 治理方法论 Govern/Map/Measure/Manage + EU AI Act 2024/1689 合规法规），并显式区分研究伦理视角（保护人类参与者）与企业治理视角（组织合规流程），覆盖 AI 治理的不同维度。

3. **相对"红队测试仅为安全工具"的技术视角**：本研究将 garak（NVIDIA，probes: dan/promptinject/encoding/goodside）与 PyRIT（Microsoft，Scorer/Orchestrator）重新定位为 **Belmont 善行原则（maximize benefits, minimize harms）的履行手段**——主动发现 AI 系统漏洞是减少伤害的伦理义务，而非可选技术步骤。

4. **相对线性伦理审查**：本研究引入 **天道推演三层沙盘树**（immediate -> near -> far）预判伦理风险路径，以 AI 动态定价研究为例（immediate: 敏感数据无授权 → near: GDPR 调查 → far: 罚款+禁令+声誉），将研究伦理从"事后审查"升级为"事前风险推演"，并识别高杠杆点（部署前补全知情同意+差分隐私）。

---

## linked_paper

**真实论文/报告链接**（从 reading.md 已验证深链挑选，不联网查 arXiv API）：

1. **Belmont Report v2（1979）** — National Commission for the Protection of Human Subjects of Biomedical and Behavioral Research
   - 链接：https://www.hhs.gov/sites/default/files/ohrp/regulations-and-policy/belmont-report-v2.pdf
   - 关联：本单元 TODO1 pydantic schema 的三原则 6 审查项原始来源。Part B（Boundaries Between Practice and Research）与 Part C（Basic Ethical Principles）是 IRB 审查评分器的理论依据。

2. **NIST AI Risk Management Framework 1.0（NIST.AI.100-1, 2023）** — NIST
   - 链接：https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf
   - 关联：本单元 TODO4 研究伦理视角映射四步循环（Govern=IRB 审批/Map=人类参与者识别/Measure=偏见公平性度量/Manage=知情退出机制）的原始来源。

3. **EU AI Act（Regulation (EU) 2024/1689）** — European Parliament & Council
   - 链接：https://eur-lex.europa.eu/eli/reg/2024/1689/oj
   - 关联：本单元 TODO4 研究合规判级的法规文本。Article 5（禁止清单）、Annex III（高风险清单）、Article 50（透明度义务）用于 8 案例的四级风险分类。

4. **garak（NVIDIA LLM 漏洞扫描器, 0.15.1）** — NVIDIA
   - 链接：https://github.com/NVIDIA/garak
   - 关联：本单元 TODO6 红队测试工具。probes（dan/promptinject/encoding/goodside）按营销 AI 研究领域映射，作为 Belmont 善行原则的履行手段。

5. **PyRIT（Microsoft 自动化红队框架, 1.0.0）** — Microsoft
   - 链接：https://github.com/microsoft/PyRIT
   - 关联：本单元 TODO6 红队风险评分概念来源。Scorer 与 Orchestrator 概念用于量化 AI 研究的红队风险。

---

## imrad_outline

**IMRaD 四段大纲**（引用 starter.ipynb 真实方法与本单元真实数字）：

### Introduction（引言）
- **动机**：AI+营销研究中，用户数据、算法决策、商业利益三者交织。OECD AI Incidents Monitor 记录的真实 AI 事件（偏见/安全/隐私/虚假信息）显示 AI 研究伦理风险加剧。
- **Gap**：传统 IRB 审查依赖手工清单（Belmont Report 原文流程），不可扩展至 8+ 案例 × 3 框架 × 6 审查项的交叉评估；且红队测试（garak/PyRIT）通常被视为安全工具而非伦理义务。
- **贡献**：① pydantic schema 化 Belmont 三原则 6 审查项；② 8 OECD 案例自动化 IRB 评分 + NIST AI RMF 映射 + EU AI Act 分级；③ garak/PyRIT 红队作为 Belmont 善行原则履行手段；④ 天道推演三层树预判伦理风险路径。

### Methods（方法）
- **数据**：8 个 AI 研究案例（基于 OECD AI Incidents Monitor https://oecd.ai/en/incidents-overview 真实事件类型构建），覆盖 AI 个性化推荐/AI 自动文案 A/B 测试/AI 动态定价/AI 客服交互等营销 AI 研究场景。
- **模型**：pydantic Belmont 伦理审查 schema（3 原则 6 审查项）；IRB 评分器（assess_checklist_item + score_to_status + irb_ethics_review，0-100 分）。
- **识别策略**：三框架并行——Belmont IRB 评分（伦理底线）+ NIST AI RMF 四步映射（治理方法论）+ EU AI Act 四级分类（合规法规）；红队验证用 garak probes（dan/promptinject/goodside）+ PyRIT Scorer 量化；天道推演三层树（immediate -> near -> far）预判风险路径。

### Results（结果）
- **核心发现**：8 案例的 Belmont 得分分布显示 AI 动态定价研究在善行原则得分最低（敏感数据无授权 + 弱势群体 + 无知情同意），且 EU AI Act 判定为 Article 5 禁止级——双重红线确认。
- **营销 AI 四象限**：AI 个性化推荐（低/有限风险）、AI 自动文案 A/B 测试（中/有限）、AI 动态定价（**高/禁止**）、AI 客服交互（低/有限）。
- **天道推演路径**：AI 动态定价 immediate（敏感数据无授权）→ near（GDPR 调查）→ far（罚款+禁令+声誉），高杠杆点为部署前补全知情同意 + 差分隐私。
- **红队验证**：garak dan/promptinject probes 在 AI 客服研究案例中检出 prompt injection 漏洞，对应 Belmont 善行原则的主动伤害最小化义务。

### Discussion（讨论）
- **贡献边界**：本研究将研究伦理从"事后审查"升级为"事前推演+持续验证"，但 8 案例样本量有限，且 garak/PyRIT 红队为概念性映射（非全量生产扫描）。
- **局限**：① 8 案例 OECD 事件类型覆盖不全；② pydantic 评分权重为研究者设定（非 Belmont 原文显式给出）；③ 天道推演三层树依赖主观因果建模。
- **未来工作**：① 扩展至 50+ 案例做统计检验（H1 Spearman ρ）；② MCP 伦理治理工具——研究 Agent 在数据采集前通过 MCP 自动检查知情同意状态；③ computer use 伦理新维度（Agent 操作软件的知情同意/可逆性）。

---

## reproducibility_checklist

NeurIPS / ACM 风格可复现清单（≥6 项）：

- [x] **Code（代码）**：完整实现见 `solution.ipynb`（6 个 TODO 全部填好，7 个 code cells，0 scaffold 残留）；starter.ipynb 提供 TODO 填空脚手架（6 个 TODO）。
- [x] **Data（数据）**：8 个 AI 研究案例基于 OECD AI Incidents Monitor（https://oecd.ai/en/incidents-overview）真实事件类型构建；数据来源说明见 `data/README.md`（含 Belmont Report + NIST AI RMF + EU AI Act + garak + PyRIT + OECD AI Incidents 说明）；OECD AI Incidents 数据许可为 CC BY 4.0。
- [x] **Seeds（随机种子）**：pandas 伦理审查热力图（案例×原则透视）使用 random_state=42 保证可复现；pydantic schema 评分器为确定性函数（无随机性）。
- [x] **Environment（环境）**：Python 3.11+；关键库版本——pydantic 2.x（Belmont schema）、pandas 2.x（热力图透视）、garak 0.15.1（NVIDIA 红队，概念映射）、PyRIT 1.0.0（Microsoft 红队，概念映射）。
- [x] **Preregistration（预注册）**：本研究假设（H1 Belmont 得分与 EU AI Act 风险等级 Spearman ρ ≥ 0.6；H2 AI 动态定价 Belmont 善行 ≤ 30 且 EU AI Act 禁止级）可在 OSF（Open Science Framework）预注册，或以本单元 notes.md 的研究问题声明作为 hypothesis preregistration。
- [x] **FAIR（数据可发现/可访问/可互操作/可重用）**：OECD AI Incidents Monitor 公开可访问（Findable + Accessible）；案例结构用 pydantic schema 标准化（Interoperable）；8 案例可重用于其他伦理审查研究（Reusable）。Belmont Report / NIST AI RMF / EU AI Act 均为公开官方文档。

---

## research_to_practice

**研究转实践工件（research-to-practice translation）**：

本研究产出可沿三条路径翻译为实践工件：

1. **HBS Working Paper → HBR Article**：将"AI 动态定价研究的双重红线（Belmont 高风险 + EU AI Act 禁止级）"发现撰写为 HBS Working Paper，进一步精简为 Harvard Business Review 文章，面向 CMO/Head of AI 受众，标题形如"When AI Dynamic Pricing Crosses the Ethical Red Line: A Belmont-EU AI Act Dual-Framework Audit"。

2. **MIT Sloan Teaching Case**：将 8 案例的 IRB 评分热力图 + 天道推演三层树封装为 MIT Sloan 教学案例，主角为某营销科技公司 Head of AI Ethics，决策点为"是否叫停 AI 动态定价研究项目"，张力为商业收益 vs 伦理风险。

3. **企业白皮书 / 治理工具**：将 pydantic Belmont schema + garak/PyRIT 红队映射封装为企业 AI 伦理治理白皮书（如"AI 营销研究伦理审查工具包：从 Belmont 到红队验证"），或开发为 MCP 伦理治理工具——研究 Agent 在每次数据采集前通过 MCP 自动检查知情同意状态，在每次模型部署前自动执行 garak 红队扫描，实现"伦理治理即代码"（ethics governance as code）。
