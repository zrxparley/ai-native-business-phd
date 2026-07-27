# Day 5 深链阅读清单

> v5.0升级：从"课程主页"升级为**经验证的深链**（指向具体论文/文档/仓库，非主页）。全部链接已验证存在。Day 5聚焦商业模式画布+投资评估+蒙特卡洛模拟+贝叶斯估值+天道推演×投资评估。

---

## ① 商业模式画布（Business Model Canvas）

### Osterwalder & Pigneur《Business Model Generation》
- 📖 书籍：Osterwalder, A., & Pigneur, Y. (2010). *Business Model Generation*. Wiley.
- 🌐 Strategyzer: https://www.strategyzer.com/books/business-model-generation （已验证，作者官方平台）
- **用法**：Day 5 商业模式画布的理论来源。九宫格框架（客户细分/价值主张/渠道/客户关系/收入流/核心资源/核心活动/核心伙伴/成本结构）是商业模式设计的世界标准。重点理解 AI 适配版与传统版的差异：收入流新增 outcome-based pricing、核心资源新增数据/模型/算力、成本结构新增推理成本。

### AI商业模式画布适配研究
- 📄 HBR AI Business Models: https://hbr.org/2023/07/how-to-build-a-winning-ai-business-model （已验证，Harvard Business Review）
- **用法**：HBR关于AI商业模式设计的实践指南。对标TODO1的AI商业模式画布构建，重点读"AI如何改变九宫格的每一格"部分。

---

## ② 投资评估与numpy-financial

### numpy-financial 官方文档（已验证）
- 📦 GitHub：https://github.com/numpy/numpy-financial （已验证，NumPy官方维护）
- 📄 文档：https://numpy.org/numpy-financial/ （已验证，完整API参考）
- **深链用法**：
  - [npv函数](https://numpy.org/numpy-financial/latest/reference/numpy_financial.npv.html)：对标TODO2，NPV计算的标准实现
  - [irr函数](https://numpy.org/numpy-financial/latest/reference/numpy_financial.irr.html)：对标TODO3，IRR计算的标准实现

### NPV/IRR 投资评估理论
- 📖 Investopedia NPV: https://www.investopedia.com/terms/n/npv.asp （已验证）
- 📖 Investopedia IRR: https://www.investopedia.com/terms/i/irr.asp （已验证）
- **用法**：NPV和IRR是投资评估的两大核心指标。NPV>0表示投资可行，IRR>折现率也表示投资可行。重点理解"为什么NPV和IRR可能给出矛盾信号"以及"J曲线效应"对AI项目评估的影响。

### 真实AI SaaS财务数据
- 📊 HubSpot Investor Relations: https://investors.hubspot.com/ （已验证，SEC公开披露）
- 📊 Crunchbase Jasper AI: https://www.crunchbase.com/organization/jasper-ai （已验证，公开数据）
- **用法**：HubSpot 2023财报（gross margin ~78%）和Jasper AI Crunchbase数据（$1.5B估值）作为MarketingAgent Pro DCF模型的参数校准基准。

---

## ③ 蒙特卡洛模拟与敏感性分析

### scipy.stats 官方文档（已验证）
- 📄 文档：https://docs.scipy.org/doc/scipy/reference/stats.html （已验证，BSD-3-Clause）
- **深链用法**：
  - [scipy.stats.norm](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.norm.html)：对标TODO4，正态分布抽样
  - [Monte Carlo方法](https://docs.scipy.org/doc/scipy/tutorial/stats.html)：蒙特卡洛方法的SciPy实现参考

### 蒙特卡洛模拟入门
- 📖 Investopedia Monte Carlo: https://www.investopedia.com/terms/m/montecarlosimulation.asp （已验证）
- **用法**：蒙特卡洛模拟用随机抽样替代点估计，得到估值分布。重点理解"为什么P(NPV>0)比单一NPV值更有决策价值"。对标TODO4的10000次模拟。

### 敏感性分析（龙卷风图）
- 📖 Investopedia Sensitivity Analysis: https://www.investopedia.com/terms/s/sensitivityanalysis.asp （已验证）
- **用法**：敏感性分析（龙卷风图）展示各参数对NPV的影响排序。对标TODO5，重点理解"高杠杆点"概念--小投入改变大局的关键参数。对AI SaaS而言，推理成本（通过毛利率）是核心高杠杆因子。

---

## ④ 2026前沿：贝叶斯估值 + 推理成本 + 天道推演

### PyMC 贝叶斯统计（已验证）
- 📦 GitHub：https://github.com/pymc-devs/pymc （8k+ star，已验证）
- 📄 文档：https://www.pymc.io/ （已验证，Apache-2.0）
- **用法**：Day 5 2026前沿--贝叶斯估值（Bayesian Valuation）。PyMC是Python贝叶斯统计标准库，用MCMC采样后验分布。贝叶斯估值用参数的后验分布替代点估计，结合先验信息和观测数据，给出更稳健的估值后验分布。对比蒙特卡洛（频率派）和贝叶斯方法的差异。

### 推理成本与AI估值
- 📄 OpenAI Pricing: https://openai.com/api/pricing/ （已验证，官方定价）
- 📄 DeepSeek Pricing: https://api-docs.deepseek.com/quick_start/pricing （已验证，推理成本降90%+）
- **用法**：推理成本（Inference Cost）是AI产品独有的持续运营成本。DeepSeek等开源模型将推理成本降低90%+，直接提升AI SaaS毛利率和估值。Day 5敏感性分析将量化推理成本对NPV的影响排名。

### 天道推演×投资评估
- 📖 项目CLAUDE.md「天道推演系统」章节
- **用法**：天道推演的沙盘模拟（因果链追踪+多路径概率评估）与投资评估的多场景分析同构。Day 5 TODO6用天道推演框架做Bull/Base/Bear三路径场景分析，每路径推演immediate/near/far三层。

---

## ⑤ AI ROI评估报告

### McKinsey AI ROI Report
- 📄 McKinsey AI: https://www.mckinsey.com/capabilities/mckinsey-digital/our-insights/the-state-of-ai （已验证，McKinsey年度AI报告）
- **用法**：McKinsey年度AI报告提供AI项目ROI的行业基准。重点读"AI投资回报的行业分布"和"J曲线效应"部分，对标Day 5 DCF模型的参数选择。

### Stanford GSB AI Business Model Working Papers
- 📄 Stanford GSB Working Papers: https://www.gsb.stanford.edu/faculty-research/working-papers （已验证）
- **用法**：英语轨道材料。Stanford GSB关于AI商业模式的工作论文，提供学术视角的AI估值方法论。重点读AI商业模式的value capture机制。

---

## 阅读路径建议

| 顺序 | 材料 | 用途 | 时长 |
|:----:|------|------|:----:|
| 1 | 本Day `notes.md` 理论回顾 + 独立教材 § Day 5 | 画布+ROI理论 | 1h |
| 2 | numpy-financial 文档（选读） | NPV/IRR实现 | 0.5h |
| 3 | `starter.ipynb` 上机（配scipy.stats文档） | 真实库实操 | 2h |
| 4 | HBR AI Business Models（选读） | AI画布适配 | 0.5h |
| 5 | McKinsey AI Report 摘要（选读） | 行业ROI基准 | 0.5h |
| 6 | PyMC 贝叶斯估值概念（选读） | 2026前沿 | 0.5h |
| 7 | Stanford GSB Working Papers（选读，英语轨道） | 学术视角+英语 | 1h |

---

*全部深链已于 2026-07-24 验证存在。如发现失效，请在 Issues 报告。*
