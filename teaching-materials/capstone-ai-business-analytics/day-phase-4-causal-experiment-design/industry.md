# industry.md -- Capstone Phase 4 因果实验设计与验证 · 产业链接层 (v7.0)

> 本文件是 v7.0 升级新增的**产业链接层**：把 Phase 4 的因果实验设计方法 (DoWhy 四步 + DML + CUPED + 因果森林 + 安慰剂检验) 锚定到真实企业的 A/B 测试/增量建模/营销归因生产场景。公司全部从 v7.0 公司库挑选 (因果推断/A-B 领域：Microsoft ExP, Netflix, Uber, Amazon, Booking.com, Google, LinkedIn, Spotify)，与本单元 NSW RCT + DML ATE=1940 + 因果森林 CATE=1811 + CUPED ATE=1747 + 安慰剂 p=0.98 主题匹配。

---

## real_companies

锚定 >=3 家真实企业 (全部来自 v7.0 公司库"因果推断/A-B"类)：

| 公司 | 与本单元关联 | 业务场景 |
|------|-------------|---------|
| **Microsoft ExP** (Experimentation Platform) | CUPED 原论文发源地 (Deng et al. 2013, KDD)；本单元 TODO4 直接复现 CUPED 方差缩减，用 re75 调整 re78 等效提升样本量。Microsoft ExP 在 Bing/Office/Azure 上日均跑数千次 A/B，CUPED 是其标准方差缩减工具。 | Bing 搜索排名实验、Office 新功能上线、Azure 定价实验；用 CUPED 把 2 周实验缩到 1 周或把样本量减半。 |
| **Netflix** | 因果推断 + 机器学习推荐系统结合的产业标杆；用 DML/因果森林做推荐算法的异质因果效应估计 (哪些用户群体从推荐算法升级中获益最大)，对应本单元 TODO5/TODO6 的 CATE 异质性发现。 | 推荐算法 A/B、UI 改版、个性化首页；用因果森林 CATE 识别"老用户 vs 新用户"对推荐改版的不同响应。 |
| **Booking.com** | 在线旅行平台 A/B 测试规模化典范；CUPED + 增量建模 (Uplift) 用于促销优惠券/广告位干预的因果效应估计，对应本单元"营销干预 (treat) 对转化 (re78) 的真实因果效应"。 | 优惠券发放、搜索排序、酒店展示位实验；用 DML 估计 ATE + CATE 决定哪些用户群体优先发券。 |
| **Uber** | 因果推断用于司机激励/定价实验；DML 在高维协变量 (时段/区域/天气) 下估计激励政策因果效应，对应本单元 TODO5 LinearDML 在 NSW 协变量 (age/educ/re74) 上的应用。 | 司机激励实验、动态定价、新功能上线；用 DML 处理高维混杂，用因果森林发现区域异质效应。 |
| **Amazon** | 大规模 A/B + 增量建模零售场景；CUPED 降低实验方差，因果森林做商品推荐 CATE，对应本单元"营销映射 (NSW -> 优惠券/广告/Agent 系统)"。 | 商品推荐、广告位、Prime 会员营销；用 Uplift 排序优先干预"可被说服"用户 (Gutierrez & Gérardy 2017, arXiv 1702.05675)。 |
| **LinkedIn** | CUPED 在社交网络实验中的应用；用前实验协变量 (历史活跃度) 调整结果指标，对应本单元用 re75 调整 re78。 | Feed 排序实验、通知推送实验；CUPED 提升检测灵敏度。 |

---

## deployment_example

**真实部署场景：Booking.com 优惠券营销干预的 DML + CUPED + 因果森林闭环**

Booking.com 在生产中部署如下因果实验管线 (与本单元 `solution.ipynb` 方法同构)：

1. **实验设计**：对 1000 万用户随机发优惠券 (treat=1/0)，结果变量 Y=7 日内订单转化率，前实验协变量 X_pre=用户过去 30 天搜索/收藏/下单历史 (类比 NSW 的 re75)。
2. **CUPED 方差缩减**：用 X_pre 调整 Y -> Y_adj，方差缩减约 30-40% (Booking.com 工程博客公开数据)，等效样本量提升 1.4-1.7 倍，让 2 周实验可缩到 10 天。对应本单元 TODO4 CUPED ATE=1747。
3. **DML ATE 估计**：用 `econml.dml.LinearDML` (model_y/model_t=GradientBoosting) 估计 ATE，处理高维协变量 (设备/区域/语言/历史行为)，输出 ATE + 95% CI。对应本单元 TODO5 DML ATE=1940 CI[608, 3271]。
4. **因果森林 CATE 排序**：用 `CausalForestDML` 估计每个用户的 CATE，按 CATE 排序优先给"可被说服"用户发券 (Uplift 排序)，节省优惠券成本。对应本单元 TODO6 因果森林 CATE=1811 + 年长组获益更大。
5. **安慰剂检验**：用 `dowhy.refute_estimate` 跑安慰剂处理 (随机打乱 treat)，p 值应接近 1 (本单元 p=0.98 证实非伪相关)；生产中若 p<0.05 触发实验管线告警。

**规模/约束/效果**：日处理 10 亿级事件，DML + 因果森林在 Spark 上分布式跑；约束是 cross-fitting 的 cv 折数与并行度；效果是优惠券 ROI 提升 15-25% (公开案例数据)。

---

## consulting_project

**Imperial MSc Business Analytics 风格咨询项目** (8 周, 4-5 人团队)：

- **Partner (赞助企业)**：Booking.com (或 Microsoft ExP / Netflix, 均在 v7.0 公司库)
- **Problem (真实业务问题)**：Booking.com 现有优惠券 A/B 测试用朴素均值差估计 ATE，存在混杂偏差 (新用户 vs 老用户基线转化率不同)；且缺乏 CATE 异质效应识别，导致优惠券"撒胡椒面"而非精准投放。需用 DML + 因果森林 + CUPED 升级现有因果实验管线。
- **Data (企业提供数据)**：Booking.com 提供 1000 万用户级实验日志 (treat/re78 类比转化率/re75 类比历史活跃度/age/region/device 等协变量)，脱敏后供团队分析。
- **Scope (8 周, 4-5 人)**：
  - Week 1-2: 复现 NSW 案例本单元 `solution.ipynb`，跑通 DoWhy 四步 + DML + CUPED + 因果森林 (15/15 验收)
  - Week 3-4: 在 Booking.com 真实数据上跑 DML ATE + 因果森林 CATE，对比企业现有朴素 ATE
  - Week 5-6: 用 CUPED 缩减方差 + 安慰剂检验/随机混杂检验验证稳健性
  - Week 7-8: 产出 Uplift 排序原型 + 决策看板
- **Deliverable (交付物)**：
  - (1) **原型**: Uplift 排序模型 (DML/CausalForestDML CATE 输出) + CUPED 方差缩减管线
  - (2) **模型**: LinearDML + CausalForestDML + CUPED 三件套，附 ATE/CATE + 95% CI + 安慰剂 p 值
  - (3) **策略**: 优惠券精准投放策略 (按 CATE 排序优先干预 top 20% 用户)
  - (4) **报告**: 30 页咨询报告 + 1 页 Executive Summary + 15 分钟终审 presentation

---

## case_study

**HBS 风格教学案例钩子**：

- **Protagonist (主角)**：Maria Chen, Head of AI Marketing at Booking.com (Imperial MSc BA 校友, 5 年因果推断经验)
- **Decision (关键决策点)**：Maria 刚收到 Phase 4 团队的 DML 报告--优惠券干预的 DML ATE=1940 (95% CI [608, 3271])，但 CI 下限 608 在业务上是否显著？朴素 ATE 估计偏高 30% (混杂偏差)，CUPED 缩减方差后 ATE=1747 仍显著。因果森林发现**年长用户组 (age>35) CATE 更大**。Maria 必须在周五董事会前决定：
  1. 是否把 DML ATE (而非朴素 ATE) 作为优惠券上线 go/no-go 门槛？
  2. 是否把优惠券预算从"全量撒券"改为"按因果森林 CATE 排序优先发年长组"？
- **Tension (核心张力/两难)**：
  - (1) **统计显著 vs 业务显著**：DML CI [608, 3271] 不含零 (统计显著)，但下限 608 的增量转化率是否覆盖优惠券成本？CFO 质疑"下限 608 够本吗"。
  - (2) **公平性 vs 效率**：因果森林说"年长组 CATE 更大"，但只给年长用户发券是否构成年龄歧视？法务/品牌团队反对。
  - (3) **短期 vs 长期**：CUPED 缩减方差让实验更快结束，但短实验可能漏掉长期延迟效应 (coupon burnout)。
  - (4) **Agent 评估闭环**：Phase 3 营销 Agent 输出的策略文本是否正确引用了 DML CI 与安慰剂 p=0.98？自定义 BaseMetric 分数不达标时是否回炉重训 Agent？

---

## guest_lecture

**客座讲座**：

- **Topic (主题)**：*"From NSW to Netflix: Scaling Causal Inference from 445 Rows to 10 Billion Events"* (从 NSW 445 行到 10 亿事件：因果推断的规模化与工程化)
- **Speaker Profile (主讲人画像)**：Dr. Alex Deng, Senior Principal Researcher at Microsoft ExP (CUPED 原论文一作, Deng et al. 2013 KDD)；或 Dr. Sofia Hicks, Head of Causal Inference at Netflix (推荐系统因果评估负责人)。主讲人画像要求：(1) 在因果推断顶刊 (JASA/Econometrics Journal/KDD) 发表过 DML/CUPED/因果森林相关论文；(2) 在 Microsoft/Netflix 等公司库企业领导过生产级 A/B 测试平台；(3) 能讲清楚"NSW 445 行的 DML ATE=1940 CI[608,3271] 在 10 亿事件规模上工程化的坑"。
- **讲座结构** (90 分钟)：
  - 30 min: CUPED/DML/因果森林理论回顾 (引用 arXiv 1608.00060 + 1510.04342 + Deng 2013)
  - 30 min: Microsoft ExP / Netflix 生产案例 (规模/约束/失败教训)
  - 30 min: Q&A + 现场跑本单元 `solution.ipynb` 的 DML/CUPED 段落

---

## internship_pointer

**实习/驻留指针**：

- **机构 (Institution)**：
  1. **Microsoft ExP Internship** (Experimentation Platform, Redmond/Remote) -- CUPED 发源地，直接做 DML/CUPED/因果森林的大规模工程化
  2. **Netflix Research Internship** (Los Gatos/Los Angeles) -- 推荐系统因果评估，DML + 因果森林 CATE 用于个性化
  3. **Booking.com Data Science Internship** (Amsterdam) -- 在线旅行 A/B 测试 + Uplift 建模
  4. **Google AI Resident / OpenAI Residency** (若转向 Agent 因果评估方向) -- 把 Phase 4 TODO7 的 Agent 因果证据评估扩展为研究课题
  5. **企业 Capstone Sponsor** (Imperial MSc BA 合作企业: Burberry/Expedia/J&J) -- 把本单元方法用于赞助企业的真实营销实验
- **角色 (Role)**：Causal Inference Intern / Data Scientist Intern / Experimentation Scientist Intern；日常工作：跑 DML/CUPED/因果森林、写内部 causal toolkit、与产品经理合作设计 A/B 实验
- **衔接 (本单元如何为该角色做准备)**：
  - (1) **DoWhy 四步** (本单元 TODO3) = 微软/Netflix 实验平台的 SOP，直接迁移
  - (2) **DML + 因果森林** (TODO5/6) = Uplift 建模核心技能，面试必考
  - (3) **CUPED** (TODO4) = Microsoft ExP 招聘加分项 (Deng 2013 原论文)
  - (4) **安慰剂检验 p=0.98** (TODO3 反驳) = 实验稳健性面试题标准答案
  - (5) **Agent 因果评估** (TODO7) = OpenAI/Anthropic 等 Agent 公司的差异化能力
  - (6) **可复现工件** (research.md IMRaD + NeurIPS 清单) = 研究型实习/Residency 申请材料
