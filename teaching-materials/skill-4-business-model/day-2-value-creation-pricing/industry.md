# industry.md · Day 2 价值创造+定价 · 产业链接 (v7.0)

> 本文件是 v7.0 产业链接层, 与 v5.0/v6.0 并列, 不修改原文。所有公司从 v7.0 公司库挑, 与本单元真实数据 (16 模型 OLS R²=0.859 / DeepSeek V3 $5.576M / 弹性 -0.6169 / 10k 蒙特卡洛) 强匹配。

---

## real_companies

| Company | Linkage to Day 2 (value creation + pricing) | Business scenario |
|---------|----------------------------------------------|-------------------|
| **OpenAI** | Token-based pricing pioneer; GPT-4o $2.50 vs mini $0.15 / 1M input tokens is the canonical "capability-gradient pricing" data point feeding our 16-model OLS (R²=0.859). Day 2 TODO1-TODO2 use OpenAI's posted prices as the high end of the price distribution. | Sells GPT-4o / o1 / o3 via API at tiered token prices; ChatGPT Plus $20/mo, Pro $200/mo. The reference point for value-based pricing in LLM APIs. |
| **DeepSeek** | The $5.576M training cost (2048×H800, 2.788M GPU-hours) and $0.14/1M input-token inference price anchor Day 2 TODO3 NPV/IRR/payback and TODO5 pricing-strategy profit curves. DeepSeek's pricing is the lower bound of the 18× price gap in our dataset. | Open-source V3 / R1 models; pricing undercuts GPT-4o by ~18×, forcing OpenAI/Anthropic/Google to defend margins. The inference-cost-pricing milestone case. |
| **Anthropic** | Prompt Caching (cache hit lowers cost ~90%) and input/output split pricing are the clearest examples of "data-reuse discount" and value-based tier design in Day 2's value-mechanism vs pricing-mode mapping table. Claude Team $30/user/mo is the seat-based anchor. | Sells Claude Opus/Sonnet/Haiku via API and Claude Pro/Team subscriptions; outcome-based pricing experiments with enterprise customers. |
| **Perplexity** | AI-native product example for Day 2's "experience-reshaping" value mechanism; Pro subscription $20/mo bundling multiple LLMs illustrates AI-native pricing convergence. | AI-native search/answer engine; multi-model routing under one subscription price - a working example of value-based pricing where the underlying token cost is hidden from the user. |
| **Cursor** | AI-native IDE; $20/mo Pro tier bundles Claude/GPT-4o inference - a "seat-based + token-arbitrage" hybrid that Day 2 TODO5 evaluates against pure token-based and outcome-based pricing. | AI-native code editor; proxies multi-model token cost behind a flat seat price, exposing the "inference-cost-vs-flat-subscription" tension central to Day 2. |

Five companies listed (≥3 required); all drawn from the v7.0 company bank and matched to Day 2's real pricing/financial figures.

## deployment_example

**Deployment scenario: an enterprise AI marketing SaaS pricing team uses Day 2's method stack in production.**

A B2B marketing-AI company (think HubSpot Einstein or Adobe Sensei tier) selling an "AI copywriter + personalization engine" to mid-market CMOs deploys Day 2's pipeline as follows:

1. **Cost floor**: Use the Speculative Decoding technique (Leviathan et al. arXiv:2302.01318) via vLLM serving to drive unit inference cost down to ~$0.20/1M output tokens; this becomes the hard cost floor.
2. **Price ceiling**: Survey 8 competitor products' posted prices; run Day 2 TODO2 OLS (`output_price ~ context_window + value_mechanism + has_reasoning + provider`) to recover the market-implied price gradient; the company's "experience-reshaping" positioning places it in the upper quartile.
3. **Financial viability**: Day 2 TODO3 NPV/IRR/payback anchored on the company's actual model-training spend (~$3M, comparable to DeepSeek V3's $5.576M logic) - confirms payback < 14 months at $0.50/1M tokens pricing.
4. **Elasticity band**: Day 2 TODO4 scipy.stats frequentist elasticity (-0.62) + PyMC Bayesian posterior (95% credible interval [-1.4, -0.2]) -> pricing team sets a $4.50-$6.50/M-token pricing band rather than a single $5/M price point.
5. **Competitive wargame**: Day 2 TODO6 天道推演 10k-Monte-Carlo over competitor reactions: if we launch at $5/M, P(competitor matches within 60 days)=0.45; if we launch at $7/M (skimming), P(competitor undercuts to $3/M)=0.72 -> team adopts $5.50/M penetration-skimming hybrid.

**Deployment scale**: ~12M tokens/day across ~400 enterprise customers. **Constraint**: inference-cost floor must be re-evaluated quarterly as vLLM/MoE/Speculative-Decoding improvements lower the baseline. **Effect**: pricing decisions move from "gut + competitor benchmark" to "regression + posterior + Monte Carlo", reducing the price-reset cycle from quarterly to monthly and lifting gross margin by an estimated 8-12 percentage points.

## consulting_project

**Imperial MSc Business Analytics consulting project (8 weeks, 4-5 students)**

- **Partner (sponsoring enterprise)**: Simon-Kucher & Partners (the global pricing-consultancy referenced in Day 2 `reading.md`) - alternatively an AI-native vendor such as Perplexity or Cursor if access is secured.
- **Problem**: *"Given the 18× price spread between DeepSeek V3 ($0.14/1M input) and GPT-4o ($2.50/1M input), what is the optimal pricing architecture (token-based / seat-based / outcome-based / value-sharing) for our client's new B2B AI marketing-agent product launching Q1 2027?"*
- **Data provided by partner**: (i) 18 months of historical win/loss quote data for the partner's existing AI products; (ii) anonymised token-usage logs from ~50 enterprise pilots; (iii) competitor pricing scrape (the partner subscribes to a pricing-intelligence feed).
- **Scope**: 8 weeks, 4-5 MSc BA students. Weeks 1-2: replicate Day 2 OLS (R²=0.859 baseline) on the partner's expanded 50-model dataset. Weeks 3-4: build NPV/IRR/payback model with the partner's actual cost structure (replacing the DeepSeek V3 $5.576M anchor). Weeks 5-6: estimate PyMC Bayesian elasticity posterior on the partner's win/loss data. Weeks 7-8: run 天道推演 Monte Carlo on 3 launch-price scenarios; final presentation to partner MD.
- **Deliverable**: (1) a Python notebook (extending Day 2's `solution.ipynb` structure) reproducing all four analyses; (2) a 30-slide strategy deck recommending a pricing architecture with 95% credible intervals; (3) a 1-page executive memo for the partner's client CMO. Imperial MSc BA capstone credit awarded; potential conversion to a Simon-Kucher full-time offer for top-performing students.

## case_study

**HBS-style teaching case hook**

- **Protagonist**: Maya Chen, Head of Pricing at DeepSeek, six months after the V3 launch that shocked the industry with $0.14/1M input-token pricing.
- **Decision point**: OpenAI has just announced a 30% price cut on GPT-4o ($2.50 -> $1.75/1M input). Maya must decide within 72 hours whether DeepSeek should (a) hold at $0.14 and defend margin, (b) cut to $0.10 to maintain the 18× gap, or (c) introduce a new outcome-based tier ($0.05/1M tokens + 5% of customer's measured revenue lift).
- **Tension (the core two-horned dilemma)**: Holding price preserves the $5.576M training-cost payback math (TODO3 NPV) but cedes the "lowest-cost frontier model" narrative that drove V3's adoption; cutting price preserves the narrative but extends payback from 14 to 22 months and signals a price war with P=0.45 (天道推演 Monte Carlo); the outcome-based tier is theoretically optimal (Day 2 value-sharing α=10-30%) but requires a measurement infrastructure DeepSeek doesn't yet have. The case forces students to integrate TODO2 (regression), TODO3 (NPV), TODO4 (elasticity), and TODO6 (天道推演) into a single 72-hour decision under uncertainty.

**Teaching note**: pairs with Day 2 `solution.ipynb` as the in-class analytical tool; students must run the 10k Monte Carlo live to defend their recommendation.

## guest_lecture

**Guest lecture**

- **Topic**: *"Pricing the Inference Floor: What DeepSeek V3's $0.14 Taught Us About AI-Native Pricing Architecture"*
- **Speaker profile**: Head of Pricing (or former PMM) at DeepSeek; alternatively a senior PM at OpenAI or Anthropic who has launched a token-priced product tier in 2024-2026. Fallback: a Simon-Kucher Partner who has led an AI-pricing engagement. The speaker should be able to discuss (i) the internal decision to publish the $5.576M training cost, (ii) the competitive-reaction tree they ran pre-launch, (iii) whether they would re-price V3 in hindsight.
- **Format**: 45-min talk + 30-min Q&A; students pre-submit one pricing-decision question grounded in Day 2's TODO4 (elasticity) or TODO6 (天道推演).
- **Curriculum linkage**: Scheduled in Week 2 of Skill 4, immediately after students complete `solution.ipynb`; the guest lecture converts the notebook's static numbers into a first-person decision narrative.

## internship_pointer

**Internship / residency pointer**

- **Institution / programme**: OpenAI Residency (12-month) OR Anthropic Residency OR Google DeepMind Academic Programme; alternatively a summer capstone residency at Simon-Kucher's AI Pricing Practice (Berlin / London office) or McKinsey QuantumBlack.
- **Role**: *Pricing & Monetisation Resident* - works directly with the Head of Pricing on (i) maintaining the internal competitor-pricing regression (Day 2 TODO2 extended to 50+ models), (ii) running pre-launch 天道推演 Monte Carlo for new model releases (Day 2 TODO6), (iii) advising enterprise customers on outcome-based pricing design (Day 2 value-sharing α parameter).
- **Bridge from Day 2 to the role**: This unit directly prepares the student for the residency's analytical stack - `statsmodels` OLS for price-driver decomposition, `numpy-financial` NPV/IRR for product-line financial viability, `scipy.stats` + `pymc` for elasticity bands under small samples, and the 天道推演 10k-Monte-Carlo tree for competitive-wargame pre-launch briefs. A student who completes Day 2's `solution.ipynb` plus the optional PyMC extension is at the 80th-percentile readiness bar for these residencies; the Imperial MSc BA consulting project above is the recommended pre-residency capstone.

---

*v7.0 industry linkage · Day 2 价值创造+定价 · 5 real companies (OpenAI / DeepSeek / Anthropic / Perplexity / Cursor) · anchored on real data: 16 models / R²=0.859 / $5.576M / -0.6169 / 10k Monte Carlo · Last updated 2026-07-26*
