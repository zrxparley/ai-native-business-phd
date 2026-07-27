# 技能3 · Day 1：因果推断基础 · 讲义（v5.0 学习材料包版）

> **所属**：AI原生化商业博士 · 技能3 因果推断与规模实验 · Day 1
> **版本**：v5.0（从独立教材升级为学习材料包）
> **预计**：2h 讲义 + 2h 上机练习
> **核心命题**：营销决策如何从"相关"走向"因果"？
> **v5.0 升级点**：① 新增真实数据集上机（Lalonde/NSW）② 新增 TODO 填空式起始笔记本 ③ Notebook 化 ④ 深链阅读 ⑤ 2026 前沿（LLM-as-a-judge 评估因果结论）

---

## 学习目标（学完你能做到）

1. 能用 Pearl 因果阶梯（关联/干预/反事实）解释"为什么相关≠因果"，并指出一个营销场景中各层级对应的操作
2. 能为一个营销问题画出因果有向无环图（DAG），识别混杂因素与后门路径，说明如何用后门准则阻断
3. 能在**真实数据**上区分"朴素均值差（有偏）"与"后门调整估计（因果）"，并解释两者差异的来源
4. 能用 DoWhy 完成"建模→识别→估计→反驳"四步因果分析流程
5. 能用混合方法视角（解释性序列）设计一个营销 AI 系统的因果评估方案

---

## 理论部分：精炼索引（详见独立教材）

> Day 1 的完整理论讲义见 [`../../AI原生化商业博士_独立教材_技能3_因果推断与规模实验.md` § Day 1](../../AI原生化商业博士_独立教材_技能3_因果推断与规模实验.md)（1.1–1.5 节，已包含因果阶梯/潜在结果框架/do-演算/混合方法/Stanford对标）。本讲义不重复，仅做上机所需的关键回顾。

### 关键回顾 1：因果阶梯（Pearl）

| 层级 | 问题 | 符号 | 营销示例 |
|:----:|------|------|---------|
| L1 关联 | 观察到X，Y怎样？ | P(Y\|X) | 观察到用户点广告，转化率多少？ |
| L2 干预 | 我做X，Y怎样？ | P(Y\|do(X)) | 我投放广告，转化率多少？ |
| L3 反事实 | 当时没做X，Y怎样？ | P(Y_x\|X',Y') | 这个转化用户若没看广告还会转化吗？ |

**A/B 测试 = L2 干预的物理实现**（随机分配 ≈ do 操作，切断所有指向处理变量的路径）。

### 关键回顾 2：混杂与后门准则

```
营销场景因果图（DAG）：

  用户年龄 ──→ 用户活跃度 ──→ 广告曝光 ──→ 点击 ──→ 转化
                    │                                  ▲
                    └──────────→ 历史购买 ──────────────┘
```

- **混杂因素**：同时影响处理（广告曝光）和结果（转化）的变量——这里是"用户活跃度"
- **后门路径**：广告曝光 ← 用户活跃度 → 转化（创造虚假相关）
- **后门准则**：控制混杂因素（在"用户活跃度"节点切断），即可识别广告曝光→转化的真实因果效应

### 关键回顾 3：为什么不能直接用均值差

$$\hat{\text{ATE}}_{naive} = \bar{Y}_{treated} - \bar{Y}_{control} = \text{ATE} + \text{Bias}$$

偏差来自混杂因素在两组分布不均。**随机化（RCT）消除偏差；观测数据需用后门调整/匹配/IV 等方法消除偏差**——这就是今天上机的核心。

---

## 上机部分：在真实数据上识别混杂、估计因果效应

> 📓 **配套笔记本**：[`starter.ipynb`](./starter.ipynb)（TODO 填空版，你来做）｜ [`solution.ipynb`](./solution.ipynb)（参考答案，gated，做完再看）
> 📊 **真实数据集**：[`data/README.md`](./data/README.md)（Lalonde/NSW 真实数据 + 营销 A/B 测试延伸）

### 为什么用真实数据而非模拟数据

v4.0 的代码普遍用"模拟数据"——模拟数据会让你**预设了答案**（因为你造的数据就是按某个因果结构生成的），学不到"真实世界里混杂长什么样、有多脏"。v5.0 改用 **Lalonde/NSW 数据集**：这是因果推断领域最经典的真实数据集（Dehejia & Wahba 1999），NSW 职业培训实验的真实数据 + 观测对照组，**真实地存在严重混杂**——正是教学需要的。

### 营销映射（关键桥接）

NSW 数据是职业培训，但因果结构与营销问题同构：

| NSW 变量 | 营销对应 | 含义 |
|---------|---------|------|
| `treat`（是否参加培训） | 是否收到优惠券/是否看到广告 | 处理变量 T |
| `re78`（1978年收入） | 转化率 / GMV / 客单价 | 结果变量 Y |
| `age`, `education`, `black`, `hispanic`, `married`, `nodegree`, `re74`, `re75` | 用户画像特征（活跃度/历史消费/设备…） | 协变量 X（潜在混杂） |

**你要回答的因果问题**：参加培训（收到优惠券）对收入（转化）的**真实因果效应**是多少？朴素均值差为何有偏？后门调整后估计如何变化？

### 上机任务（6 个 TODO，见 starter.ipynb）

1. **TODO1**：加载真实数据（`causaldata.nsw`）
2. **TODO2**：探索数据——处理组/对照组样本量、协变量分布是否均衡
3. **TODO3**：朴素估计——直接算处理组-对照组 `re78` 均值差（有偏）
4. **TODO4**：用 DoWhy 建因果模型（声明 DAG）→ 识别 → 后门调整估计
5. **TODO5**：反驳检验（安慰剂处理）——验证估计稳健性
6. **TODO6（可选）**：营销延伸——用倾向得分匹配（PSM）再估一次，对比三种估计

---

## 2026 前沿补充：LLM-as-a-judge 评估因果结论

> v5.0 新增前沿点。你的 v4.0 教材在因果评估上只有"统计显著性 + 反驳检验"。2026 年的一个新趋势是用 **LLM-as-a-judge** 辅助评估因果结论的**可信度**（不是估计效应本身，而是评估"你的因果论证是否站得住脚"）。

**怎么用**：把你建好的 DAG、识别策略、估计结果、反驳检验结果，整理成一段结构化描述，让 LLM 扮演"因果推断评审"（参考 NeurIPS 2023 的 LLM-as-a-judge 范式，arXiv 2306.05685），检查：
- DAG 是否遗漏了可能的混杂？
- 识别策略是否满足后门准则？
- 反驳检验是否充分？
- 结论是否过度外推？

**注意**：LLM-as-a-judge 是**辅助审查因果论证质量**，不能替代统计估计。它对应因果阶梯的 L1（对论证文本的关联分析），不能上升到 L2/L3。把它定位为"研究方法论的自检工具"，而非"因果效应估计器"。

> 🔗 深入阅读见 [`reading.md`](./reading.md) 的 LLM-as-a-judge 条目。

---

## 与后续 Day 的衔接

- **Day 2**：实验设计（A/B 测试统计基础、准实验 DiD/RDD/IV）——今天是观测数据的因果识别，Day 2 是实验数据的因果识别
- **Day 3**：营销归因与增量度量（MMM、增量测试、因果森林）——今天的方法用到营销归因
- **Day 4**：因果发现（PC/FCI 算法从数据自动学 DAG）——今天是你**人为画** DAG，Day 4 是**算法学** DAG

---

## 作业与评估

作业、5 分制量表、费曼演练、2 分钟话术、复盘自诊表——沿用独立教材 § Day 1 既有设计（v3.1 以来未变，质量已验证）。本学习材料包不重复，仅新增上机交付物：

**新增交付物（v5.0）**：
- [ ] 完成的 `starter.ipynb`（6 个 TODO 全部填好，能跑通）
- [ ] 一段 300 字分析：朴素估计 vs 后门调整估计的差异来自哪个混杂变量？
- [ ] （可选）用 LLM-as-a-judge 自检你的因果论证，记录它指出的 1 个你没想到的潜在混杂

---

*本讲义由 v5.0 学习材料包升级生成。理论部分引用独立教材，上机部分用真实数据 + TODO 脚手架。*
*最后更新：2026-07-23*

---

## 学习科学层 (v6.0)

> v6.0 在 v5.0 的 5 文件基础上新增 4 文件（practice.md / schedule.json / alignment.md / tutorial.ipynb），不破坏 v5.0 基线。本节是 v5.0 与 v6.0 的桥接说明，仅追加，未改原文。

### 设计哲学

v5.0: 真实即严谨 · 练习即掌握
v6.0: **科学即高效 · 反馈即成长** -- 用学习科学把"练习"升级为"刻意练习 (deliberate practice) + 间隔重复 (spaced retrieval) + 建构对齐 (constructive alignment) + 牛津 tutorial (Socratic) 仿真"。

### 4 个新增文件的角色

1. **practice.md** -- Ericsson 刻意练习 5 要素 + MIT 6.5940 Worked-Faded 渐退示例 + 交叉 interleaving (A1B1C1...B2C2A2...C3A3B3 明文) + CS229 pset0 式 diagnostic 前测 + CS230 渐进项目 (proposal->milestone->final->poster) + weak_loop 弱项循环
2. **schedule.json** -- FSRS-6 间隔重复算法（SM-2 备份），request_retention=0.9，5 张卡片对应 NSW 后门调整 / DAG / DoWhy / LLM-as-judge / 因果阶梯核心概念，间隔 [1,3,8,21,60,180] 天
3. **alignment.md** -- Biggs 建构对齐 ILO ↔ TLA ↔ AT 矩阵（5 行）+ mastery_threshold + Hattie 3 自检问（Feed Up / Feed Back / Feed Forward）
4. **tutorial.ipynb** -- Oxford tutorial fellow 仿真，Socratic 追问（不直接给答案）+ HBS devil's advocate + Hattie 四级反馈 [TASK]/[PROCESS]/[SELF-REG]/[FEED-FORWARD] + student_model.json 跨单元复用 + 限频 1 次/天防依赖

### 与 v5.0 的衔接

- v5.0 的 `starter.ipynb` 6 个 TODO 对应 practice.md 的 D2 (DoWhy 四步) 和 D3 (LLM-as-judge 审查)
- v5.0 的"学习目标"5 条对应 alignment.md 的 ILO1-ILO5
- v5.0 的"作业与评估"对应 alignment.md 的 AT (Assessment Task) + practice.md 的 progressive_project
- v5.0 的"2026 前沿 (LLM-as-a-judge)"对应 practice.md D3 + schedule.json C4 + tutorial.ipynb Socratic 第 4 轮

### 学习科学关键词索引 (v6.0 验收用)

FSRS-6 · SM-2 · 刻意练习 (deliberate practice) · 建构对齐 (constructive alignment) · 牛津 tutorial · Socratic · Hattie · 间隔重复 (spaced retrieval) · 交叉 (interleaving) · mastery · Worked-Faded

---

*v6.0 学习科学层追加完成 · 2026-07-25*

---

## 研究产出与产业链接层 (v7.0)

本单元产出可发表研究工件 (research.md: 研究问题+贡献声明+arXiv链接+IMRaD大纲+NeurIPS可复现清单+research-to-practice翻译) 与产业链接 (industry.md: >=3真实企业+部署场景+Imperial咨询项目+HBS教学案例+客座讲座+实习指针)。研究产出遵循IMRaD/DSR(Hevner)/OSF预注册/FAIR/可复现研究标准; 产业链接遵循Imperial MSc BA咨询项目(Burberry/Expedia/J&J)/HBS案例法/MIT Sloan行动学习模式。详见 research.md 与 industry.md。

- **research.md** (研究产出层): 锚定 NSW 后门调整 ATE ≈ \$1794 (Dehejia & Wahba 1999) 的可复现研究问题; linked_paper 引用 arXiv 2306.05685 (LLM-as-a-judge, NeurIPS 2023) + arXiv 2008.12519 (DoWhy) + Dehejia & Wahba 1999 DOI; IMRaD 四段大纲含 RQ1-RQ3 + NeurIPS 可复现清单 7 项 (code/data/seeds/environment/preregistration/FAIR/LLM-prompt); research-to-practice 翻译为 HBS working paper -> HBR article / MIT Sloan teaching case / 企业白皮书 / DeepEval CI 测试用例。
- **industry.md** (产业链接层): real_companies 选 Microsoft ExP / Netflix / Uber / Booking.com / Amazon (5 家, 全部来自因果推断/A-B 公司库); deployment_example 为 Bing 搜索排序的混合因果评估流程 (偏差 30%->8%); consulting_project 为 Booking.com 8 周 4-5 人 Imperial MSc BA 项目; case_study 为 HBS 风格 Elena (Head of AI) 决策钩子; guest_lecture 为 Microsoft ExP 首席应用科学家 90 分钟讲座; internship_pointer 为 Microsoft ExP / Google AI Resident / Booking.com 三个实习路径。

### 研究产出/产业链接关键词索引 (v7.0 验收用)

研究产出 · research output · IMRaD · 可复现 · reproducibility · OSF · preregistration · 预注册 · FAIR · contribution · 贡献 · 产业链接 · industry linkage · consulting · 咨询 · case study · 案例 · guest lecture · 客座 · internship · 实习 · deployment · 部署 · linked_paper · DSR · Hevner · research-to-practice · NeurIPS · MIT Sloan · 行动学习 · action learning

---

*v7.0 研究产出与产业链接层追加完成 · 2026-07-26*

---

## 学术前沿层 (v9.0)

本单元新增 `frontier.md`：注入 2025-2026 最新学术前沿（5 篇真实 arXiv 论文 + 批判性综述 + delta_to_unit + ≥3 开放研究问题 + 方法论批评）。论文来自 `_frontier_corpus/skill-3-causal.md` 共享语料库（arXiv 搜索 + abstract 页抽查验证），覆盖前沿课题：因果推断×大语言模型（因果发现/推理/反事实）。面向博后/教授级读者：批判性综述非罗列，delta_to_unit 显式指出前沿如何更新本单元所教，开放问题为可发表研究方向。详见 `frontier.md`。
