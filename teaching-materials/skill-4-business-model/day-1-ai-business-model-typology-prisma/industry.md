# 产业链接 (v7.0) - AI商业模式类型学 + PRISMA文献综述

> 本单元产出产业链接: >=3 真实企业锚点 + 部署场景 + Imperial MSc BA 风格咨询项目 + HBS 风格教学案例 + 客座讲座 + 实习指针

## real_companies (>=3 家真实企业锚点)

| 公司 | 与本单元的关联 | 业务场景 |
|---|---|---|
| OpenAI | AI基础设施类型标杆 (GPT API 按 token 计费) | 为下游营销AI提供底层模型能力, 是五类型中"基础设施"的典型 |
| Hugging Face | AI平台类型标杆 (模型市场 + 双边网络效应) | 营销模型/Agent的分发与交易市场, 平台抽佣+增值服务+托管费 |
| Perplexity / Cursor | AI原生产品类型标杆 (从头基于AI) | AI原生营销工具/搜索, 混合订阅+用量+增值定价 |
| Sierra / Cognition(Devin) | Agent经济类型标杆 (outcome-based + AgentaaS) | AI营销Agent自主执行全流程, outcome-based 分成 |
| Salesforce Einstein | AI增强产品类型标杆 (传统SaaS+AI增值) | 传统营销SaaS加AI增值特性, 维持原定价 |

(5 家真实企业, 覆盖五类型全谱; 见 notes.md 关键回顾 1 表格的"典型企业"列)

## deployment_example

**Hugging Face 平台部署 AI 模型市场 (AI平台型商业模式的真实生产部署)**:
- 规模: 托管 >100 万个模型, 月活开发者 >50 万, 双边市场 (模型开发者 + 模型使用者)
- 约束: 模型推理成本 (GPU 小时) + 安全审核 (恶意模型防护) + 版本治理 (模型卡 Model Card 强制)
- 效果: 平台抽佣 + Inference Endpoints 托管费 + Enterprise Hub 订阅, 估值 >40 亿美元 (2026)
- 与本单元关联: Hugging Face 是 PRISMA 综述中"AI平台"类型的典型实例, 其商业模式 (网络效应 + 抽佣 + 增值) 可用五类型框架解释

## consulting_project (Imperial MSc BA 风格)

- **partner**: Burberry (奢侈品零售, Imperial MSc BA 真实合作企业之一)
- **problem**: Burberry 营销部门需决定: 自建 AI 内容生成能力 (AI原生产品型) vs 采购 Salesforce Einstein (AI增强产品型) vs 部署 Sierra 类营销 Agent (Agent经济型) -- 哪种 AI 商业模式最适合奢侈品营销的高调性 + 合规要求?
- **data**: Burberry 提供 12 个月营销内容绩效数据 (脱敏) + 品牌调性指南 + 合规约束清单
- **scope**: 8 周, 4-5 人团队 (1 数据科学家 + 1 策略 + 1 设计 + 1 合规 + 1 PM)
- **deliverable**: (1) 五类型适配度评分卡 (2) PRISMA 综述验证同类企业选择 (3) 推荐方案 + 3 年 TCO 对比 + 风险矩阵 (4) 试点 PoC 原型

## case_study (HBS 风格教学案例钩子)

- **protagonist**: Sarah Chen, 某中型零售集团 CMO (年营销预算 $50M)
- **decision**: 2026 年营销 AI 化转型, 需在 3 个月内决定采用哪种 AI 商业模式: (A) 加购 Salesforce Einstein 增强现有 SaaS (低风险, 月费可预测) (B) 自建基于 GPT API 的原生内容生成 (高控制力, 用量计费波动) (C) 部署 Sierra 类 outcome-based 营销 Agent (对齐激励, 但 Agent 可靠性未验证)
- **tension**: Agent经济型的 outcome-based pricing 与 CFO 要求的预算可预测性冲突; 且若 Agent 可靠性突破, SaaS 订阅模式可能被颠覆 (天道推演沙盘分支1) -- 选 A 安全但可能被颠覆, 选 C 抢先但风险高

## guest_lecture

- **topic**: "AI 商业模式的演化 -- 从 API 计费到 Agent 经济"
- **speaker_profile**: a16z AI 投资合伙人 或 Hugging Face Head of Enterprise (两者都在 reading.md 已验证链接中, 均为 AI 商业模式领域的产业实践者)

## internship_pointer

- **机构**: a16z AI 研究实习生 / OpenAI Residency / Hugging Face 企业方案实习 (三选一, 均为 AI 商业模式前沿机构)
- **角色**: AI 商业模式研究实习生 -- 用 PRISMA + 天道推演分析 portfolio 公司的商业模式类型演化
- **衔接**: 本单元的 PRISMA 综述 + 五类型分类器 + 天道推演沙盘正是该角色的核心方法论准备; practice.md 的 progressive_project (proposal->milestone->final->poster) 即实习面试作品集
