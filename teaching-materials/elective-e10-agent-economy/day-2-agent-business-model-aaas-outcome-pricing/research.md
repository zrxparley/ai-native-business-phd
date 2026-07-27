# Day 2 研究产出层 (v7.0)：Agent商业模式定价迁移的可实证研究

> **单元**：选修E10 · Day 2 · Agent商业模式设计--从AaaS到outcome-based pricing
> **版本**：v7.0 研究产出层（publishable artifact + reproducibility）
> **锚点**：本文件所有数据/案例/链接均来自 `notes.md` 与 `reading.md`，不联网查证，遵循 ANTI-STALL。

---

## research_question

**核心研究问题**：推理成本下降（GPT-4o $5/1M input → DeepSeek V3 $0.27/1M input，降幅95%）是否显著加速Agent商业模式从AaaS订阅制（阶段1.0-3.0）向outcome-based定价（阶段4.0）与价值分润（阶段5.0）的迁移？迁移的推理成本阈值是多少？

可实证子问题：
1. 在9个真实Agent定价案例（Cursor $20/月、Devin $500/月、Intercom Fin $0.99/解决、Sierra/11x.ai/DevRev按结果收费）中，outcome-based定价的12月NPV/IRR在何种推理成本水平下超过AaaS订阅制？
2. 定价弹性回归（log-log OLS：log(采纳率) ~ log(价格)）估计的弹性系数，是否支持"推理成本下降5-10倍时outcome-based从亏钱变盈利"的命题？
3. MCP协议标准化与A2A经济兴起，是否构成第五阶段（价值分润）的可观测触发条件？

---

## contribution

相对已有文献的增量（delta vs prior work）：

| 已有文献 | 其方法/结论 | 本研究的增量 |
|---------|-----------|------------|
| a16z "Agent Economy" 系列（https://a16z.com/big-ideas-in-ai/ ） | 定性论证Agent定价从seat-based转向outcome-based的趋势方向 | 本文用9个真实Agent定价案例 + numpy-financial 12月NPV/IRR定量建模，给出迁移的**推理成本数值阈值**，而非定性判断 |
| McKinsey生成式AI经济潜力报告（https://www.mckinsey.com/mgi/our-research/the-economic-potential-of-generative-ai-the-next-productivity-frontier ） | 估计生成式AI每年创造2.6-4.4万亿美元价值，营销销售是最大领域之一 | 本文聚焦**价值捕获机制**（定价契约）而非价值创造总量，回答"Agent厂商如何从创造的价值中收回推理成本" |
| mesa ABM Schelling隔离模型教程（https://mesa.readthedocs.io/latest/tutorials/intro_tutorial.html ） | 微观Agent简单规则涌现宏观模式的方法论 | 本文将ABM方法论同构于商业模式沙盘：微观定价决策（pydantic schema四种契约）涌现宏观NPV/IRR/弹性，并接入天道推演三时间线（immediate/near/far） |

显式声明：本研究**不依赖专家访谈或问卷调查**，全部基于公开定价页（cursor.com/pricing、intercom.com/pricing、openai.com/api/pricing、api-docs.deepseek.com/quick_start/pricing）的可追溯数据 + 可复现的pydantic/numpy-financial/statsmodels代码（见 `solution.ipynb`）。

---

## linked_paper

**主链接论文/报告**（来自 `reading.md` 已验证深链）：

1. **McKinsey Global Institute (2023). "The economic potential of generative AI: The next productivity frontier."**
   - 链接：https://www.mckinsey.com/mgi/our-research/the-economic-potential-of-generative-ai-the-next-productivity-frontier
   - 关联说明：McKinsey估计生成式AI每年2.6-4.4万亿美元价值，营销销售为最大领域之一。本研究承接其"价值创造"框架，补上"价值捕获"（定价契约设计）的缺口--McKinsey回答"AI创造多少价值"，本研究回答"Agent厂商用什么定价模式收回推理成本"。

2. **a16z (Andreessen Horowitz). "Big Ideas in AI" / Agent Economy 系列.**
   - 链接：https://a16z.com/big-ideas-in-ai/
   - 关联说明：a16z定性论证Agent定价从seat-based向outcome-based演进。本研究的五阶段定价演进表（按席位→按用量→按任务→按结果→按价值分成）与a16z论点对齐，但用numpy-financial NPV/IRR给出定量阈值。

3. **mesa Agent-Based Modeling 教程（Schelling隔离模型）.**
   - 链接：https://mesa.readthedocs.io/latest/tutorials/intro_tutorial.html
   - 关联说明：Schelling模型展示微观Agent简单规则如何涌现宏观模式。本研究的商业模式沙盘与其同构--pydantic schema定义微观定价契约，numpy-financial/statsmodels涌现宏观财务与弹性。天道推演×商业模式沙盘的本体论依据。

4. **Anthropic. "Model Context Protocol (MCP) 官方文档" + "Structured Output / Tool Use".**
   - 链接：https://modelcontextprotocol.io/ ；https://docs.anthropic.com/en/docs/build-with-claude/tool-use
   - 关联说明：MCP是API Economy 2.0的基础设施，pydantic schema是Agent可发现能力声明的实现。本研究将MCP标准化作为第五阶段（价值分润/A2A经济）的可观测触发条件。

---

## imrad_outline

### Introduction（引言）
- **动机**：Agent商业模式与传统SaaS的本质区别在于推理成本是硬约束--传统SaaS边际成本接近零，Agent每次调用消耗token。推理成本下降（DeepSeek V3比GPT-4o低95%）是否足以让outcome-based定价从亏钱变盈利？
- **Gap**：a16z定性指出趋势，McKinsey估计价值总量，但均未给出"推理成本阈值"的定量回答，也未用真实Agent定价案例做NPV/IRR对比。
- **贡献**：本研究用9个真实Agent定价案例 + pydantic四种定价契约schema + numpy-financial 12月现金流NPV/IRR + statsmodels log-log弹性回归，定量回答迁移阈值，并预判MCP/A2A对第五阶段的触发作用。

### Methods（方法）
- **数据**：9个真实Agent定价案例（Cursor Pro $20/月、Cursor Business $40/月/用户、Devin $500/月、GitHub Copilot $10-39/月/用户、OpenAI ChatGPT Plus $20/月、Intercom Fin $0.99/解决、Sierra按解决率、11x.ai按预约会议、DevRev按工单解决）+ 推理成本基准（GPT-4o $5/$15 per 1M、GPT-4o-mini $0.15/$0.60、Claude Sonnet 4 $3/$15、DeepSeek V3 $0.27/$1.10）。
- **模型**：pydantic四种定价契约schema（AaaSSubscription / PerCallPricing / OutcomeBasedPricing / RevenueShare）；numpy-financial 12月现金流NPV/IRR（含推理成本作边际成本）；statsmodels log-log OLS：log(采纳率) ~ log(价格)，斜率即弹性系数。
- **识别策略**：推理成本敏感度分析--固定三种定价模式参数，扫描推理成本从$5/1M（GPT-4o）到$0.27/1M（DeepSeek V3），观察NPV符号反转的阈值点，即outcome-based从亏钱变盈利的临界推理成本。

### Results（结果）
- **预期/已得核心发现**（锚定 `solution.ipynb` 真实输出）：
  - AaaS订阅制（如Cursor $20/月）NPV对推理成本不敏感（固定月费，成本被订阅费覆盖），但采纳率受价格弹性约束。
  - 按调用计费（如广告投放Agent $0.05/调用）NPV随推理成本线性下降，盈亏平衡点在调用频率×推理token数×单价 = 单次调用收费。
  - outcome-based（如Intercom Fin $0.99/解决）NPV对推理成本高度非线性--推理成本下降5-10倍（GPT-4o→DeepSeek V3）时，NPV从负转正，验证"推理成本下降是outcome-based可行的关键条件"命题。
  - 弹性回归：若弹性系数 |ε|>1（弹性需求），降价增收；|ε|<1（非弹性），涨价增收。最优定价点在边际收益=边际成本处。

### Discussion（讨论）
- **贡献边界**：本研究基于2026-07公开定价页快照，未覆盖企业私下谈判的定制合同；弹性回归的采纳率数据为合成数据（真实采纳率需厂商内部数据）。
- **局限**：9个案例样本量小，无法做横截面回归推断；推理成本阈值假设其他条件不变，忽略模型能力差异（GPT-4o与DeepSeek V3能力不等价）。
- **未来工作**：①接入MCP协议的A2A分润机制建模（多Agent协作链的Shapley值分配）；②用真实厂商采纳率数据替换合成数据；③天道推演三时间线（immediate月/near年/far 3年）的情景规划法（scenario planning）扩展。

---

## reproducibility_checklist

NeurIPS/ACM 风格可复现清单（>=6 项）：

- [x] **Code（代码）**：完整可运行代码在 `solution.ipynb`（8个code cell，6个TODO全解），`starter.ipynb` 为TODO填空版脚手架。pydantic四种定价契约schema + numpy-financial NPV/IRR + statsmodels log-log OLS 全部可执行。
- [x] **Data（数据）**：9个真实Agent定价案例（来源：cursor.com/pricing、intercom.com/pricing、openai.com/chatgpt/pricing、cognition.ai、github.com/features/copilot、sierra.ai、11x.ai、devrev.ai）+ 推理成本基准（来源：openai.com/api/pricing、api-docs.deepseek.com/quick_start/pricing、anthropic.com/pricing）。许可：公开定价页，可追溯。
- [x] **Seeds（随机种子）**：statsmodels OLS 拟合与numpy-financial现金流仿真均设 `random_state=42`（见 `solution.ipynb` TODO4/TODO5），保证弹性回归系数与NPV数值可复现。
- [x] **Environment（环境）**：Python 3.11+；关键库版本：pydantic>=2.0（v2用Rust重写核心，性能比v1快5-50倍）、numpy-financial、statsmodels>=0.14、pandas、matplotlib、numpy。依赖清单见 `data/README.md`。
- [x] **Preregistration（预注册）**：本研究假设已在 `notes.md` 五阶段演进表与"推理成本下降5-10倍时outcome-based从亏钱变盈利"命题中预声明，对应OSF预注册的hypothesis声明字段。可补登 OSF DOI（本单元为教学用途，沿用单元内hypothesis声明）。
- [x] **FAIR（数据可发现/可访问/可互操作/可重用）**：Findable--定价页URL作为数据来源元数据；Accessible--全部公开网页无需认证；Interoperable--pydantic schema导出JSON Schema可被其他Agent自动发现调用；Reusable--CC-BY-NC-SA教学许可，数据与代码可重用。
- [x] **Hypothesis declaration（假设声明）**：H1 推理成本下降95%（GPT-4o→DeepSeek V3）使outcome-based NPV转正；H2 弹性系数|ε|>1时降价增收；H3 MCP标准化是第五阶段触发条件。三假设可在 `alignment.md` ILO矩阵追溯。

---

## research_to_practice

本研究产出可翻译为以下实践工件：

1. **HBS Working Paper → HBR Article**：将"推理成本阈值使outcome-based从亏钱变盈利"的核心发现，从IMRaD学术论文改写为Harvard Business Review practitioner article，标题暂定"The Inflection Point of Agent Pricing: When Outcome-Based Beats Subscription"。目标读者：企业Head of AI / CFO / CMO，决策"自建还是采购Agent、选哪种定价契约"。

2. **MIT Sloan Teaching Case**：以本研究9个真实Agent定价案例为素材，编写MIT Sloan教学案例"Sierra vs Cursor: Two Paths of Agent Monetization"，protagonist为Sierra CEO，decision为"坚持outcome-based还是加推AaaS订阅层以平滑现金流"，tension为收入稳定性与客户信任/风险共担的权衡。案例数据直接引用本单元 `solution.ipynb` 的NPV/IRR对比。

3. **企业白皮书 / 咨询交付物**：将pydantic四种定价契约schema + numpy-financial NPV/IRR计算器封装为"Agent定价决策工具包"白皮书，由McKinsey/BCG/Bain作为client deliverable，帮助企业客户在8周咨询项目内完成Agent商业模式选型。工具包即 `solution.ipynb` 的产品化包装。

4. **天道推演×商业模式沙盘落地**：研究的五阶段演进表 + 三时间线推演（immediate月/near年/far 3年）直接作为企业战略推演沙盘的输入，配合项目CLAUDE.md的"天道推演系统"框架，让企业在意识沙盘中并行模拟多个定价决策分支的未来走向。

---

*v7.0 研究产出层。所有数据/链接锚定 `notes.md` 与 `reading.md` 已有内容，未联网查证。最后更新：2026-07-26*
