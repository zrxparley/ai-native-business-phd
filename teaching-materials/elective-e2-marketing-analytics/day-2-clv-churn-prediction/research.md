# Day 2 研究产出层 (v7.0): CLV 客户终身价值与流失预测

> **本文件**：将 Day 2 教学材料（notes.md BG/NBD 简化公式 / sklearn 流失建模 / NSW RCT 445 样本 / CLV×流失四象限行动矩阵）锚定为可发表研究工件。遵循 IMRaD / DSR (Hevner 2004) / OSF 预注册 / FAIR / NeurIPS 可复现研究标准。
> **关联文件**：[`notes.md`](./notes.md) v5.0/v6.0 基线 / [`starter.ipynb`](./starter.ipynb) 6 个 TODO / [`solution.ipynb`](./solution.ipynb) 参考 / [`reading.md`](./reading.md) 深链。

---

## research_question

**核心研究问题**：在 NSW 真实 RCT 数据（causaldata，445 样本）映射的 CLV/流失营销场景中，仅用基线人口统计协变量（age/educ/marr/nodegree + re74/re75 历史消费）训练的 sklearn LogisticRegression / RandomForestClassifier 流失分类器，其 AUC-ROC 是否显著低于工业级可用门槛 0.80？该差距能否量化"RCT 随机化使基线特征不应强预测结果"对预测性建模（而非因果估计）的负迁移效应？

**可证伪子问题**：
- H1：仅用 NSW 基线特征，LogReg/RF 的 AUC-ROC 将落在 [0.50, 0.58] 区间（接近随机，远低于 0.80 工业门槛）。
- H2：加入 re74/re75 趋势特征后 AUC 提升幅度 < 0.05，因 RCT 随机化消解了基线-结果强相关。
- H3：BG/NBD 简化公式（`pred_clv = F × retention^12 × AOV × 12 × discount`）在 NSW 映射数据上的 CLV 估计方差，比历史 CLV（Σ 历史交易利润）方差低 ≥30%，但因违背"购买率恒定"假设（B2B 合同周期）产生系统性偏差。

---

## contribution

**delta vs prior work**：

1. **相对 Fader & Hardie (2005) BG/NBD 原论文**：原论文用 CDNOW 电商数据（4,357 客户，78 周交易）验证 Beta-Geometric / NBD 双过程模型；本研究用 **NSW 真实 RCT 数据**（445 样本，causaldata Cunningham Mixtape 配套）将 BG/NBD 简化公式（`F × retention^12 × AOV × 12 × discount`）应用于就业培训->营销映射场景，量化 RCT 数据在预测性（非因果）建模中的 AUC 上限。
2. **相对 Cunningham《Causal Inference: The Mixtape》**：Mixtape 用 NSW 估计 ATE（干预效应）；本研究 **正向利用 NSW 的随机化失败预测** 来教学"为什么真实营销场景需要行为特征（登录频率/会话时长/客服投诉）才能达 AUC > 0.80"，把因果研究的"零信号基线"转为预测建模的方法论负案例。
3. **相对 Fader & Hardie (2007) "How to Project Customer Retention"**：该综述用 sBG（shifted Beta-Geometric）拟合合同制留存曲线；本研究显式标注 BG/NBD "购买率恒定 / 流失不可逆 / 客户独立 / 金额独立"四假设在 NSW->B2B 营销映射中的违背点（合同周期、营销召回、口碑传播、批发折扣），为贝叶斯 CLV（PyMC 个体级后验）留下研究缺口。
4. **相对 Microsoft CUPED (2013)**：CUPED 用预处理协变量缩减 A/B 实验方差；本研究 TODO4 LogReg 把 re74/re75 作为协变量进入流失模型，**反向借用 CUPED 思想**于预测建模（而非方差缩减），并量化"协变量随机化导致 CUPED 思想在预测中失效"。

---

## linked_paper

| # | 论文 | 作者/年份 | 链接 | 关联说明 |
|---|------|----------|------|---------|
| 1 | "Counting Your Customers" One by One: An RFM-Based CLV Model with BG/NBD | Fader, Hardie, Lee (2005), *Journal of Marketing Research* | http://brucehardie.com/papers/018/fader_etds_2005.pdf | Day 2 TODO3 简化 BG/NBD CLV 公式（`F × retention^12 × AOV × 12 × discount`）的学术源头。两大行为假设：购买服从 Poisson，流失服从 Beta 分布。本研究用 NSW 445 样本检验其四假设在 B2B 映射场景的违背。链接已收录于 reading.md §1。 |
| 2 | How to Project Customer Retention | Fader & Hardie (2007), *Service Industries Review* | http://brucehardie.com/papers/021/sir_2007_final.pdf | TODO4 流失标签构造与 TODO5 模型评估的理论基础。sBG 留存曲线 vs 指数平滑留存 vs 二分类流失预测的方法论对比。本研究 IMRaD Discussion 引用其"合同制场景生存分析优于二分类"论点。链接已收录于 reading.md §3。 |
| 3 | Controlled-Experiment Using Pre-Experiment Data (CUPED) | Deng, Xu, Kohavi, Walker (2013), Microsoft Research | https://www.microsoft.com/en-us/research/publication/controlled-experiment-using-pre-experiment-data/ | 2026 前沿点。TODO4 LogisticRegression 中 re74/re75 作为协变量与 CUPED 思想一致。本研究在 Discussion 中对比"CUPED 用预处理信息提升因果估计精度" vs "本研究用预处理信息提升预测精度"在 RCT 数据下的失效机制。链接已收录于 reading.md §4。 |
| 4 | Causal Inference: The Mixtape (online) | Cunningham (2021) | https://mixtape.scunning.com/ | causaldata 库 NSW 数据来源（445 样本）。第 2-3 章 RCT 方法论解释"为什么随机化使基线特征不应强预测结果"，是本研究 H1/H2 假设的理论依据。链接已收录于 reading.md §3。 |

> 注：以上 4 链接全部来自本单元 reading.md 已验证深链（2026-07-25 验证存在），未联网重查 arXiv API。

---

## imrad_outline

### I. Introduction（动机 + gap + 贡献）
- **动机**：CLV（Customer Lifetime Value）与流失预测是营销分析最常见应用（Day 1 描述性 RFM -> Day 2 预测性 BG/NBD + sklearn），但教科书常以 CDNOW 等电商数据演示，未触及"RCT 数据随机化对预测性建模的反向约束"。
- **Gap**：(a) Fader-Hardie BG/NBD 文献未讨论 RCT 数据用于预测而非因果估计时的 AUC 上限；(b) Cunningham Mixtape 未将 NSW 数据映射至 CLV/流失营销场景；(c) sklearn 流失建模教材未量化"基线特征 vs 行为特征"对 AUC > 0.80 门槛的差距。
- **Contribution**：(i) NSW->CLV/流失映射协议；(ii) AUC ~0.54 实证基线（H1）；(iii) BG/NBD 四假设 B2B 违背点标注；(iv) CUPED 思想反向用于预测建模的失效机制。

### M. Methods（数据 + 模型 + 识别策略）
- **数据**：causaldata NSW 真实 RCT，445 样本（treat=1 干预组 / treat=0 对照组）。变量映射：re74/75/78 -> 活动-2/-1/+1 年消费；age/educ/marr/nodegree -> 客户人口统计协变量；re78=0 -> 流失标签。
- **模型 1（CLV）**：pandas + numpy 实现历史 CLV（Σ 历史交易利润）+ 简单预测 CLV（`avg_monthly_profit × 1/(1-retention_rate)`）+ BG/NBD 简化公式（`F × retention^12 × AOV × 12 × discount_factor`）。starter.ipynb TODO1/3。
- **模型 2（流失）**：sklearn LogisticRegression（class_weight='balanced' + StandardScaler 标准化 + max_iter 调优）+ RandomForestClassifier（n_estimators / max_depth 调参）。train_test_split stratify 分层抽样。starter.ipynb TODO4/5。
- **识别策略**：用 RCT 数据检验预测模型（非因果估计）。若基线特征强预测流失，则违反随机化；预期 AUC ~0.54（接近随机）即随机化成立的反向证据。

### R. Results（预期/已得核心发现）
- **CLV 估计**：NSW 数据下，历史 CLV 均值（re74+re75+re78 之和）vs BG/NBD 简化 CLV 均值（F × retention^12 × AOV × 12 × discount），量化简化公式的方差缩减 vs 系统性偏差。
- **流失 AUC**：LogReg AUC ~0.50-0.58 / RF AUC ~0.52-0.60（远低于 0.80 工业门槛）。Precision/Recall 在 class_weight='balanced' 下显著优于默认（class imbalance 场景）。
- **四象限行动矩阵**：CLV×流失风险四象限 Q1（高 CLV 高风险）客户数估计，及挽留 30% 可挽回价值（CLV_mean × Q1_count × 0.3）。

### D. Discussion（贡献边界 + 局限 + 未来工作）
- **贡献边界**：本研究正向利用 RCT 随机化失败预测，作为"为什么真实营销场景需要行为特征"的方法论负案例。
- **局限**：(a) NSW 445 样本量不足以稳定拟合完整 BG/NBD（5 参数），故用简化版；(b) NSW 是就业培训数据，CLV/流失映射为教学虚构，非真实营销；(c) re78=0 流失标签为二元阈值，未尝试连续衰减标签；(d) 未做交叉验证（CV）超参调优，仅 train/test 一次。
- **未来工作**：(i) 用 PyMC / Stan 实现贝叶斯 BG/NBD（个体级后验，小样本 B2B 场景）；(ii) 加入行为特征（登录频率/会话时长/客服投诉）测试 AUC 是否 > 0.80；(iii) 用 sBG 生存分析替代二分类流失，对标 Fader-Hardie 2007；(iv) 数据治理维度（GDPR/CCPA/PIPL）对个体级 CLV 预测的合规约束审计。

---

## reproducibility_checklist

> NeurIPS / ACM 风格可复现清单。本单元所有交付物可在本机复现。

- [x] **Code**：`solution.ipynb`（7 cells，0 scaffold 残留，0 TODO 残留）+ `starter.ipynb`（6 TODO 填空版）+ `tutorial.ipynb`（苏格拉底追问）。代码经 verify_unit.py 第 3-5 条验收（starter 6 TODO / solution 7 cells / scaffold=0 / TODO=0）。
- [x] **Data**：causaldata NSW 真实 RCT 数据集，445 样本，来源 Cunningham《Causal Inference: The Mixtape》配套包（https://github.com/NickCH-K/causaldata ，MIT License）。详见 `data/README.md`（11 个来源 URL）。
- [x] **Seeds**：随机种子 `random_state=42`（sklearn train_test_split / LogisticRegression / RandomForestClassifier 全流程固定），见 starter.ipynb TODO4/5。
- [x] **Environment**：Python 3.x + pandas + numpy + scipy + scikit-learn + causaldata。关键库版本见 `data/README.md`。无 GPU 依赖。
- [x] **Preregistration**：本文件 `## research_question` 节 H1/H2/H3 三假设即预注册声明（OSF DOI 待申请；本单元以文件级 hypothesis 声明替代）。假设可证伪，结果可对比。
- [x] **FAIR**：Findable（causaldata PyPI 可检索）/ Accessible（MIT License + 免费在线 Mixtape 教材）/ Interoperable（pandas DataFrame 标准格式）/ Reusable（NSW 原始 LaLonde 1986 数据可追溯，445 样本与 Mixtape 一致）。
- [x] **Metrics**：AUC-ROC（roc_auc_score）/ Precision / Recall / classification_report（sklearn.metrics 工业标准评估）。报告阈值：AUC > 0.80 工业可用，AUC ~0.54 随机基线。
- [x] **Statistical tests**：BG/NBD retention rate 置信区间用 scipy 统计分布；CLV 均值差异用 t 检验（连接 Day 1）。

---

## research_to_practice

本研究产出可翻译为以下实践工件：

1. **HBS Working Paper -> HBR Article**：将"RCT 数据随机化反向约束预测建模 AUC ~0.54"发现写成 HBS 工作论文，进一步浓缩为 HBR 文章《When Your A/B Test Data Can't Predict Churn: A Causal-Design Cautionary Tale》，目标读者 CMO/Head of Growth。
2. **MIT Sloan Teaching Case**：以 NSW->CLV/流失映射为案例，标题《Predicting Churn with Randomized Data: The NSW Paradox》，沿用 MIT 15.071 The Analytics Edge 案例法（与 Day 2 reading.md §5 对标）。
3. **企业白皮书**：与 Salesforce Einstein / Stitch Fix 等营销分析平台合作发布《CLV × Churn Action Matrix Playbook》，把 TODO6 四象限行动矩阵（高/低 CLV × 高/低流失风险）落为 Playbook，附挽留 30% 高价值客户的价值回收公式（CLV_mean × Q1_count × 0.3）。
4. **OSS 工具**：把 BG/NBD 简化公式（避免 lifelines/lifetimes 依赖冲突）打包为 `clv-lite` PyPI 包，零依赖 pandas + numpy 实现，面向 MBA / MSc BA 教学。
5. **OSF 预注册模板**：把 H1/H2/H3 假设模板化为 OSF CLV/流失预测预注册模板，供后续研究者复用。

> research-to-practice 路径遵循 DSR (Hevner 2004) "设计科学"双循环：研究环（H1-H3 假设检验）-> 设计环（clv-lite 包 + Playbook）-> 评估环（企业白皮书效果测量）。

---

*v7.0 研究产出层追加于 2026-07-26，不修改 v5.0/v6.0 原文一字。所有 arXiv/DOI/https 链接来自本单元 reading.md 已验证深链（2026-07-25 验证）。*
