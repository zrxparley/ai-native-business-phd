# Day 1 · 价值对齐与 Constitutional AI · 研究产出 (v7.0)

> **所属**：AI原生化商业博士 · 选修E9 · Day 1 · 研究产出层 (v7.0)
> **配套**：[`notes.md`](./notes.md)（理论与上机锚点）｜[`reading.md`](./reading.md)（arXiv深链）｜[`starter.ipynb`](./starter.ipynb)（上机脚手架）｜[`solution.ipynb`](./solution.ipynb)（参考实现）
> **标准**：IMRaD / Design Science Research (Hevner) / OSF preregistration / FAIR / NeurIPS 可复现清单

---

## research_question

**核心研究问题**：在广告法合规与消费者保护约束下，Constitutional AI（RLAIF + 显式宪法原则集）驱动的营销内容生成 Agent，相对纯 RLHF（InstructGPT 三步流程）方案，在 HHH 三维度（Helpful / Harmless / Honest）上的对齐失败率是否显著降低，且宪法原则的可审计性是否补足了 RLHF 的标注偏见与 Reward Hacking 风险？

可实证拆解为两个子假设：
- **H1**：在广告法违规检测（"绝对化用语""虚构成分""暗示治愈"）上，CAI 方案的 Harmless 维度失败率显著低于 RLHF baseline。
- **H2**：LLM-as-a-judge（deepeval GEval + 自定义 BaseMetric）对 HHH 三维度的自动评分与人类专家排序的 Spearman 相关 ≥ 0.7，验证 LLM-as-a-judge 在营销对齐评估中的效度。

---

## contribution

相对已有文献的 delta：

1. **相对 Christiano / Stiennon 等 RLHF 路线（InstructGPT, arXiv 2203.02155）**：本文不依赖人类偏好标注，而是用显式"企业营销宪法"（不夸大宣传 / 不误导消费者 / 符合广告法 / 尊重用户自主决策）驱动 AI 自我批评+修改，标注成本从 O(N·人工) 降至 O(宪法原则集·API 调用)，且宪法原则可版本化、可审计。
2. **相对 Bai et al. Constitutional AI（arXiv 2212.08073）**：原文在通用对话安全场景验证 RLAIF，本文将其迁移到**营销合规**这一垂直领域，引入广告法绝对化用语白名单 + 知识库锚定（防幻觉=防虚假宣传），用 deepeval BaseMetric 量化 HHH 三维度，而非通用 harmlessness 单维度。
3. **相对 Rafailov et al. DPO（arXiv 2305.18290）**：DPO 跳过奖励模型，但偏好数据仍需标注。本文用 garak alignment probes（NVIDIA/garak 0.15.1, 2026-06）作为外部红队探针，系统化扫描 CAI 与 DPO 两类方案的价值偏差，提供独立的、可复现的对齐回归测试集。
4. **相对 Zheng et al. LLM-as-a-judge（arXiv 2306.05685）**：原文在通用 QA/Chat 场景评估 judge 偏差，本文在营销合规场景显式声明位置偏差/冗长偏差/自我偏好对本评估的威胁效度，并用宪法原则集作为 rubric 缓解。

---

## linked_paper

1. **Constitutional AI: Harmlessness from AI Feedback** — Bai, Y., et al. (Anthropic, 2022)
   - arXiv: https://arxiv.org/abs/2212.08073
   - 关联：本 Day 核心理论来源。§2 Constitutional SL（监督学习阶段）+ §3 Constitutional RL（RLAIF 阶段）映射到 starter.ipynb 的 TODO1-6，本文用其"宪法原则 → AI 自我批评 → 偏好数据"流程构建营销 Agent 的对齐信号。
2. **Training language models to follow instructions with human feedback (InstructGPT)** — Ouyang, L., et al. (OpenAI, 2022)
   - arXiv: https://arxiv.org/abs/2203.02155
   - 关联：RLHF baseline。§3 三步流程（SFT → RM → PPO）+ §5 局限性（标注偏见 / Reward Hacking）作为 H1 的对照基线，CAI 的增量贡献以此为锚。
3. **Direct Preference Optimization** — Rafailov, R., et al. (Stanford, 2023)
   - arXiv: https://arxiv.org/abs/2305.18290
   - 关联：DPO 作为第三类对齐范式对照。§3 数学推导（最优奖励函数可从策略推导）解释为何 DPO + CAI 可组合使用（DPO 解决训练稳定性，CAI 解决标注成本）。
4. **Judging LLM-as-a-judge with MT-Bench and Chatbot Arena** — Zheng, L., et al. (NeurIPS 2023)
   - arXiv: https://arxiv.org/abs/2306.05685
   - 关联：LLM-as-a-judge 方法学基础。§3 评估方法 + §5 已知偏差（位置 / 冗长 / 自我偏好）映射到 deepeval GEval 的 criteria 模式与 H2 的效度威胁声明。

---

## imrad_outline

### Introduction
- **动机**：营销内容生成 Agent 在追求转化率最大化时，对齐失败表现为 Reward Hacking（欺骗性广告）、价值偏差（歧视性定向）、幻觉（虚构成分）—— 这些不只是产品 bug，而是广告法与消费者保护法的合规风险。
- **Gap**：现有 RLHF 工程化（InstructGPT 2203.02155）在通用对齐上验证充分，但 (a) 标注成本高、(b) 标注偏见、(c) 宪法不可审计；(c) 在营销垂直场景缺乏 HHH 三维度量化评估。
- **贡献**：(1) 设计企业营销宪法原则集（5-10 条，覆盖广告法 / 消费者保护 / 品牌调性）；(2) 用 deepeval 自定义 BaseMetric 量化 HHH 三维度对齐失败率；(3) 用 garak alignment probes 作为外部红队，对比 CAI vs RLHF baseline 的对齐回归。

### Methods
- **数据**：HHH 对齐测试用例集（见 `data/README.md`，三类：合规文案 / 违规文案 / 混合文案），广告法绝对化用语白名单（"最佳""第一""治愈"等）。
- **模型**：营销内容生成 Agent（基座 LLM），三种对齐方案对照：(a) RLHF baseline（InstructGPT 三步流程模拟）、(b) CAI（宪法 SL + 宪法 RL/RLAIF）、(c) DPO（偏好数据直接优化）。
- **识别策略**：HHH 三维度评分用 deepeval 自定义 BaseMetric + GEval（LLM-as-a-judge，criteria 模式按宪法原则）；价值偏差用 garak alignment probes（`latentinjection` / `goodside` / `snowball`）；无 API key 时用本地静态扫描 fallback。随机种子 `random_state=42`，每条用例跑 3 次取均值。
- **统计**：H1 用 McNemar 检验比较 CAI vs RLHF 在 Harmless 维度的失败率；H2 用 Spearman ρ 评估 LLM-judge 与人类专家排序一致性。

### Results（预期/已得）
- 预期 CAI 方案在 Harmless 维度失败率显著低于 RLHF baseline（H1），因宪法原则显式禁止广告法违规用语。
- 预期 LLM-as-a-judge 在 Honest 维度（夸大宣传/虚构成分）与人类专家排序一致性最高（H2，ρ ≥ 0.7），因 FaithfulnessMetric 对知识库锚定敏感。
- 已得锚点：starter.ipynb 的 6 个 TODO 实现 HHH 三维度评估闭环；solution.ipynb 的参考实现给出可复现基线（具体数字以上机跑通结果为准，本大纲不预设）。

### Discussion
- **贡献边界**：对齐评估是发现问题的手段，不能证明"已对齐"（通过测试 ≠ 价值观正确）。本方法对应因果阶梯 L1（输入-输出对关联分析），不能反事实推断"若换宪法原则会怎样"。
- **局限**：(a) garak 完整功能需 API key，本地静态扫描 fallback 覆盖度有限；(b) LLM-as-a-judge 存在位置偏差/冗长偏差/自我偏好（Zheng et al. 2306.05685 §5）；(c) 广告法边界本身文化相关（中国《广告法》vs FTC guidelines）。
- **未来工作**：(1) 因果推断（用 causaldata 风格的反事实）评估宪法原则单条修改的边际效应；(2) 在线 A/B 测试（Microsoft ExP / Netflix 风格）验证对齐评估与真实用户投诉率的相关性；(3) 跨文化宪法原则迁移研究。

---

## reproducibility_checklist

NeurIPS / ACM 风格可复现清单（≥6 项）：

- [x] **Code**：完整代码在 `solution.ipynb`（7 个 code cells，与 starter.ipynb 6 个 TODO 一一对应）；starter.ipynb 为 TODO 填空版脚手架。
- [x] **Data**：HHH 对齐测试用例集（合规/违规/混合三类）见 `data/README.md`；广告法绝对化用语白名单内置；许可：教学用 CC-BY-NC 4.0。
- [x] **Seeds**：`random_state=42`（sklearn / numpy / torch.dataloader 一致）；每条用例跑 3 次取均值 + 标准差。
- [x] **Environment**：Python 3.11；deepeval ≥ 2.5（confident-ai/deepeval, 17k★, MIT）；garak 0.15.1（NVIDIA/garak, 2026-06-05 PyPI）；openai ≥ 1.50（LLM-as-a-judge backend）；详见 `data/README.md` 安装指令。
- [x] **Preregistration**：本单元 H1/H2 假设声明见上文 research_question（OSF 风格预注册：变量、检验、阈值在数据采集前固定）；如需正式 OSF DOI，partner 投入后补登记。
- [x] **FAIR**：数据可发现（data/README.md 索引）/ 可访问（GitHub 仓库公开）/ 可互操作（JSON Lines 格式，deepeval 原生兼容）/ 可重用（CC-BY-NC 4.0 + 原则集可版本化）。
- [x] **Models**：基座 LLM 接口与版本（如 gpt-4o-2024-08 / claude-3-5-sonnet-20241022）在 `data/README.md` 显式声明；宪法原则集版本（v1.0, 2026-07）在 starter.ipynb cell 1 注释。
- [x] **Statistical reporting**：McNemar 检验报告 p 值 + 95% CI；Spearman ρ 报告 ρ + p 值 + n；效应量（Cohen's h for proportions）。

---

## research_to_practice

本研究产出的翻译路径遵循 HBS working paper → HBR article → MIT Sloan teaching case 三段式：

1. **HBS working paper 阶段**（学术严谨）：将 IMRaD 大纲扩展为 20-30 页工作论文，标题暂定 *"Constitutional AI for Marketing Compliance: A Reproducible HHH Evaluation of RLAIF vs RLHF Baselines"*，提交 HBS Working Paper Series / SSRN。核心附录含企业营销宪法原则集 v1.0 + deepeval BaseMetric 实现代码 + garak 探针命中报告。
2. **HBR article 阶段**（ practitioner 翻译）：压缩为 2500 字 HBR 文章，标题 *"Your Marketing Agent Needs a Constitution"*，面向 CMO / Head of AI，核心论点"对齐不是合规补丁，而是产品安全工程"，配 3 个企业宪法原则设计模板（快消 / 金融 / 医美）。
3. **MIT Sloan teaching case 阶段**（教学落地）：写作 HBS 风格教学案例（见 `industry.md` § case_study），protagonist 为某 DTC 品牌 Head of AI，decision point 为"是否将 RLHF baseline 切换为 CAI + garak 红队"，配 teaching note 引用本 Day starter.ipynb 作为上机附件。
4. **企业白皮书阶段**（咨询交付）：与 Anthropic / Salesforce Einstein 合作发布 *"Marketing Alignment Maturity Model"* 白皮书，5 级成熟度（手动关键词 → RLHF → CAI → CAI+红队 → 在线对齐监控），本研究对应 Level 3-4 的可复现评估方法。

所有翻译工件均以本 `research.md` 的可复现清单为方法学锚点，确保学术-产业-教学三环不脱钩。
