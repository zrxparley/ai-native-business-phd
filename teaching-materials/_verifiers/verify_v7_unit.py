#!/usr/bin/env python3
"""Loop Engineering v7.0 验证脚本: 检查研究产出+产业链接层新增 3 条标准 (13-15)。
v5.0 的 1-7 条由 /tmp/verify_unit.py 检查; v6.0 的 8-12 条由 /tmp/verify_v6_unit.py 检查 (绝不覆盖)。
一个单元 v7.0 收敛 = verify_unit.py 全通过 (1-7) + verify_v6_unit.py 全通过 (8-12) + 本脚本全通过 (13-15) = 15/15。

用法: python3 verify_v7_unit.py <day_dir>

v7.0 新增标准:
  13. research.md: 研究产出 (research_question + contribution + linked_paper含arxiv/DOI/https
                   + imrad_outline + reproducibility_checklist>=4项 + research_to_practice)
  14. industry.md: 产业链接 (>=3 real_companies + deployment_example + consulting_project
                   (partner+problem+deliverable) + case_study + guest_lecture + internship_pointer)
  15. notes.md v7.0关键词: 命中研究产出/产业链接关键词 (>=4)
"""
import json, re, os, sys

def check(D):
    def read(p):
        fp = os.path.join(D, p)
        return open(fp, encoding="utf-8").read() if os.path.exists(fp) else ""
    R = []

    # ---- 13. research.md ----
    r = read("research.md")
    has_rq = "research_question" in r.lower() or "研究问题" in r
    has_contrib = "contribution" in r.lower() or "贡献" in r
    # linked_paper: must contain a real link (arxiv.org / doi.org / https)
    has_link = ("arxiv.org" in r.lower() or "doi.org" in r.lower() or "https://" in r.lower() or "http://" in r.lower())
    has_imrad = ("imrad" in r.lower() or ("introduction" in r.lower() and "method" in r.lower() and "result" in r.lower() and "discussion" in r.lower()) or ("引言" in r and "方法" in r and "结果" in r and "讨论" in r))
    # reproducibility checklist: count items
    repro_items = 0
    for kw in ["code", "代码", "data", "数据", "seed", "种子", "environment", "环境", "preregistration", "预注册", "FAIR", "osf"]:
        if kw.lower() in r.lower():
            repro_items += 1
    has_repro = repro_items >= 4
    has_rtp = "research_to_practice" in r.lower() or "research-to-practice" in r.lower() or "研究转实践" in r or "翻译为实践" in r or "实践工件" in r
    c13 = has_rq and has_contrib and has_link and has_imrad and has_repro and has_rtp
    R.append(("13. research.md: 研究产出(rq+contribution+linked_paper+IMRaD+repro>=4+rtp)",
              c13, f"rq={has_rq}, contribution={has_contrib}, link={has_link}, imrad={has_imrad}, repro_items={repro_items}, rtp={has_rtp}, len={len(r)}"))

    # ---- 14. industry.md ----
    i = read("industry.md")
    # real_companies: count table rows or capitalized company names from a known bank
    company_bank = ["Salesforce","HubSpot","Adobe","Klaviyo","Shopify","Meta","Google","Coca-Cola","Unilever","P&G","Sephora","Stitch Fix",
                    "Microsoft","Netflix","Uber","Amazon","Booking.com","Lyft","DoorDash","LinkedIn","Spotify","Apple",
                    "Sierra","Cognition","Devin","MultiOn","Adept","LangChain","CrewAI","LlamaIndex","AutoGPT",
                    "OpenAI","Anthropic","DeepMind","Llama","Mistral","Cohere","DeepSeek","Hugging Face","Together AI",
                    "Apollo","Conjecture","Scale AI","Replicate","AWS","Azure","Vertex AI",
                    "McKinsey","BCG","Bain","Deloitte","Accenture","IBM","SAP","Oracle",
                    "Burberry","Expedia","J&J","Johnson & Johnson","Walmart","Target","Tesco","Nike",
                    "Neo4j","Pinecone","Weaviate","NVIDIA","Perplexity","Cursor","Jasper","Midjourney","Replicate"]
    companies_found = set()
    for c in company_bank:
        if c.lower() in i.lower():
            companies_found.add(c)
    n_companies = len(companies_found)
    has_deployment = "deployment" in i.lower() or "部署" in i
    has_consulting = ("consulting" in i.lower() or "咨询" in i) and ("partner" in i.lower() or "赞助" in i or "problem" in i.lower() or "问题" in i) and ("deliverable" in i.lower() or "交付" in i or "deliver" in i.lower())
    has_case = "case_study" in i.lower() or "case study" in i.lower() or "教学案例" in i or "案例" in i
    has_guest = "guest_lecture" in i.lower() or "guest lecture" in i.lower() or "客座" in i or "客座讲座" in i
    has_internship = "internship" in i.lower() or "实习" in i or "residency" in i.lower() or "驻留" in i or "resident" in i.lower()
    c14 = n_companies >= 3 and has_deployment and has_consulting and has_case and has_guest and has_internship
    R.append(("14. industry.md: 产业链接(>=3公司+deployment+consulting+case+guest+internship)",
              c14, f"companies={n_companies}({','.join(sorted(companies_found)[:5])}), deployment={has_deployment}, consulting={has_consulting}, case={has_case}, guest={has_guest}, internship={has_internship}, len={len(i)}"))

    # ---- 15. notes.md v7.0 关键词 ----
    n = read("notes.md")
    kws = ["研究产出","research output","IMRaD","可复现","reproducibility","OSF","preregistration","预注册",
           "FAIR","contribution","贡献","产业链接","industry linkage","consulting","咨询","case study","案例",
           "guest lecture","客座","internship","实习","deployment","部署","linked_paper","arXiv","DSR","Hevner",
           "research-to-practice","NeurIPS","行动学习","action learning"]
    hits = sum(1 for k in kws if k.lower() in n.lower())
    c15 = hits >= 4
    R.append(("15. notes.md: v7.0研究产出/产业链接关键词(>=4命中)", c15, f"hits={hits}"))
    return R

if __name__ == "__main__":
    d = sys.argv[1]
    R = check(d)
    print("=" * 70)
    print(f"LOOP ENGINEERING v7.0 验证: {d}")
    print("=" * 70)
    allok = True
    for name, ok, detail in R:
        if not ok: allok = False
        print(f"{'PASS' if ok else 'FAIL'}  {name}\n         {detail}")
    print("=" * 70)
    print(f"结果: {'v7.0层全部3条通过 (13-15) - 收敛' if allok else '有失败，需修复'}")
    print("注: v5.0基线 (1-7) 请跑 verify_unit.py; v6.0层 (8-12) 请跑 verify_v6_unit.py")
    sys.exit(0 if allok else 1)
