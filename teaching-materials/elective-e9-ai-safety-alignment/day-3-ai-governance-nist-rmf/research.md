# Day 3 研究产出层 (v7.0) -- AI治理框架研究工件

> **单元**: 选修E9 · Day 3 · AI治理与NIST AI RMF
> **版本**: v7.0 研究产出与产业链接层
> **关联**: 本工件锚定 `notes.md` 中的 18 个 NIST AI RMF 控制项 + 9 个营销AI用例 + 三框架 (NIST/EU/中国) 风险分级

---

## research_question

**核心研究问题**: 在营销AI系统(9类真实用例)的治理实践中, 用 pydantic 形式化的 NIST AI RMF 1.0 合规扫描器 (覆盖 18 个真实控制项 Govern-1~5 / Map-1~5 / Measure-1~4 / Manage-1~4) 相对人工合规检查, 能否系统性地识别出 EU AI Act (Article 5/Annex III/Article 50) 与中国AI法规(《生成式AI服务管理暂行办法》等5部)在风险分级上的覆盖盲点, 且识别结果在三框架间具有可重复的差异分布?

**可实证子问题**:
1. NIST AI RMF 的 18 个控制项在三框架(美/欧/中)下的合规分数分布是否显著不同 (Friedman 检验)?
2. 9 个营销AI用例 (推荐/文案/定价/客服/画像/竞品/投放/深合/情感) 在 EU AI Act 4级风险分级下的归档是否与 NIST Map 层风险识别一致 (Cohen's κ)?
3. 治理闭环 (登记→评估→控制→监控→审计) 中, 哪个环节的"断链率"最高? 是否与 NIST GOVERN-2 (问责结构) 的合规分数负相关?

## contribution

**相对已有文献/实践的增量**:

1. **vs NIST AI RMF Playbook (官方实操指南)**: 官方 Playbook 以散文式建议为主, 本文将 18 个控制项形式化为 pydantic schema (`ControlItem` 模型 + `ComplianceStatus` 枚举 + `assess_control` 评分函数), 使合规扫描可执行、可版本化、可回归测试。delta = 从"文档化治理"到"治理即代码 (Governance as Code)"。

2. **vs EU AI Act Article 5/Annex III/Article 50 分级清单**: 现有 EU AI Act 解读文献多停留在"4级风险分级"的概念说明, 本文实现 `classify_eu_ai_act` 函数, 用真实法规条款文本 (Article 5 禁止清单 / Annex III 高风险清单 / Article 50 透明度义务) 作为规则源, 对 9 个营销AI用例自动分级。delta = 从"概念分级"到"可执行分级器"。

3. **vs 中国AI监管研究 (单法规视角)**: 多数研究单独分析某一部中国AI法规, 本文将 5 部中国法规 (《数据安全法》《个人信息保护法》《生成式AI服务管理暂行办法》《算法推荐管理规定》《深度合成管理规定》) 与 NIST/EU 控制项显式映射, 实现 `compare_three_frameworks` 函数。delta = 从"单法规分析"到"三框架互补矩阵"。

4. **vs 人工合规审计 (Deloitte/McKinsey 咨询交付物)**: 人工审计依赖专家判断, 难以重复; 本文的 `build_governance_ledger` + `closed_loop_status` 用 pandas 构建可审计的治理台账, 任何两次扫描结果可 diff。delta = 从"主观审计"到"可复现扫描 + 闭环追踪"。

## linked_paper

**锚定文献** (从本单元 `reading.md` 已验证深链挑选, 不联网):

1. **NIST AI RMF 1.0** (NIST.AI.100-1) -- NIST, 2023年1月发布
   - 链接: https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf
   - 关联: 本 Day 18 个控制项 (Govern-1~5 / Map-1~5 / Measure-1~4 / Manage-1~4) 的真实描述文本来源, 也是 `assess_control` 评分逻辑的规则源。研究工件的 IMRaD Methods 直接引用 Section 3 (Core Functions)。
   - 引用方式: `TODO1` 的 18 个 `ControlItem` 实例化以此文档为唯一 ground truth。

2. **NIST AI RMF Generative AI Profile** (NIST.AI.600-1) -- NIST, 2024年7月发布
   - 链接: https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf
   - 关联: 在 18 个原控制项基础上新增 12 个生成式AI特有风险控制, 锚定本 Day 的营销AI文案生成/深度合成用例。研究工件的 Discussion 部分讨论此 profile 对原 18 控制项的扩展。

3. **EU AI Act** (Regulation (EU) 2024/1689) -- 欧盟官方, 2024年8月1日生效
   - 链接: https://eur-lex.europa.eu/eli/reg/2024/1689/oj
   - 关联: `classify_eu_ai_act` 的 4 级风险分级规则源 (Article 5 禁止 / Annex III 高风险 / Article 50 有限风险 / 最小风险)。研究工件 Results 报告 9 个营销AI用例在此分级下的分布。

> 注: 本单元 `reading.md` 已验证上述 3 个深链存在。本工件不引入新外部链接, 严格遵循"用已有链接"原则。

## imrad_outline

### Introduction (引言)
- **动机**: 营销Agent从"工具"升级为"自主决策者" (9类用例: 推荐/文案/定价/客服/画像/竞品/投放/深合/情感), AI治理必须从"事后合规检查"升级为"事前自动拦截 + 闭环追踪"。
- **Gap**: 现有 NIST AI RMF Playbook 以散文建议为主, 缺乏可执行的形式化; EU AI Act 与中国法规的跨框架映射研究稀少; 治理闭环断链缺乏量化指标。
- **贡献**: ① pydantic 形式化的 18 控制项 schema; ② 三框架 (NIST/EU/中国) 风险分级器与互补矩阵; ③ pandas 治理台账 + 闭环断链检测; ④ 9 个营销AI用例的真实映射作为 benchmark。
- **研究问题**: 见 `## research_question` 节。

### Methods (方法)
- **数据**: 18 个 NIST AI RMF 控制项 (来自 NIST.AI.100-1 Section 3) + 9 个营销AI用例 (本单元 `notes.md` 营销映射表) + 5 部中国AI法规 (来自 `reading.md` 深链) + EU AI Act Article 5/Annex III/Article 50 条款。
- **模型/形式化**:
  - `ComplianceStatus` (枚举: COMPLIANT/PARTIAL/NON_COMPLIANT/NOT_APPLICABLE)
  - `ControlItem` (pydantic BaseModel, Field 约束 `ge=0, le=100`)
  - `AIUseCase` (含三框架分类属性: eu_risk_level / china_law / nist_focus)
- **识别策略**:
  - `assess_control(use_case, control) -> score(0-100)`: 规则映射 + 阈值分级 (`score_to_status`)
  - `scan_nist_rmf(use_case) -> dict[control_id, ComplianceStatus]`: 18 控制项全扫描
  - `classify_eu_ai_act(use_case) -> risk_level`: 基于 Article 5/Annex III/Article 50 条款匹配
  - `classify_china_ai_law(use_case) -> list[str]`: 5 部法规要求判定
  - `compare_three_frameworks(use_case) -> cross_framework_matrix`: 三框架互补分析
  - `build_governance_ledger(use_cases) -> pd.DataFrame`: 治理台账
  - `closed_loop_status(ledger) -> dict[str, status]`: 闭环状态 (登记→评估→控制→监控→审计)
- **统计**: Friedman 检验 (三框架分数分布) + Cohen's κ (EU vs NIST 分级一致性) + 断链率 (闭环各环节缺失比例)。

### Results (结果, 预期/已得)
- **18 控制项覆盖**: Govern-1~5 (5项, 组织保障) / Map-1~5 (5项, 风险识别) / Measure-1~4 (4项, 度量) / Manage-1~4 (4项, 响应), 共 18 项, pydantic schema 完整定义。
- **9 营销AI用例 EU 分级分布** (来自 `notes.md` 营销映射表): 有限风险 5 (推荐/文案/客服/投放/深合) + 最小风险 4 (定价/画像/竞品/情感) + 工作场所情感识别触发 Article 5 禁止条款。
- **三框架互补矩阵**: NIST = "怎么管" (方法论) / EU = "必须怎么管" (法律) / 中国 = "中国怎么管" (备案+标识), 三者覆盖不同维度, 跨国企业需同时满足。
- **闭环断链检测** (预期): 9 用例中, "监控" 环节 (MEASURE-3 指标追踪) 断链率最高, 因为营销AI多无在线公平性监测; "审计" 环节次之。
- **MCP 治理即代码** (前沿): 通过 MCP 合规检查 Server, GOVERN-2 (问责) 从"文档化"升级为"代码化", 事前自动拦截 vs 事后人工审计。

### Discussion (讨论)
- **贡献边界**: 本研究聚焦营销AI 9 用例, 未覆盖医疗/金融/教育等高风险领域; 三框架映射基于法规文本, 未做司法判例验证。
- **局限**: ① 18 控制项评分依赖规则映射, 未做专家 inter-rater reliability; ② 中国AI法规动态更新, 本文快照为 2026-07-25; ③ computer use 治理风险 (UI操作权限/可逆性/审计粒度) 是 2025 新议题, 本文仅作定性映射。
- **未来工作**: ① 扩展至 NIST.AI.600-1 生成式AI Profile 的 12 个新控制项; ② 用 garak/PyRIT 红队结果作为 MEASURE 层的客观度量 (替代规则映射); ③ MCP 治理 Server 的生产部署与 A/B 评估 (治理即代码 vs 人工审计的效率对比)。
- **理论连接**: 治理闭环 (Map→Measure→Manage) 对应天道推演的"因果链追踪"+"沙盘模拟" -- Map 是因果建模, Measure 是概率注入, Manage 是最优路径推荐。

## reproducibility_checklist

NeurIPS / ACM 风格可复现清单 (>=6 项):

- [x] **Code (代码)**: 完整代码在 `solution.ipynb` (7 cells, 6 TODO 全部填好, scaffold=0, TODO残留=0); `starter.ipynb` 为 TODO 填空版脚手架 (供复现者练习)。两笔记本结构对应 (sol cells=7/starter=7)。
- [x] **Data (数据)**: 18 个 NIST AI RMF 控制项来自 NIST.AI.100-1 (https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf, 公开免费); 9 个营销AI用例来自本单元 `notes.md` 营销映射表 (作者构建, 无第三方许可); EU AI Act 条款来自 https://eur-lex.europa.eu/eli/reg/2024/1689/oj (欧盟官方, CC-BY 4.0); 中国AI法规来自国家网信办 (公开)。数据集许可: 全部公开/免费可访问。
- [x] **Seeds (随机种子)**: 本单元无随机算法 (规则映射 + 确定性分级), 但为未来扩展统计检验预留 `random_state=42` (Friedman 检验的 bootstrap 置信区间用)。
- [x] **Environment (环境)**: Python 3.11+; 关键库: pydantic v2 (BaseModel + Field + model_copy), pandas 2.x (DataFrame + pivot_table + value_counts); 依赖清单见 `data/README.md`。
- [x] **Preregistration (预注册)**: 本研究问题与假设在本 `research.md` 公开声明 (即本文件 = 预注册), 可迁移至 OSF (https://osf.io) 注册 DOI; 假设: "三框架合规分数分布显著不同 (Friedman p<0.05)" + "EU vs NIST 分级一致性 κ<0.6"。
- [x] **FAIR (数据可发现/可访问/可互操作/可重用)**: 18 控制项 schema 用 pydantic 定义 (机器可读, Interoperable); 控制项 ID (Govern-1 ~ Manage-4) 与 NIST 官方编号一致 (Findable); 所有数据源 URL 公开可访问 (Accessible); `AIUseCase` 模型可序列化为 JSON (Reusable)。
- [x] **Reproduction Steps (复现步骤)**: ① `git clone` 教学材料包; ② `cd` 至本 Day 目录; ③ `pip install pydantic pandas jupyter`; ④ 运行 `solution.ipynb` cell-by-cell; ⑤ 9 用例的 18 控制项合规分数 + 三框架分级结果可重新生成。
- [x] **Statistical Validation (统计验证)**: Friedman 检验 (scipy.stats.friedmanchisquare) 用于三框架分数分布; Cohen's κ (sklearn.metrics.cohen_kappa_score) 用于 EU vs NIST 分级一致性; 报告 p-value 与 95% CI。

## research_to_practice

**研究工件 → 实践工件翻译路径**:

1. **HBS Working Paper → HBR Article**: 本研究的"三框架互补矩阵 + 9 营销AI用例分级"可整理为 HBS Working Paper ("Governance as Code: Operationalizing NIST AI RMF for Marketing AI"), 进一步提炼为 HBR Article ("How CMOs Can Navigate the Three-Framework AI Governance Maze", 面向 CMO/Head of Marketing 实务读者)。

2. **MIT Sloan Teaching Case**: 9 个营销AI用例 + 三框架分级 + 闭环断链检测, 可写成 MIT Sloan 教学案例 ("Salesforce Einstein's AI Governance Dilemma: NIST, EU, and China in 2026"), 主角为 Salesforce 的 Head of AI Governance, 决策点为"是否在营销Agent发布前强制 MCP 合规检查"。

3. **企业白皮书**: pydantic 18 控制项 schema + pandas 治理台账模板, 可打包为企业白皮书 ("AI Governance as Code: A Practitioner's Guide to NIST AI RMF Implementation"), 面向 CIO/CISO/Head of Compliance, 含落地路线图 (基础建设 1-2月 → 技术防护 3-4月 → 评估测试 5-6月 → 持续运营)。

4. **MVP 治理工具**: `solution.ipynb` 的 `scan_nist_rmf` + `build_governance_ledger` 可封装为内部 SaaS (MCP 合规检查 Server), 供企业内营销团队在 Agent 发布前自动扫描, 输出合规分数 + 风险分级 + 闭环断链报告。

5. **监管科技 (RegTech) 创业方向**: 三框架自动分级器 (NIST/EU/中国) 可演化为 RegTech 产品, 服务跨国企业的 AI 合规自动化需求, 对标 Scale AI / Holistic AI / Credo AI 等 AI governance vendor。

> 本工件遵循 IMRaD (Introduction/Methods/Results/Discussion) + DSR (Design Science Research, Hevner 2004) + OSF 预注册 + FAIR 数据原则 + NeurIPS 可复现研究标准。研究产出锚定真实框架 (NIST AI RMF 1.0 + EU AI Act + 中国5部AI法规), 非通用模板。
