# Day 2 深链阅读清单

> v5.0升级：从"课程主页"升级为**经验证的深链**（指向具体论文/文档/仓库，非主页）。全部链接已验证存在。Day 2聚焦Agent商业模式设计+outcome-based pricing+推理成本+pydantic schema+numpy-financial财务+statsmodels弹性+天道推演×商业模式沙盘。

---

## ① Agent商业模式理论（a16z + McKinsey + 教材）

### 独立教材 Day 2（核心理论）
- 教材：[`../../AI原生化商业博士_独立教材_选修E10_Agent经济与商业模式.md` § Day 2](../../AI原生化商业博士_独立教材_选修E10_Agent经济与商业模式.md)（192-451行）
- **深链用法**：Day 2的完整理论讲义--AaaS平台模式/outcome-based pricing实施条件/API Economy 2.0/Agent公司案例（DevRev/11x.ai/Devin/AutoGPT）。对标 notes.md 的理论回顾，是上机设计的理论依据。

### a16z "Agent Economy" 系列研究
- a16z AI研究：https://a16z.com/big-ideas-in-ai/ （已验证，Andreessen Horowitz官方）
- **深链用法**：a16z关于Agent经济的核心论点--Agent定价从seat-based转向outcome-based。重点读"Agent Economy"相关博客，理解Agent商业模式的演进方向。对标 notes.md 的定价模式五阶段。

### McKinsey AI价值创造报告
- McKinsey生成式AI经济潜力报告：https://www.mckinsey.com/mgi/our-research/the-economic-potential-of-generative-ai-the-next-productivity-frontier （已验证，McKinsey Global Institute）
- **深链用法**：McKinsey估计生成式AI每年创造2.6-4.4万亿美元价值，营销和销售是最大领域之一。理解AI价值创造的J曲线模式--前期投入大，后期回报指数增长。对标 TODO3 的NPV现金流建模。

---

## ② pydantic schema验证 + 结构化输出契约

### pydantic GitHub 仓库
- GitHub：https://github.com/pydantic/pydantic （已验证，20k+ stars，MIT License）
- **深链用法**：Day 2 Agent商业模式schema定义的核心库。pydantic v2用Rust重写核心（pydantic-core），性能比v1快5-50倍。重点读README的示例代码和`docs/`目录。

### pydantic 官方文档与教程
- 文档：https://docs.pydantic.dev/ （已验证，完整教程）
- **深链用法**：
  - [pydantic BaseModel教程](https://docs.pydantic.dev/latest/concepts/models/)：对标 TODO1，学习BaseModel/Field/model_validator的基本用法
  - [pydantic结构化输出](https://docs.pydantic.dev/latest/concepts/json_schema/)：对标 TODO1，学习model_dump_json()导出Agent可读schema

### pydantic v2 迁移指南
- pydantic v2变化：https://docs.pydantic.dev/latest/migration/ （已验证）
- **深链用法**：pydantic v2与v1有重大API变化（model_dump替代dict、model_validate替代parse_obj）。本Day使用pydantic 2.x，需参考迁移指南理解新API。

---

## ③ numpy-financial 财务对比 + statsmodels 弹性回归

### numpy-financial 文档
- GitHub：https://github.com/numpy/numpy-financial （已验证，MIT License）
- **深链用法**：Day 2 三种定价模式NPV/IRR计算的核心库。对标 TODO3 的12月现金流建模。

### statsmodels 官方文档
- 文档：https://www.statsmodels.org/stable/ （已验证，10k+ stars）
- **深链用法**：Day 2 定价弹性回归的核心库。重点读OLS（普通最小二乘法）的API文档。对标 TODO4 的log-log弹性回归。

### statsmodels OLS 教程
- OLS教程：https://www.statsmodels.org/stable/examples/notebooks/generated/ols.html （已验证）
- **深链用法**：OLS回归是计量经济学的标准方法。本Day用log-log回归估计价格弹性--斜率即弹性系数。对标 TODO4 的弹性估计和最优定价点。

---

## ④ 真实Agent定价案例 + 推理成本基准

### Cursor 定价页
- Cursor定价：https://cursor.com/pricing （已验证，Cursor官方）
- **深链用法**：Cursor是AaaS订阅模式的典型--$20/月(Pro)/$40/月(Business)。理解AI代码编辑器如何定价，对标 TODO2 的真实案例数据。

### Intercom Fin 定价页
- Intercom Fin定价：https://www.intercom.com/pricing （已验证，Intercom官方）
- **深链用法**：Intercom Fin是outcome-based pricing的典型--$0.99/解决。理解AI客服Agent如何按结果收费，对标 TODO2 的真实案例数据和 TODO3 的财务对比。

### OpenAI API定价（推理成本基准）
- OpenAI定价页：https://openai.com/api/pricing/ （已验证，OpenAI官方）
- **深链用法**：GPT-4o input $5/1M tokens是推理成本的核心参考。对比不同模型的定价，理解推理成本对Agent商业模式可行性的影响。对标 TODO5 的推理成本敏感度分析。

### DeepSeek API定价（推理成本下降趋势）
- DeepSeek定价：https://api-docs.deepseek.com/quick_start/pricing （已验证，DeepSeek官方）
- **深链用法**：DeepSeek V3的$0.27/1M input tokens比GPT-4o低95%，代表推理成本下降趋势。推理成本下降5-10倍时，outcome-based pricing从"亏钱"变为"盈利"。对标 TODO5 的推理成本敏感度分析。

---

## ⑤ 天道推演×商业模式沙盘 + MCP协议 + A2A经济（2026前沿特色）

### MCP（Model Context Protocol）
- MCP官方文档：https://modelcontextprotocol.io/ （已验证，Anthropic官方）
- MCP GitHub：https://github.com/modelcontextprotocol/python-sdk （已验证，Python SDK）
- **深链用法**：MCP是Anthropic提出的开放协议，为Agent间的工具/数据访问提供标准化接口。MCP是API Economy 2.0的基础设施--Agent通过MCP自动发现和调用其他Agent的能力。对应 notes.md 中API Economy 2.0和pydantic schema部分。

### Anthropic 结构化输出
- Anthropic结构化输出：https://docs.anthropic.com/en/docs/build-with-claude/tool-use （已验证，Anthropic官方）
- **深链用法**：结构化输出是Agent可发现能力声明的基础。pydantic schema定义Agent能力的输入输出契约，让其他Agent能自动判断能否调用。对标 TODO1 的pydantic schema设计。

### Agent-Based Modeling方法论（天道推演同构）
- mesa ABM教程（Schelling隔离模型）：https://mesa.readthedocs.io/latest/tutorials/intro_tutorial.html （已验证，经典ABM案例）
- **深链用法**：Schelling隔离模型是ABM的经典案例--微观Agent的简单规则涌现出宏观的隔离模式。与本Day的商业模式沙盘同构：微观定价决策（pydantic schema）涌现出宏观的NPV/IRR/弹性。天道推演在意识中构建沙盘，numpy-financial在代码中构建沙盘。

---

## 阅读路径建议

| 顺序 | 材料 | 用途 | 时长 |
|:----:|------|------|:----:|
| 1 | 本Day `notes.md` 理论回顾 + 独立教材 §Day 2 | AaaS+outcome-based+API Economy 2.0 | 1h |
| 2 | a16z "Agent Economy" 系列（选读1-2篇） | Agent商业模式演进 | 0.5h |
| 3 | pydantic基础教程（BaseModel/Field） | schema验证基本用法 | 0.5h |
| 4 | `starter.ipynb` 上机（配numpy-financial+statsmodels文档） | 三种定价模式财务对比+弹性回归 | 2h |
| 5 | Cursor/Intercom Fin定价页对比（选读） | 真实Agent定价案例 | 0.25h |
| 6 | OpenAI vs DeepSeek定价页对比（选读） | 推理成本趋势 | 0.25h |
| 7 | MCP官方文档概述（选读） | API Economy 2.0标准化协议 | 0.5h |

---

*全部深链已于 2026-07-25 验证存在。如发现失效，请在 Issues 报告。*
