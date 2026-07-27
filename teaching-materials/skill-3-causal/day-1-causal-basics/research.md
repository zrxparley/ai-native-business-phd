# Day 1 研究产出层 (v7.0)

> 本单元 (因果推断基础) 的可发表研究工件 + 可复现研究标准锚点。与 v5.0 上机 (NSW 后门调整) 与 v6.0 学习科学层互补: v5.0 教"做对", v6.0 教"学会", v7.0 教"产出可被学界/产业认可的工件"。

---

## research_question

**在 NSW 真实观测数据上, 后门调整估计相对朴素均值差能否系统性消除"用户活跃度"类混杂带来的偏差, 且这一识别增益能否被 LLM-as-a-judge (NeurIPS 2023, arXiv 2306.05685) 辅助审查稳定复现?**

可实证拆解为三个子问题:
- (RQ1) 朴素估计 $\hat{\text{ATE}}_{naive} = \bar{Y}_{treated} - \bar{Y}_{control}$ 在 NSW 上的偏差方向与量级?
- (RQ2) 用 DoWhy 声明 DAG 并做后门调整后, ATE 估计是否收敛到 RCT 基准 (Dehejia & Wahba 1999 报告的 NSW 真实 ATE ≈ \$1794)?
- (RQ3) LLM-as-a-judge 对"DAG 是否遗漏混杂 / 识别策略是否满足后门准则 / 反驳是否充分"的判定, 与统计反驳检验 (安慰剂处理) 的一致性如何?

## contribution

相对既有文献的 delta:

1. **相对 Dehejia & Wahba (1999)**: 原作用 NSW 验证 PSM 在观测数据上的识别能力; 本文/本单元进一步用 DoWhy 的"建模->识别->估计->反驳"四步流程把后门调整显式化, 并将 NSW 的"职业培训->收入"因果结构同构映射到"广告曝光->转化"营销场景, 让因果识别方法可直接迁移到营销 AI 系统评估。
2. **相对 Pearl《The Book of Why》**: Pearl 用直觉语言介绍因果阶梯与 do-演算; 本单元在真实 `causaldata.nsw` 数据上让学生亲手验证 L1 (朴素关联) → L2 (后门干预) 的偏差缩减, 而非止步于概念理解。
3. **相对 LLM-as-a-judge 原论文 (arXiv 2306.05685)**: 原论文把 LLM-as-a-judge 用于 NLG 任务评估; 本单元把它**限定**为"因果论证质量审查器"(检查 DAG/识别/反驳), 显式声明其位于因果阶梯 L1 (对论证文本的关联分析), 不能上升到 L2/L3 估计--这是对 LLM-as-a-judge 应用边界的方法论澄清。

## linked_paper

1. **Zheng et al., "Judging LLM-as-a-judge with MT-Bench and Chatbot Arena" (NeurIPS 2023)**
   - arXiv: https://arxiv.org/abs/2306.05685
   - 关联: 本单元 2026 前沿点的方法论来源。用它做因果论证审查 (DAG 遗漏混杂 / 后门准则 / 反驳充分性), 而非因果效应估计。本单元明确将其定位为研究方法论自检工具, 对应因果阶梯 L1。

2. **Dehejia, R. H. & Wahba, S. (1999), "Causal Effects in Nonexperimental Studies: Reevaluating the Evaluation of Training Programs", Journal of the American Statistical Association 94(448): 1053-1062**
   - JSTOR/DOI 锚点: https://doi.org/10.1080/01621459.1999.10473858
   - 关联: NSW 数据集与 PSM 识别策略的源头论文。本单元 starter.ipynb 的 TODO3-4 (朴素估计 vs 后门调整) 直接复现其核心发现: 朴素均值差在 NSW 观测对照组上有偏, 匹配/调整后接近 RCT 基准 ATE ≈ \$1794。

3. **Sharma, A. & Kiciman, E. (2020), "DoWhy: An End-to-End Library for Causal Inference", arXiv:2008.12519**
   - arXiv: https://arxiv.org/abs/2008.12519
   - 关联: 本单元上机使用的 DoWhy 库的方法学论文。其"建模->识别->估计->反驳"四步流程对应 starter.ipynb 的 TODO4-5, 是 RQ1/RQ2 识别与估计的工程实现。

## imrad_outline

### Introduction
- **动机**: 营销决策长期依赖"相关≠因果"的观察性指标 (点击率/转化率均值差), 在存在用户活跃度等混杂时系统性误判增量。NSW 是因果推断领域经典的"观测数据 vs RCT 基准"对照, 但其方法论尚未被营销 AI 系统评估广泛采用。
- **Gap**: 现有营销归因实践 (Day 3 MMM/增量测试) 缺乏一个从 DAG 到后门调整到 LLM 审查的端到端可复现流程; LLM-as-a-judge 在因果论证审查上的应用边界未被显式声明。
- **贡献**: 用 NSW + DoWhy + LLM-as-a-judge 构建可复现流程, 并明确 LLM-as-a-judge 的因果阶梯定位 (L1 审查, 非 L2/L3 估计)。

### Methods
- **数据**: `causaldata.nsw` (Dehejia & Wahba 1999), 处理=`treat` (职业培训), 结果=`re78` (1978 收入), 协变量=`age/education/black/hispanic/married/nodegree/re74/re75`。
- **模型**: Pearl 因果阶梯 L1/L2/L3 + DAG 声明 + 后门准则。
- **识别策略**: 后门调整 (控制"用户活跃度"类混杂, 即 NSW 中的 `age/education/re74/re75`); 备选: 倾向得分匹配 (PSM, TODO6)。
- **估计器**: DoWhy `CausalModel` + `identify_effect` + `estimate_effect` (backdoor调整); 对照: 朴素均值差 (TODO3)。
- **稳健性**: DoWhy `refute_estimate` 的 placebo_treatment_refuter (安慰剂处理, TODO5)。
- **LLM 审查**: 把 DAG + 识别 + 估计 + 反驳结果整理为结构化文本, 让 LLM (参考 arXiv 2306.05685 范式) 审查论证质量, 检查遗漏混杂/识别成立/反驳充分/外推边界。

### Results
- **预期/已得核心发现** (基于 NSW 真实数据):
  - 朴素均值差 (TODO3) 因协变量分布不均 (处理组 baseline 收入 `re74/re75` 显著低于 RCT 对照组) 而**低估** NSW 真实 ATE。
  - 后门调整估计 (TODO4) 收敛到 Dehejia & Wahba 1999 报告的 RCT 基准 ATE ≈ **\$1794** (具体值取决于协变量子集, 但方向一致)。
  - 反驳检验 (TODO5, 安慰剂处理) 估计应接近 0, 证明估计非虚假相关。
  - LLM-as-a-judge (RQ3) 应能指出"用户活跃度"作为潜在混杂 (与人工 DAG 一致), 但不能给出 ATE 数值。

### Discussion
- **贡献边界**: 本流程在 NSW 单数据集上验证; 营销场景需补充时间动态 (Day 3 增量测试) 与高维混杂 (Day 4 因果发现)。
- **局限**: (1) NSW 是单时点截面, 营销场景常为面板; (2) LLM-as-a-judge 对 DAG 完备性的判断受 prompt 与模型能力限制; (3) 后门调整假设无未观测混杂, 营销场景常违反。
- **未来工作**: Day 2 实验设计 (A/B + DiD/RDD/IV) 弥补观测数据识别; Day 4 因果发现 (PC/FCI) 自动学 DAG; 把 LLM-as-a-judge 升级为 DeepEval CI 测试用例 (reading.md ③)。

## reproducibility_checklist

NeurIPS / ACM 风格可复现清单 (>=6 项):

- [x] **code**: 完整代码在 `solution.ipynb` (8 cells, 与 `starter.ipynb` 8 cells 结构对应, scaffold=0, TODO 残留=0); DoWhy 四步流程显式实现。
- [x] **data**: 真实数据集 `causaldata.nsw` (PyPI: https://pypi.org/project/causaldata/), 来源 Dehejia & Wahba 1999 的 NSW职业培训实验 + 观测对照组 (CPS), 许可见 causaldata 包文档; `data/README.md` 给出 >=2 来源链接。
- [x] **seeds**: 随机种子 `random_state=42` (DoWhy 估计器 + PSM 匹配 + 安慰剂反驳均显式 set, 确保 bootstrap CI 可复现)。
- [x] **environment**: Python 3.10+, 关键库 `dowhy>=0.8`, `causaldata>=0.1`, `econml>=0.12`, `scikit-learn>=1.2`, `statsmodels>=0.13`; 笔记本顶部 cell 给出 `!pip install` 一次成型。
- [x] **preregistration**: 本单元 hypothesis 声明 (NSW 后门调整 ATE 应收敛到 RCT 基准 ≈ \$1794, 朴素估计有偏) 已在 notes.md 上机任务 + alignment.md ILO3 写明; 可上传 OSF (https://osf.io/) 作为预注册 DOI。
- [x] **FAIR**: 数据可发现 (causaldata PyPI 索引) / 可访问 (公开下载) / 可互操作 (pandas DataFrame 标准格式) / 可重用 (Dehejia & Wahba 公开数据, 许可宽松)。
- [x] **LLM-as-a-judge prompt**: 审查 prompt 固化在 `solution.ipynb` 最后一个 cell, 模型版本 (Claude/GPT) 在 prompt 中声明, 确保审查结果可复现。

## research_to_practice

本研究产出可翻译为多个实践工件:

1. **HBS Working Paper -> HBR Article**: "When Naive A/B Comparison Fails: A Backdoor-Adjustment Playbook for Marketing AI Systems" -- 把 NSW 复现流程写成 HBS working paper, 再压缩为 Harvard Business Review 文章, 给 CMO 一个"何时该用后门调整而非朴素 A/B 对比"的决策框架。
2. **MIT Sloan Teaching Case**: 以某零售品牌"广告曝光->转化"为情境, 用 NSW 同构映射 (treat=广告曝光, re78=GMV, age/education=re74/re75 历史消费), 写成 MIT Sloan 教学案例 (带数据 + 决策点 + LLM 审查环节)。
3. **企业白皮书**: 与 Microsoft ExP / Netflix / Booking.com 等 experimentation platform 团队合作, 把"后门调整 + LLM-as-a-judge 论证审查"流程写成企业白皮书, 给 experimentation platform 用户提供"观测数据因果识别"补充工具链 (当 RCT 不可行或样本不足时)。
4. **DeepEval CI 测试用例**: 把 LLM-as-a-judge 因果论证审查写成 DeepEval (https://github.com/confident-ai/deepeval) 测试用例, 纳入营销 AI 系统的 CI 流水线, 自动拦截"DAG 遗漏关键混杂"的 PR。

---

*v7.0 研究产出层 · 2026-07-26 · 遵循 IMRaD / DSR (Hevner) / OSF 预注册 / FAIR / NeurIPS 可复现研究标准*
