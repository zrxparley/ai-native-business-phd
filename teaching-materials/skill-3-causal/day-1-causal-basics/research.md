# Day 1 研究产出层 (v7.0)

> 本单元 (因果推断基础) 的可发表研究工件 + 可复现研究标准锚点。与 v5.0 上机 (NSW 后门调整) 与 v6.0 学习科学层互补: v5.0 教"做对", v6.0 教"学会", v7.0 教"产出可被学界/产业认可的工件"。CQ-S3-1 要求所有研究结论明确 estimand、识别假设、overlap、refuter/敏感性与证据复核日期。

---

## research_question

**以 `nsw_mixtape` 随机实验均值差为基准，在 NSW 处理组 + `cps_mixtape` 观测对照的比较中，后门调整能否缩小选择偏差；这一结论对 overlap、估计器与未观测混杂有多敏感？**

可实证拆解为三个子问题:
- (RQ1) NSW处理组/CPS观测对照的朴素均值差，相对 NSW 随机实验基准的偏差方向与量级是什么?
- (RQ2) 用 DoWhy 声明 DAG 并做后门调整后, ATE 估计是否接近文献中的 NSW 实验基准 (Dehejia & Wahba 1999 常被引用的量级约为 \$1794；具体复现值取决于样本版本、协变量集合与估计器)?
- (RQ3) LLM-as-a-judge 对"DAG 是否遗漏混杂 / 识别策略是否满足后门准则 / 反驳是否充分"的判定, 与统计反驳检验 (安慰剂处理) 的一致性如何?

## contribution

相对既有文献的 delta:

1. **相对 Dehejia & Wahba (1999)**: 原作用实验基准审计观测方法; 本单元用 DoWhy 的“建模→识别→估计→反驳”复刻审计结构，并要求先核验 overlap，再讨论向营销场景迁移的限制。
2. **相对 Pearl《The Book of Why》**: 本单元让学生在 `nsw_mixtape` / `cps_mixtape` 上区分随机实验与观测识别；DoWhy 调整属于基于假设的 L2 估计，不是由软件自动把 L1“升级”为因果真值。
3. **相对 LLM-as-a-judge 原论文 (arXiv 2306.05685)**: 原论文把 LLM-as-a-judge 用于 NLG 任务评估; 本单元把它**限定**为"因果论证质量审查器"(检查 DAG/识别/反驳), 显式声明其位于因果阶梯 L1 (对论证文本的关联分析), 不能上升到 L2/L3 估计--这是对 LLM-as-a-judge 应用边界的方法论澄清。

## linked_paper

1. **Zheng et al., "Judging LLM-as-a-judge with MT-Bench and Chatbot Arena" (NeurIPS 2023)**
   - arXiv: https://arxiv.org/abs/2306.05685
   - 关联: 本单元 2026 前沿点的方法论来源。用它做因果论证审查 (DAG 遗漏混杂 / 后门准则 / 反驳充分性), 而非因果效应估计。本单元明确将其定位为研究方法论自检工具, 对应因果阶梯 L1。

2. **Dehejia, R. H. & Wahba, S. (1999), "Causal Effects in Nonexperimental Studies: Reevaluating the Evaluation of Training Programs", Journal of the American Statistical Association 94(448): 1053-1062**
   - JSTOR/DOI 锚点: https://doi.org/10.1080/01621459.1999.10473858
   - 关联: NSW 实验基准与观测比较策略的源头论文。本单元 TODO3-4 复刻其审计思路；只有实际运行、样本版本锁定且诊断完整后，才能报告调整值与实验基准的距离。

3. **Sharma, A. & Kiciman, E. (2020), "DoWhy: An End-to-End Library for Causal Inference", arXiv:2008.12519**
   - arXiv: https://arxiv.org/abs/2008.12519
   - 关联: 本单元上机使用的 DoWhy 库的方法学论文。其"建模->识别->估计->反驳"四步流程对应 starter.ipynb 的 TODO4-5, 是 RQ1/RQ2 识别与估计的工程实现。

## imrad_outline

### Introduction
- **动机**: 营销决策长期依赖"相关≠因果"的观察性指标 (点击率/转化率均值差), 在存在用户活跃度等混杂时系统性误判增量。NSW 是因果推断领域经典的"观测数据 vs RCT 基准"对照, 但其方法论尚未被营销 AI 系统评估广泛采用。
- **Gap**: 现有营销归因实践 (Day 3 MMM/增量测试) 缺乏一个从 DAG 到后门调整到 LLM 审查的端到端可复现流程; LLM-as-a-judge 在因果论证审查上的应用边界未被显式声明。
- **贡献**: 用 NSW + DoWhy + LLM-as-a-judge 构建可复现流程, 并明确 LLM-as-a-judge 的因果阶梯定位 (L1 审查, 非 L2/L3 估计)。

### Methods
- **数据**: `causaldata.nsw_mixtape` 随机实验样本（445 行）用于基准；其处理组与 `causaldata.cps_mixtape` 观测对照合并为观测比较样本。处理=`treat`，结果=`re78`，字段=`age/educ/black/hisp/marr/nodegree/re74/re75`。
- **模型**: Pearl 因果阶梯 L1/L2/L3 + DAG 声明 + 后门准则。
- **识别策略**: 先用 NSW 随机实验组内均值差建立基准；再对 NSW处理组/CPS对照观测样本做后门调整（`age/educ/re74/re75` 等）与 PSM，并显式检查共同支撑。
- **估计器**: DoWhy `CausalModel` + `identify_effect` + `estimate_effect` (backdoor调整); 对照: 朴素均值差 (TODO3)。
- **稳健性**: DoWhy `refute_estimate` 至少覆盖 placebo_treatment_refuter、random_common_cause_refuter、data_subset_refuter/bootstrap_refuter 三类中的两类；另补 1 个负对照与未观测混杂敏感性分析。
- **LLM 审查**: 把 DAG + 识别 + 估计 + 反驳结果整理为结构化文本, 让 LLM (参考 arXiv 2306.05685 范式) 审查论证质量, 检查遗漏混杂/识别成立/反驳充分/外推边界。

### Results
- **预期核心发现** (需以执行后的 notebook 输出为准):
  - 观测样本朴素均值差 (TODO3) 会偏离 NSW 随机实验基准；偏差方向必须由实际样本输出决定，不能预写成“必然低估”。
  - 后门调整估计 (TODO4) 应向 Dehejia & Wahba 1999 常用实验基准量级靠近, 但不能在未运行、未锁环境、未报告置信区间时声称“已收敛”。
  - 反驳检验 (TODO5, 安慰剂处理) 估计应接近 0；这只能说明未在该 refuter 下发现明显矛盾，不能证明因果结论为真。
  - LLM-as-a-judge (RQ3) 应能指出"用户活跃度"作为潜在混杂 (与人工 DAG 一致), 但不能给出 ATE 数值。

### Discussion
- **贡献边界**: 本流程在 NSW 单数据集上验证; 营销场景需补充时间动态 (Day 3 增量测试) 与高维混杂 (Day 4 因果发现)。
- **局限**: (1) NSW 是单时点截面, 营销场景常为面板; (2) LLM-as-a-judge 对 DAG 完备性的判断受 prompt 与模型能力限制; (3) 后门调整假设无未观测混杂, 营销场景常违反。
- **未来工作**: Day 2 实验设计 (A/B + DiD/RDD/IV) 弥补观测数据识别; Day 4 因果发现 (PC/FCI) 自动学 DAG; 把 LLM-as-a-judge 升级为 DeepEval CI 测试用例 (reading.md ③)。

## reproducibility_checklist

NeurIPS / ACM 风格可复现清单 (>=6 项):

- [ ] **code**: `solution.ipynb` 含 DoWhy 四步流程示例；当前仓库未保存执行输出，发布前需提交 clean-run 版本或独立运行日志。
- [x] **data**: `causaldata.nsw_mixtape` 与 `causaldata.cps_mixtape` (PyPI: https://pypi.org/project/causaldata/) 分别提供随机实验与观测对照；`data/README.md` 记录两者角色，禁止混写。
- [ ] **seeds**: 发布前需在 notebook 或环境说明中显式设置 refuter、bootstrap/子样本、PSM 匹配相关随机种子；当前 `solution.ipynb` 尚未固化这些随机性。
- [ ] **environment**: 发布前需补锁定环境（如 `requirements.txt` / `pyproject.toml` / `environment.yml`）；当前 notebook 只有注释形式的 `!pip install` 提示，不足以证明可复现。
- [ ] **preregistration**: 发布前需冻结实验基准、观测样本构造、estimand、overlap 规则、估计器与敏感性阈值；课堂讲义中的预期方向不等于正式预注册。
- [x] **FAIR**: 数据可发现 (causaldata PyPI 索引) / 可访问 (公开下载) / 可互操作 (pandas DataFrame 标准格式) / 可重用 (Dehejia & Wahba 公开数据, 许可宽松)。
- [ ] **LLM-as-a-judge prompt**: 发布前需固化 prompt、模型版本、评审日期与人工复核记录；当前材料把 LLM-as-a-judge 定位为论证审查器，但未在 `solution.ipynb` 保存可复现评审输出。

证据复核日期：2026-08-03

## research_to_practice

本研究产出可翻译为多个实践工件:

1. **HBS Working Paper -> HBR Article**: "When Naive A/B Comparison Fails: A Backdoor-Adjustment Playbook for Marketing AI Systems" -- 把 NSW 复现流程写成 HBS working paper, 再压缩为 Harvard Business Review 文章, 给 CMO 一个"何时该用后门调整而非朴素 A/B 对比"的决策框架。
2. **MIT Sloan Teaching Case**: 以某零售品牌"广告曝光->转化"为情境, 用 NSW/CPS 同构映射 (treat=广告曝光, re78=GMV, age/educ/re74/re75=用户画像与历史消费), 写成 MIT Sloan 教学案例 (带数据 + 决策点 + LLM 审查环节)。
3. **企业白皮书**: 与 Microsoft ExP / Netflix / Booking.com 等 experimentation platform 团队合作, 把"后门调整 + LLM-as-a-judge 论证审查"流程写成企业白皮书, 给 experimentation platform 用户提供"观测数据因果识别"补充工具链 (当 RCT 不可行或样本不足时)。
4. **DeepEval CI 测试用例**: 把 LLM-as-a-judge 因果论证审查写成 DeepEval (https://github.com/confident-ai/deepeval) 测试用例, 纳入营销 AI 系统的 CI 流水线, 自动拦截"DAG 遗漏关键混杂"的 PR。

---

*v7.0 研究产出层 · 2026-07-26 · 遵循 IMRaD / DSR (Hevner) / OSF 预注册 / FAIR / NeurIPS 可复现研究标准*
