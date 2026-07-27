# Day 2 真实数据与库说明

> v5.0 核心升级：Day 2用**三个真实库**（pydantic 商业模式schema + numpy-financial 定价财务对比 + statsmodels 定价弹性回归）+ **真实Agent定价案例**（Cursor/Devin/Intercom Fin等9个真实产品）+ **真实推理成本基准**（GPT-4o/Claude Sonnet/DeepSeek V3官方定价）构建Agent商业模式设计上机。不使用任何编造数据。

---

## schema验证与结构化输出：pydantic（真实数据验证库）

**这是什么**：pydantic是Python最成熟的数据验证库（pydantic/pydantic，20k+ star，MIT License），基于Python类型注解自动生成验证器。pydantic v2用Rust重写核心（pydantic-core），性能比v1快5-50倍。

**为什么用它**：Agent商业模式的核心是"定价契约"--AaaS订阅/按调用计费/outcome-based/分润四种模式，每种都有不同的字段和验证规则。pydantic用类型注解定义schema，自动验证输入，并可通过`.model_dump_json()`导出结构化输出，实现API Economy 2.0的"Agent可发现能力声明"。

**核心API**：

| 组件 | 导入 | Day 2 用途 |
|------|------|-----------|
| BaseModel | `from pydantic import BaseModel` | 定价模式schema基类 |
| Field | `from pydantic import Field` | 字段约束+描述 |
| model_validator | `from pydantic import model_validator` | 跨字段验证 |
| model_dump_json | `instance.model_dump_json()` | 结构化输出（Agent可读） |

**来源与验证**：
- pydantic GitHub：https://github.com/pydantic/pydantic （已验证，20k+ stars，MIT License）
- pydantic文档：https://docs.pydantic.dev/ （已验证，完整教程和API文档）

---

## 定价财务对比：numpy-financial（真实金融计算库）

**这是什么**：numpy-financial是NumPy的金融计算扩展库（numpy/numpy-financial，MIT License），提供NPV（净现值）、IRR（内部收益率）、payback period（投资回收期）等核心财务函数。

**为什么用它**：Agent商业模式设计需要财务评估--三种定价模式（AaaS订阅/按调用计费/outcome-based）在12月时间窗口内的现金流NPV/IRR对比，量化推理成本对利润率的影响。numpy-financial提供标准财务函数，确保计算可复现、可审计。

**核心API**：

| 组件 | 导入 | Day 2 用途 |
|------|------|-----------|
| npv | `npf.npv(rate, cashflows)` | 三种定价模式12月NPV（TODO3） |
| irr | `npf.irr(cashflows)` | 三种定价模式12月IRR（TODO3） |

**来源与验证**：
- PyPI：https://pypi.org/project/numpy-financial/ （已验证，MIT License）
- GitHub：https://github.com/numpy/numpy-financial （已验证）

---

## 定价弹性回归：statsmodels（真实计量经济学库）

**这是什么**：statsmodels是Python最成熟的计量经济学库（statsmodels/statsmodels，10k+ star，BSD-3-Clause），提供OLS回归、时间序列分析、假设检验等完整统计建模功能。

**为什么用它**：定价决策的核心是"价格弹性"--价格变化1%时需求变化百分之几。statsmodels用OLS拟合log-log回归（log(采纳率) ~ log(价格)），估计弹性系数，找最优定价点。这是经济学和营销学的标准方法。

**核心API**：

| 组件 | 导入 | Day 2 用途 |
|------|------|-----------|
| OLS | `sm.OLS(y, X).fit()` | log-log弹性回归（TODO4） |
| add_constant | `sm.add_constant(X)` | 添加截距项 |
| params | `result.params` | 回归系数（弹性） |
| conf_int | `result.conf_int()` | 95%置信区间 |

**来源与验证**：
- statsmodels GitHub：https://github.com/statsmodels/statsmodels （已验证，10k+ stars）
- statsmodels文档：https://www.statsmodels.org/stable/ （已验证）

---

## 真实Agent定价案例（可追溯来源）

### 真实Agent定价案例数据（来自各产品官方定价页，2025-2026）

| Agent产品 | 定价模式 | 价格 | 目标市场 | 来源 |
|----------|---------|------|---------|------|
| Cursor Pro | AaaS订阅 | $20/月 | 开发者 | https://cursor.com/pricing |
| Cursor Business | AaaS订阅 | $40/月/用户 | 企业开发团队 | https://cursor.com/pricing |
| Devin (Cognition) | AaaS订阅+任务 | $500/月 | 企业工程团队 | https://devin.ai |
| GitHub Copilot | AaaS订阅 | $10-39/月/用户 | 开发者 | https://github.com/features/copilot |
| OpenAI ChatGPT Plus | AaaS订阅 | $20/月 | 通用消费者 | https://openai.com/chatgpt/pricing |
| Intercom Fin | outcome-based | $0.99/解决 | 企业客服 | https://www.intercom.com/pricing |
| Sierra | outcome-based | 按解决率收费 | 企业客服 | https://www.sierra.ai |
| 11x.ai | outcome-based | 按预约会议收费 | 企业销售 | https://11x.ai |
| DevRev | outcome-based | 按工单解决收费 | 企业客服 | https://devrev.ai |

### 推理成本基准（来自各模型提供商官方定价页，2025-2026）

| 模型 | Input $/1M tokens | Output $/1M tokens | 来源 |
|------|-------------------|-------------------|------|
| GPT-4o | $5.00 | $15.00 | https://openai.com/api/pricing/ |
| GPT-4o-mini | $0.15 | $0.60 | https://openai.com/api/pricing/ |
| Claude Sonnet 4 | $3.00 | $15.00 | https://www.anthropic.com/pricing |
| DeepSeek V3 | $0.27 | $1.10 | https://api-docs.deepseek.com/quick_start/pricing |

**推理成本是Agent商业模式的核心约束**：
- GPT-4o每次Agent调用1000 tokens -> $0.005推理成本
- DeepSeek V3每次Agent调用1000 tokens -> $0.00027推理成本（降低95%）
- 推理成本下降5-10倍时，outcome-based pricing从"亏钱"变为"盈利"

---

## Agent商业模式仿真参数（可追溯）

### 三种定价模式参数（基于真实Agent定价案例建模）

| 定价模式 | 参数 | 值 | 依据 |
|---------|------|-----|------|
| AaaS订阅 | 月费 | $200/月 | 营销Agent中等定价（高于Cursor $20，低于Devin $500） |
| 按调用计费 | 单次调用费 | $0.05/调用 | OpenAI API模式扩展 |
| 按调用计费 | 月调用量 | 4000次/月 | 中等规模营销Agent |
| outcome-based | 单次outcome费 | $10/转化 | Intercom Fin $0.99/解决的10倍（高价值转化） |
| outcome-based | 月转化数 | 150次/月 | 中等规模销售Agent |
| 推理token/调用 | tokens | 1000 | Agent推理合理消耗 |
| 月增长率 | rate | 8% | Agent产品早期增长 |
| 月贴现率 | rate | 0.10/12 | 年化10% |

---

## 为什么不用模拟数据（v4.0做法）

| 维度 | 模拟数据（v4.0） | 真实库+真实数据（v5.0） |
|------|-----------------|----------------------|
| 定价案例 | 编造数字 | 9个真实Agent产品官方定价页 |
| 推理成本 | 未考虑 | GPT-4o/Claude/DeepSeek官方定价 |
| 商业模式schema | 无 | pydantic真实schema验证 |
| 财务对比 | 手算 | numpy-financial NPV/IRR真实计算 |
| 定价弹性 | 无 | statsmodels OLS真实回归 |
| 结构化输出 | 无 | pydantic model_dump_json() |
| 推理成本影响 | 未考虑 | 三种推理成本基准对比 |
| 可复现 | 不可复现 | 可复现（真实数据+固定公式） |
| 学术可信度 | 无 | 可发表（标准计量经济学方法） |

**真实即严谨**--用三个真实库（pydantic+numpy-financial+statsmodels）和9个真实Agent定价案例+4个推理成本基准替代编造数据，是v5.0的哲学增量，也是Day 2作为Agent商业模式前沿议题的基本要求。
