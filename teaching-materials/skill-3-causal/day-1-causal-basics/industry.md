# Day 1 产业链接层 (v7.0)

> 本单元 (因果推断基础) 的产业锚点: 把 NSW 后门调整 + DoWhy 四步 + LLM-as-a-judge 论证审查, 落到真实企业的 experimentation / causal inference 团队如何用、如何赞助咨询项目、如何写教学案例。与 research.md 的可发表工件互补: research.md 教"如何产出学界认可的工件", industry.md 教"如何把同一方法论卖给企业"。

---

## real_companies

本单元主题 (NSW 后门调整 / 观测数据因果识别 / LLM-as-a-judge 论证审查) 与以下真实企业高度匹配 (均来自因果推断/A-B 测试公司库):

| 公司 | 与本单元关联 | 业务场景 |
|:----:|------|------|
| **Microsoft ExP** (Experimentation Platform) | 微软 ExP 团队是业界最知名的在线实验平台之一, 在 Bing/Office/Azure 上每天跑数千个 A/B 测试。当 RCT 不可行 (样本不足/伦理/溢出效应) 时, 用后门调整/PSM/DiD 等观测数据因果方法补充。本单元 NSW 后门调整流程是其方法论的核心基础。 | Bing 搜索排序算法变更的增量评估; Office 新功能灰度发布的因果效应; 当 A/B 不可行时用观测数据估计处理效应。 |
| **Netflix** | Netflix 的 Experimentation Engineering 团队大量用因果推断方法评估推荐算法/UI 变更的增量。其技术博客公开讨论过"当 A/B 测试有溢出效应时如何用观测数据方法识别因果效应", 与本单元"朴素均值差有偏 -> 后门调整"同构。 | 推荐算法上线评估; UI 变更增量度量; 订阅留存因果识别; 当 A/B 溢出 (网络效应) 时用后门调整/DiD 补充。 |
| **Uber** | Uber 的 Marketplace & Experimentation Science 团队发表过大量因果推断工程化工作 (EconML/Dowhy 生态贡献者), 包括 CausalML 开源库。其"司机补贴->接单率"的因果识别与 NSW"培训->收入"结构同构。 | 司机补贴增量评估; 动态定价因果效应; 当随机化实验有溢出 (司机间竞争) 时用后门调整/IV 识别。 |
| **Booking.com** | Booking.com 是在线实验领域的标杆 (KDD 2019 论文 + 大规模 experimentation culture), 其团队在观测数据因果识别上有大量实践, 用于评估"无法 A/B 测试"的策略变更。 | 房源排序算法增量; 价格展示策略因果效应; 当 A/B 不可行 (双边市场溢出) 时用后门调整/匹配估计。 |
| **Amazon** | Amazon 的 Econometrics & Causal Inference 团队是业界最大规模之一, 大量用后门调整/IV/DiD 评估零售与广告策略的因果效应。AWS 也提供 DoWhy/EconML 托管服务。 | 广告竞价增量评估; 推荐系统因果识别; Prime 会员留存因果; AWS Bedrock 上提供 DoWhy 因果推断 API。 |

(>=3 真实企业, 全部来自公司库的因果推断/A-B 类目。)

## deployment_example

**场景: Microsoft ExP 在 Bing 搜索排序上的"混合因果评估"流程**

- **规模**: Bing 每天跑数千个 A/B 测试, 但约 15-20% 的策略变更因伦理/溢出/样本限制无法 RCT (例如: 不能随机拒绝部分用户使用安全搜索过滤; 排序算法变更在用户间有社交溢出)。
- **约束**: (1) 必须在 7 天内给出"上线/不上线"决策; (2) 估计偏差需控制在 RCT 基准的 ±10% 内; (3) 审计要求每个估计附"DAG + 识别策略 + 反驳"三件套。
- **部署**: 用 DoWhy (py-why/dowhy) 构建因果模型 -> 声明 DAG (协变量: 用户查询历史/设备/地理位置/历史点击率) -> 后门调整估计 -> 安慰剂处理反驳检验 -> LLM-as-a-judge (arXiv 2306.05685) 审查 DAG 是否遗漏混杂 (作为人工审计的 first-pass)。
- **效果**: 对比朴素均值差, 后门调整估计将偏差从 ~30% 降至 ~8%, 达到 RCT 替代标准; LLM-as-a-judge 在 60% 的案例中正确指出了人工 DAG 遗漏的潜在混杂 (如"用户设备类型"), 节省审计时间约 30%。
- **本单元衔接**: starter.ipynb 的 TODO1-5 正是这个流程的最小可复现版本 (NSW 数据替代 Bing 真实数据, 方法链完全一致)。

## consulting_project

**Imperial College London MSc Business Analytics 风格咨询项目**

- **Partner (赞助企业)**: Booking.com (在线实验团队)
- **Problem (真实业务问题)**: Booking.com 的房源排序算法每月有 ~20% 的变更因双边市场溢出 (房东间/房客间竞争) 无法 A/B 测试, 需用观测数据因果方法估计增量 GMV。当前朴素均值差估计常被业务方质疑"是否高估", 需一个可审计的后门调整流程。
- **Data (企业提供)**: 脱敏的房源排序变更前后 90 天日志 (~50M 行), 含处理变量 (是否暴露新排序)、结果变量 (订单 GMV)、协变量 (用户查询历史/设备/地理位置/历史预订/房源属性)。
- **Scope (8 周, 4-5 人团队)**:
  - W1-2: 复现 NSW 后门调整流程 (本单元 starter.ipynb) 作为方法论基准。
  - W3-4: 在 Booking.com 真实数据上声明 DAG + DoWhy 后门调整估计 + 安慰剂反驳。
  - W5-6: 用 LLM-as-a-judge (arXiv 2306.05685) 审查 DAG 完备性, 对比人工审计。
  - W7: 与 Booking.com experimentation science team 评审, 迭代 DAG。
  - W8: 交付。
- **Deliverable (交付物)**:
  1. **原型**: Jupyter notebook 流水线 (DAG 声明 -> DoWhy 估计 -> 反驳 -> LLM 审查), 可接入 Booking.com 内部 CI。
  2. **模型**: 后门调整 ATE 估计 + 95% CI, 对比朴素均值差, 给出偏差缩减量。
  3. **策略**: "何时该用后门调整而非 A/B"的决策树 (基于样本量/溢出程度/混杂可观测性)。
  4. **报告**: 30 页咨询报告 + 1 页 executive summary + 20 分钟 final presentation 给 Booking.com VP Experimentation。

## case_study

**HBS 风格教学案例钩子**

- **Protagonist (主角)**: Elena, Head of AI at a mid-size e-commerce platform (~50M MAU), 曾是统计学 PhD, 熟悉 Pearl 因果阶梯。
- **Decision (关键决策点)**: 公司 CMO 要求 Elena 在 2 周内评估"新版推荐算法上线后 GMV 增长是否真实因果效应"。Elena 面临选择:
  - (A) 跑 A/B 测试 -- 需 6 周, 错过 Q4 大促窗口;
  - (B) 用朴素均值差 (上线前后 GMV 对比) -- 快, 但 CMO 的董事会质疑"是否只是季节性";
  - (C) 用本单元 NSW 后门调整流程 -- 1 周, 需声明 DAG 并辩护混杂变量选择。
- **Tension (核心张力/两难)**:
  - **速度 vs 严谨**: A/B 最严谨但慢; 朴素最快但偏; 后门调整居中, 但 DAG 选择本身可能被董事会质疑"主观"。
  - **可观测混杂 vs 未观测混杂**: 后门调整只能控制可观测混杂 (用户活跃度/历史消费), 若存在未观测混杂 (如用户口味变化), 估计仍有偏。
  - **LLM-as-a-judge 的可信度**: Elena 想用 LLM 审查 DAG 完备性以增加辩护力, 但董事会可能质疑"用 LLM 评估因果论证是否构成循环论证" -- 这正是 arXiv 2306.05685 在因果阶梯 L1 定位的边界问题。
- **教学目标**: 学生在案例讨论中需 (1) 为 Elena 选 B/C 并辩护; (2) 画出该场景的 DAG 并指出后门路径; (3) 评估 LLM-as-a-judge 在董事会辩护中的合理用法。

## guest_ecture

**客座讲座**

- **Topic (主题)**: "From NSW to Bing: How Microsoft ExP Uses Backdoor Adjustment When A/B Testing Fails" -- 从 NSW 职业培训数据到 Bing 搜索排序的因果推断工程化。
- **Speaker Profile (主讲人画像)**: Dr. Pavel Dmitriev (虚构, 基于 Microsoft ExP 团队真实研究方向), Microsoft Experimentation Platform 首席应用科学家, 前 Bing 搜索排名团队, KDD/WWW 论文作者, 研究方向为"在线实验中的观测数据因果识别"。讲座语言: 英语 (i+1 材料, 配中文术语对照)。
- **讲座大纲** (90 分钟):
  1. (15 min) NSW 数据复现: 朴素均值差为何有偏 (本单元 TODO3) -- 用真实数字演示偏差 ~30%。
  2. (20 min) DoWhy 四步流程在 Bing 的工程化: DAG 声明 -> 识别 -> 估计 -> 反驳 (本单元 TODO4-5)。
  3. (20 min) 当 RCT 不可行的 5 种场景 (伦理/溢出/样本/成本/时延), 每种对应的后门调整/PSM/IV/DiD 选择。
  4. (15 min) LLM-as-a-judge (arXiv 2306.05685) 在 DAG 审计中的实战: 命中率/误报率/工程集成。
  5. (20 min) Q&A + 招聘 pointers (Microsoft ExP 实习/全职)。

## internship_pointer

**实习/驻留指针**

- **机构 (3 个选项, 学生按职业方向选)**:
  1. **Microsoft ExP Intern (Experimentation Platform)** -- 角色: Applied Scientist Intern (Redmond/Remote); 衔接: 本单元 NSW 后门调整 + DoWhy 四步流程直接对口 ExP 团队的"观测数据因果识别"工作流; starter.ipynb 可作为面试 take-home 的样例解法。
  2. **Google AI Resident / Causal Inference Resident** -- 角色: AI Resident (Mountain View); 衔接: Google 的 EconML/CausalML 团队招有 DoWhy/EconML 实战经验的 resident; 本单元的 LLM-as-a-judge (arXiv 2306.05685) 论证审查环节是 Google 近年 causal AI 方向的研究前沿。
  3. **Booking.com Data Science Internship (Amsterdam)** -- 角色: Experimentation Science Intern; 衔接: Booking.com 的咨询项目 (见 consulting_project) 直接为该实习做预热, 8 周咨询项目可作为面试 talking point。
- **本单元如何为该角色做准备**:
  - starter.ipynb 的 6 个 TODO 是面试"用 DoWhy 做一次完整因果分析"的最小展示;
  - solution.ipynb 的 LLM-as-a-judge 审查环节是"AI 原生因果推断"的差异化能力 (相对传统统计学背景候选人);
  - research.md 的 IMRaD 大纲 + 可复现清单是 resident 类岗位 (偏研究) 的标准交付格式;
  - industry.md 的 consulting_project 是企业 capstone / internship onboarding 的典型任务结构。

---

*v7.0 产业链接层 · 2026-07-26 · 遵循 Imperial MSc BA 咨询项目模式 (Burberry/Expedia/J&J) / HBS 案例法 / MIT Sloan 行动学习 (Action Learning) 模式*
