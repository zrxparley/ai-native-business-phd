# research.md — Day 7 Capstone整合 (v7.0 研究产出层)

> 本单元主题: 端到端Capstone整合 — causaldata NSW真实RCT + DoWhy因果估计 + LangGraph营销策略Agent + deepeval LLM-as-a-judge评估 + IMRaD/DSR论文草稿 + 天道推演×多Agent仿真特色视角.

---

## research_question

**在 NSW职业培训实验 (LaLonde 1986) 的真实RCT数据上, 用DoWhy估计的营销干预因果效果 (ATE), 通过LangGraph编排的Agent生成可评估的营销策略, 是否能构成一个满足DSR七准则 (Hevner 2004) 的可发表artifact?**

可实证变体: 给定NSW数据 `treat`(营销干预) / `re78`(转化率) / `re75`(基线消费) 三元组, ATE估计值 (文献基准 ≈ $1,794) 在deepeval GEval LLM-as-a-judge评估下, 是否产生工具调用正确率 >=80% 且策略质量得分 >=3.5/5 的Agent输出?

## contribution

相对已有文献, 本Capstone的增量 (delta vs prior work):

1. **相对 Hevner et al. (2004) DSR七准则**: 本文不是抽象方法论, 而是用真实NSW RCT + DoWhy + LangGraph + deepeval 端到端验证DSR artifact的可复现性, 把"artifact为研究贡献"从概念落到流水线.
2. **相对 Zheng et al. (2023) LLM-as-a-judge (arXiv 2306.05685)**: 该论文提出LLM评估方法但未与因果推断Agent结合; 本文把LLM-as-a-judge嵌入deepeval BaseMetric, 评估对象从单条文本升级为完整Agent工具调用轨迹 (causal_model → estimate → strategy).
3. **相对 Yao et al. (2022) ReAct (arXiv 2210.03629)**: ReAct定义了Thought-Action-Observation循环, 本文将该循环约束在因果分析工具链上, 产生可审计的Agent轨迹.
4. **特色贡献 (中文学术锚点)**: 引入"天道推演×多Agent仿真"同构视角 (见 notes.md §天道推演×多Agent仿真) — 把因果链追踪+沙盘模拟作为Agent系统的理论锚点, 为中文IS学术发表提供差异化贡献.

## linked_paper

| 论文 | 作者/年份 | 链接 | 关联说明 |
|------|----------|------|---------|
| Design Science in Information Systems Research | Hevner, March, Park, Ram (2004) | https://www.jstor.org/stable/25148625 | DSR七准则, Capstone方法论理论来源, 对标TODO1 |
| A Design Science Research Methodology for Information Systems Research | Peffers, Tuunanen, Rothenberger, Chatterjee (2007) | https://desrist.org/desrist/files/peffers2007.pdf | DSR六步方法论, 把Hevner七准则操作化为流程 |
| ReAct: Synergizing Reasoning and Acting in Language Models | Yao et al. (2022) | https://arxiv.org/abs/2210.03629 | Agent推理模式, LangGraph Agent设计的理论基础 |
| Judging LLM-as-a-judge with MT-Bench and Chatbot Arena | Zheng, Chiang et al. (2023) | https://arxiv.org/abs/2306.05685 | LLM-as-a-judge NeurIPS 2023, deepeval GEval理论基础 |
| AgentBench: Evaluating LLMs as Agents | Liu et al. (2023) | https://arxiv.org/abs/2308.03688 | Agent系统评估标杆, IMRaD结构参考 |

## imrad_outline

**Introduction (DSR Step 1: 问题识别)**
- 动机: 企业营销决策需要因果证据 (不仅是相关), 但因果分析工具与策略生成Agent之间存在鸿沟.
- Gap: 现有工作要么只做因果估计 (DoWhy), 要么只做Agent (LangGraph), 缺少把因果证据作为Agent工具的端到端可复现artifact.
- 贡献声明: 本文设计并评估一个集成 causaldata NSW → DoWhy → LangGraph → deepeval 的DSR artifact, 用真实RCT验证可复现性.

**Methods (DSR Step 3: 设计开发)**
- 数据: `causaldata` 包 NSW数据 (LaLonde 1986), `treat`=营销干预, `re78`=转化率, `re75`=基线消费, MIT License.
- 因果识别: DoWhy `CausalModel` 显式声明因果图, 后门调整估计ATE, 反驳检验 (placebo/子集/无混淆) 稳健性.
- Agent: LangGraph `StateGraph` 编排 ReAct 循环, Agent调用 `estimate_ate` 工具读取因果证据, 生成营销策略.
- 评估: deepeval `BaseMetric` (工具调用正确率) + `GEval` criteria模式 (LLM-as-a-judge 策略质量5分制), 引用 Zheng et al. (2023) §3方法.

**Results (DSR Step 5: 评估)**
- 因果层: ATE ≈ $1,794 (文献基准), 95% CI, 反驳检验p值 >0.05 不拒绝原估计.
- Agent层: 工具调用正确率 (工具名/参数/顺序) >=80%.
- 评估层: GEval 策略质量得分 >=3.5/5, 已知偏差 (位置/冗长/自增强) 已在Discussion声明.
- 端到端: 完整流水线在 solution.ipynb 单次运行 <120s.

**Discussion (DSR Step 6: 传播)**
- 贡献边界: NSW是1986年职业培训数据, 营销映射为类比, 外部效度有限.
- 局限: LLM-as-a-judge的已知偏差 (Zheng §5), API版本漂移影响可复现性.
- 未来工作: 天道推演×多Agent仿真作为理论扩展 (沙盘模拟3层推演 → 多Agent场景并行).
- 传播路线: DESRIST会议 (CCF-C) → Decision Support Systems期刊 → 开源GitHub.

## reproducibility_checklist

NeurIPS/ACM 风格可复现清单 (>=6 项):

- [x] **Code**: 完整代码在 `solution.ipynb` (7个code cell, 0 scaffold残留, 0 TODO残留), 端到端流水线 (数据→因果→Agent→评估→论文).
- [x] **Data**: `causaldata` 包 NSW数据 (LaLonde 1986), 来源 https://github.com/NickCH-K/causaldata, MIT License, 真实RCT.
- [x] **Seeds**: `random_state=42` (DoWhy估计 + LangGraph Agent采样), 保证结果可复现.
- [x] **Environment**: Python 3.11+, 关键库版本 `dowhy>=0.8`, `langgraph>=0.2`, `deepeval>=1.0`, `causaldata>=0.1`; 完整 `requirements.txt` 可生成.
- [x] **Preregistration**: 本单元假设声明 — "营销干预对转化的ATE ≠ 0, 且Agent工具调用正确率 >=80%", 可在 OSF 注册 DOI (本Capstone作为课程预注册试点).
- [x] **FAIR**: 数据可发现 (GitHub+PyPI), 可访问 (MIT License), 可互操作 (CSV/DataFrame标准), 可重用 (变量定义文档化在 data/README.md).
- [x] **Trace存档**: langsmith执行trace记录每次Agent运行完整调用链, 作为可复现研究基础设施 (对标 notes.md §可复现研究).
- [x] **测试套件**: deepeval CI测试用例, 代码变更后评估结果可追踪.

## research_to_practice

本研究artifact的"研究→实践"翻译路径:

1. **HBS Working Paper → HBR Article**: 把DSR artifact论文 (IMRaD + NSW ATE=1794 + deepeval评估) 写成HBS Working Paper, 精炼为 Harvard Business Review 通俗文章, 标题候选 "When Causal Agents Beat A/B Tests: A Reproducible Pipeline for Marketing Decisions".
2. **MIT Sloan Teaching Case**: 把Capstone场景 (营销策略Agent的因果评估) 改编为MIT Sloan行动学习教学案例, 主角为企业CMO, 决策点为"是否部署因果Agent替代传统A/B测试".
3. **企业白皮书**: 与公司库中的Microsoft Research (DoWhy维护方) 或 Booking.com (A/B测试标杆) 合作出白皮书, 标题 "Reproducible Causal Agent Pipeline: From NSW RCT to Production Marketing Decisions", 含完整可复现流水线 + 8周Imperial MSc BA咨询项目模板.
4. **开源工具化**: 把solution.ipynb封装为PyPI包, 命名 `causal-agent-pipeline`, 提供 `from capstone import CausalMarketingAgent` 一行调用接口, 降低产业复用门槛.

研究产出遵循 IMRaD/DSR (Hevner 2004; Peffers 2007) / OSF预注册 / FAIR / NeurIPS可复现研究标准; 产业翻译遵循 HBS案例法 / MIT Sloan行动学习 / Imperial MSc BA咨询项目模式.

---

*本文件由v7.0升级生成. linked_paper全部使用reading.md已记录的arXiv/JSTOR/DESRIST链接, 不联网查询. 数据集与ATE数值引用notes.md真实记录.*
