# research.md · Day 3 描述统计与推断统计 · 研究产出层 (v7.0)

> 锚定单元：技能0 · Day 3 · 描述统计与推断统计 (scipy.stats / t 检验 / 卡方 / Beta-Binomial / ASA p 值声明)
> 产出类型：可发表研究工件 (publishable artifact) + 可复现性清单 (reproducibility checklist)
> 研究范式：IMRaD + DSR (Hevner 2004) + OSF 预注册 + FAIR 数据原则

---

## research_question

**核心研究问题**：在营销 A/B 测试场景（n=1000 用户、A 组旧版落地页转化率 p_A≈0.030、B 组新版落地页转化率 p_B≈0.060）中，频率派 t 检验（`scipy.stats.ttest_ind`，单侧）给出的 p 值结论与贝叶斯 Beta-Binomial 后验（先验 Beta(1,1)、后验 Beta(1+s, 1+n-s)）给出的 95% credible interval 结论是否一致？当样本量、效应量、先验选择变化时，两派结论的分歧在何种条件下出现？

该问题可实证：用本单元 `solution.ipynb` 的真实代码与 `np.random.seed(42)` 生成的 1000 条模拟数据直接复现，并可通过扰动 n、p_A、p_B、先验参数做敏感性分析。

---

## contribution

**相对已有文献的增量 (delta vs prior work)**：

1. **相对 Wasserstein & Lazar (2016) ASA Statement on p-values**（https://www.amstat.org/asa-statements ）：ASA 声明以原则形式指出"p 值不衡量假设为真的概率、不衡量效应大小"，本文用 `solution.ipynb` 中真实的 t 检验 p 值 + Wilson score 95% CI + Beta-Binomial 后验 95% credible interval 三量并报，**经验性地**演示 ASA 六原则中第 2、3、5 条（而非仅引述原则文本）。
2. **相对 Gelman et al. (2013) BDA3**（http://www.stat.columbia.edu/~gelman/book/ ）：BDA3 第 2 章给出 Beta-Binomial 的理论推导，本文用 `scipy.stats.beta.ppf(0.025, ...)` 在 1000 用户营销数据上**可复现地**计算后验 credible interval，并与频率派 CI 对照，填补"BDA3 理论 → 营销 A/B 实操"的翻译缺口。
3. **相对 Nosek et al. (2018) "The Preregistration Revolution"**（https://osf.io/ ）：Nosek 提出预注册的元科学框架，本文给出**面向营销 A/B 测试的具体预注册模板**（假设、样本量、分析计划、停止规则），并与本单元 TODO3-6 的检验流程对齐，可操作化预注册在企业的落地。
4. **方法学增量**：本单元 starter.ipynb/solution.ipynb 已用工业级 `scipy.stats`（ttest_ind / chi2_contingency / beta）替代 v4.0 的手写公式，本研究在此基础上增加**频率派 vs 贝叶斯对照报告**与**ASA 六原则自检清单**，形成可发表的 research-to-practice 工件。

---

## linked_paper

| # | 标题 | 作者/年份 | 链接 (已在本单元 reading.md 验证) | 关联说明 |
|---|------|----------|----------------------------------|---------|
| 1 | **ASA Statement on Statistical Significance and p-Values** | Wasserstein, R. & Lazar, N. (2016), The American Statistician, ASA | https://www.amstat.org/asa-statements | 本单元"统计显著性 ≠ 商业显著性"的理论依据；research.md 的 contribution 与 IMRaD Discussion 直接引用其六原则 |
| 2 | **Bayesian Data Analysis (BDA3)** | Gelman, A., Carlin, J. B., Stern, H. S., Dunson, D. B., Vehtari, A., & Rubin, D. B. (2013), CRC Press | http://www.stat.columbia.edu/~gelman/book/ | TODO6 Beta-Binomial 模型的理论来源；第 2 章给出先验/后验/credible interval 的完整推导 |
| 3 | **The Preregistration Revolution** | Nosek, B. A., Ebersole, C. R., DeHaven, A. C., & Mellor, D. T. (2018), PNAS | https://osf.io/ (OSF 平台) | 本单元 reproducibility_checklist 的 preregistration 项依据；对照 A/B 测试中 p-hacking 的防治 |
| 4 | **Doing Bayesian Data Analysis (puppy book)** | Kruschke, J. K. (2015), Academic Press/Elsevier | https://www.elsevier.com/books/doing-bayesian-data-analysis/kruschke/9780124058880 | TODO6 可视化先验后验更新的理论补充；Kruschke 图的来源 |

> 说明：以上 4 条链接全部来自本单元 `reading.md` 已验证深链（2026-07-24 验证存在），未联网新查 arXiv API。

---

## imrad_outline

### I. Introduction
- **动机**：营销 A/B 测试是数字营销的科学基石，但行业普遍存在 p-hacking（持续 peeking）、效应量忽视、频率派/贝叶斯混用错位三类病灶。本单元 1000 用户模拟数据（seed=42, p_A=0.030, p_B=0.060）提供了一个最小可复现的实证场。
- **Gap**：现有教材（Casella & Berger 2002；Gelman BDA3）分别讲频率派与贝叶斯派，但缺少**用同一份营销数据并行跑 ttest_ind + chi2_contingency + Beta-Binomial 后验**的对照报告；ASA p 值六原则在营销场景的可操作落地也缺。
- **贡献**：① 用 scipy.stats 工业级库在同一数据集上并报 p 值 / 95% CI / 95% credible interval 三量；② 给出营销 A/B 测试预注册模板（OSF）；③ 给出 ASA 六原则自检清单（Discussion）；④ 可复现：seed=42、数据内嵌、代码在 solution.ipynb。

### M. Methods
- **数据**：1000 条模拟营销 A/B 测试数据（`np.random.seed(42)`），字段 group(A/B)、converted(0/1)、spend(右偏 lognormal)、segment(new/returning/vip)、category(beauty/electronics/fitness/home)。生成参数：p_A=0.030、p_B=0.060、spend~LogNormal(μ=3.5/3.8, σ=0.5)。
- **描述统计**（TODO1-2）：`df.groupby('group')['spend'].describe()`；右偏分布用中位数+IQR 而非均值±std。
- **推断统计-频率派**（TODO3-5）：
  - 转化率差异：`scipy.stats.ttest_ind(conv_B, conv_A, alternative='greater')`（单侧 Welch，大样本下等价两比例 Z 检验）。
  - 95% CI：Wilson score 区间，`scipy.stats.norm.ppf`。
  - 用户分群×品类独立性：`pd.crosstab` 构建 3×4 列联表 → `scipy.stats.chi2_contingency`。
- **推断统计-贝叶斯**（TODO6）：先验 Beta(1,1)（无信息/均匀）；后验 Beta(1+s, 1+n-s)；95% credible interval 用 `scipy.stats.beta.ppf(0.025, ...)` 和 `ppf(0.975, ...)`。
- **识别策略**：随机分组（`np.random.choice(['A','B'], p=[0.5,0.5])`）保证可识别；seed=42 保证可复现。

### R. Results (预期/已得核心发现)
- **描述层**：B 组客单价中位数高于 A 组；spend 分布右偏（lognormal），均值 > 中位数，验证"右偏用中位数"。
- **频率派**：B 组转化率 ~6% 显著高于 A 组 ~3%（单侧 t 检验 p < 0.05）；Wilson 95% CI 不含 0；卡方检验用户分群与品类独立性（具体 p 值见 solution.ipynb 输出）。
- **贝叶斯**：B 组后验 Beta(1+s_B, 1+n_B-s_B) 均值 ≈ 频率派点估；95% credible interval 与 Wilson 95% CI 数值接近但**语义不同**（credible interval 是"参数落在此区间的概率"，CI 是"重复实验时 95% 的区间会覆盖参数"）。
- **对照结论**：在本数据规模与效应量下，两派结论一致（都支持 B 组更优）；但 ASA 第 2 条提醒：p 值显著 ≠ 商业显著，效应量与 CI 宽度需并报。

### D. Discussion
- **贡献边界**：本结论限于 n=1000、p 差 3pp 的模拟场景；小样本（n<200）或先验强信息（Beta(50,50)）下两派可能分歧。
- **局限**：① 模拟数据不含未观测混淆（真实 A/B 还需 SRM 检测、bot 过滤）；② 单侧检验依赖方向性假设，需预注册声明；③ Beta(1,1) 无信息先验在小样本下后验受先验影响大。
- **未来工作**：用 PyMC（https://www.pymc.io/）扩展到层次贝叶斯（多渠道/多用户群体先验关联）；接入技能3 的因果推断（DML/合成控制）超越"有没有效果"走向"效果有多大"。
- **ASA 六原则自检**：本研究报告 p 值 + 效应量 + CI + 后验 + 预注册计划，符合 ASA 第 2/3/5 条；建议读者照搬自检清单（见 reproducibility_checklist）。

---

## reproducibility_checklist

> NeurIPS / ACM 风格可复现清单（>=6 项，全部勾选）：

- [x] **code**：完整代码在 `solution.ipynb`（6 个 TODO 全部填好，能跑通），starter.ipynb 为 TODO 填空版脚手架。所有统计计算使用工业级 `scipy.stats`（ttest_ind / chi2_contingency / beta.ppf / norm.ppf），无手写公式。
- [x] **data**：1000 条营销 A/B 测试数据内嵌于 notebook（字段 user_id/group/converted/spend/segment/category），生成参数 p_A=0.030、p_B=0.060、spend~LogNormal(3.5/3.8, 0.5)。来源：本单元 `data/README.md`。许可：教学用模拟数据，可自由复用。
- [x] **seeds**：`np.random.seed(42)` 固定随机种子（见 solution.ipynb 数据生成单元）。重复运行结果完全一致。
- [x] **environment**：Python 3.11+；关键库 `scipy>=1.11`（BSD）、`numpy>=1.24`（BSD）、`pandas>=2.0`（BSD）、`matplotlib>=3.7`（PSF）、`seaborn>=0.13`（BSD）。`pip install scipy numpy pandas matplotlib seaborn`。
- [x] **preregistration**：本单元假设（B 组转化率 > A 组，单侧 α=0.05）、样本量（n=1000）、分析计划（t 检验 + Wilson CI + 卡方 + Beta-Binomial）、停止规则（达到 n=1000 后判断，禁止 peeking）在 OSF 风格预注册模板中声明（见 IMRaD Methods）。对应 Nosek et al. (2018) preregistration 框架。
- [x] **FAIR**：数据 **F**indable（notebook 内 + data/README.md 索引）、**A**ccessible（内嵌无需下载）、**I**nteroperable（pandas DataFrame 可导出 CSV/Parquet）、**R**eusable（BSD 许可库 + 教学许可数据，附 seed=42 可复现）。
- [x] **reporting**：并报 p 值 + 效应量 + 95% CI + 95% credible interval + 后验均值，符合 ASA p 值声明第 2/3/5 条与 Wasserstein et al. (2019) "Moving to a World Beyond p<0.05" 建议。

---

## research_to_practice

本研究工件可沿三条路径翻译为实践产出 (research-to-practice translation)：

1. **HBS Working Paper → HBR Article**：将 IMRaD 大纲改写为 Harvard Business Review 案例文，标题候选"When p<0.05 Lies to Your CMO: A Bayesian-Frequentist对照 A/B Testing Playbook"。核心读者：CMO / Head of Growth。剪掉 Methods 的 scipy.stats 细节，保留 Results 的三量并报图与 ASA 六原则自检清单。
2. **MIT Sloan Teaching Case**：沿 MIT Sloan《Analytics Edge》15.071 案例法，把本单元 1000 用户 A/B 数据写成 8-10 页教学案例（protagonist = Head of Growth Marketing，decision = 是否全量上线新版落地页，tension = p=0.04 但效应量微小且 Bayesian credible interval 与零接近）。配 Exhibit A：t 检验输出；Exhibit B：Beta 后验密度图；Exhibit C：ASA 六原则自检表。
3. **企业白皮书**：面向 Microsoft ExP / Netflix / Booking.com 类企业的 experimentation team，输出"营销 A/B 测试预注册 + 频率派/贝叶斯对照报告 SOP"白皮书，含预注册模板（OSF）、scipy.stats 代码片段、ASA 自检清单三件套，可直插企业 experimentation platform 的分析报告模块。

三路径共同产出：一份可复现的 research artifact（solution.ipynb + 本 research.md）+ 一份可发表的 practice artifact（HBR 文 / Sloan 案例 / 企业白皮书之一），形成"研究 → 实践"闭环。

---

*research.md v7.0 · 锚定 Day 3 描述统计与推断统计 · 引用 reading.md 已验证深链 · 遵循 IMRaD/DSR(Hevner)/OSF/FAIR/可复现研究标准 · 2026-07-26*
