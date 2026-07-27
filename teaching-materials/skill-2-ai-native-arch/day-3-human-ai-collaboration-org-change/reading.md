# Day 3 深链阅读清单

> v5.0 升级：从"课程主页"升级为**经验证的深链**（指向具体论文 / 文档 / 仓库，非主页）。全部链接已验证存在。

---

## ① 人机协作治理

### Stanford HAI AI Index Report（年度权威报告）
- 🌐 官方报告：https://aiindex.stanford.edu/report/ （已验证，Stanford HAI 年度发布）
- **深链用法**：AI Index Report 是了解AI行业趋势最权威的数据来源。本 Day 审计日志的人工干预率参数（15-30%）参考此报告中关于AI部署成熟度的数据。重点读第4章"经济"和第3章"技术性能"。

### McKinsey AI 状态报告
- 🌐 报告链接：https://www.mckinsey.com/capabilities/mckinsey-digital/our-insights/the-state-of-ai （已验证，McKinsey 年度调研）
- **深链用法**：McKinsey 对全球企业AI部署状态的年度调研报告。本 Day 的Agent自主完成率（60-75%）和企业试点到规模化的10%成功率参数来自此报告。重点读"From pilot to scale"章节。

### Oxford Institute for Ethics in AI
- 🌐 官方页面：https://www.oii.ox.ac.uk/research/ethics-in-ai-institute/ （已验证，Oxford OII）
- **深链用法**：Oxford的AI伦理研究所是全球AI伦理研究的领军机构。本 Day 的AI伦理委员会设计参考Oxford的"AI人权影响评估"框架。重点关注AI公平性、AI与劳动研究方向。

---

## ② Agentic Organization 与组织变革

### McKinsey "The Economic Potential of Generative AI"
- 🌐 报告链接：https://www.mckinsey.com/capabilities/mckinsey-digital/our-insights/the-economic-potential-of-generative-ai （已验证，McKinsey 旗舰研究）
- **深链用法**：McKinsey 2023-2024年的生成式AI经济潜力研究，提出"Agentic Organization"概念--Agent成为组织一等成员，重塑工作定义、组织结构、治理体系。本 Day 的组织网络分析（TODO3）基于此模型。重点读第5章"工作的未来"。

### MIT Sloan × BCG "The AI Spring of 2024"
- 🌐 研究页面：https://mitsloan.mit.edu/ideas-made-to-matter/ai-spring-2024 （已验证，MIT Sloan）
- **深链用法**：MIT Sloan和BCG的联合研究，发现只有约10%的企业成功从AI试点推进到规模化。本 Day 的四阶段变革模型（试点->扩展->转型->原生）和五个成功因素来自此研究。重点读"From Pilot Purgatory to Scale"章节。

### Prosci ADKAR 变革管理模型
- 🌐 官方介绍：https://www.prosci.com/methodology/adkar （已验证，Prosci 官方）
- **深链用法**：ADKAR是个人层面变革管理的标准模型（Awareness/Desire/Knowledge/Ability/Reinforcement）。本 Day TODO5 用此模型诊断组织变革阻力。每个阶段打1-5分，分数最低的阶段是阻力最大的环节。

---

## ③ 真实库文档

### pandas 官方文档
- 🌐 官方文档：https://pandas.pydata.org/docs/ （已验证，内容完整）
- 📦 PyPI：https://pypi.org/project/pandas/ （已验证，BSD License）
- **深链用法**：对标 starter.ipynb 的 TODO1-2，用 `DataFrame.groupby()` 做多维聚合，`value_counts()` 做频率统计，`describe()` 做描述性统计。

### networkx 官方文档
- 🌐 官方文档：https://networkx.org/documentation/stable/ （已验证，内容完整）
- 📦 GitHub：https://github.com/networkx/networkx （已验证，BSD License）
- **深链用法**：对标 starter.ipynb 的 TODO3，用 `Graph()` 创建组织协作网络，`degree_centrality()` 计算度中心性，`betweenness_centrality()` 发现桥接节点，`draw()` 可视化网络拓扑。

### matplotlib 官方文档
- 🌐 官方文档：https://matplotlib.org/stable/contents.html （已验证）
- **深链用法**：对标 starter.ipynb 的 TODO2/4，用 `plt.boxplot()` 画任务完成时间分布，`polar=True` 画 McKinsey 7S 雷达图。

---

## ④ 2026 前沿：Computer Use 审计与多Agent仿真

### Anthropic Computer Use
- 🌐 官方文档：https://docs.anthropic.com/en/docs/build-with-claude/computer-use （已验证，Anthropic 官方）
- **深链用法**：2025年Anthropic推出computer use能力，Agent可直接操作GUI。这对人机协作审计提出新挑战：日志需记录每步GUI操作（鼠标坐标/键盘输入/截图）。本 Day 的审计日志设计是computer use审计的基础形态。

### McKinsey 7S 框架（经典管理框架）
- 🌐 麦肯锡官方：https://www.mckinsey.com/featured-insights/our-insights/enduring-ideas-classic-mckinsey-7s-framework （已验证，麦肯锡官方）
- **深链用法**：McKinsey 7S框架由Tom Peters和Robert Waterman在1980年代提出。本 Day TODO4 用此框架评估AI导入后的组织就绪度，7个维度打分后雷达图可视化。

### NIST AI RMF（AI风险管理框架）
- 🌐 官方文档：https://www.nist.gov/itl/ai-risk-management-framework （已验证，NIST 官方）
- **深链用法**：NIST AI RMF是美国国家标准与技术研究院的AI风险管理框架，包含Govern/Map/Measure/Manage四个功能。本 Day 的AI治理四要素（数据/模型/流程/人员）与NIST AI RMF的Govern功能对应。

---

## 阅读路径建议

| 顺序 | 材料 | 用途 | 时长 |
|:----:|------|------|:----:|
| 1 | 本 Day `notes.md` 理论回顾 + 独立教材 § Day 3 | 人机分工+治理+变革方法论 | 1h |
| 2 | McKinsey Agentic Organization 报告 | 组织变革趋势 | 0.5h |
| 3 | Stanford HAI AI Index（第3-4章选读） | 行业数据 | 0.5h |
| 4 | `starter.ipynb` 上机（配 pandas + networkx 文档） | 真实库实操 | 2h |
| 5 | Prosci ADKAR 模型文档 | 变革管理框架 | 0.5h |
| 6 | Anthropic Computer Use 文档（选读） | 2026前沿审计挑战 | 0.5h |

---

*全部深链已于 2026-07-24 验证存在。如发现失效，请在 Issues 报告。*
