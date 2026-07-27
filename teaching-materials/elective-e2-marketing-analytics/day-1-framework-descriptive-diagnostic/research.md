# Day 1 研究产出层 (v7.0)

> **单元主题**：营销分析框架-描述/诊断分析
> **可发表研究工件锚点**：NSW 真实 RCT 数据 (445 样本, `causaldata` 库) 营销映射 (treat=营销干预, re78=活动后消费) + pandas/scipy.stats/statsmodels 工具链 + CUPED (Microsoft 2013) 方差缩减思想

---

## research_question

**核心研究问题**：在 NSW 营销映射设定下, 用 OLS 回归控制预处理协变量 (re75/re74/age/educ) 估计的营销干预 (treat) 净效应, 是否与未控制协变量的简单 t 检验 (TODO4 `ttest_ind`) 估计存在统计意义上的显著差异, 且该差异是否可由 CUPED (Microsoft 2013) 的方差缩减思想解释？

**可实证假设**：H1 -- 控制协变量后, treat 系数的标准误较未控制时缩小 (CUPED-adjacent variance reduction); H2 -- 两种估计方法下的 treat 效应点估计方向一致但幅度不同 (混杂偏差可量化)。

---

## contribution

相对已有文献, 本研究工件的增量 (delta) 如下：

1. **相对 LaLonde (1986)**: LaLonde 用 NSW 原始数据揭示非实验方法的因果效应偏差, 但未做营销场景映射。本研究将 NSW 就业培训数据**显式映射**为营销干预场景 (treat=促销活动, re78=活动后消费), 在保持 RCT 金标准的同时, 为营销分析教学提供可复用的真实数据基线。
2. **相对 Dehejia & Wahba (1999)**: DW 用 propensity score matching 逼近 RCT 真值, 关注匹配方法。本研究聚焦更基础的 OLS 协变量调整 (TODO6 `sm.OLS`), 并显式连接 CUPED (Microsoft 2013) 的方差缩减视角, 解释"为什么控制预处理变量提升估计精度"。
3. **相对 Cunningham《Causal Inference: The Mixtape》**: Mixtape 第 2-3 章用 NSW 讲 RCT 基础, 但未覆盖营销漏斗 (AARRR) 与客户分群 (RFM) 的描述/诊断整合。本研究在同一 NSW 数据上**并行**完成描述性 (TODO1-3) 与诊断性 (TODO4-6) 分析, 形成营销分析四层框架的前两层可复现工件。

---

## linked_paper

**LaLonde, R. J. (1986). "Evaluating the Econometric Evaluations of Training Programs with Experimental Data." *American Economic Review*, 76(4): 604-620.**

- 链接: https://www.jstor.org/stable/1806062 (已验证, AER 经典论文, 见 reading.md §3)
- 关联说明: NSW 数据的原始论文。LaLonde 用 NSW 实验数据揭示非实验方法 (回归、匹配) 的因果效应估计与实验真值差距很大。本研究工件用同一 NSW 数据的 `causaldata` 子样本 (Dehejia-Wahba Sample), 在 TODO6 中复现"控制协变量后的 OLS 估计"并与 TODO4 的简单 t 检验对比, 直接呼应 LaLonde 的核心命题。

**配套参考论文 (本单元 reading.md 已记录链接)**：

- Dehejia, R. H. & Wahba, S. (1999). "Causal Effects in Nonexperimental Studies." 链接: https://www.uh.edu/~adkugler/DehejiaWahba.pdf -- NSW 子样本来源, propensity score matching 逼近 RCT 真值。
- Cunningham, S. "Causal Inference: The Mixtape." 链接: https://mixtape.scunning.com/ -- `causaldata` 库配套教材, 第 2-3 章 NSW 与 RCT 基础。
- Microsoft Research (2013). "Controlled-Experiment Using Pre-Experiment Data (CUPED)." 链接: https://www.microsoft.com/en-us/research/publication/controlled-experiment-using-pre-experiment-data/ -- TODO6 协变量调整思想的源头。

---

## imrad_outline

**Introduction (动机 + gap + 贡献)**
- 动机: 营销分析四层框架 (描述->诊断->预测->处方) 中, 描述/诊断是基础与桥梁, 但企业实践中常被跳过 (notes.md "售前洞察": 大多数中国企业处于描述性早期)。
- Gap: 现有营销分析教材多用模拟数据演示概念, 缺乏真实 RCT 数据的描述/诊断整合工件, 且未将 CUPED (2013) 方差缩减思想前置到 Day 1 诊断层。
- 贡献: (a) NSW 营销映射真实数据基线 (445 样本); (b) 描述 (TODO1-3) + 诊断 (TODO4-6) 整合的 TODO 脚手架; (c) 显式连接 OLS 协变量调整与 CUPED 思想。

**Methods (数据 + 模型 + 识别策略)**
- 数据: `causaldata` 库 NSW 真实 RCT, n=445 (Dehejia-Wahba Sample)。字段营销映射: treat (营销干预 0/1), re74 (活动前2年消费基线), re75 (活动前1年消费), re78 (活动后消费效果), age/educ/marr/nodegree (客户特征)。
- 模型: (1) TODO1 `pandas.DataFrame.describe()` 基线对比; (2) TODO4 `scipy.stats.ttest_ind` 独立样本 t 检验 (Welch, `equal_var=False`); (3) TODO5 `scipy.stats.chi2_contingency` 卡方独立性检验 (干预分组 × 已婚/无学位); (4) TODO6 `statsmodels.api.OLS` 多元回归 `re78 ~ treat + re75 + re74 + age + educ + marr`。
- 识别策略: RCT 随机分配保证 unconfoundedness; OLS 协变量调整缩减方差 (CUPED-adjacent); Welch t 检验放松等方差假设; 卡方检验诊断分组-特征独立性 (检测基线不平衡)。

**Results (预期/已得核心发现)**
- TODO4 t 检验: treated vs control 在 re78 上的差异, p 值与 Cohen's d (效应量) -- notes.md 强调"p 值只告诉你有没有效果, 不告诉你效果多大", 故同时报告 d。
- TODO5 卡方检验: 干预分组与 marr/nodegree 的独立性, 检测 NSW 营销映射下的基线平衡性 (RCT 质量诊断)。
- TODO6 OLS: treat 系数 (控制 re75/re74/age/educ/marr 后的净效应) 与 TODO4 简单 t 检验的点估计对比, 标准误是否较 TODO4 缩小 (CUPED-adjacent variance reduction 验证)。
- TODO3 RFM: Champions/At-Risk 等 5 分群在 treated/control 的分布, 诊断"营销干预是否在不同客户价值层有异质效应"。

**Discussion (贡献边界 + 局限 + 未来工作)**
- 边界: NSW 营销映射是教学性映射, 非 445 真实营销样本; re78 作为"活动后消费"假设单调线性。
- 局限: (a) n=445 对小效应检测功效有限, CUPED 工程实现 (theta 估计、Y' 构造) 留待 Day 2/3; (b) 仅 OLS 协变量调整, 未做 propensity score matching (Dehejia-Wahba 1999) 或 DML (Day 3); (c) 卡方检验为边际独立性, 未做分层分析。
- 未来工作: Day 2 BG/NBD CLV 预测 + CUPED 工程实现; Day 3 MMM 预算优化 + DML 异质处理效应; 技能3 合成控制/增量建模。

---

## reproducibility_checklist

NeurIPS / ACM 风格可复现清单 (>=6 项):

- [x] **Code (代码)**: 完整代码在 `solution.ipynb` (gated, 7 cells, 6 TODO 全部填好), 起始脚手架在 `starter.ipynb` (7 cells, 6 TODO 填空)。`verify_unit.py` 检查 scaffold=0 / TODO 残留=0。
- [x] **Data (数据)**: NSW 真实 RCT 数据集, 来源 `causaldata` 库 (PyPI: https://pypi.org/project/causaldata/, MIT License), 原始数据见 LaLonde (1986) AER。字段营销映射见 notes.md "营销映射"表。数据可发现/可访问/可互操作/可重用 (FAIR) -- `causaldata` 库一键加载, 无需手动下载。
- [x] **Seeds (随机种子)**: 涉及随机过程 (如 RFM K-Means 聚类, TODO3) 时使用 `random_state=42`; OLS/t 检验/卡方检验为确定性统计, 无随机性。
- [x] **Environment (环境)**: Python 3.x; 关键库: `pandas` (BSD, https://github.com/pandas-dev/pandas), `scipy` (BSD, https://github.com/scipy/scipy), `statsmodels` (BSD, https://github.com/statsmodels/statsmodels), `causaldata` (MIT, https://github.com/NickCH-K/causaldata)。版本固定见 `data/README.md`。
- [x] **Preregistration (预注册)**: 本单元假设 H1 (协变量调整缩减标准误, CUPED-adjacent) / H2 (点估计方向一致幅度不同) 在 notes.md "上机任务" 与 "CUPED" 节显式声明, 可作为 OSF 预注册 hypothesis 锚点 (OSF DOI 待提交时分配)。
- [x] **FAIR (数据治理)**: NSW 数据通过 `causaldata` 库满足 FAIR 原则 -- Findable (PyPI/GitHub 索引), Accessible (MIT License, 一键 `import causaldata`), Interoperable (pandas DataFrame 标准格式), Reusable (含 LaLonde 1986 / Dehejia-Wahba 1999 原始文献溯源)。
- [x] **Provenance (溯源)**: `reading.md` §3 记录 NSW 数据完整溯源链 (LaLonde 1986 AER -> Dehejia-Wahba 1999 子样本 -> Cunningham Mixtape -> `causaldata` 库); `data/README.md` 记录本地数据获取与字段映射。

---

## research_to_practice

本研究工件的"研究->实践"翻译路径如下：

1. **HBS Working Paper -> HBR Article**: 将 NSW 营销映射的 OLS vs t 检验对比 (TODO4 vs TODO6) 撰写为 HBS Working Paper "When Covariate Adjustment Matters in Marketing A/B Tests: A CUPED-Adjacent View from NSW Data", 再压缩为 HBR Article "Don't Trust the Simple t-Test: Why Marketers Should Control Pre-Treatment Covariates"。核心论点: notes.md 已强调"统计显著≠商业显著", 本研究给出可操作方法 (协变量调整) 缩小标准误、检测小效应 (1-3% 提升)。
2. **MIT Sloan Teaching Case**: 基于 TODO3 RFM 五分群在 treated/control 的分布, 撰写 MIT Sloan 教学案例 "RFM Heterogeneous Treatment Effects: Which Customer Segment Responds to the Promotion?" 主角为某 CPG 公司 CMO, 决策点是"是否对 Champions 与 At-Risk 投放同一促销"。
3. **企业白皮书**: 将四层框架 (描述/诊断/预测/处方) + NSW 真实数据上机流程打包为 McKinsey QuantumBlack 风格企业白皮书 "From Reports to Diagnostics: The First Two Layers of Marketing Analytics Maturity", 对应 notes.md "售前洞察" (诊断客户在四层框架中的当前位置)。
4. **咨询交付物**: 转化为 Imperial MSc BA 风格 8 周咨询项目原型 (见 `industry.md` consulting_project), 用 pandas/scipy/statsmodels 在客户真实交易数据上复现 TODO1-6 流程, 交付漏斗仪表盘 + RFM 分群策略 + 协变量调整 ATE 报告。

> 研究产出遵循 IMRaD (Introduction/Methods/Results/Discussion) 结构 + DSR (Hevner Design Science Research) 范式 + OSF 预注册 + FAIR 数据原则 + NeurIPS/ACM 可复现清单。本工件为 AI 原生化商业博士选修 E2 Day 1 的可发表单元, 与 Day 2 (CLV 预测) / Day 3 (MMM 优化) 形成研究产出链。
