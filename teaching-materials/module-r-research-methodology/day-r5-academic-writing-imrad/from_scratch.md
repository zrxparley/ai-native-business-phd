# from_scratch.md · AI工程从零构建层 (v11.0)

> **单元**：模块R · R5 学术写作 IMRaD
> **scratch 哲学**：不调 arxiv/statsmodels，手写 IMRaD 章节依赖 DAG 完整性校验 + BibTeX 引文图谱解析，从拓扑序与引用接地约束直译到 numpy/re。

## scratch_topic

本单元 from-scratch 主题：**手写 IMRaD 结构完整性校验器（章节依赖 DAG 拓扑序 + 支撑完备性 + 引文接地）+ BibTeX 引文图谱解析**。对应 rohitg00 P14 Agent Observability Platforms（结构化记录的可审计性）。notes.md/starter.ipynb 用 arxiv 包下论文、用关键词字典做句级 IMRaD 分类、用 statsmodels 跑统计，本层把"IMRaD 结构是否自洽"拆开：从 IMRaD 四节的依赖 DAG 与引文接地约束出发，手写 numpy/re 实现拓扑校验 + BibTeX 解析 + 引文密度，让"论文结构合理"不再是 LLM-as-judge 的主观评分，而是可逐行审计的图论约束。

## core_algorithm

IMRaD（Introduction-Methods-Results-Discussion）是一棵**修辞性依赖 DAG** $G=(V,E)$，节点 $V$ 是修辞单元（claim/method/result/interpretation），边 $(u,v) \in E$ 表示"$v$ 依赖 $u$"。一篇自洽的 IMRaD 论文必须满足三条约束：

**(C1) 拓扑无环**：存在拓扑序 $\sigma$ 使 $(u,v)\in E \Rightarrow \sigma(u)<\sigma(v)$。IMRaD 的隐式依赖为 $I \to M$（方法回应引言问题）、$M \to R$（结果来自方法）、$R \to D$、$I \to D$（讨论回扣引言），故合法序为 $I,M,R,D$；若 Discussion 出现指向 Methods 的反向边则成环，违反 IMRaD 逻辑。

**(C2) 支撑完备性**：每个非引言节点 $v$ 的入度满足节类约束。形式化：

$$\forall v \in R:\; \exists (u,v)\in E,\; u \in M \quad;\quad \forall v \in D:\; \exists (u_1,v)\in E,\; u_1\in R \;\wedge\; \exists (u_2,v)\in E,\; u_2\in I$$

即每个 Result 必须链接到一个 Method，每个 Discussion 必须同时链接到一个 Result 和一个 Introduction claim--否则为"孤儿结果"或"悬空讨论"。

**(C3) 引文接地**：每个 Introduction claim $v$ 的引用入度 $\text{indeg}_{cite}(v) \geq 1$（至少引一篇参考文献）。**引用密度** $\rho(s) = \frac{1}{|C_s|}\sum_{c\in C_s}|\text{cites}(c)|$ 度量各节证据接地强度；$\rho(I)$ 低 = 引言缺乏文献支撑，$\rho(M)$ 高 = 方法节引用密集（正常）。BibTeX 解析用正则 `@type{key, fields}` 抽取 entries 构建引文图谱 $C \subseteq \text{claims}\times\text{refs}$。关键洞察：starter.ipynb TODO1 的"句级 IMRaD 关键词分类"只能判单句归属，无法检测跨节依赖断裂；本层把 IMRaD 升级为可计算的 DAG 完整性问题，"孤儿结果"与"悬空讨论"是关键词分类永远抓不到的结构缺陷。

## code_artifact

```python
import re
import numpy as np

IMRAD_DEPS = {"I": [], "M": ["I"], "R": ["M"], "D": ["R", "I"]}

def topo_valid(order):
    seen = set()
    for s in order:
        for dep in IMRAD_DEPS.get(s, []):
            if dep not in seen:
                return False, f"{s} before dep {dep}"
        seen.add(s)
    return True, "ok"

def integrity(claims_by_sec):
    issues = []
    for v in claims_by_sec.get("R", []):
        if not v.get("method_link"):
            issues.append(f"orphan result: {v['text'][:25]}")
    for v in claims_by_sec.get("D", []):
        if not v.get("result_link") or not v.get("intro_link"):
            issues.append(f"dangling discussion: {v['text'][:25]}")
    for v in claims_by_sec.get("I", []):
        if not v.get("cites"):
            issues.append(f"ungrounded intro claim: {v['text'][:25]}")
    return issues

def bibtex_parse(text):
    entries = {}
    for m in re.finditer(r'@(\w+)\s*\{\s*([^,\s]+)\s*,(.*?)\n\}', text, re.DOTALL):
        kind, key, body = m.group(1).lower(), m.group(2), m.group(3)
        fields = dict(re.findall(r'(\w+)\s*=\s*\{([^}]*)\}', body))
        entries[key] = {"type": kind, **fields}
    return entries

def citation_density(claims_by_sec):
    out = {}
    for sec, claims in claims_by_sec.items():
        n = len(claims)
        out[sec] = (sum(len(c.get("cites", [])) for c in claims) / n) if n > 0 else 0.0
    return out

if __name__ == "__main__":
    bib = bibtex_parse("@article{he2004,\n title={Design Science},\n year={2004}\n}")
    assert "he2004" in bib and bib["he2004"]["year"] == "2004"
    assert topo_valid(["I", "M", "R", "D"])[0] and not topo_valid(["I", "R", "M", "D"])[0]
    claims = {"I": [{"text": "DSR is key", "cites": ["he2004"]}],
              "M": [{"text": "use pydantic"}],
              "R": [{"text": "ATE=1794", "method_link": "M"}],
              "D": [{"text": "confirms", "result_link": "R", "intro_link": "I"}]}
    assert integrity(claims) == [], "well-formed IMRaD must have no issues"
    bad = {"I": [{"text": "claim", "cites": []}], "R": [{"text": "res"}],
           "D": [{"text": "disc"}]}
    assert len(integrity(bad)) >= 3, "must flag ungrounded+orphan+dangling"
```

**verification_property**: 合法 IMRaD（claims 有 cites/method_link/result_link/intro_link）`integrity` 返回空列表；残缺 IMRaD（intro 无 cite、result 无 method_link、discussion 无 link）`integrity` 返回 $\geq 3$ 条问题。拓扑序 `I,M,R,D` 合法、`I,R,M,D` 非法（R 在 M 前）。BibTeX 解析提取 `he2004` 的 year=2004。

## connection_to_unit

1. **库 vs 手写的结构校验**：starter.ipynb TODO1 用关键词字典做"句级 IMRaD 分类"（单句归属），from-scratch 版 `integrity` 做"跨节依赖完整性校验"（DAG 约束）--前者抓"这句话属于哪节"，后者抓"这节是否逻辑依赖于它该依赖的节"，是 TODO1 无法覆盖的结构层。
2. **LLM-as-judge 的可计算前置**：TODO6 用 LLM-as-judge 评 IMRaD 各节质量（主观评分），from-scratch 版 `integrity` 提供客观的结构性前置检查--"孤儿结果"是任何 LLM 评审都应先 flag 的硬约束，不应依赖主观判断。
3. **BibTeX vs 手工引文**：solution.ipynb 假设引文已结构化，from-scratch 版 `bibtex_parse` 用 `re` 从原始 `.bib` 文本抽取 entries，暴露了"引文图谱的原始数据是半结构化文本"这一被库隐藏的现实。
4. **citation_density 的方法论意义**：notes.md 把"引言漏斗结构"描述为写作技巧，from-scratch 版 `citation_density` 把它量化为 $\rho(I)$--引言节引用密度低 = 漏斗"窄口"无文献支撑，是可计算的写作缺陷信号。

## deep_dive_links

- [P14/24 Agent Observability Platforms - rohitg00](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/14-agent-engineering/24-agent-observability-platforms/README.md) - 结构化记录与可审计性：IMRaD DAG 完整性校验与 agent trace 结构化记录同构，都是"结构化产物的可审计验证"

## exercises

1. 在本单元 `starter.ipynb` TODO1（句级 IMRaD 分类）完成后，把分类结果按节聚合成 `claims_by_sec`，喂入 `integrity` 校验。对比 TODO1 的"句数占比统计"与 from-scratch 的"依赖完整性"：哪篇论文句数占比正常但 `integrity` 报孤儿结果？
2. 扩展 `IMRAD_DEPS` 加入 `C`（Conclusion）节，依赖 `[D]`；再为 TODO3 的 Introduction 漏斗结构（5 层：背景->问题->缺口->贡献->结构）建模为 Introduction 内部子 DAG，校验"缺口层必须 cites $\geq 1$ 且贡献层必须 link 到方法预告"。
3. 实现引文图谱分析：用 `bibtex_parse` 解析一份真实 `.bib` 文件（≥10 entries），构建 claim$\to$ref 二部图，计算每个 reference 的 in-degree（被多少 claim 引用），输出" foundational refs"（in-degree top-3）。讨论 in-degree 集中度与论文"理论锚点清晰度"的关系。
4. TODO: 在 `practice.md` 的 IMRaD drill 中，用 `integrity` 作为 TODO6 LLM-as-judge checklist 的客观前置过滤器--先跑 `integrity`，结构性问题修复后再跑 LLM 主观评分。验证"结构校验 + LLM 评审"分层是否减少 LLM 误判。
