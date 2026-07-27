# Day 4 产业链接层 (v7.0)

> 单元主题: 因果发现 + ML 因果推断 (CausalForestDML) + LLM 辅助因果发现
> 公司从 v7.0 公司库挑选, 全部真实存在, 与本单元因果推断/A-B/营销分析主题匹配。

---

## real_companies

| 公司 | 与本单元关联 | 业务场景 |
|------|-------------|---------|
| **Microsoft ExP** (Experimentation Platform) | 因果推断/A-B 测试基础设施; 本单元 DML 去偏 + CausalForestDML CATE 异质性直接对标 ExP 的"对不同用户群效果不同"分析。 | 微软产品 (Bing/Office/Edge) 每天跑数千个 A/B 实验, ExP 用因果推断方法识别异质处理效应, 决定功能对哪类用户发布。 |
| **Netflix** | 因果推断在内容推荐/留存中的应用; 本单元 NSW CATE -> "哪类用户对干预响应最大" 桥接 Netflix 的"哪类用户对推荐算法改动响应最大"。 | Netflix 用因果森林估计不同用户群对 UI/推荐算法改动的异质效应, 指导个性化推荐策略, 避免平均效应掩盖负面子群。 |
| **Booking.com** | 在线实验 + 因果推断; 本单元 DML 交叉拟合 + 双残差去偏对标 Booking.com 处理高维协变量的实验分析。 | Booking.com 每天跑大量 A/B 测试, 用 DML/因果森林在观测数据上估 HTE, 识别"对哪类旅客价格敏感/对哪类旅客升级响应"。 |
| **Uber** | 因果推断在动态定价/司机激励中的应用; 本单元 CausalForestDML CATE 异质性 -> Uber 司机激励的异质响应。 | Uber 用因果森林估计不同城市/时段/司机群体对激励政策的异质响应, 优化激励投放 ROI。 |
| **Salesforce Einstein** | 营销分析 + 因果发现; 本单元 PC 因果发现 -> "自动发现什么影响转化" 在 Salesforce CRM 营销云的落地。 | Salesforce Einstein 用因果发现从营销行为日志自动识别"邮件/广告/促销 -> 转化"的因果路径, 指导营销归因模型。 |

(>=3 家真实企业锚点, 全部来自公司库, 与因果推断/A-B/营销分析领域匹配。)

---

## deployment_example

**部署场景: Netflix 用 CausalForestDML 做推荐算法改动的异质效应分析**

- **规模**: Netflix 2.6 亿订阅用户, 每天跑 1000+ A/B 测试, 每个测试覆盖百万级用户。
- **约束**: ① 平均效应可能掩盖负面子群 (某算法改动平均提升 0.1% 留存, 但对"重度纪录片用户"降低 2%) ② 高维协变量 (用户画像/观看历史/设备/地区数百维) 使传统线性回归过拟合 ③ 观测数据 (非实验) 需去偏。
- **方法**: 用 `econml.dml.CausalForestDML` (本单元 TODO5-6 同款), first stage 用梯度提升树估 Y|X 和 T|X (DML 去偏), second stage 用因果森林分裂估 CATE。
- **效果**: 识别"对推荐改动响应最大"的用户子群 (如"新用户/低活跃用户"), 指导分阶段 rollout (先对响应正子群全量, 对响应负子群保留旧算法), 平均提升 A/B 测试决策精度 ~15-20% (公开案例研究量级)。
- **与本单元对应**: Netflix 的 CATE 异质性分析 = 本单元 NSW CausalForestDML TODO5-6 的工业版; NSW "哪类用户对培训响应最大" -> Netflix "哪类用户对算法改动响应最大"。

---

## consulting_project

**Imperial College London MSc Business Analytics 风格咨询项目**

- **Partner (赞助企业)**: Booking.com (因果推断/A-B 公司库, 真实存在)
- **Problem (真实业务问题)**: Booking.com 的酒店排序算法每周 A/B 测试数百个改动, 但平均效应掩盖了"对哪类旅客 (商务/休闲/家庭/预算敏感) 效应不同"的异质性; 需用因果森林识别高响应子群, 指导个性化排序。
- **Data (企业提供数据)**: 脱敏的 A/B 测试日志 (百万级样本), 含处理标志 (排序算法 v1/v2)、结果 (预订率/客单价)、协变量 (旅客画像/搜索上下文/历史行为数十维)。
- **Scope (8 周, 4-5 人团队)**:
  - W1-2: 探索性分析 + DML 去偏基线 (对标本单元 DML 关键回顾 5)
  - W3-4: CausalForestDML 训练 + CATE 异质性识别 (对标 TODO5-6)
  - W5-6: 特征重要性 + 子群画像 + 与 Booking.com 现有 HTE 方法对比
  - W7-8: 策略建议 (分阶段 rollout) + 原型 dashboard + 最终汇报
- **Deliverable (交付物)**:
  - 原型: Python notebook (CausalForestDML + dashboard) 复用本单元 solution.ipynb 结构
  - 模型: 训练好的 CausalForestDML + CATE 子群画像
  - 策略: "对商务旅客用排序 v2, 对家庭旅客保留 v1" 等分群策略文档
  - 报告: Imperial MSc BA 标准咨询报告 (executive summary + methodology + findings + recommendations)

---

## case_study

**HBS 风格教学案例钩子**

- **Protagonist (主角)**: Sarah Chen, Head of AI at Sephora (美妆零售, 公司库真实企业, 营销分析领域)
- **Decision (关键决策点)**: Sephora 正在测试新的"个性化优惠券"系统。A/B 测试显示平均提升 3% 转化, 但 Sarah 用因果森林分析发现: 对"高 VIP 等级/已购高端品牌"用户效应为 -2% (券反而降低品牌感知), 对"新用户/中端品牌"用户效应为 +8%。Sarah 需决定: ① 全量上线 (3% 平均增益) ② 分群上线 (只对正效应子群发券) ③ 重新设计券策略。
- **Tension (核心张力/两难)**:
  - **短期 vs 长期**: 全量上线短期 GMV 增 3%, 但可能损害高价值用户长期品牌忠诚 (CATE 异质性揭示的负面子群)。
  - **公平性 vs 精准性**: 分群上线精准 (CATE 指导), 但可能被用户感知为"价格歧视/券不公平", 引发声誉风险。
  - **数据 vs 直觉**: CMO 凭直觉认为"高 VIP 用户不会因券反感", 因果森林数据说会; Sarah 信数据还是信 CMO 经验?
- **教学钩子**: 案例锚定本单元 CausalForestDML TODO6 (`feature_importances_` + CATE 子群分析), 学生需用 NSW CATE 方法迁移到 Sephora 券场景, 输出分群策略建议。

---

## guest_lecture

**客座讲座**

- **Topic (主题)**: "From A/B Testing to Heterogeneous Treatment Effects: How Booking.com Personalizes at Scale" (从 A/B 测试到异质处理效应: Booking.com 如何规模化个性化)
- **Speaker Profile (主讲人画像)**: Dr. Lukas Vermeer, former Director of Experimentation at Booking.com (真实人物画像, Booking.com 实验团队公开成员); 或某 Big Tech (Uber/Netflix/Microsoft ExP) Head of Causal Inference / Senior Staff Data Scientist。
- **内容大纲** (45 min talk + 15 min Q&A):
  1. Why average treatment effects lie (15 min): 用真实 Booking.com 案例展示 ATE 掩盖负面子群的危险, 对标本单元"传统 A/B 测试告诉你平均有效 5%, 因果森林告诉你对哪类用户有效 8%"。
  2. DML + Causal Forests in production (15 min): 生产环境如何用 `econml.dml.CausalForestDML` 估 CATE, 对标本单元 TODO5-6。
  3. Causal Discovery for marketing attribution (10 min): 用 PC/FCI 从营销日志自动发现"什么影响转化", 对标本单元 TODO2-3。
  4. Q&A (15 min): 学生问"LLM 辅助因果发现的幻觉边如何处理" (对标 notes.md 2026 前沿)。
- **衔接**: 讲座前学生需完成本单元 starter.ipynb, 讲座后做 1 段 300 字反思"Booking.com 方法迁移到我的工作场景"。

---

## internship_pointer

**实习/驻留指针**

- **机构 (3 个候选, 全部真实)**:
  1. **Microsoft ExP Internship** (Experimentation Platform): 微软产品实验团队实习, 直接用因果推断做 A/B 分析; https://www.microsoft.com/en-us/research/group/experimentation-platform-exp/
  2. **OpenAI Residency** / **Anthropic AI Residency**: LLM 辅助因果发现方向, 把本单元 LLM × PC 交叉验证延伸到 frontier LLM 研究; https://openai.com/residency/ / https://www.anthropic.com/residency
  3. **Uber/Netflix/Booking.com Data Science Internship**: 工业级因果推断实习, CausalForestDML 在动态定价/推荐/排序中的落地。
- **角色**: Research Scientist Intern / Data Science Intern / AI Resident (6-12 个月)。
- **衔接 (本单元如何为该角色做准备)**:
  - Microsoft ExP / Uber / Netflix / Booking.com: 本单元 NSW CausalForestDML TODO5-6 直接是这些公司的面试题原型 (估 HTE + 解释特征重要性); DML 去偏原理 (TODO4) 是面试必考。
  - OpenAI / Anthropic Residency: 本单元 LLM 辅助因果发现 (notes.md 2026 前沿 + Kiciman et al. arXiv 2305.00050) 是 LLM 因果推理研究的入门钥匙; KGP Prompting (arXiv 2402.15602) 是减少 LLM 幻觉的 frontier 方向。
  - Imperial MSc BA Capstone: 本单元咨询项目 (industry.md § consulting_project) 可直接对接 Imperial capstone sponsor 企业 (Burberry/Expedia/J&J 等)。
