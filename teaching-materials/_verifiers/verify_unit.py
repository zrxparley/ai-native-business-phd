#!/usr/bin/env python3
"""Loop Engineering 验证脚本(通用版):对任意 Day 目录检查 7 条验收标准。
处理 list/string 两种 source 格式。涵盖所有技能的前沿关键词。
用法: python3 verify_unit.py <day_dir>
重要:此为通用脚本,请勿覆盖。如需自检请写到 /tmp/verify_unit_<your_day>.py
"""
import json, re, os, sys

def check(D):
    def read(p):
        fp = os.path.join(D, p)
        return open(fp, encoding="utf-8").read() if os.path.exists(fp) else ""
    def nb(p):
        fp = os.path.join(D, p)
        return json.load(open(fp, encoding="utf-8")) if os.path.exists(fp) else {"cells": []}
    def src(c):
        x = c["source"]
        return "".join(x) if isinstance(x, list) else x
    R = []
    n = read("notes.md")
    obj_count = len(re.findall(r"^\d+\.\s", n, re.M))
    c1 = ("学习目标" in n) and obj_count >= 3 and len(n) > 1500
    R.append(("1. notes.md: 学习目标(>=3)+理论+真实数据指针", c1, f"目标条目={obj_count}, 长度={len(n)}"))
    d_rd = read("data/README.md")
    urls_d = re.findall(r"https?://[^\s)]+", d_rd)
    c2 = len(urls_d) >= 2 and ("真实" in d_rd or "real" in d_rd.lower())
    R.append(("2. data/README.md: 真实数据集+>=2来源链接", c2, f"URL数={len(urls_d)}"))
    s = nb("starter.ipynb"); scode = [c for c in s["cells"] if c["cell_type"] == "code"]
    scaffold = sum(1 for c in scode if "你的代码" in src(c))
    c3 = scaffold >= 5
    R.append(("3. starter.ipynb: >=5个TODO填空脚手架", c3, f"你的代码块={scaffold}, code cells={len(scode)}"))
    sol = nb("solution.ipynb"); solcode = [c for c in sol["cells"] if c["cell_type"] == "code"]
    sol_scaffold = sum(1 for c in solcode if "你的代码" in src(c))
    sol_todo = sum(1 for c in solcode if "= None  # TODO" in src(c) or "# TODO: 替换" in src(c))
    c4 = (sol_scaffold == 0) and (sol_todo == 0) and len(solcode) == len(scode) and len(solcode) > 0
    R.append(("4. solution.ipynb: 完整无scaffold+结构对应", c4, f"scaffold={sol_scaffold}, TODO残留={sol_todo}, sol cells={len(solcode)}/starter={len(scode)}"))
    c5 = os.path.exists(os.path.join(D, "starter.ipynb")) and os.path.getsize(os.path.join(D, "starter.ipynb")) > 1000
    R.append(("5. Notebook化: 独立.ipynb", c5, f"starter={os.path.getsize(os.path.join(D,'starter.ipynb')) if os.path.exists(os.path.join(D,'starter.ipynb')) else 0}B"))
    r = read("reading.md"); rurls = re.findall(r"https?://[^\s)]+", r)
    c6 = len(rurls) >= 3
    R.append(("6. reading.md: >=3深链", c6, f"URL数={len(rurls)}"))
    c7 = any(k in n for k in ["LLM-as-a-judge","CUPED","DML","双重机器学习","NOTEARS","Uplift","增量建模","MAB","贝叶斯","合成控制","因果森林","Neural","deepeval","MCP","A2A","vLLM","computer use","计算机使用","garak","PyRIT","红队","推理成本","投机解码","MoE","AgentBench","LangSmith","Trajectory","DeepSeek","RAGAS","LangGraph","ReAct","Plan-Execute","天道推演","多Agent仿真","多模态","对比学习","CLIP","BLIP","LLaVA","表示工程","Representation Engineering","GraphRAG","知识图谱","Two-Tower","sentence-transformers","Neo4j","DSR","可复现研究","APA","IMRaD","arxiv","贝叶斯统计","可复现","OSF","preregistration","数据治理","概率编程","PyMC","pandas","numpy","scipy","statsmodels","SQL","Apache Arrow"])
    R.append(("7. 2026前沿点", c7, f"命中={c7}"))
    return R

if __name__ == "__main__":
    d = sys.argv[1]
    R = check(d)
    print("=" * 70)
    print(f"LOOP ENGINEERING 验证: {d}")
    print("=" * 70)
    allok = True
    for name, ok, detail in R:
        if not ok: allok = False
        print(f"{'PASS' if ok else 'FAIL'}  {name}\n         {detail}")
    print("=" * 70)
    print(f"结果: {'全部7条通过 - 收敛' if allok else '有失败，需修复'}")
    sys.exit(0 if allok else 1)
