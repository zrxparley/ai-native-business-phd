# from_scratch.md · AI工程从零构建层 (v11.0)

> **单元**：选修E3 LLM导论 · Day 2 LLM应用工程（⭐旗舰模块 Day 2）
> **scratch 哲学**：不调 langchain VectorStore / sentence-transformers，手写 BM25 概率检索 + top-k RAG 上下文拼接，从 Robertson 2-泊松模型直译到 numpy。

## scratch_topic

本单元 from-scratch 主题：**手写 BM25 检索 + top-k RAG 上下文拼接**。对应 rohitg00 P11/06 RAG。notes.md/starter.ipynb TODO4 用 numpy TF-IDF + 余弦相似度做营销知识库检索（向量空间模型），本层进一步：BM25 是 TF-IDF 的概率检索变体，带文档长度归一化（k1/b 参数），是 Elasticsearch/Lucene 的默认排序算法。手写 BM25 让"为什么长文档需要长度惩罚""k1 如何控制词频饱和""IDF 的概率含义"三个问题在白板级代码中显形。延伸练习覆盖 BPE tokenization 片段（不调 transformers）。

## core_algorithm

BM25（Okapi BM25, Robertson 1994/2009）源自概率检索框架的 2-泊松模型：一个词在相关文档中的出现频率服从泊松分布，在不相关文档中服从另一个泊松分布。给定查询 $Q = (q_1, \dots, q_n)$ 和文档 $D$，BM25 评分函数为：

$$\text{BM25}(D, Q) = \sum_{i=1}^{n} \text{IDF}(q_i) \cdot \frac{f(q_i, D) \cdot (k_1 + 1)}{f(q_i, D) + k_1 \cdot \left(1 - b + b \cdot \frac{|D|}{\text{avgdl}}\right)}$$

其中 $f(q_i, D)$ 是词 $q_i$ 在文档 $D$ 中的词频，$|D|$ 是文档长度，$\text{avgdl}$ 是语料库平均文档长度，$k_1 \in [1.2, 2.0]$ 控制词频饱和速度，$b \in [0, 1]$ 控制文档长度归一化强度（经验值 $b=0.75$）。

**IDF 的概率推导**：BM25 的 IDF 来自贝叶斯后验比的对数：

$$\text{IDF}(q_i) = \ln\left(\frac{N - n(q_i) + 0.5}{n(q_i) + 0.5} + 1\right)$$

其中 $N$ 是文档总数，$n(q_i)$ 是含 $q_i$ 的文档数。当 $n(q_i) \to N$（常见词出现在所有文档中），$\text{IDF} \to \ln(1) = 0$，该词对排序无贡献--这正是"停用词无信息量"的数学根源。$+0.5$ 是拉普拉斯平滑，避免零除；外层 $+1$ 保证 IDF 非负（Robertson 后期修正）。

**词频饱和**：当 $f \to \infty$，分子分母同趋于 $f \cdot (k_1+1) / f = k_1+1$，分数趋于 $\frac{k_1+1}{1} \cdot \frac{f}{f} = k_1+1$。即无论词频多大，单项贡献上界为 $\text{IDF} \cdot (k_1+1)$--这修正了 raw TF 的线性增长缺陷（一个词出现 100 次不比 1 次相关 100 倍）。

**文档长度惩罚**：当 $|D| > \text{avgdl}$，分母中 $b \cdot |D|/\text{avgdl} > b$，分母增大，分数减小--长文档被惩罚。$b=0$ 时无惩罚（退化为无长度归一化），$b=1$ 时完全线性归一化。这是 RAG 检索中"长文档不天然更相关"的数学保障。

## code_artifact

```python
import numpy as np
import math
from collections import Counter, defaultdict

def tokenize(text):
    return list(text.replace(" ", ""))

class BM25:
    def __init__(self, docs, k1=1.2, b=0.75):
        self.docs = [tokenize(d) for d in docs]
        self.k1, self.b = k1, b
        self.N = len(self.docs)
        self.avgdl = sum(len(d) for d in self.docs) / max(self.N, 1)
        self.df = defaultdict(int)
        for d in self.docs:
            for t in set(d):
                self.df[t] += 1

    def _idf(self, term):
        n = self.df.get(term, 0)
        return math.log((self.N - n + 0.5) / (n + 0.5) + 1)

    def score(self, query, doc_idx):
        d = self.docs[doc_idx]; dl = len(d); tf = Counter(d); s = 0.0
        for q in tokenize(query):
            f = tf.get(q, 0); idf = self._idf(q)
            num = f * (self.k1 + 1)
            den = f + self.k1 * (1 - self.b + self.b * dl / self.avgdl)
            s += idf * (num / den if den > 0 else 0)
        return s

    def search(self, query, top_k=3):
        scores = np.array([self.score(query, i) for i in range(self.N)])
        idx = np.argsort(-scores)[:top_k]
        return [(int(i), float(scores[i])) for i in idx]

# verification_property: BM25 score 0 when f=0; tf saturation bounded by idf*(k1+1);
#   long docs penalized by b>0; top-1 for "续航" query must be the doc containing 续航
if __name__ == "__main__":
    docs = ["智能手表7天续航低功耗芯片", "手表100运动模式跑步游泳", "心率血氧监测24小时守护"]
    bm = BM25(docs)
    res = bm.search("手表续航", top_k=2)
    assert res[0][0] == 0, "doc0 should rank first for 续航"
    assert all(s >= 0 for _, s in res), "scores non-negative"
    # saturation: query term appearing once vs absent -> bounded single-term contribution
    print(f"scale avgdl={bm.avgdl:.1f}, top-1: doc{res[0][0]} score={res[0][1]:.4f}")
```

**verification_property**：BM25 单项贡献当 $f=0$ 时为 0（词不在文档中不贡献）；词频饱和上界为 $\text{IDF} \cdot (k_1+1)$（无论 $f$ 多大）；长文档被 $b>0$ 惩罚（$|D|>\text{avgdl}$ 时分数减小）；top-1 召回必须命中含查询关键词的文档。

## connection_to_unit

1. **检索模型对比**：starter.ipynb TODO4 用 numpy TF-IDF + 余弦相似度（向量空间模型，tf 线性增长），from-scratch 用 BM25（概率检索模型，tf 有饱和上界）。TF-IDF 的词频是线性的（出现 100 次 = 100 倍相关），BM25 的 $k_1$ 把词频压缩到饱和上界 $\text{IDF}\cdot(k_1+1)$--更符合"一个词重复出现边际效益递减"的经验，这是 Elasticsearch/Lucene 选 BM25 而非 raw TF-IDF 的根本原因。
2. **文档长度归一化对比**：starter.ipynb 的 TF-IDF 用 `TF = 词频/文档长度` 做简单线性归一化，from-scratch 的 BM25 用 $b \cdot |D|/\text{avgdl}$ 做可调长度惩罚（$b=0.75$ 经验最优）。前者是硬归一化（完全消除长度影响），后者是软归一化（$b$ 可调，$b=0$ 无惩罚）。BM25 的软归一化保留了长文档的信息量优势，同时抑制"长文档天然得分高"的偏差。
3. **相似度方向性**：starter.ipynb 的余弦相似度是对称的（$\cos(q,d) = \cos(d,q)$），from-scratch 的 BM25 是非对称评分函数（query→doc 评分，doc 不能反向检索 query）。检索本质是"短 query 检索长 doc"，对称度量（余弦）把 query 和 doc 放在同一空间，而 BM25 用 query 词逐个评分 doc--后者更贴合检索的不对称性。
4. **IDF 公式差异**：starter.ipynb 用 `IDF = log((N+1)/(df+1)) + 1`（平滑向量空间版），from-scratch 用 BM25 的 `IDF = log((N-n+0.5)/(n+0.5)+1)`（概率版，来自 Robertson 2-泊松模型）。后者当 $n \to N$ 时 IDF→0（常见词零信息量），前者仅渐近趋向 1--BM25 的 IDF 更激进地惩罚高频词，这与营销 RAG 中"产品名是高频词不应主导排序"的需求一致。

## deep_dive_links

- [P11/06 RAG - rohitg00](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/11-llm-engineering/06-rag/README.md) - RAG 基础，本 from-scratch BM25 检索的理论锚点（检索→上下文拼接→生成全链路）
- [P11/09 Function Calling - rohitg00](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/11-llm-engineering/09-function-calling/README.md) - 函数调用，RAG 提供知识 + Function Calling 提供操作能力的工具分发层
- [P11/14 Model Context Protocol - rohitg00](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/11-llm-engineering/14-model-context-protocol/README.md) - MCP 工具协议标准化，Function Calling 的可移植层

## exercises

1. 在本单元 `starter.ipynb` TODO4（numpy TF-IDF + 余弦相似度 RAG 检索）运行后，用上面的 `BM25` 类对**同一个 knowledge_base** 和**同一个 query "手表续航多久"** 做检索，对比两者的 top-3 召回顺序。提示：固定 docs 列表，分别打印 TF-IDF top-3 和 BM25 top-3，观察排序差异（长文档 doc5 品牌故事在 BM25 下应因长度惩罚排名更低）。
2. 实现 **BPE tokenization 片段**（不调 transformers/tiktoken）：给定一个 mini 语料 `["低功耗芯片", "低功耗模式", "芯片架构"]`，从字符级 vocab 开始，迭代找最高频相邻 token 对合并，运行 3 轮 merge，输出合并后的 vocab 和 tokenized 结果。对应 notes.md TODO1 的 tiktoken BPE 原理--从零理解 `o200k_base` 为什么比 `cl100k_base` 对中文更省 token。
3. 构造 **k1/b 参数扫描实验**：固定 knowledge_base，令 $k_1 \in \{0.5, 1.2, 2.0, 5.0\}$、$b \in \{0, 0.25, 0.5, 0.75, 1.0\}$，对 query "手表续航" 打印 5×4 的 BM25 score 矩阵。观察：$k_1 \to \infty$ 时退化为 raw TF-IDF（无饱和），$b=0$ 时长文档无惩罚。这是 practice.md drill D2 "分块策略 worked example"的 from-scratch 延伸--理解 $b$ 如何影响长文档（按段落切分 vs 按句号切分）的召回偏好。
4. TODO: 在 `practice.md` drill D3 的 RAGAS 评估练习中，用 BM25 的 `search()` 替换 numpy TF-IDF 检索，重跑 faithfulness/context_recall，对比 BM25 vs TF-IDF 的 RAGAS 指标差异。这是 starter.ipynb TODO4+TODO6 的 from-scratch 串联练习。
