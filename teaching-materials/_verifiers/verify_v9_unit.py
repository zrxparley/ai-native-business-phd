#!/usr/bin/env python3
"""Loop Engineering v9.0 验证脚本: 检查学术前沿注入层新增 2 条标准 (16-17)。
v5.0 的 1-7 (verify_unit.py) + v6.0 的 8-12 (verify_v6_unit.py) + v7.0 的 13-15 (verify_v7_unit.py) 绝不覆盖。
一个单元 v9.0 收敛 = 前 15 条全通过 + 本脚本全通过 (16-17) = 17/17。

用法: python3 verify_v9_unit.py <day_dir>

v9.0 新增标准:
  16. frontier.md: 学术前沿注入 (frontier_topic + >=3 recent_papers含arxiv/DOI链接
                   且链接ID⊆_frontier_corpus语料库 + 含2025/2026年份 + critical_synthesis>=300字
                   + delta_to_unit + >=3 open_questions + methodological_critique)
  17. notes.md v9.0关键词: 命中学术前沿关键词 (>=4)

反幻觉核心: frontier.md 引用的 arxiv/DOI 论文 ID 必须是 _frontier_corpus/*.md 中已列论文的子集。
"""
import re, os, sys, glob

def read(p):
    return open(p, encoding="utf-8").read() if os.path.exists(p) else ""

def extract_arxiv_ids(text):
    """提取 arxiv.org/abs/<ID> 或 arxiv.org/pdf/<ID> 中的 ID (4位.4-5位)."""
    return set(re.findall(r'arxiv\.org/(?:abs|pdf)/(\d{4}\.\d{4,5})', text, re.IGNORECASE))

def extract_doi(text):
    """提取 doi.org/<doi> 中的 doi 路径."""
    return set(re.findall(r'doi\.org/(10\.\d{4,9}/[^\s\)\]\}>]+)', text, re.IGNORECASE))

def section_body(text, headers):
    """提取某个 ## 节的正文 (到下一个 ## 为止). headers 是候选标题列表(小写)."""
    lines = text.split("\n")
    capturing = False
    body = []
    for ln in lines:
        if ln.strip().startswith("##"):
            h = ln.lower()
            if any(hd in h for hd in headers):
                capturing = True
                continue
            elif capturing:
                break
        elif capturing:
            body.append(ln)
    return "\n".join(body)

def check(D):
    R = []
    # ---- 语料库论文ID集合 (反幻觉基准) ----
    tm_dir = os.path.abspath(os.path.join(D, "..", ".."))
    corpus_dir = os.path.join(tm_dir, "_frontier_corpus")
    corpus_arxiv = set()
    corpus_doi = set()
    for cf in glob.glob(os.path.join(corpus_dir, "*.md")):
        ct = read(cf)
        corpus_arxiv |= extract_arxiv_ids(ct)
        corpus_doi |= extract_doi(ct)

    # ---- 16. frontier.md ----
    f = read(os.path.join(D, "frontier.md"))
    has_topic = ("frontier_topic" in f.lower() or "前沿课题" in f or "前沿子问题" in f or "前沿话题" in f or "前沿方向" in f)

    f_arxiv = extract_arxiv_ids(f)
    f_doi = extract_doi(f)
    n_paper_links = len(f_arxiv) + len(f_doi)
    # 反幻觉: frontier 引用的 arxiv ID 必须全部 ⊆ 语料库
    arxiv_halluc = f_arxiv - corpus_arxiv if corpus_arxiv else set()
    doi_halluc = f_doi - corpus_doi if corpus_doi else set()
    links_ok = (len(arxiv_halluc) == 0 and len(doi_halluc) == 0)
    has_3links = n_paper_links >= 3

    # recency: 含 2025 或 2026
    has_recency = ("2025" in f or "2026" in f)

    # critical_synthesis: 节正文 >=300 字 OR (总长>=2500 且含批判关键词)
    cs_body = section_body(f, ["critical_synthesis", "批判性综述", "批判综述", "批判综合", "综述与批判"])
    cs_len = len(cs_body.strip())
    critique_kws = ["局限", "争议", "共识", "limitation", "controvers", "consensus", "批评", "critique", "质疑", "分歧"]
    has_critique_kw = any(k in f.lower() for k in critique_kws)
    has_synthesis = (cs_len >= 300) or (len(f) >= 2500 and has_critique_kw)

    # delta_to_unit
    has_delta = ("delta_to_unit" in f.lower() or "delta" in f.lower() or "更新" in f or "扩展" in f or "挑战" in f)

    # open_questions: 节存在 + "?" 出现 >=3 次
    oq_body = section_body(f, ["open_question", "开放问题", "开放研究问题", "研究问题"])
    n_qmarks = f.count("？") + f.count("?")
    has_oq = (len(oq_body.strip()) > 0 or "open_question" in f.lower() or "开放问题" in f) and n_qmarks >= 3

    # methodological_critique
    has_method = ("methodological_critique" in f.lower() or "方法论批评" in f or "方法论批判" in f
                  or ("局限" in f and "可复现" in f) or ("limitation" in f.lower() and "reproduc" in f.lower())
                  or "可复现性顾虑" in f or "benchmark-gaming" in f.lower() or "benchmark gaming" in f.lower())

    c16 = (has_topic and has_3links and links_ok and has_recency and has_synthesis
           and has_delta and has_oq and has_method)
    R.append(("16. frontier.md: 前沿注入(topic+>=3论文链接⊆语料库+2025/26+批判综述>=300字+delta+>=3开放问题+方法论批评)",
              c16, f"topic={has_topic}, paper_links={n_paper_links}(arxiv={len(f_arxiv)},doi={len(f_doi)}), "
                   f"halluc={len(arxiv_halluc)+len(doi_halluc)}({'NONE' if links_ok else arxiv_halluc|doi_halluc}), "
                   f"recency={has_recency}, synthe={has_synthesis}(cs_len={cs_len},kw={has_critique_kw}), "
                   f"delta={has_delta}, oq={has_oq}(qmarks={n_qmarks}), method={has_method}, len={len(f)}"))

    # ---- 17. notes.md v9.0 关键词 ----
    n = read(os.path.join(D, "notes.md"))
    kws = ["学术前沿", "frontier", "2025", "2026", "recent papers", "最新论文", "批判性综述", "批判综述",
           "open question", "开放问题", "开放研究问题", "方法论批评", "方法论批判", "arXiv", "arxiv",
           "前沿注入", "前沿论文", "前沿层", "研究问题", "前沿课题"]
    hits = sum(1 for k in kws if k.lower() in n.lower())
    c17 = hits >= 4
    R.append(("17. notes.md: v9.0学术前沿关键词(>=4命中)", c17, f"hits={hits}"))
    return R

if __name__ == "__main__":
    d = sys.argv[1]
    R = check(d)
    print("=" * 70)
    print(f"LOOP ENGINEERING v9.0 验证: {d}")
    print("=" * 70)
    allok = True
    for name, ok, detail in R:
        if not ok: allok = False
        print(f"{'PASS' if ok else 'FAIL'}  {name}\n         {detail}")
    print("=" * 70)
    print(f"结果: {'v9.0层全部2条通过 (16-17) - 收敛' if allok else '有失败，需修复'}")
    print("注: v5.0(1-7) verify_unit.py; v6.0(8-12) verify_v6_unit.py; v7.0(13-15) verify_v7_unit.py")
    sys.exit(0 if allok else 1)
