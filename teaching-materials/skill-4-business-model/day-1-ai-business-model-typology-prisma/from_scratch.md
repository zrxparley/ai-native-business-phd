# from_scratch.md · AI工程从零构建层 (v11.0)

> **单元**：技能4 AI驱动商业模式创新 · Day 1 AI商业模式类型学 + PRISMA文献综述
> **scratch 哲学**：不调 arxiv/pandas/sklearn，手写 PRISMA 四阶段筛选流水线 + 主动学习不确定性采样，从 PRISMA 单调过滤链 + 熵采样公式直译到 numpy。

## scratch_topic

本单元 from-scratch 主题：**手写 PRISMA 四阶段筛选流水线 + 主动学习（Active Learning）不确定性采样排序**。对应 rohitg00 P5 Information Retrieval（检索筛选）+ P18 Ethics（模型卡透明度）。notes.md/starter.ipynb 用 `arxiv` 包查 arXiv API + `pandas` 去重筛选 + `sklearn.LogisticRegression` 做 ASReview 主动学习排序，本层把"去重->筛选->主动学习排序"三步全部去库化：纯 numpy 手写 logistic 回归梯度下降 + 熵不确定性采样，让"PRISMA 为什么单调缩减""ASReview 为什么选 p≈0.5 的论文"两个问题在白板级代码中显形。

## core_algorithm

PRISMA 系统文献综述是一条单调缩减的过滤链。给定检索结果集 $P$（$n_{\text{id}}$ 篇），经四阶段过滤后纳入 $n_{\text{incl}}$ 篇：

$$n_{\text{incl}} \le n_{\text{scr}} \le n_{\text{dedup}} \le n_{\text{id}}$$

每阶段是一个过滤函数 $F$：去重阶段 $F_{\text{dedup}}(P) = \{p \in P \mid \text{key}(p) \text{ 唯一}\}$（按标题归一化键去重）；筛选阶段 $F_{\text{scr}}(P) = \{p \in P \mid \text{year}(p) \ge 2023 \wedge \text{hasAI}(p) \wedge \text{hasBiz}(p)\}$（年份+关键词双条件）。单调性来自 $F$ 的幂等收缩性质--每阶段只移除不新增，$|F(P)| \le |P|$ 恒成立。

主动学习（ASReview 核心）用**不确定性采样**加速筛选。在种子集 $S$ 上训练 logistic 分类器，对未标注池 $U$ 按预测熵排序，优先标注最不确定的论文：

$$x^* = \arg\max_{x \in U} H(p_\theta(y=1|x)), \quad H(p) = -p\log p - (1-p)\log(1-p)$$

其中 $p_\theta(y=1|x) = \sigma(w^Tx) = \frac{1}{1+e^{-w^Tx}}$，熵最大值 $\log 2 \approx 0.693$ 在 $p=0.5$（决策边界附近）取得。logistic 回归用梯度下降训练，损失梯度为：

$$\nabla_w \mathcal{L} = \frac{1}{n}\sum_{i=1}^{n}(\sigma(w^Tx_i) - y_i)\,x_i, \quad w \leftarrow w - \eta\,\nabla_w \mathcal{L}$$

直觉：种子集标注了少量相关/不相关论文后，分类器对剩余论文预测相关性概率 $p$；$p \approx 0.5$ 的论文"分类器最没把握"，标注它信息增益最大--这是 ASReview 比人工全读快 10x 的数学根源。

## code_artifact

```python
import numpy as np
import math

def prisma_filter(papers, year_min=2023):
    ai_kw = ['ai','llm','machine learning','neural','gpt','transformer','agent']
    biz_kw = ['business','market','commerce','pricing','revenue','platform','strategy']
    seen, dedup = set(), []
    for t, y, a in papers:
        k = ' '.join(t.lower().split())
        if k not in seen:
            seen.add(k); dedup.append((t, y, a))
    scr = [(t,y,a) for t,y,a in dedup if y >= year_min
           and any(k in (t+' '+a).lower() for k in ai_kw)
           and any(k in (t+' '+a).lower() for k in biz_kw)]
    return len(papers), len(dedup), len(scr), scr

def active_learn_rank(X, seed_idx, seed_y, n_query=5, lr=0.1, ep=200):
    w = np.zeros(X.shape[1])
    Xs, ys = X[seed_idx], np.array(seed_y, dtype=float)
    for _ in range(ep):
        p = 1.0/(1.0+np.exp(-(Xs @ w)))
        w -= lr * Xs.T @ (p - ys) / len(ys)
    pool = np.array([i for i in range(len(X)) if i not in set(seed_idx)])
    pp = 1.0/(1.0+np.exp(-(X[pool] @ w)))
    ent = -pp*np.log(pp+1e-12) - (1-pp)*np.log(1-pp+1e-12)
    return pool[np.argsort(-ent)[:n_query]].tolist(), ent

# verification_property:
#   PRISMA counts monotone decrease: n_id >= n_dedup >= n_screen;
#   active learning queries the n_query highest-entropy unlabeled points;
#   entropy <= log(2) (max at p=0.5)
if __name__ == "__main__":
    papers = [("AI Business Model Survey", 2024, "llm business pricing"),
              ("AI Business Model Survey", 2024, "dup"),
              ("Cooking Recipes Guide", 2020, "food cooking"),
              ("LLM Platform Strategy", 2024, "ai platform revenue")]
    n_id, n_dd, n_sc, _ = prisma_filter(papers)
    assert n_id >= n_dd >= n_sc, "PRISMA counts must monotone decrease"
    assert n_dd == 3 and n_sc == 2, f"dedup={n_dd} scr={n_sc}"
    X = np.array([[0.1,0.9],[0.8,0.2],[0.5,0.5],[0.3,0.7]])
    q, ent = active_learn_rank(X, [0,1], [0,1], n_query=2)
    assert len(q) == 2, "must query exactly n_query"
    assert all(e <= math.log(2)+1e-6 for e in ent), "entropy <= log(2)"
```

**verification_property**: PRISMA 计数单调递减（`n_id >= n_dedup >= n_screen`）；主动学习返回熵最大的 `n_query` 个未标注样本索引；每个样本的预测熵 $H(p) \le \log 2$（最大值在 $p=0.5$ 取得）。

## connection_to_unit

1. **pandas vs 手写集合**：starter.ipynb TODO2 用 `df.drop_duplicates(subset='title_lower')` 一行去重，from-scratch 版用 `set()` + 标题归一化 `' '.join(t.lower().split())` 手写--让"去重=按规范化键去重"这个操作在纯 Python 数据结构中可见，不被 pandas 的向量化抽象遮蔽。
2. **sklearn vs 手写 logistic**：practice.md D3（ASReview 主动学习）用 `sklearn.LogisticRegression.fit/predict_proba`，from-scratch 版手写梯度下降 `w -= lr * Xs.T @ (p - ys) / len(ys)`--让"主动学习排序"的分类器训练过程完全透明，能逐行审计权重更新，理解 ASReview 的"种子集->分类器->熵排序"三步链条。
3. **检索抽象层级**：notes.md 用 `arxiv.Search(query=...)` 调真实 arXiv API，from-scratch 版把检索阶段抽象为输入 `papers` 列表（元组），聚焦 PRISMA 的"去重->筛选->排序"后三阶段--这是 ASReview 论文中最核心的算法部分，arxiv 包只是数据获取层。
4. **PRISMA 流程图的数字来源**：notes.md 用 matplotlib 画 PRISMA 流程图（160->96->30->30），from-scratch 版的 `prisma_filter` 返回值 `(n_id, n_dedup, n_scr, scr)` 就是流程图四个节点的真实计数--让"流程图数字怎么来的"可追溯到每一行过滤逻辑。

## deep_dive_links

- [P5/14 Information Retrieval Search - rohitg00](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/05-nlp-foundations-to-advanced/14-information-retrieval-search/README.md) - 信息检索：PRISMA 的检索+筛选阶段的算法基础（相关性排序、召回率/精确率），本单元 from-scratch PRISMA 流水线的理论锚点
- [P18/26 Model System Dataset Cards - rohitg00](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/18-ethics-safety-alignment/26-model-system-dataset-cards/README.md) - 模型卡与透明度：PRISMA 的"质量评估"阶段要求系统化记录筛选标准，与模型卡的透明度原则同构

## exercises

1. 在本单元 `starter.ipynb` TODO2/TODO3（pandas 去重+筛选）运行后，用上面的 `prisma_filter` 在同一份论文数据上手动执行 PRISMA 四步，对比 pandas 版与 from-scratch 版的计数（应完全一致），解释差异来源（提示：pandas 的 `str.lower()` 与手写 `.lower()` 在 Unicode 边界行为可能不同）。
2. 将 `active_learn_rank` 的种子集从 2 个扩展到 5 个（3 相关/2 不相关），在 `practice.md` D3 的 ASReview 模拟场景中，对比 from-scratch logistic 与 sklearn `LogisticRegression` 的 `predict_proba` 排序差异。观察种子集偏置（全正相关）如何导致熵采样失效。
3. 为 `prisma_filter` 添加第四阶段"质量评估"：对筛选后的论文按摘要长度+引用关键词数打分，取 top-k 纳入。对应 notes.md PRISMA Step 3（质量评估），观察 k 的选择如何影响最终纳入集。
4. TODO: 在 `practice.md` 的 D2 drill（PRISMA 流程执行）中，为本 from-scratch 实现添加"PRISMA 流程图文本输出"（ASCII art 打印 `n_id -> n_dedup -> n_scr -> n_incl`），替代 matplotlib 可视化。这是 starter.ipynb TODO6 的 from-scratch 版本，让流程图不依赖 matplotlib 也能输出。
