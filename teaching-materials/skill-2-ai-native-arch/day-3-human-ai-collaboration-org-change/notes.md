# 技能2 · Day 3：人机协作治理 + 组织变革 · 讲义（v5.0 学习材料包版）

> **所属**：AI原生化商业博士 · 技能2 AI原生企业架构 · Day 3
> **版本**：v5.0（从独立教材升级为学习材料包）
> **预计**：2h 讲义 + 2h 上机练习
> **核心命题**：AI Agent 成为组织一等成员后，如何设计人机分工？如何用审计日志数据驱动治理决策？如何用组织变革模型预判阻力路径？
> **v5.0 升级点**：① 新增真实库上机（pandas + matplotlib + networkx 分析人机协作审计日志）② 新增 TODO 填空式起始笔记本 ③ Notebook 化 ④ 深链阅读 ⑤ 2026 前沿（Agentic Organization + computer use 审计 + 天道推演×组织变革）

---

## 学习目标（学完你能做到）

1. 能解释人机分工矩阵的二维框架（任务复杂度 × AI成熟度），并为营销领域的 8 类任务选择正确的分工模式（人类主导 / 人机协作 / AI主导）
2. 能用 **pandas** 加载和分析人机协作审计日志（audit log），计算人工干预率、Agent自主完成率、人工修正率、任务完成时间分布，并用 **matplotlib** 可视化对比不同分工模式的效率
3. 能用 **networkx** 构建组织协作网络（节点=角色含人/Agent，边=协作关系），计算度中心性识别关键节点，发现桥接节点（信息瓶颈/协作枢纽）
4. 能用 **McKinsey 7S 框架**（Strategy/Structure/Systems/Shared Values/Skills/Style/Staff）评估AI导入后的组织就绪度，识别7个维度的薄弱环节
5. 能用 **ADKAR 变革管理模型**（Awareness/Desire/Knowledge/Ability/Reinforcement）诊断组织变革阻力，并用**天道推演**预判阻力扩散路径与临界点

---

## 理论部分：精炼索引（详见独立教材）

> Day 3 的完整理论讲义见 [`../../AI原生化商业博士_独立教材_技能2_AI原生企业架构.md` § Day 3](../../AI原生化商业博士_独立教材_技能2_AI原生企业架构.md)（§一 人机分工矩阵 / §二 AI治理四要素 / §三 Oxford AI伦理框架 / §四 Stanford HAI以人为本框架 / §五 AI伦理委员会 / §六 变革管理从试点到规模化）。本讲义不重复，仅做上机所需的关键回顾。

### 关键回顾 1：人机分工矩阵

| | AI成熟度低 | AI成熟度中 | AI成熟度高 |
|---|---|---|---|
| **任务复杂度高** | 人类主导 | 人机协作（人审核） | 人机协作（AI建议，人决策） |
| **任务复杂度中** | 人机协作（AI辅助） | 人机协作（AI主导，人监督） | AI主导，人例外处理 |
| **任务复杂度低** | 人类执行 | AI辅助执行 | AI全自动 |

**核心洞察**：分工不是"能替代就替代"，而是基于任务复杂度和AI成熟度的系统化设计。营销领域8类任务各有最佳分工模式。审计日志的作用是**用数据验证分工设计是否合理**--如果某类"AI主导"任务的人工干预率超过30%，说明AI成熟度被高估，需要重新划入"人机协作"。

### 关键回顾 2：AI治理四要素

| 要素 | 核心要求 | 审计日志的角色 |
|:----:|---------|---------------|
| 数据治理 | 来源合规、质量保障、偏见检测 | 日志记录数据来源和使用范围 |
| 模型治理 | 评估标准、版本管理、漂移监测 | 日志追踪模型版本和输出质量 |
| 流程治理 | 审批流程、上线评估、事件响应 | 日志是流程合规的审计证据 |
| 人员治理 | AI素养、角色责任、问责机制 | 日志记录"谁在何时干预了什么" |

**审计日志是AI治理的"黑匣子"**：就像飞行数据记录器一样，记录每一次人机协作的完整过程，用于事后追溯、责任界定和持续改进。

### 关键回顾 3：变革管理 -- 从试点到规模化

**MIT Sloan × BCG 四阶段模型**：试点(Pilot) -> 扩展(Scale) -> 转型(Transform) -> 原生(Native)

**关键数据**：只有约10%的企业成功从试点推进到规模化，90%卡在"试点陷阱"（Pilot Purgatory）。

**五个关键成功因素**：高管战略承诺、业务-技术协同、人才能力建设、数据基础设施、变革沟通。

**天道推演视角**：组织变革是一个有阻力的动力学系统。用天道推演可以：
1. 识别阻力源（哪些角色、哪些部门最可能抵抗）
2. 模拟阻力扩散路径（个体焦虑 -> 团队消极 -> 部门对抗）
3. 预判临界点（何时阻力达到不可逆阈值，需要提前干预）
4. 设计高杠杆干预（小投入改变大局的关键节点）

---

## 上机部分：用 pandas + networkx 分析人机协作审计日志

> 📓 **配套笔记本**：[`starter.ipynb`](./starter.ipynb)（TODO 填空版，你来做）｜ [`solution.ipynb`](./solution.ipynb)（参考答案，gated，做完再看）
> 📊 **真实数据/库**：[`data/README.md`](./data/README.md)（pandas + matplotlib + networkx 库 + 人机协作审计日志样本）

### 为什么用真实库（pandas + networkx）而非手写分析脚本

v4.0 的代码用"手写 for 循环 + 字典统计"--手写统计只能做单维度计数，无法做 DataFrame 级别的多维切片聚合，无法做网络拓扑分析。v5.0 改用真实数据分析库：

- **pandas**（PyPI 持续更新，BSD License）：DataFrame 结构化分析，`groupby` 多维聚合，`value_counts` 频率统计，是数据分析的事实标准
- **matplotlib**（PyPI 持续更新，PSF License）：出版级数据可视化，柱状图/饼图/箱线图/雷达图
- **networkx**（PyPI 持续更新，BSD License）：图论与网络分析，`degree_centrality` 度中心性，`betweenness_centrality` 桥接中心性，是组织网络分析的标准工具

> **框架补充**：McKinsey 7S 框架和 ADKAR 模型是真实管理咨询框架（McKinsey 1980年代提出 7S；Prosci 2003年提出 ADKAR），上机用 Python 对其评分进行量化和可视化。

### 营销映射（关键桥接）

企业营销团队导入AI Agent后的人机协作场景：

| 协作环节 | 执行者 | 分工模式 | 审计关注点 |
|---------|--------|---------|-----------|
| 营销策划 | 人（营销策划师） | 人类主导 | 策略方向是否被AI误导 |
| 文案生成 | Agent（LLM） | AI主导，人监督 | 品牌调性/合规性人工修正率 |
| 合规审核 | 人（法务/合规） | 人类主导 | 审核通过率和驳回原因 |
| 投放优化 | Agent（优化算法） | AI主导，人例外 | 人工干预频率和原因 |
| 效果归因 | 人机协作 | 人机协作 | 因果解读是否依赖人 |

审计日志分析回答：哪类任务Agent自主完成率高？哪类需频繁人工干预？组织变革后角色如何重塑？

### 上机任务（6 个 TODO，见 starter.ipynb）

1. **TODO1**：用 pandas 加载审计日志，计算人工干预率/Agent自主完成率/人工修正率
2. **TODO2**：用 matplotlib 可视化任务完成时间分布，对比不同分工模式的效率
3. **TODO3**：用 networkx 构建组织协作网络，计算度中心性，发现桥接节点
4. **TODO4**：用 McKinsey 7S 框架评估组织AI就绪度，雷达图可视化薄弱维度
5. **TODO5**：用 ADKAR 模型诊断变革阻力，识别阻力最大的阶段
6. **TODO6**：用天道推演模拟组织变革阻力扩散路径，预判临界点

---

## 2026 前沿补充：Agentic Organization + Computer Use 审计

> v5.0 新增前沿点。2024-2026 年组织形态正在经历范式转移：Agent 从"工具"升级为"组织成员"。

**Agentic Organization（McKinsey 提出）**：2024年McKinsey在"The economic potential of generative AI"研究中提出，Agent 成为组织的一等成员（first-class member），重塑组织架构的三个维度：工作重新定义（岗位拆解为任务）、结构重新设计（树形->网络）、治理重新构建（人机协作+可审计+渐进授权）。这意味着组织网络分析（本Day上机TODO3）不再是可选技能，而是组织设计的核心方法。

**Computer Use / 计算机使用**：2025年Anthropic推出computer use能力，Agent可以直接操作GUI（点击、输入、截图），带来人机协作的新模式和审计挑战。当Agent自主操作GUI时，审计日志需要记录每一步GUI操作（鼠标坐标、键盘输入、屏幕截图），人工干预从"审核内容"扩展到"审核操作过程"。这对审计日志的粒度和可追溯性提出了更高要求。

**天道推演×组织变革**：传统变革管理模型（如ADKAR）是静态的--告诉你"当前在哪个阶段"。天道推演是动态的--模拟不同干预策略下，组织变革的阻力如何演化，预判临界点。这是将管理咨询框架升级为"可推演的动力学系统"的关键能力。用多Agent仿真可以模拟组织成员的个体行为和群体动力学，预判变革阻力扩散路径。

> 🔗 深入阅读见 [`reading.md`](./reading.md) 的 McKinsey Agentic Organization / Stanford HAI AI Index / computer use 审计条目。

---

## 与后续 Day 的衔接

- **Day 1-2**：从流程驱动到智能驱动 + Agent编排架构--今天的人机分工设计基于Day 1-2的Agent能力分析
- **Day 4**：企业级架构参考设计 + 行动研究--今天的治理体系是Day 4架构设计的治理层基础
- **技能5**：Agentic系统工程与落地--今天的审计日志设计是Day 5生产化可观测性的业务层补充

---

## 作业与评估

作业、5分制量表、费曼演练、2分钟话术、复盘自诊表--沿用独立教材 § Day 3 既有设计。本学习材料包不重复，仅新增上机交付物：

**新增交付物（v5.0）**：
- [ ] 完成的 `starter.ipynb`（6 个 TODO 全部填好，能跑通）
- [ ] 一段 300 字分析：你的营销团队审计日志显示哪类任务的人工干预率最高？根因是什么？（AI成熟度不足？任务复杂度过高？治理流程问题？）
- [ ] （可选）用天道推演设计一个组织变革干预方案：识别1个高杠杆干预点，推演3层未来走向

---

*本讲义由 v5.0 学习材料包升级生成。理论部分引用独立教材，上机部分用真实库（pandas + matplotlib + networkx）+ TODO 脚手架。*
*最后更新：2026-07-24*

---

## 学习科学层 (v6.0)

> v6.0 升级：在 v5.0 "真实即严谨 · 练习即掌握" 之上，加 **科学即高效 · 反馈即成长** 层。用学习科学把"练习"升级为"刻意练习 + 间隔重复 + 建构对齐 + 牛津tutorial 仿真"。
>
> **4 个新文件 (本单元新增):**
> - `practice.md` - Ericsson **刻意练习** (deliberate practice) + MIT 4C/ID + Worked-Faded 渐退示范 + interleaving **交叉**练习 (A1B1C1...B2C2A2...C3A3B3) + weak_loop 弱项循环 + retry_policy
> - `schedule.json` - **FSRS-6** (SM-2 backup) **间隔重复** (spaced retrieval) 算法, request_retention=0.9, 6 cards 覆盖人机分工矩阵/pandas聚合/networkx中心性/7S/ADKAR/天道推演, due [1,3,8,21,60,180], EF0=2.5
> - `alignment.md` - Biggs **建构对齐** (constructive alignment) ILO↔TLA↔AT 矩阵 + **mastery** threshold + 3 自检 (Feed Up/Back/Forward)
> - `tutorial.ipynb` - **牛津tutorial** LLM 仿真 (Oxford tutorial fellow persona, **Socratic** 苏格拉底追问, 禁直接答案, devil's advocate, 4 轮 scaffold 渐退, **Hattie** 四级 [TASK]/[PROCESS]/[SELF-REG]/[FEED-FORWARD] formative feedback, student_model.json 跨单元记忆, 限频 1次/天防依赖)
>
> **研究依据:** Ericsson deliberate practice 5 要素 / FSRS-6 (open-spaced/fsrs4anki 21 weights) / SM-2 (Wozniak 1985) / Biggs & Tang (2011) / Hattie & Timperley (2007) RER 77(1):81-112 / Butler 2010 retrieval practice (提取练习 68% vs 重学 44%) / Oxford PPE tutorial + Cambridge supervision 1对1-3 / arxiv 2024-2025 Socratic LLM 论文 / MIT 6.5940 mastery 阈值 / Christensen Center HBS devil's advocate / Vygotsky 共构->内化
>
> **不破坏 v5.0 基线:** notes.md/reading.md/data/starter.ipynb/solution.ipynb 全部保留，v6.0 仅追加 4 新文件 + 本节。verify_unit.py 7/7 + verify_v6_unit.py 5/5 = 12/12 收敛。

---

## 研究产出与产业链接层 (v7.0)

本单元产出可发表研究工件 (research.md: 研究问题+贡献声明+arXiv链接+IMRaD大纲+NeurIPS可复现清单+research-to-practice翻译) 与产业链接 (industry.md: >=3真实企业+部署场景+Imperial咨询项目+HBS教学案例+客座讲座+实习指针)。研究产出遵循IMRaD/DSR(Hevner)/OSF预注册/FAIR/可复现研究标准; 产业链接遵循Imperial MSc BA咨询项目(Burberry/Expedia/J&J)/HBS案例法/MIT Sloan行动学习模式。详见 research.md 与 industry.md。

---

## 学术前沿层 (v9.0)

本单元新增 `frontier.md`：注入 2025-2026 最新学术前沿（N 篇真实 arXiv 论文 + 批判性综述 + delta_to_unit + ≥3 开放研究问题 + 方法论批评）。论文来自 `_frontier_corpus/skill-2-ai-native-arch.md` 共享语料库（arXiv 搜索 + abstract 页抽查验证），覆盖前沿课题：企业Agent编排 × MCP/A2A 标准化协议。面向博后/教授级读者：批判性综述非罗列，delta_to_unit 显式指出前沿如何更新本单元所教，开放问题为可发表研究方向。详见 `frontier.md`。

---

## AI工程从零构建层 (v11.0)

> v11.0 新增 [`from_scratch.md`](./from_scratch.md)：AI工程从零构建，与本单元 pandas + networkx + LangGraph interrupt 形成对照。
> - **从零构建主题**：手写 HITL interrupt 工作流 + 审批门控 + 人工干预率统计
> - **核心算法**：interrupt_before 等待状态机 + 审批门控 $\text{gate}(s) = \text{approved}(s) \lor \text{rev} \ge r_{\max}$ + 干预率 $r_k = \frac{1}{|T_k|}\sum \mathbb{1}[\text{human}]$（含数学推导 + LaTeX）
> - **code_artifact**：手写 numpy 骨架，imports ⊆ {numpy, typing}，附 verification_property
> - **延伸阅读**：rohitg00 AI工程 from scratch P14 Agent Engineering（Anthropic Workflow Patterns / REWOO Plan and Execute）
> - **手写实现要点**：用 from-scratch numpy + dict 而非 LangGraph interrupt_before + pandas groupby，理解到 HITL 等待状态机的金属层
> - **verification_property**：interrupt 在 approve 前暂停；resume 跳过首节点中断检查执行被暂停节点；干预率 0.4>0.3 触发降级
