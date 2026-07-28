# from_scratch.md · AI工程从零构建层 (v11.0)

> **单元**：模块R · R4 系统综述 + PRISMA 2020
> **scratch 哲学**：不调 pandas/sklearn，手写 PRISMA 4 阶段漏斗状态机 + ASReview 主动学习余弦排序器，从 recall/precision 权衡与种子扩样直译到 numpy。

## scratch_topic

本单元 from-scratch 主题：**手写 PRISMA 2020 四阶段筛选漏斗 + ASReview 主动学习排序（种子扩样余弦排序 + recall/precision 度量）**。对应 rohitg00 P5 Information Retrieval Search（信息检索排序）+ P18 Data Provenance Training Governance（数据溯源）。notes.md/starter.ipynb 用 pandas 去重、用 sklearn 算 Cohen's $\kappa$、调 ASReview 模拟主动学习，本层把"为什么主动学习能用更少标注达更高 recall"拆开：从 recall/precision 的定义与种子扩样的余弦排序出发，手写 numpy 实现 PRISMA 状态机 + ASReview 排序器，让"主动学习省力"不再是库的黑箱，而是可逐行审计的检索过程。

## core_algorithm

PRISMA 2020 定义四阶段 attrition 漏斗：Identification（$n_1$ 条记录识别）-> 去重后 $n_2$ -> Screening（$n_3$ 筛选）-> Eligibility（$n_4$ 全文评估）-> Included（$n_5$ 纳入）。设第 $i$ 条记录真实相关性 $y_i \in \{0,1\}$，筛选者决策 $\hat y_i \in \{0,1\}$。筛选阶段的 **recall（灵敏度）** 与 **precision** 为：

$$\text{recall} = \frac{TP}{TP+FN} = \frac{|\{i: \hat y_i=1, y_i=1\}|}{|\{i: y_i=1\}|}, \quad \text{precision} = \frac{TP}{TP+FP} = \frac{|\{i: \hat y_i=1, y_i=1\}|}{|\{i: \hat y_i=1\}|}$$

低 recall = 漏掉相关文献（筛选的 Type II 错误，PRISMA 最致命）；低 precision = 浪费全文评估 effort。ASReview 主动学习 mitigate recall 损失：给定种子标注集 $L^+$（已知 included），对未标注集 $U$ 用相关性函数 $f(u) = \max_{l \in L^+} \cos(\mathbf{tf}_u, \mathbf{tf}_l)$ 排序，其中 $\mathbf{tf}_u$ 是归一化词频向量、$\cos(\mathbf{a},\mathbf{b}) = \mathbf{a}\cdot\mathbf{b}/(\|\mathbf{a}\|\|\mathbf{b}\|)$。reviewer 按高 $f$ 优先标注，每轮将新标 included 加入 $L^+$ 重排--种子不断"吸附"语义近邻。关键洞察：朴素随机标注需标 $O(n)$ 才达 recall$\to 1$；主动学习因 included 文档在词频空间聚簇，标 $O(\log n)$ 轮即可捕获大多数--这是 ASReview "省 80% 标注"的几何解释。PRISMA 报告要求同时给 $n_k$ 计数与筛选一致性（Cohen's $\kappa$），本层补 recall/precision 这两个被 notes.md 弱化的检索指标。

## code_artifact

```python
import numpy as np

VOCAB = {"ai":0, "marketing":1, "agent":2, "causal":3, "llm":4, "rag":5, "eval":6}

def tf_norm(tokens, v=VOCAB):
    x = np.zeros(len(v))
    for t in tokens:
        if t in v: x[v[t]] += 1
    n = np.linalg.norm(x)
    return x / n if n > 0 else x

def cosine(a, b):
    d = np.linalg.norm(a) * np.linalg.norm(b)
    return float(np.dot(a, b) / d) if d > 0 else 0.0

def prisma_funnel(records, dedup_fn, screen_fn, elig_fn):
    dedup = [r for r in records if dedup_fn(r)]
    screened = [r for r in dedup if screen_fn(r)]
    eligible = [r for r in screened if elig_fn(r)]
    return {"id": len(records), "dedup": len(dedup),
            "screen": len(screened), "elig": len(eligible), "incl": len(eligible)}

def asreview_rank(docs, seed_idx, top_k=2, v=VOCAB):
    seeds = [tf_norm(docs[i], v) for i in seed_idx]
    labeled = set(seed_idx); order = list(seed_idx)
    rem = [i for i in range(len(docs)) if i not in labeled]
    while rem:
        sc = sorted(((max(cosine(tf_norm(docs[i], v), s) for s in seeds), i)
                     for i in rem), reverse=True)
        for _, i in sc[:top_k]:
            order.append(i); labeled.add(i)
            seeds.append(tf_norm(docs[i], v)); rem.remove(i)
        if len(sc) < top_k: break
    return order

def recall_precision(retrieved, truth):
    tp = sum(1 for i in retrieved if truth[i] == 1)
    fn = sum(1 for i, t in enumerate(truth) if t == 1 and i not in retrieved)
    fp = sum(1 for i in retrieved if truth[i] == 0)
    r = tp / (tp + fn) if (tp + fn) > 0 else 0.0
    p = tp / (tp + fp) if (tp + fp) > 0 else 0.0
    return r, p

if __name__ == "__main__":
    docs = [["ai","marketing","agent"], ["ai","llm","eval"], ["causal","marketing"],
            ["ai","marketing","rag"], ["causal","agent"], ["marketing","rag","eval"]]
    truth = [1, 0, 1, 1, 0, 0]
    order = asreview_rank(docs, seed_idx=[0], top_k=2)
    r, p = recall_precision(order[:4], truth)
    assert r >= 0.66, f"recall {r:.2f} must recover >=2/3 included via seed expansion"
    assert p > 0.0
```

**verification_property**: 种子扩样排序后 recall $\geq 0.66$（构造数据 3 个 included，种子 1 个，扩样 4 步内应找回 $\geq 2$ 个 included）；precision $> 0$（至少命中 1 个真 included）。当种子从 `[0]` 改为不相关文档时 recall 下降，证明 ASReview 的省力性依赖于"种子语义聚簇"假设。

## connection_to_unit

1. **库 vs 手写的检索逻辑**：starter.ipynb TODO5-6 调 ASReview 模拟主动学习（黑箱模型），from-scratch 版 `asreview_rank` 用余弦相似度显式实现种子扩样，暴露了 ASReview "为什么省力"--included 文档在词频空间聚簇，排序器是几何近邻搜索。
2. **recall vs precision 的权衡**：solution.ipynb TODO3 用 sklearn Cohen's $\kappa$ 衡量筛选者一致性，但未报 recall/precision；from-scratch 版 `recall_precision` 补全了 PRISMA 报告缺失的检索指标--$\kappa$ 高不代表 recall 高（两个筛选者可能一致地漏掉文献）。
3. **PRISMA 计数的状态机化**：notes.md 把 PRISMA 四阶段描述为流程图，from-scratch 版 `prisma_funnel` 把它建模为可执行的 `id->dedup->screen->elig->incl` 状态机，每个 `*_fn` 是一个可审计的过滤谓词--这是 TODO2 去重、TODO3 筛选逻辑的统一抽象。
4. **vocab 的方法论暴露**：ASReview 内部用预训练 embedding，from-scratch 版 `VOCAB` 显式列 7 个词，迫使研究者回答"我的检索式覆盖了哪些概念"--这是 PRISMA Item 5（检索式可复现）的 from-scratch 验证。

## deep_dive_links

- [P5/14 Information Retrieval Search - rohitg00](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/05-nlp-foundations-to-advanced/14-information-retrieval-search/README.md) - 信息检索：余弦排序、recall/precision 权衡，ASReview 主动学习的检索理论锚点
- [P18/27 Data Provenance Training Governance - rohitg00](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/18-ethics-safety-alignment/27-data-provenance-training-governance/README.md) - 数据溯源：PRISMA Item 5 检索式可复现与文献来源溯源的方法论对照

## exercises

1. 在本单元 `starter.ipynb` TODO3（双盲筛选 + Cohen's $\kappa$）完成后，用上面的 `recall_precision` 在同一份筛选结果上计算 recall 与 precision。讨论"$\kappa$ 高但 recall 低"的场景--两个筛选者高度一致地漏掉了同一批相关文献，$\kappa$ 无法捕捉这一 PRISMA 致命缺陷。
2. 实现 ASReview 省力性量化：扫描 `top_k` 与种子数 `len(seed_idx)`，绘制"标注数 - recall"曲线。对比随机标注（`random.sample` 排序）与 `asreview_rank` 的曲线，量化"主动学习省 80% 标注"在 from-scratch 版的具体数字。
3. 将 `VOCAB` 从 7 词扩展到 TODO1 arXiv 检索式的全部关键词，重跑 `asreview_rank`，观察 recall 变化。讨论"vocab 覆盖不全导致语义近邻漏检"--这是 PRISMA Item 5 检索式敏感性的 from-scratch 验证。
4. TODO: 在 `practice.md` 的 PRISMA drill 中，用 `prisma_funnel` 替代手动计数，为 TODO2-4 的每个阶段添加 `*_fn` 谓词单元测试（输入构造 record，验证 stage 转移正确）。这是 PRISMA 流程图从"文档描述"升级为"可执行状态机"的 from-scratch 交付。
