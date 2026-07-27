# 技能4 · Day 5：商业模式画布 + 投资评估 · 讲义（v5.0 学习材料包版）

> **所属**：AI原生化商业博士 · 技能4 AI驱动商业模式创新 · Day 5（收官）
> **版本**：v5.0（从独立教材升级为学习材料包）
> **预计**：2h 讲义 + 2h 上机练习
> **核心命题**：如何用商业模式画布结构化一个AI产品？如何用真实财务模型评估AI投资？
> **v5.0 升级点**：① 真实库（numpy-financial + scipy.stats蒙特卡洛）② TODO填空脚手架 ③ Notebook化 ④ 深链阅读 ⑤ 2026前沿（贝叶斯估值 + 推理成本对AI估值的影响 + 天道推演×投资评估）

---

## 学习目标（学完你能做到）

1. 能用 **pandas** 构建 AI 商业模式画布的九宫格结构（客户细分/价值主张/渠道/客户关系/收入流/核心资源/核心活动/核心伙伴/成本结构），对比 AI 适配版与传统 SaaS 的差异
2. 能用 **numpy-financial** 计算 NPV（`npf.npv()`）、IRR（`npf.irr()`）、回收期、盈利指数（PI），判断 AI 项目投资可行性
3. 能用 **scipy.stats + numpy** 做蒙特卡洛模拟（Monte Carlo），对营收/毛利率/增长率做随机抽样，得到估值分布而非点估计，计算 P(NPV>0) 概率
4. 能用 **pandas + matplotlib** 做敏感性分析（龙卷风图），识别 NPV 的高杠杆因子，理解推理成本对 AI 估值的决定性影响
5. 能用**天道推演**框架做 Bull/Base/Bear 三路径场景分析，每路径推演 immediate/near/far 三层，整合 Day 1-4 为完整投资评估

---

## 理论部分：精炼索引（详见独立教材）

> Day 5 的完整理论讲义见 [`../../AI原生化商业博士_独立教材_技能4_AI驱动商业模式创新.md` § Day 5](../../AI原生化商业博士_独立教材_技能4_AI驱动商业模式创新.md)（722-863行，已包含AI商业模式画布九宫格适配/AI ROI评估框架/PoC->PoV->PoB->Scale验证路径/MarketingAgent Pro综合案例/单位经济模型）。本讲义不重复，仅做上机所需的关键回顾。

### 关键回顾 1：AI商业模式画布（九宫格适配版）

商业模式画布（Business Model Canvas）是 Alexander Osterwalder 提出的经典工具。AI 驱动的商业模式画布在传统九宫格基础上进行了适配：

| 构件 | 传统画布 | AI适配版 | 关键变化 |
|------|---------|---------|---------|
| 客户细分 | 目标用户群体 | + AI能力可达的新用户群体 | AI降低使用门槛 |
| 价值主张 | 解决什么问题 | + 个性化/实时/预测性/自主性 | 从工具到Agent |
| 渠道 | 如何触达客户 | + Agent分发渠道 | Agent作为新渠道 |
| 客户关系 | 如何维系客户 | + AI驱动个性化关系 | 每客户独特体验 |
| 收入流 | 怎么赚钱 | + outcome-based + 价值分成 | seat->outcome |
| 核心资源 | 关键资产 | + 数据 + 模型 + 算力 | 数据是护城河 |
| 核心活动 | 关键业务 | + 模型训练/评估 + Agent运维 | 持续迭代 |
| 核心伙伴 | 关键合作 | + 基础模型提供商 + 开源社区 | 依赖与风险 |
| 成本结构 | 主要成本 | + 推理成本（持续）+ 数据成本 | 推理成本是核心变量 |

### 关键回顾 2：AI项目的ROI评估框架

AI项目的投资回报率评估与传统IT项目有本质差异：

```
ROI = (总价值 - 总成本) / 总成本 × 100%

总成本 = 开发成本 + 推理成本(持续) + 数据成本 + 运维成本 + 合规成本
总价值 = 效率价值 + 体验价值 + 模式创新价值
```

**AI ROI评估的特殊挑战**：
1. **J曲线效应**：AI项目前期投入大、回报慢，需3-5年评估窗口
2. **价值滞后性**：AI系统价值随数据积累和模型优化递增
3. **间接价值**：品牌提升、组织能力建设难以直接量化
4. **推理成本**：AI产品独有的持续运营成本，直接决定毛利率

### 关键回顾 3：从PoC到规模化的四阶段验证

| 阶段 | 名称 | 目标 | 投入 | 商业模式关注 |
|------|------|------|------|------------|
| 1 | PoC | 技术可行性验证 | 1-2人, 2-4周 | 暂不验证 |
| 2 | PoV | 商业价值验证 | 3-5人, 2-3月 | 初步验证价值主张 |
| 3 | PoB | 商业模式验证 | 完整团队, 3-6月 | 全面验证画布假设 |
| 4 | Scale | 规模化扩展 | 组织级, 6-12月 | 迭代优化 |

### 关键回顾 4：MarketingAgent Pro 综合案例

**单位经济模型**（独立教材Day5）：
```
ARPU = $2,000/月（基础订阅$500 + 结果付费$1,500）
CAC = $8,000
LTV = $2,000 × 18月 = $36,000
LTV/CAC = 4.5（健康，>3为合格）
毛利率 = 65%（推理成本30% + 数据成本5%）
回收周期 = $8,000 / ($2,000 × 0.65) ≈ 6.2月
```

**真实数据校准**：
- HubSpot 2023 财报：Revenue $2.17B, gross margin ~78%（AI SaaS因推理成本拉低至65%）
- Jasper AI：$125M ARR, $1.5B估值（2022 Series A, Crunchbase公开数据）
- OpenAI GPT-4 定价：$0.03/1K input tokens, $0.06/1K output tokens（推理成本基准）

---

## 上机部分：用真实库做商业模式画布 + 投资评估

> 📓 **配套笔记本**：[`starter.ipynb`](./starter.ipynb)（TODO填空版，你来做）｜ [`solution.ipynb`](./solution.ipynb)（参考答案，做完再看）
> 📊 **真实数据/库**：[`data/README.md`](./data/README.md)（numpy-financial + scipy.stats + 真实AI SaaS财务数据）

### 为什么用真实库+真实数据而非模拟数据

v4.0 用手写公式演示 NPV/IRR 概念。v5.0 改用真实库和真实行业基准数据：

- **numpy-financial**：金融计算标准库（NPV/IRR/MI/ROR），替代手写公式
- **scipy.stats 蒙特卡洛**：用统计分布做不确定性分析，替代点估计
- **真实行业基准**：HubSpot 2023 财报、Jasper AI Crunchbase 数据、OpenAI 定价，替代编造数字
- **推理成本建模**：AI SaaS 独有的成本结构，用真实 API 定价校准

### 营销场景映射（Day 1-5 整合）

本 Day 是技能4收官，把 Day 1-4 整合为完整投资评估：

| Day | 能力 | Day 5 整合角色 |
|-----|------|--------------|
| Day 1 | AI商业模式类型学 | 画布的客户细分 + 价值主张 |
| Day 2 | AI定价策略 | 画布的收入流（outcome-based pricing） |
| Day 3 | Agent经济学 | 画布的成本结构（推理成本30%） |
| Day 4 | 平台生态战略 | 画布的核心伙伴 + 渠道 |
| Day 5 | 商业模式画布 + 投资评估 | **整合为完整投资评估** |

### 上机任务（6个TODO，见starter.ipynb）

1. **TODO1**：用 pandas 构建商业模式画布 DataFrame（9宫格 + AI适配对比列）
2. **TODO2**：用 numpy-financial 构建5年DCF模型并计算NPV
3. **TODO3**：计算IRR + 回收期 + 盈利指数（PI），判断投资可行性
4. **TODO4**：用 scipy.stats 做蒙特卡洛模拟（10000次），得到估值分布
5. **TODO5**：做敏感性分析（龙卷风图），识别NPV高杠杆因子
6. **TODO6**：用天道推演做Bull/Base/Bear三路径场景分析

---

## 2026前沿：贝叶斯估值 + 推理成本 + 天道推演×投资评估

> v5.0新增前沿点。Day 5作为技能4收官，聚焦三个前沿方向。

### 贝叶斯估值（Bayesian Valuation）

传统DCF给出NPV的点估计，蒙特卡洛给出频率派分布。**贝叶斯估值**（Bayesian Valuation）用 **PyMC** 构建参数的后验分布，结合先验信息和观测数据，给出更稳健的估值后验分布。

- **工具**：PyMC（`pip install pymc`），概率编程框架
- **优势**：小样本下通过先验正则化更稳健；天然输出预测不确定性
- **与频率派对比**：DCF的NPV是一个数；蒙特卡洛的NPV是一个分布；贝叶斯的NPV是一个后验分布（可随新数据更新）
- **营销应用**：贝叶斯方法可计算"P(NPV>0 | 已观测数据)>95%"这种直接可用的决策概率

### 推理成本对AI估值的影响

推理成本（Inference Cost）是 AI 产品独有的持续运营成本，直接决定长期毛利率和估值：

- **DeepSeek 效应**：DeepSeek 等开源模型将推理成本降低 90%+，直接提升 AI SaaS 毛利率
- **成本曲线**：推理成本随模型竞争和技术进步持续下降，但用量增长可能抵消
- **估值影响**：推理成本每降低1个百分点，毛利率提升1个百分点，NPV显著上升
- **敏感性分析**：本Day的龙卷风图将量化推理成本（通过毛利率）对NPV的影响排名

### 天道推演×投资评估（特色章节）

> 本节与项目CLAUDE.md的「天道推演系统」同构。

**天道推演**是一种元认知沙盘推演能力--以天神视角俯视局势，构建无限可能的沙盘，模拟不同决策路径下的未来走向。

**与投资评估的同构关系**：

| 天道推演能力 | 投资评估对应 | 实现方式 |
|-------------|------------|---------|
| 局势感知 | 市场环境建模 | 场景定义 |
| 因果链追踪 | 价值驱动因素分析 | 敏感性分析 |
| 沙盘模拟（3层推演） | 多路径推演 | Bull/Base/Bear |
| 概率评估 | 估值概率分布 | 蒙特卡洛模拟 |
| 最优路径推荐 | 投资决策 | NPV/IRR/PI |

**三路径推演**：Bull（乐观）/ Base（基准）/ Bear（悲观），每路径推演3层（immediate/near/far），形成完整的投资天道推演沙盘。

> ⚠️ 天道推演不是占卜，而是基于因果链和模式识别的逻辑推演。与蒙特卡洛互补：蒙特卡洛评估"参数不确定性"，天道推演评估"场景路径优不优"。

> 🔗 深入阅读见 [`reading.md`](./reading.md) 的贝叶斯估值和天道推演条目。

---

## 与前序Day的衔接

- **Day 1**（AI商业模式类型学）：今天的画布客户细分和价值主张基于Day 1的类型学
- **Day 2**（AI定价策略）：今天的收入流（outcome-based pricing）来自Day 2的定价模型
- **Day 3**（Agent经济学）：今天的成本结构（推理成本30%）来自Day 3的Agent经济分析
- **Day 4**（平台生态战略）：今天的核心伙伴和渠道来自Day 4的生态设计
- **技能5**（Agentic系统工程）：今天的投资评估为技能5的Agent系统落地提供商业论证

---

## 作业与评估

作业、5分制量表、费曼演练、2分钟话术、复盘自诊表--沿用独立教材 § Day 5 既有设计。本学习材料包不重复，仅新增上机交付物：

**新增交付物（v5.0）**：
- [ ] 完成的 `starter.ipynb`（6个TODO全部填好，能跑通）
- [ ] 一段300字分析：MarketingAgent Pro的NPV/IRR/PI是多少？投资可行吗？蒙特卡洛的P(NPV>0)是多少？
- [ ] （可选）用PyMC对NPV做贝叶斯估值，对比蒙特卡洛频率派分布和贝叶斯后验分布的差异

---

## 英语轨道（i+1）

打开 [Stanford GSB Working Papers](https://www.gsb.stanford.edu/faculty-research/working-papers) 和 [McKinsey AI Report](https://www.mckinsey.com/capabilities/mckinsey-digital/our-insights)，用浏览器翻译插件辅助阅读。重点关注术语：Business Model Canvas, NPV, IRR, payback period, profitability index, Monte Carlo simulation, sensitivity analysis, Bayesian valuation, inference cost。这些术语在后续技能5和Capstone中反复出现。

---

*本讲义由v5.0学习材料包升级生成。理论部分引用独立教材，上机部分用真实库（numpy-financial + scipy.stats + pandas + matplotlib）+ 真实AI SaaS行业基准数据 + TODO脚手架。*
*最后更新：2026-07-24*

---

## 学习科学层 (v6.0)

> v6.0 在 v5.0 基线上注入**学习科学层**: 刻意练习 (Ericsson deliberate practice) + 间隔重复 (FSRS-6 / SM-2 备份) + 建构对齐 (Biggs constructive alignment ILO↔TLA↔AT) + 牛津tutorial LLM仿真 (Socratic, 禁直接答案) + Hattie四级形成性反馈。本节不动 v5.0 原文, 只追加。

**四新文件**:
- `practice.md` - **刻意练习** (Ericsson 5要素): skill_target + 3 subskills + 3 drills (worked-faded 三阶段: 完整示范 -> 部分填空 -> 独立解) + **交叉练习 interleaving** (A1B1C1...B2C2A2...C3A3B3 明文排布, 不块状) + weak_loop (连续2次失败回退上一drill + worked example) + retry_policy
- `schedule.json` - **间隔重复** (FSRS-6, request_retention=0.9, 21权重 + SM-2备份 EF₀=2.5 I(1)=1 I(2)=6): 4张卡片 - 画布九宫格AI适配 / NPV-IRR-PI / 蒙特卡洛P(NPV>0)+天道推演 / 推理成本影响, due=[1,3,8,21,60,180]
- `alignment.md` - **建构对齐** (Biggs ILO↔TLA↔AT): 3行矩阵 + mastery_threshold (>=80% / 能独立解) + 3自检 (Feed Up / Feed Back / Feed Forward) + 复盘对齐缺口表
- `tutorial.ipynb` - **牛津tutorial LLM仿真**: persona (Socratic + 禁直接答案 + devil's advocate) + pre-task 强制 retrieval + 4-5轮 Socratic 追问 (静态if/else) + student_model.json 读写 + Hattie四级 [TASK]/[PROCESS]/[SELF-REG]/[FEED-FORWARD] + 限频 1次/天 防依赖 + exit artifact (2-3盲点 + 推荐复习)

**研究依据**: Ericsson 刻意练习5要素 / FSRS-6 21权重 (request_retention=0.9) / Biggs ILO↔TLA↔AT constructive alignment / Hattie 2007 RER 77(1):81-112 (formative feedback d=0.79-0.9, 禁Self级表扬) / Vygotsky 共构 / Oxford tutorial 1对1-3 每周强制口头辩护 / MIT 6.5940 mastery 阈值 ("至少 4/5 实验提交方可及格") / Butler 2010 检索练习证据 (推断题 68% vs 重学 44%) / d.school 设计思维 Bootleg 方法卡

**mastery 阈值 (本单元)**:
- ILO1 (画布构建): >=80% - 九宫格全对 + AI独有4项(推理成本+数据成本+Agent渠道+outcome-based)全识别
- ILO2 (DCF 财务计算): >=80% - NPV/IRR/PI/回收期数值正确 + 符号方向正确
- ILO3 (蒙特卡洛+天道推演): 能独立解 - P(NPV>0)代码正确 + 三路径×三层完整 + 决策建议有依据
- 整体: 6个TODO全跑通 + 300字分析引用 NPV=$451.2K / IRR=20.08% / P(NPV>0)=55.7%

**验收**: `/tmp/verify_v6_unit.py` 5/5 (v6.0层 8-12) + `/tmp/verify_unit.py` 7/7 (v5.0基线 1-7) = 12/12 收敛

> 本学习科学层与项目 CLAUDE.md 的「天道推演系统 - 自我进化机制」同构: 记录前提假设 (ILO/TLA设计) -> 追踪 outcomes (AT分数) -> 复盘差异 (对齐缺口表) -> 更新因果模型 (下次迭代 worked-faded 比例与 tutorial 追问深度)。

## 研究产出与产业链接层 (v7.0)

本单元产出可发表研究工件 (research.md: 研究问题+贡献声明+arXiv链接+IMRaD大纲+NeurIPS可复现清单+research-to-practice翻译) 与产业链接 (industry.md: >=3真实企业+部署场景+Imperial咨询项目+HBS教学案例+客座讲座+实习指针)。研究产出遵循IMRaD/DSR(Hevner)/OSF预注册/FAIR/可复现研究标准; 产业链接遵循Imperial MSc BA咨询项目(Burberry/Expedia/J&J)/HBS案例法/MIT Sloan行动学习模式。详见 research.md 与 industry.md。

**研究产出 (research output, 6 段)**:
- `research_question`: 蒙特卡洛频率派 P(NPV>0)=55.7% vs 天道推演 Bull/Base/Bear 三路径权重, 在推理成本扰动下是否显著一致 (H1/H0 可实证)
- `contribution`: delta vs HBR 2023 / Investopedia / McKinsey / Stanford GSB -- 用真实库+真实数据+天道推演三路径沙盘
- `linked_paper`: Osterwalder&Pigneur 2010 / Hevner 2004 DSR / HBR 2023 / McKinsey 2024 / Stanford GSB Working Papers (全部从 reading.md 已验证深链挑, 不联网查)
- `imrad_outline`: IMRaD 四段, 引用 NPV=$451.2K / IRR=20.08% / P(NPV>0)=55.7% / 龙卷风图排名 / Bull 路径 P(NPV>0)~80%
- `reproducibility_checklist`: NeurIPS 风格 7 项 (code/data/seeds/environment/preregistration/FAIR/DSR-rigor), random_state=42
- `research_to_practice`: HBR article / MIT Sloan teaching case / 企业白皮书 (Anthropic/OpenAI) / Imperial MSc BA Capstone

**产业链接 (industry linkage, 6 段)**:
- `real_companies`: 6 家 (HubSpot / OpenAI / Anthropic / Jasper AI / DeepSeek / Perplexity), 全部从公司库挑, 与"画布+投资估值"主题匹配
- `deployment_example`: 中型 B2B SaaS 公司评估"自建 vs API", 5000 客户, 5 年窗口, CFO/CTO/CEO 三重约束
- `consulting_project`: Imperial MSc BA 8 周, partner=Burberry, AI Stylist Agent 投资可行性, 4 项 deliverable
- `case_study`: HBS 风格, protagonist=Sarah Chen (HubSpot Head of AI), decision=GPT-4 API vs 自研+DeepSeek 蒸馏, tension=推理成本 vs 客户流失
- `guest_lecture`: HubSpot Director of AI Strategy, "From PoC to Scale: Monte Carlo + Scenario Planning"
- `internship_pointer`: OpenAI/Anthropic Residency + McKinsey/BCG AI + Sequoia/a16z AI 投资 + Imperial Capstone

**验收**: `/tmp/verify_v7_unit.py` 3/3 (v7.0层 13-15) + `/tmp/verify_v6_unit.py` 5/5 (v6.0层 8-12) + `/tmp/verify_unit.py` 7/7 (v5.0基线 1-7) = 15/15 收敛

> 本产业链接层与项目 CLAUDE.md 的「天道推演系统 - 沙盘模拟 + 反馈学习」同构: real_companies 是棋手, deployment_example 是棋盘, consulting_project/case_study 是沙盘分支, internship_pointer 是高杠杆点。本单元通过研究产出+产业链接, 把"上机跑通 NPV=$451.2K"升级为"可发表研究工件+可落地产业实践", 完成技能4收官。
