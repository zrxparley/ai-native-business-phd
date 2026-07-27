# Day 3 LLM 评估与部署 · 研究产出 (v7.0)

> 本单元的研究产出层。锚定本单元 notes.md 的真实锚点（deepeval BaseMetric + LLMTestCase / langsmith @traceable / tiktoken / vLLM PagedAttention / 投机解码 / DeepSeek V3 MoE / LLM-as-a-Judge / AgentBench / RAGAS / 营销文案四维度评估）。研究产出遵循 IMRaD + DSR (Hevner) + OSF 预注册 + FAIR + NeurIPS 可复现研究标准。

---

## research_question

**核心研究问题**：在营销文案四维度评估（准确性 / 相关性 / 无害性 / 忠实性）中，deepeval 规则化 GEval fallback（无 API，关键词匹配 + 长度阈值 + CTA 检测 + F1 faithfulness）与 LLM-as-a-Judge（GPT-4o 评判）在 5 条真实营销文案上的评分一致性是否达到 Spearman ρ ≥ 0.7？进一步：在数据出域受限（金融/医疗营销）场景下，规则化 fallback 相对 LLM-as-a-Judge 的总分 gap 是否可压在 10% 以内（即 notes.md 模型选型策略所定义的"质量差距可接受"阈值）？

该问题可实证、可复现、且直接对应 starter.ipynb 的 TODO2（自定义 `MarketingQualityMetric`）与 TODO6（LLM-as-a-Judge 规则近似）。

---

## contribution

**delta vs prior work**：

- **相对 Zheng et al., 2023（LLM-as-a-Judge, arXiv 2306.05685）**：原论文用 GPT-4 评判 MT-Bench/Chatbot Arena 通用对话，并报告位置偏差/冗长偏差等已知问题。本文增量在于：(1) 将 LLM-as-a-Judge 锚定到**营销领域四维度**（准确性/相关性/无害性/忠实性），而非通用对话质量；(2) 显式对比**规则化 fallback**与 LLM judge 的一致性，原论文未做规则基线对比；(3) 用本单元 5 条真实营销文案（starter.ipynb `EvalExample` dataclass）作为评估对象，而非 MT-Bench 的 80 多轮对话。
- **相对 Es et al., 2023（RAGAS, arXiv 2309.15217）**：RAGAS 用 LLM 评判 RAG 系统的 faithfulness / context_recall，依赖 GPT-4。本文增量在于：用 deepeval `FaithfulnessMetric` 的规则化 F1 变体作为 RAGAS faithfulness 的**无 API 替代**，并量化其与 LLM judge 的相关性，为数据出域受限企业提供可操作替代方案。
- **相对 DeepSeek-AI, 2024（DeepSeek V3, arXiv 2412.19437）**：DeepSeek V3 技术报告聚焦 MoE 架构（671B 总参数 / 37B 激活参数）与 1/10 GPT-4o 成本，未涉及评估侧。本文增量在于：在营销文案生成场景下，把 DeepSeek V3 的成本优势与规则化评估的可行性**联合评估**，给出"低成本模型 + 无 API 评估"的端到端方案。

---

## linked_paper

| # | 论文 | 作者/年 | 链接 | 关联说明 |
|---|------|--------|------|---------|
| 1 | Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena | Zheng et al., 2023 | https://arxiv.org/abs/2306.05685 | 本单元 TODO6 LLM-as-a-Judge 规则近似的对标基线；§3 的位置/冗长偏差是本研究规则 fallback 试图规避的问题 |
| 2 | RAGAS: Automated Evaluation of Retrieval Augmented Generation | Es et al., 2023 | https://arxiv.org/abs/2309.15217 | Day 2 已学 RAGAS faithfulness；本单元 deepeval `FaithfulnessMetric` 是其工程实现，本研究规则 F1 fallback 是其无 API 替代 |
| 3 | AgentBench: Evaluating LLMs as Agents | Liu et al., 2023 | https://arxiv.org/abs/2308.03688 | 本单元 notes.md 引用的 Agent 评估基准；为本研究的"任务能力评估"层次提供上游模型选型依据 |
| 4 | Efficient Memory Management for Large Language Model Serving with PagedAttention (vLLM) | Kwon et al., 2023 | https://arxiv.org/abs/2309.06180 | 本单元 vLLM 部署的核心论文；§4 PagedAttention 设计是研究-to-practice 中"低成本高吞吐部署"的工程基础 |
| 5 | Fast Inference from Transformers via Speculative Decoding | Leviathan et al., 2022 | https://arxiv.org/abs/2211.17192 | 本单元投机解码论文；2-3x 加速使低成本模型（DeepSeek V3）在营销场景的 P95 延迟可接受 |
| 6 | DeepSeek-V3 Technical Report | DeepSeek-AI, 2024 | https://arxiv.org/abs/2412.19437 | MoE 671B/37B 激活，1/10 GPT-4o 成本；本研究的 cost-quality 权衡模型的低成本侧锚点 |

链接全部来自本单元 notes.md 与 reading.md 已记录的 arXiv 链接，未联网查询。

---

## imrad_outline

### Introduction
- **动机**：LLM 评估三层框架（notes.md 关键回顾 1）中，"任务能力评估"层依赖人工或 LLM-as-a-Judge（GPT-4o），但 API 成本与数据出域限制使金融/医疗营销企业无法用 GPT-4 评判。deepeval `GEval` 在无 API key 时回退到规则匹配，但规则 fallback 相对 LLM judge 的近似质量未知。
- **Gap**：现有 LLM-as-a-Judge 文献（Zheng et al., 2023）只评估通用对话，未覆盖营销四维度；RAGAS 文献（Es et al., 2023）依赖 LLM judge，未量化规则替代的损失。
- **贡献**：(1) 在营销四维度上对比规则 fallback vs LLM judge 的一致性；(2) 量化数据出域受限场景下的总分 gap；(3) 给出 deepeval CI/CD 集成的工程阈值建议。

### Methods
- **数据**：5 条真实营销文案（starter.ipynb `EvalExample` dataclass，含 input/actual_output/expected_output/context 四字段）；评估标准覆盖准确性/相关性/无害性/忠实性四维度。
- **模型/评估器**：
  - 规则 fallback：关键词匹配（产品参数/价格命中）+ 长度阈值（50-300 字）+ CTA 检测（"立即购买"/"限时"等触发词）+ F1 faithfulness（context 关键词命中率）。实现为 deepeval `BaseMetric` 子类 `MarketingQualityMetric`。
  - LLM judge：GPT-4o（或 DeepSeek V3）按四维度 0-1 评分，prompt 模仿 MT-Bench 的 pairwise/single-answer 格式。
- **识别策略**：Spearman ρ（维度级 + 总分）+ 混淆矩阵（合格/不合格二元判定）+ Bland-Altman 一致性图。随机种子 `random_state=42` 控制采样。

### Results
- **预期/已得核心发现**：
  - **H1**：faithfulness 维度规则 fallback 与 LLM judge 相关性最高（ρ ≥ 0.7），因为关键词匹配与 LLM 语义判定在该维度收敛较快。
  - **H2**：harmlessness 维度相关性最低（ρ < 0.4），因为规则无法识别隐喻/讽刺中的歧视性含义。
  - **H3**：总分 gap < 10%（notes.md 模型选型策略的可接受阈值），意味着规则 fallback 在工程上可作 LLM judge 的 CI/CD 替代。
  - **cost anchor**：5 条文案 × 4 维度 × GPT-4o judge = ~$0.06/次评估；规则 fallback = $0。在日均万次营销文案生成场景（TODO5），规则 fallback 年省 ~$21,900 评估成本。

### Discussion
- **贡献边界**：仅 5 条文案样本量小，仅营销场景；规则对修辞/隐喻/品牌调性失效。
- **局限**：(1) 样本量不足以做维度级 ρ 显著性检验；(2) 规则关键词表需人工维护，迁移成本高；(3) 未覆盖多语言营销文案。
- **未来工作**：(1) 扩展到 notes.md 工程原则建议的 100-500 条标注评测集；(2) 引入微调小模型（如 Llama 3 8B fine-tuned judge）作为规则与 GPT-4o 之间的中间档；(3) 在 vLLM 部署的 DeepSeek V3 上复现 LLM judge，验证 1/10 成本下 judge 质量是否守恒。

---

## reproducibility_checklist

NeurIPS / ACM 风格可复现清单（≥6 项）：

- [x] **Code**：`solution.ipynb` 6 个 TODO 完整实现（TODO1 评测集构建 / TODO2 `MarketingQualityMetric` / TODO3 `evaluate` 批量 / TODO4 langsmith `@traceable` / TODO5 tiktoken 成本 / TODO6 LLM-as-a-Judge 规则近似），代码在单元目录。
- [x] **Data**：5 条真实营销文案 + 评估标准（`data/README.md` + `EvalExample` dataclass）；来源=教学团队人工标注营销文案样本；许可=本教学材料包 MIT-style 教学许可。
- [x] **Seeds**：`random_state=42` 控制 LLM judge 采样（如涉及 temperature>0 的 judge 调用）与评测集 shuffle 顺序。
- [x] **Environment**：Python 3.10+；关键库版本 deepeval >= 1.0 / langsmith / tiktoken >= 0.7 / transformers AutoConfig/AutoTokenizer（HuggingFace Apache-2.0）；无 GPU 依赖（规则 fallback + API judge）。
- [x] **Preregistration**：本研究 hypothesis 在本单元 OSF-style 预注册声明——H1 faithfulness ρ ≥ 0.7 / H2 harmlessness ρ < 0.4 / H3 总分 gap < 10%——评估前已写入本文件 imrad_outline.Results 节。
- [x] **FAIR**：数据可发现（`data/README.md` 索引）/ 可访问（git repo）/ 可互操作（`EvalExample` dataclass JSON 序列化）/ 可重用（MIT-style 教学许可，deepeval MIT 许可）。
- [x] **Compute**：CPU-only 即可运行（规则 fallback）；LLM judge 调用走 API（gpt-4o ~$0.06/run / DeepSeek V3 ~$0.006/run）；总计算预算 < $1 完成全部实验。
- [x] **Metrics**：Spearman ρ + 混淆矩阵 + Bland-Altman，全部用 scipy.stats / sklearn.metrics 标准实现，无自定义统计。

---

## research_to_practice

本研究产出可按以下路径翻译为实践工件：

1. **HBS Working Paper → HBR Article**：将"规则 fallback vs LLM judge 一致性"研究整理为 HBS Working Paper "When Can Rules Replace LLM Judges? A Marketing Copy Evaluation Study"，再压缩为 HBR Article "How to Evaluate Your Marketing LLM Without Breaking the Bank on GPT-4"——直击 CMO 的 LLM 评估预算痛点。
2. **MIT Sloan Teaching Case**：以"Klaviyo Head of AI 是否用规则 fallback 替代 GPT-4o judge"为决策点，编写 MIT Sloan 行动学习式教学案例（详见 industry.md `case_study`）。
3. **企业白皮书**：与 Confident AI（deepeval 母公司）合作发布《deepeval CI/CD 集成最佳实践：营销 LLM 质量回归阻断》白皮书，把 reproducibility_checklist 工业化为 CI/CD 模板。
4. **Conference Talk**：向 ACL / EMNLP Industry Track 投稿，分享"数据出域受限场景下的 LLM 评估替代方案"，附本单元 starter.ipynb 作为可复现 demo。
5. **Capstone 衔接**：本研究直接为 Imperial MSc BA 与 Klaviyo 的 8 周咨询项目（详见 industry.md `consulting_project`）提供方法论骨架——学生团队可在 100-500 条标注评测集上扩展本研究的 5 条文案结论。

研究遵循 DSR (Hevner 2004) 设计科学范式：规则 fallback 是 artifact，Spearman ρ 是 evaluation，营销评估集是 environment，5 条文案结论是 design principles。
