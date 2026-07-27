# 研究产出层 (v7.0) · 人机协作治理 + 组织变革

> 本单元 v5.0/v6.0 已建好上机脚手架（pandas + networkx + McKinsey 7S + ADKAR + 天道推演）。v7.0 将其升级为**可发表研究工件**：研究问题可实证、贡献显式声明、引用已记录深链、IMRaD 大纲对齐 `solution.ipynb` 真实方法、NeurIPS/ACM 可复现清单、research-to-practice 翻译路径。

---

## research_question

> **核心研究问题（一句话，可实证）**：在人机协作审计日志数据上，AI Agent 自主完成率（60-75%，McKinsey 2024）与人工干预率（15-30%，Stanford HAI AI Index）的差距，能否用 McKinsey 7S 七维就绪度评分与 ADKAR 五阶段阻力评分联合预测，从而识别"试点陷阱"（Pilot Purgatory，仅约10%企业从试点推进到规模化，MIT Sloan × BCG 2024）的关键组织阻力源？

此问题可实证：以审计日志的"分工模式 × 干预率"为因变量，以 7S/ADKAR 评分为自变量，做回归或因果森林；用 networkx 度中心性识别桥接节点是否为变革阻力扩散的"高杠杆点"。本单元 `starter.ipynb` TODO1-6 已为此铺好数据与代码骨架。

---

## contribution

> **Delta vs prior work（显式声明增量）**

1. **相对 Prosci ADKAR 静态模型（2003）**：ADKAR 只告诉组织"当前在哪个阶段"。本研究用 pandas 多维切片 + 天道推演多Agent仿真，把 ADKAR 从**静态诊断**升级为**可推演的动力学系统**，模拟不同干预策略下阻力扩散路径与临界点。
2. **相对 McKinsey Agentic Organization 报告（2024，定性案例研究）**：McKinsey 报告用案例访谈论证 Agent 成为组织一等成员。本研究用真实审计日志（pandas DataFrame + groupby 聚合）+ networkx 拓扑分析，把"Agent 是组织节点"从**定性命题**升级为**可量化的网络节点**（度中心性、桥接中心性）。
3. **相对 MIT Sloan × BCG "AI Spring 2024"（10% 试点成功率宏观数据）**：该研究给出宏观比例但不解释**为什么 90% 卡住**。本研究在审计日志+7S+ADKAR 联合数据上做识别，定位"哪个 7S 维度薄弱 + 哪个 ADKAR 阶段阻力"导致卡点，提供**微观因果机制**。
4. **相对 Oxford AI Ethics Institute 框架（伦理原则层）**：Oxford 给原则，本研究给**可执行审计日志 schema**（谁在何时干预了什么 + Agent 自主操作 GUI 的鼠标/键盘/截图轨迹，对接 Anthropic Computer Use 2025 审计粒度要求）。

---

## linked_paper

> 从 `notes.md` / `reading.md` 已记录的深链挑选，不联网查。

1. **McKinsey. "The Economic Potential of Generative AI"** (2023-2024)
   - 链接：https://www.mckinsey.com/capabilities/mckinsey-digital/our-insights/the-economic-potential-of-generative-ai
   - 关联：提出 "Agentic Organization" 概念，Agent 成为组织一等成员，重塑工作定义/结构/治理。本研究的 networkx 组织网络节点（人+Agent）直接锚定此概念。
2. **MIT Sloan × BCG. "The AI Spring of 2024"**
   - 链接：https://mitsloan.mit.edu/ideas-made-to-matter/ai-spring-2024
   - 关联：给出 10% 试点到规模化成功率与"From Pilot Purgatory to Scale"五因素。本研究用它作为研究问题的"被解释现象"。
3. **Stanford HAI. "AI Index Report"** (年度)
   - 链接：https://aiindex.stanford.edu/report/
   - 关联：第3章技术性能 + 第4章经济数据。本研究的 15-30% 人工干预率、60-75% Agent 自主完成率参数来源。
4. **Anthropic. "Computer Use" 文档** (2025)
   - 链接：https://docs.anthropic.com/en/docs/build-with-claude/computer-use
   - 关联：Agent 直接操作 GUI 带来审计新挑战（鼠标坐标/键盘输入/截图）。本研究审计日志 schema 扩展到 computer use 粒度。
5. **Prosci. "ADKAR Change Management Methodology"**
   - 链接：https://www.prosci.com/methodology/adkar
   - 关联：个人层面变革管理标准模型。本研究将其升级为可推演动力学系统。

---

## imrad_outline

> IMRaD 四段大纲，引用 `starter.ipynb`/`solution.ipynb` 真实方法与本单元真实数字。

### Introduction
- **动机**：Agent 成为组织一等成员（McKinsey Agentic Organization），但 90% 企业卡在"试点陷阱"（MIT Sloan × BCG）。组织变革阻力不可观测，传统 ADKAR 只做静态诊断。
- **Gap**：缺一个用审计日志数据 + 组织网络拓扑 + 变革阻力评分**联合识别**卡点的方法。
- **贡献**：本文提出 7S-ADKAR-AuditLog 三角识别框架，用 pandas + networkx + 天道推演多Agent仿真，在真实审计日志上验证。

### Methods
- **数据**：人机协作审计日志样本（`data/README.md`），含 task_id / executor（人/Agent）/ mode（分工模式）/ intervention_count / completion_time / 7S 七维评分 / ADKAR 五阶段评分 / 协作网络边表。
- **模型**：
  - pandas `groupby(['mode','executor'])` 计算人工干预率、Agent 自主完成率、人工修正率（TODO1）
  - matplotlib `boxplot` 对比分工模式完成时间分布（TODO2）
  - networkx `Graph()` + `degree_centrality()` + `betweenness_centrality()` 识别桥接节点（TODO3）
  - McKinsey 7S 雷达图（TODO4）+ ADKAR 阻力诊断（TODO5）
  - 天道推演多Agent仿真阻力扩散路径（TODO6）
- **识别策略**：以 7S 薄弱维度 + ADKAR 低分阶段作为自变量，以"分工模式干预率超阈值（>30%即高估 AI 成熟度）"为因变量，回归识别关键卡点；用 networkx 桥接节点作为高杠杆干预候选。

### Results
- **预期/已得核心发现**（锚定本单元真实数字）：
  - Agent 自主完成率 60-75%（McKinsey），人工干预率 15-30%（Stanford HAI），二者差距约 40-45 个百分点。
  - "AI 主导"任务若人工干预率 >30% → AI 成熟度被高估，需降级为"人机协作"。
  - networkx 桥接节点（高 betweenness）通常是变革阻力扩散的高杠杆点；干预该节点阻力扩散概率下降最大。
  - 7S 中 Shared Values 与 Skills 两维最薄弱时，ADKAR 的 Knowledge/Ability 阶段阻力最大，对应"试点陷阱"。

### Discussion
- **贡献边界**：本框架是观测性研究，因果识别需配合 A/B 或准实验（如 staggered rollout）；天道推演仿真的 agent 行为规则需用真实组织问卷校准。
- **局限**：审计日志样本量小（单组织），跨组织泛化需多企业数据；computer use 审计粒度（鼠标/键盘/截图）数据量是文本日志的 100-1000 倍，存储与隐私需重新设计。
- **未来工作**：用 causaldata NSW ATE=1794 风格的因果识别在审计日志上做反事实；与 NIST AI RMF 的 Govern/Map/Measure/Manage 四功能对齐。

---

## reproducibility_checklist

> NeurIPS / ACM 风格可复现清单（>=6 项）。

- [x] **Code（代码）**：完整代码在 `solution.ipynb`（8 个 code cell，对应 TODO1-6 + 初始化 + 可视化），`starter.ipynb` 为 TODO 填空版脚手架。
- [x] **Data（数据）**：人机协作审计日志样本，见 `data/README.md`，含来源说明（McKinsey 60-75% 自主率参数 + Stanford HAI 15-30% 干预率参数）、许可声明（pandas/networkx/matplotlib 均 BSD/PSF License）。
- [x] **Seeds（随机种子）**：networkx 布局与天道推演多Agent仿真使用 `random_state=42`（numpy `np.random.seed(42)`，networkx `nx.spring_layout(G, seed=42)`），保证网络可视化与仿真可复现。
- [x] **Environment（环境）**：Python 3.11 + pandas 2.x + networkx 3.x + matplotlib 3.x + numpy 1.26；`requirements.txt` 风格在 `data/README.md` 声明。
- [x] **Preregistration（预注册）**：本研究假设在 OSF 预注册风格声明 -- H1: 7S Shared Values 评分 < 3 时，ADKAR Desire 阶段阻力评分 < 3 的概率 > 70%；H2: networkx betweenness 前 10% 节点干预后，阻力扩散临界点延后至少 1 个时间步。本 notes.md 即 hypothesis 注册载体。
- [x] **FAIR（数据原则）**：Findable（`data/README.md` 索引）/ Accessible（pandas/networkx 均开源 PyPI）/ Interoperable（CSV + JSON 标准格式）/ Reusable（BSD/PSF License + 完整文档）。
- [x] **Randomization & Identification**：天道推演仿真采用贝叶斯主观概率注入，不确定性标注已知盲点；观测数据用 7S+ADKAR 联合回归识别，不claim纯因果。

---

## research_to_practice

> 研究如何翻译为实践工件。

本研究产出可沿三条路径翻译为实践：

1. **HBS Working Paper → HBR Article**：将 7S-ADKAR-AuditLog 三角识别框架写成 HBS Working Paper（学术严谨，IMRaD 完整），再浓缩为 Harvard Business Review 文章（如 "Why 90% of AI Pilots Stall—and How Network Centrality Predicts the Blockers"），面向 CMO/Head of AI 决策者。
2. **MIT Sloan Teaching Case**：以本单元营销团队导入 AI Agent 审计日志为素材，写 MIT Sloan 风格教学案例（protagonist = 营销 VP，decision = 是否将"AI 主导"任务降级为"人机协作"，tension = 效率 vs 合规）。案例可直接用于 Day 3 课堂讨论。
3. **企业白皮书**：与 McKinsey/BCG/Deloitte 合作出"Agentic Organization 治理白皮书"，把 7S-ADKAR-AuditLog 框架落地为企业自评工具（含 Excel/Streamlit 评分表 + 审计日志 schema 模板 + computer use 审计扩展规范）。

这三条路径分别对应学术发表、教学应用、产业标准化，覆盖研究产出的全生命周期，符合 Imperial MSc BA 行动学习与 HBS 案例法的双重标准。
