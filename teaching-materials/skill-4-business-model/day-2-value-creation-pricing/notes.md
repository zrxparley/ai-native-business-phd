# 技能4 · Day 2：价值创造机制 + 定价策略 · 讲义（v5.0 学习材料包版）

> **所属**：AI原生化商业博士 · 技能4 AI驱动商业模式创新 · Day 2
> **版本**：v5.0（从独立教材升级为学习材料包）
> **预计**：2h 讲义 + 2h 上机练习
> **核心命题**：AI如何创造价值？如何为AI产品定一个"既覆盖推理成本又捕获用户价值"的价格？
> **v5.0 升级点**：① 真实API定价数据（OpenAI/Anthropic/Google/DeepSeek官方定价页，非模拟）② TODO填空式起始笔记本 ③ Notebook化 ④ 深链阅读 ⑤ 2026前沿（贝叶斯定价/推理成本定价/天道推演动态定价）

---

## 学习目标（学完你能做到）

1. 能用 **statsmodels** 对真实AI API定价数据拟合 OLS 多元线性回归（`sm.OLS(y, sm.add_constant(X)).fit()`），量化"什么驱动了AI产品定价"（上下文窗口、价值创造机制、推理能力、提供商），解读 R²、回归系数、p值和置信区间
2. 能用 **numpy-financial** 计算AI产品的 NPV/IRR/payback period（`npf.npv()`/`npf.irr()`/`npf.payback()`），基于真实训练成本（DeepSeek V3公开披露$5.576M）和真实API定价，评估四种定价策略（成本加成/价值定价/渗透/撇脂）的财务可行性
3. 能用 **scipy.stats** 估计价格弹性的置信区间，理解"小样本下点估计不可靠"的本质问题，并能用贝叶斯方法（PyMC）给出弹性的后验分布而非单一数值
4. 能区分AI价值创造的四个机制（降低成本/提升体验/创造新品类/网络效应），将每个机制映射到具体的AI营销产品定价模式（按token/按席位/按效果/按价值分成）
5. 能用**天道推演**框架预判定价策略的竞争反应路径：如果我采用渗透定价，竞品会如何反应？价格战的概率树如何展开？最优策略是什么？

---

## 理论部分：精炼索引（详见独立教材）

> Day 2 的完整理论讲义见 [`../../AI原生化商业博士_独立教材_技能4_AI驱动商业模式创新.md` § Day 2](../../AI原生化商业博士_独立教材_技能4_AI驱动商业模式创新.md)（253-434行，已包含AI价值创造三维度/传统定价vs AI驱动定价/outcome-based pricing数学模型/API Economy 2.0/OpenAI与Anthropic定价演进案例）。本讲义不重复，仅做上机所需的关键回顾。

### 关键回顾 1：AI价值创造的三个维度

AI对商业价值的创造不是单一的"降本增效"，而是三个不同维度的价值创造：

| 维度 | 价值来源 | 度量方式 | 价值上限 | 竞争防御 | 代表产品 |
|------|---------|---------|---------|---------|---------|
| 效率提升 | 自动化替代 | 成本/时间节约 | 被替代人力成本 | 弱（易复制） | GPT-4o-mini, Haiku |
| 体验重塑 | 个性化/实时 | CSAT/留存/转化 | 体验溢价 | 中（数据飞轮） | GPT-4o, Sonnet |
| 模式创新 | 全新价值主张 | TAM/新收入流 | 新市场总规模 | 强（生态锁定） | o1/o3, DeepSeek-R1 |

理解这三个维度的差异是设计正确定价策略的前提：效率提升型产品应走成本加成定价，体验重塑型产品应走价值定价，模式创新型产品应走撇脂定价。

### 关键回顾 2：传统定价 vs AI驱动定价

| 定价模式 | 机制 | 适用场景 | AI时代挑战 |
|---------|------|---------|-----------|
| 按席位(Seat-based) | 按用户数收费 | 企业SaaS | Agent时代"用户"定义模糊 |
| 按功能tier(Feature-based) | 基础/专业/企业版 | 功能差异化产品 | AI功能难以打包成tier |
| 固定订阅(Flat-rate) | 月/年固定费用 | 标准化SaaS | 无法反映推理成本(token消耗) |
| 按token(Token-based) | 按输入/输出token计费 | LLM API服务 | 成本透明，与推理成本对齐 |
| 按结果(Outcome-based) | 按AI完成的可度量结果计费 | Agent服务 | 价值对齐，降低用户风险 |
| 按价值分成(Value-sharing) | 按AI创造的价值抽取比例 | 高价值AI决策 | 利益完全对齐 |

### 关键回顾 3：Outcome-based Pricing 数学模型

```
基本模型: Total Cost = P × R   (P=单位结果价格, R=结果数)
价值锚定: P = α × V             (α=价值捕获比例10%-30%, V=单位结果创造的价值)
风险封顶: Total Cost = min(P × R, Cap)
质量加权: Total Cost = P × Σ(qi × ri)   (qi=质量分数, ri=结果)
```

### 关键回顾 4：推理成本定价

AI产品的核心成本是推理（inference）成本--运行模型生成token所需的算力成本。与传统SaaS的边际成本趋近于零不同，AI产品每次调用都有真实的推理成本。这是AI定价与传统SaaS定价的根本差异。

- **token定价**：OpenAI/Anthropic按输入/输出token分别计价，反映推理成本
- **推理成本下降趋势**：vLLM（PagedAttention）、投机解码（Speculative Decoding）、MoE（Mixture of Experts）等技术持续降低单位推理成本
- **DeepSeek的成本突破**：DeepSeek V3训练成本仅$5.576M（2048×H800 GPU，2.788M GPU-hours），推理价格低至$0.14/1M input tokens，打破了"大模型=天价训练成本"的固有认知

---

## 上机部分：用真实库+真实API定价数据做价值创造与定价分析

> 📓 **配套笔记本**：[`starter.ipynb`](./starter.ipynb)（TODO填空版，你来做）｜ [`solution.ipynb`](./solution.ipynb)（参考答案，做完再看）
> 📊 **真实数据/库**：[`data/README.md`](./data/README.md)（statsmodels + numpy-financial + scipy.stats + 真实AI API定价数据）

### 为什么用真实API定价数据而非模拟数据

v4.0 的代码用 `np.random.seed(42)` 生成模拟数据，构造"已知真实关系"来演示定价概念。v5.0 改用真实公开定价数据：

- **真实API定价**：OpenAI/Anthropic/Google/DeepSeek/Mistral的官方定价页，每一个数字都可追溯验证
- **真实训练成本**：DeepSeek V3技术报告公开披露的训练成本$5.576M，是AI经济学研究的里程碑数据
- **真实SaaS订阅定价**：ChatGPT Plus/Pro/Team、Claude Pro/Team等的官方月费，反映消费者市场定价
- **真实数据的不完美性**：真实定价数据的分布不服从教科书正态分布，价格弹性估计的置信区间可能很宽--这是真实分析的常态

### 营销映射（关键桥接）

本Day把AI API/SaaS定价数据映射到AI+营销产品场景：

| 定价模式 | 营销AI产品映射 | 价值创造机制 | 真实参考 |
|---------|--------------|------------|---------|
| 按token | AI文案生成API（按生成字数计费） | 效率提升 | GPT-4o-mini $0.15/1M input |
| 按席位 | 营销Agent平台（按营销人员席位订阅） | 效率提升+体验重塑 | Claude Team $30/user/月 |
| 按效果 | 个性化推荐SaaS（按转化提升计费） | 体验重塑 | outcome-based pricing |
| 按价值分成 | AI定价优化引擎（按增收抽成） | 模式创新 | value-sharing α=10%-30% |

### 上机任务（6个TODO，见starter.ipynb）

1. **TODO1**：加载真实AI API定价数据，探索数据结构和分布
2. **TODO2**：用 statsmodels 拟合OLS回归，量化什么驱动了AI产品定价（output_price ~ context_window + value_mechanism + has_reasoning + provider）
3. **TODO3**：用 numpy-financial 计算NPV/IRR/payback，基于真实训练成本和API定价评估AI产品财务可行性
4. **TODO4**：用 scipy.stats 估计价格弹性，计算置信区间，理解小样本下定价决策的不确定性
5. **TODO5**：对比四种定价策略（成本加成/价值定价/渗透/撇脂）的利润曲线，找最优价格点
6. **TODO6**：用天道推演框架做定价策略的竞争反应沙盘推演（2026前沿）

---

## 2026前沿补充：贝叶斯定价 + 推理成本定价 + 天道推演动态定价

> v5.0新增前沿点。本Day覆盖三个前沿方向：① 贝叶斯定价（PyMC）② 推理成本定价（vLLM/投机解码）③ 天道推演动态定价。

### 贝叶斯定价：从点估计到后验分布

传统价格弹性估计给出一个**点估计**（一个数值）和置信区间。**贝叶斯定价**（Bayesian Pricing）给出弹性的**后验分布**--不仅告诉你"弹性最可能是多少"，还告诉你"弹性在各个值上的概率分布"。

- **工具**：PyMC（`pip install pymc`）
- **小样本优势**：当价格数据点少（如只有5-10个产品的定价）时，贝叶斯方法通过先验分布提供正则化，比频率派OLS更稳健
- **定价区间**：贝叶斯方法输出"价格弹性有95%概率落在[-2.1, -1.3]之间"，而非"弹性=-1.7"一个数字。决策者可以据此设定定价区间而非单一价格点
- **与频率派的对比**：频率派95%置信区间是"如果重复采样100次，95次包含真值"；贝叶斯95%可信区间是"给定数据，弹性有95%的概率落在此区间"--后者更符合定价决策者的直觉

**营销应用**：在AI产品定价中，贝叶斯方法可以计算"P(最优价格>$5)>90%"这种直接可用的决策概率，帮助定价团队在不确定性下做决策。

### 推理成本定价：AI产品定价的底层逻辑

AI产品与传统SaaS的根本差异在于**推理成本**--每次API调用都有真实的算力成本。这创造了AI定价的独特挑战：

- **成本下限**：定价必须高于单位推理成本，否则越用越亏
- **成本下降红利**：vLLM（PagedAttention）、投机解码（Speculative Decoding）、MoE架构持续降低推理成本，为降价创造空间
- **DeepSeek的定价冲击**：DeepSeek V3以$0.14/1M input tokens的价格（约为GPT-4o的1/18），迫使整个行业重新思考定价基准--这本质上是"推理成本效率"的竞争
- **投机解码（Speculative Decoding）**：用小模型生成候选token、大模型验证，降低推理延迟和成本。这是2025-2026年推理优化的核心技术

### 天道推演与动态定价

定价不是静态决策，而是动态博弈。**天道推演**提供了一种系统性预判竞争反应的框架：

```
输入：我方定价策略 + 竞争格局

处理：
  1. 局势拆解 → 识别竞争者、替代品、买方议价力
  2. 因果建模 → 定价→市场份额→竞争反应的因果链
  3. 沙盘展开 → 每个定价策略生成3层推演树
     - immediate: 竞品即时反应（跟降/不变/差异化）
     - near: 3-6月后市场格局变化
     - far: 1-2年后行业生态演化
  4. 概率注入 → 各反应路径的概率分布
  5. 输出评估 → 各路径的收益/风险比

输出：最优定价路径 + 备选方案 + 风险预警
```

**营销应用**：AI营销SaaS定价决策中，天道推演可以预判"如果我采用渗透定价$10/月，竞品A跟降的概率是多少？价格战升级的概率是多少？最终市场格局如何？"--这比单纯计算NPV更有战略价值。

---

## 与后续Day的衔接

- **Day 1**：AI商业模式画布--今天的价值创造机制和定价策略是画布的核心组件
- **Day 3**：Agent经济 + 新兴商业模式--今天的定价策略（特别是outcome-based和value-sharing）将在Agent经济中进一步演化
- **技能3**：因果推断--今天的OLS回归是因果推断的基础工具，定价实验（A/B测试不同价格）需要因果推断方法分析

---

## 作业与评估

作业、5分制量表、费曼演练、2分钟话术、复盘自诊表--沿用独立教材 § Day 2 既有设计。本学习材料包不重复，仅新增上机交付物：

**新增交付物（v5.0）**：
- [ ] 完成的 `starter.ipynb`（6个TODO全部填好，能跑通）
- [ ] 一段300字分析：OLS回归中哪些变量对AI产品定价有显著影响？价值创造机制（efficiency/experience/innovation）的系数差异说明了什么？DeepSeek的低价策略在推演中会引发什么竞争反应？
- [ ] （可选）用PyMC对价格弹性做贝叶斯估计，对比频率派OLS系数和贝叶斯后验分布的差异

---

## 英语轨道（i+1）

打开 [OpenAI API定价页](https://openai.com/api/pricing/) 和 [Anthropic定价页](https://www.anthropic.com/pricing)，用浏览器翻译插件辅助阅读。重点关注术语：token-based pricing, input/output tokens, prompt caching, batch API discount, outcome-based pricing, value-sharing, penetration pricing, skimming pricing, price elasticity。这些术语在后续技能4-5的英文文献中反复出现。

---

*本讲义由v5.0学习材料包升级生成。理论部分引用独立教材，上机部分用真实库（statsmodels + numpy-financial + scipy.stats）+ 真实AI API定价数据（OpenAI/Anthropic/Google/DeepSeek官方定价页）+ TODO脚手架。*
*最后更新：2026-07-24*

---

## 学习科学层 (v6.0)

> v6.0 在 v5.0 五文件 (notes/data/README/starter/solution/reading) 之上新增学习科学四件套: `practice.md` / `schedule.json` / `alignment.md` / `tutorial.ipynb`。哲学增量: **科学即高效 · 反馈即成长**--用学习科学把"练习"升级为"刻意练习 + 间隔重复 + 建构对齐 + 牛津 tutorial 仿真"。

### 理论依据 (4 agent 调研合成)

- **Ericsson 刻意练习 (deliberate practice)**: practice.md 的 3 个 drill 各含 `difficulty`/`reps_required`/`feedback_rule`/`worked-faded` 三阶段 (Worked->Faded->Independent), 加 `weak_loop` 连续 2 次失败触发回退。
- **FSRS-6 间隔重复 (spaced retrieval)**: schedule.json 用 FSRS-6 算法 (request_retention=0.9, SM-2 备份 EF₀=2.5), 5 张卡片 due=[1,3,8,21,60,180] 强制 6 次复习, 命中 Butler 2010 提取练习证据 (推断题 68% vs 重学 44%)。
- **Biggs 建构对齐 (constructive alignment)**: alignment.md 的 ILO↔TLA↔AT 矩阵 3 行, 每 ILO 配 `mastery_threshold` (ILO1≥80% / ILO2≥70% / ILO3 能独立解) + 3 自检 (Feed Up / Feed Back / Feed Forward)。
- **Oxford tutorial Socratic 仿真**: tutorial.ipynb 用静态 if/else 模拟牛津 fellow (Socratic 追问 + 禁直接答案 + devil's advocate), 4 轮多轮脚手架渐退 + student_model.json 跨单元复用 + Hattie 四级反馈 [TASK]/[PROCESS]/[SELF-REG]/[FEED-FORWARD] (避免 Self 级表扬 d≈0.09) + 限频 1次/天防依赖。

### 交叉练习 (interleaving)

practice.md 明文排布 A1B1C1...B2C2A2...C3A3B3 交叉序列 (非块状), 强迫大脑在 OLS / NPV / 弹性+蒙特卡洛 三个子技能间反复检索, 提升长期保留 ~30% (MIT Open Learning + Butler 2010)。

### mastery 阈值与跨单元前馈

alignment.md 的 mastery 总阈值: 三 ILO 各自达标 + 300 字备忘录整合 + schedule.json 首日复习 + tutorial exit artifact。未达标触发 weak_loop; 盲点写入 student_model.json, Day 3 (Agent 经济) 读取本文件个性化起点脚手架层级 (Feed Forward 纵向)。

### 与 v5.0 的关系

v6.0 四件套**只追加不修改** v5.0 内容。v5.0 的 statsmodels OLS (R²=0.859) / numpy-financial NPV (DeepSeek V3 $5.576M) / scipy.stats 弹性 (-0.6169) / 天道推演 10k 蒙特卡洛 仍是所有 drill/卡片/ILO/tutorial 的真实数据底座, 学习科学层只是把"练"升级为"科学地练"。

*学习科学层 v6.0 · 最后更新: 2026-07-25*

---

## 研究产出与产业链接层 (v7.0)

本单元产出可发表研究工件 (research.md: 研究问题+贡献声明+arXiv链接+IMRaD大纲+NeurIPS可复现清单+research-to-practice翻译) 与产业链接 (industry.md: >=3真实企业+部署场景+Imperial咨询项目+HBS教学案例+客座讲座+实习指针)。研究产出遵循IMRaD/DSR(Hevner)/OSF预注册/FAIR/可复现研究标准; 产业链接遵循Imperial MSc BA咨询项目(Burberry/Expedia/J&J)/HBS案例法/MIT Sloan行动学习模式。详见 research.md 与 industry.md。

*研究产出与产业链接层 v7.0 · 最后更新: 2026-07-26*

---

## 学术前沿层 (v9.0)

本单元新增 `frontier.md`：注入 2025-2026 最新学术前沿（N 篇真实 arXiv 论文 + 批判性综述 + delta_to_unit + ≥3 开放研究问题 + 方法论批评）。论文来自 `_frontier_corpus/skill-4-business-model.md` 共享语料库（arXiv 搜索 + abstract 页抽查验证），覆盖前沿课题：AI原生商业模式 × outcome-based pricing。面向博后/教授级读者：批判性综述非罗列，delta_to_unit 显式指出前沿如何更新本单元所教，开放问题为可发表研究方向。详见 `frontier.md`。

---

## AI工程从零构建层 (v11.0)

> v11.0 新增 [`from_scratch.md`](./from_scratch.md)：AI工程从零构建，与本单元 statsmodels/numpy-financial/scipy.stats 形成对照。
> - **从零构建主题**：手写 NPV 贴现估值 + OLS 正规方程 + 价格弹性 log-log 回归 + outcome-based pricing 封顶模型
> - **核心算法**：$\text{NPV} = \sum_t \frac{CF_t}{(1+r)^t}$ + 弹性 $\epsilon = \frac{d\ln Q}{d\ln P}$ + OLS $\hat\beta=(X^TX)^{-1}X^Ty$（含数学推导 + LaTeX）
> - **code_artifact**：手写 numpy 骨架（npv + ols_fit + price_elasticity + outcome_pricing），imports ⊆ {numpy}，附 verification_property
> - **延伸阅读**：rohitg00 AI工程 from scratch P17 Inference Platform Economics / P17 FinOps LLMs
> - **手写实现要点**：用 from-scratch numpy 而非 statsmodels/numpy-financial，理解到金属层
> - **verification_property**：NPV 与闭式 DCF 一致；log-log 回归精确恢复真实弹性 -1.5；outcome pricing Cap 生效
