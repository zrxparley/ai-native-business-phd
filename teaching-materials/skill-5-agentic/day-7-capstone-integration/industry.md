# industry.md — Day 7 Capstone整合 (v7.0 产业链接层)

> 本单元主题: 端到端Capstone整合 — causaldata NSW + DoWhy + LangGraph + deepeval + DSR + 天道推演×多Agent仿真. 本文件把Capstone产出锚定到真实产业场景, 遵循Imperial MSc BA咨询项目/HBS案例法/MIT Sloan行动学习模式.

---

## real_companies

>=3 家真实企业锚点 (从公司库挑选, 与本单元因果推断+Agent+评估主题匹配):

| 公司 | 与本单元关联 | 业务场景 |
|------|-------------|---------|
| **Microsoft Research** | DoWhy因果推断库的维护方 (reading.md已记录 github.com/py-why/dowhy); Microsoft ExP团队是A/B测试产业标杆 | 企业内部营销/产品决策的因果评估流水线, 用DoWhy估计干预效果, Agent调用因果证据生成策略 |
| **Booking.com** | 因果推断/A/B测试领域的产业标杆 (公司库"因果推断/A-B"类目); 每年数千次在线实验 | 在线旅游平台的营销干预因果评估, 把NSW RCT方法论迁移到酒店/机票推荐场景的Agent决策 |
| **LangChain** | LangGraph是本单元Agent层的核心库 (reading.md已记录 langchain-ai/langgraph); LangChain团队主导Agent编排生态 | 企业级Agent编排平台, 营销策略Agent作为LangGraph StateGraph的生产部署案例 |
| **Cognition (Devin)** | 公司库"Agents"类目, AI Agent产品化代表 | 软件工程Agent的因果评估范式迁移 — 把DoWhy+deepeval流水线用于评估Devin式代码Agent的工具调用质量 |
| **Sierra** | 公司库"Agents"类目, 企业级对话式AI Agent | 客服/营销Agent的因果评估, 用本单元流水线评估Agent策略对企业KPI的因果效果 |

## deployment_example

**真实合理部署场景: Microsoft Research (DoWhy团队) 内部营销决策Agent**

- **规模**: Microsoft ExP团队每年运行数千次A/B实验 (公开数据), 营销干预的因果评估是其核心基础设施. 部署一个基于本单元流水线的"因果营销策略Agent"可服务数百名内部营销决策者.
- **约束**: (1) 数据合规 — 客户行为数据不可外泄, Agent必须在Azure内部VNet运行; (2) 模型版本漂移 — GPT-4o/GPT-5版本切换影响可复现性, 需用langsmith trace存档每次调用链; (3) 评估偏差 — LLM-as-a-judge的已知偏差 (Zheng 2023 §5) 需人工抽样校验.
- **效果 (合理预估)**: 用NSW RCT基准 (ATE ≈ $1,794) 校准因果估计器后, Agent工具调用正确率 >=80%, GEval策略质量得分 >=3.5/5, 完整流水线单次运行 <120s; 相对纯LLM策略生成, 因果证据增强的Agent在"策略可解释性"维度提升约30% (deepeval BaseMetric测量).
- **生产架构**: causaldata NSW (校准基准) → DoWhy (因果估计) → LangGraph StateGraph (Agent编排) → deepeval CI测试 (评估) → langsmith trace存档 → Azure OpenAI (LLM后端). 全链路在Azure AI Foundry部署.

## consulting_project

**Imperial College London MSc Business Analytics 风格咨询项目 (8周, 4-5人团队)**

- **Partner (赞助企业)**: Booking.com (A/B测试产业标杆, 公司库"因果推断/A-B"类目)
- **Problem (真实业务问题)**: Booking.com 的在线实验平台每年产生数千个A/B测试结果, 但营销决策者难以从统计显著的实验中提取**因果可解释的策略建议**. 现有报告只说"干预提升了转化率X%", 无法回答"为什么这个干预有效? 下次该投放哪类用户?".
- **Data (企业提供数据)**: 脱敏的酒店推荐A/B测试数据 (类似NSW结构: treatment/outcome/covariates), 含用户画像/预订漏斗/实验分组标识, 约100万行.
- **Scope (8周4-5人)**:
  - Week 1-2: 用DSR六步 (Peffers 2007) 定义问题与artifact目标
  - Week 3-4: 用DoWhy估计ATE, 后门调整+反驳检验, 把NSW基准迁移到Booking.com数据
  - Week 5-6: 用LangGraph构建"因果营销策略Agent", Agent读取ATE证据生成可解释策略
  - Week 7: 用deepeval GEval + 自定义BaseMetric评估Agent输出, 对标Zheng (2023) LLM-as-a-judge
  - Week 8: IMRaD论文草稿 + 向Booking.com决策层汇报
- **Deliverable**: (1) 原型: 因果营销策略Agent (LangGraph+DoWhy); (2) 模型: ATE估计+反驳检验pipeline; (3) 策略: 可解释营销建议清单; (4) 报告: IMRaD论文草稿 (3000-5000字, 含DSR artifact描述).

## case_study

**HBS风格教学案例钩子**

- **Protagonist (主角)**: Maria Chen, Booking.com 全球营销决策科学负责人 (Head of Marketing Decision Science), 博士背景为因果推断, 管理一个15人数据科学团队.
- **Decision (关键决策点)**: Maria面临一个预算分配决策 — 明年是否把传统A/B测试团队 (8人, 年预算$2M) 的30%资源转向部署"因果营销策略Agent" (基于本单元的DoWhy+LangGraph+deepeval流水线)? 该Agent声称能把策略生成周期从2周缩短到2天, 并提供因果可解释性.
- **Tension (核心张力/两难)**:
  - **效率 vs 严谨**: Agent快速生成策略, 但LLM-as-a-judge存在已知偏差 (Zheng 2023 §5), 可能产生"看起来合理但因果错误"的建议; 传统A/B测试慢但可信.
  - **可复现 vs 漂移**: langsmith trace存档保证可复现, 但GPT-4o→GPT-5版本切换破坏可比性, Maria无法证明"去年的Agent决策今年仍有效".
  - **人 vs Agent**: 团队8人中5人是因果推断博士, 担心被Agent替代; Maria需要在效率提升与团队士气间平衡.
  - **天道推演锚点**: Maria用"沙盘模拟3层推演"评估决策 — 立即(immediate: 效率提升30%) / 近期(near: 团队重组阵痛) / 远期(far: Agent成为标准决策基础设施, 团队转型为Agent监督者).

## guest_ecture

**客座讲座设计**

- **Topic (主题)**: "From NSW RCT to Production: Building a Reproducible Causal Agent Pipeline at Microsoft Research"
- **Speaker Profile (主讲人画像)**: Dr. Amit Sharma, Microsoft Research Senior Researcher, DoWhy库共同维护者 (py-why/dowhy), 因果推断与机器学习交叉领域专家, NeurIPS/ICML审稿人. 主讲人曾公开讨论DoWhy的设计哲学与产业落地.
- **讲座大纲 (60分钟)**:
  1. (10min) DoWhy的设计原则: 显式因果图 + 识别+估计+反驳三步法, 对标本单元TODO3
  2. (15min) 因果推断在Microsoft ExP A/B测试平台的生产部署案例
  3. (15min) 把DoWhy作为Agent工具: LangGraph编排 + deepeval评估的端到端流水线, 对标本单元TODO4-5
  4. (10min) 可复现研究挑战: API版本漂移 + langsmith trace存档 + FAIR数据原则
  5. (10min) Q&A: 学生可问"天道推演×多Agent仿真"作为理论视角的可行性
- **衔接本单元**: 讲座前要求学生完成starter.ipynb的TODO1-3 (DSR+数据+因果), 讲座后完成TODO4-6 (Agent+评估+论文), 形成理论与产业的闭环.

## internship_pointer

**实习/驻留指针**

- **机构 (3个候选, 按匹配度排序)**:
  1. **Microsoft Research (DoWhy团队) Research Internship** — 因果推断方向, 12周, Redmond/Remote. 直连本单元DoWhy+deepeval流水线, 实习产出可成为本Capstone的产业验证版本.
  2. **Google AI Resident (Causal Inference track)** — 18个月轮岗, Mountain View. Google有成熟的因果推断研究组 (Pearl学派传承), 适合把天道推演×多Agent仿真发展为计算化沙盘.
  3. **OpenAI Residency** — 12个月, San Francisco. 侧重LLM+Agent前沿, 适合把本单元的deepeval LLM-as-a-judge升级为OpenAI自带的对齐评估栈.
- **角色**: Research Resident / Applied Scientist Intern, 工作内容为"因果Agent的可复现评估", 直接延续Capstone的DSR artifact贡献.
- **衔接 (本单元如何为该角色做准备)**:
  - DSR六步 (Hevner 2004 / Peffers 2007): 实习面试可展示"如何用DSR框架规划一个研究项目", 这是MSR/Google研究组的标准思维.
  - DoWhy实操 (TODO3): 直接匹配Microsoft Research DoWhy团队的技能要求.
  - LangGraph+deepeval (TODO4-5): 匹配Agent评估方向, OpenAI/Google的Residency越来越关注Agent系统的可复现评估.
  - IMRaD论文草稿 (TODO6): 实习申请writing sample可直接用本Capstone草稿.
  - 天道推演×多Agent仿真: 作为差异化面试亮点 — 中文IS学术背景 + 因果建模底层 + Agent系统设计, 是OpenAI/Google多元化学术招聘的稀缺组合.

---

*本文件由v7.0升级生成. real_companies全部从公司库挑选且真实存在; 部署场景基于reading.md已记录的Microsoft Research DoWhy维护事实; 咨询项目遵循Imperial MSc BA模式 (partner/data/scope/deliverable); 案例遵循HBS案例法 (protagonist/decision/tension).*
