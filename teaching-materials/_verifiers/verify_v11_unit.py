#!/usr/bin/env python3
"""Loop Engineering v11.0 验证脚本: 检查AI工程从零构建层新增 2 条标准 (18-19)。
v5.0 的 1-7 (verify_unit.py) + v6.0 的 8-12 (verify_v6_unit.py) + v7.0 的 13-15 (verify_v7_unit.py)
+ v9.0 的 16-17 (verify_v9_unit.py) 绝不覆盖。
一个单元 v11.0 收敛 = 前 17 条全通过 + 本脚本全通过 (18-19) = 19/19。

用法: python3 verify_v11_unit.py <day_dir>

v11.0 新增标准:
  18. from_scratch.md: AI工程从零构建 (scratch_topic + core_algorithm含数学公式≥150字
      + code_artifact含python代码块且ast.parse语法验证通过+imports⊆白名单+verification_property
      + connection_to_unit≥3 delta + deep_dive_links含rohitg00链接 + exercises≥3且≥1绑定TODO)
  19. notes.md v11.0关键词: 命中从零构建关键词 (>=4)

反幻觉: rohitg00 GitHub blob URL 检查格式(regex)不检查可达性。代码 ast.parse 静态验证不执行。
反停滞: 不 pip install / 不执行代码 / 不联网。
"""
import re, os, sys, ast

ALLOWED_IMPORTS = {"numpy", "math", "random", "collections", "re", "itertools",
                   "functools", "operator", "typing", "abc", "dataclasses"}
FORBIDDEN_IMPORTS = {"torch", "transformers", "jax", "langchain", "langgraph",
                     "tensorflow", "sklearn", "pandas", "crewai", "autogen",
                     "openai", "anthropic", "sentence_transformers"}


def read(p):
    return open(p, encoding="utf-8").read() if os.path.exists(p) else ""


def section_body(text, headers):
    """提取某个 ## 节的正文 (到下一个 ## 为止, 不把 ### / #### 当边界)."""
    lines = text.split("\n")
    capturing = False
    body = []
    for ln in lines:
        stripped = ln.strip()
        if stripped.startswith("## ") and not stripped.startswith("###"):
            h = stripped.lower()
            if any(hd in h for hd in headers):
                capturing = True
                continue
            elif capturing:
                break
        elif capturing:
            body.append(ln)
    return "\n".join(body)


def extract_python_blocks(text):
    return re.findall(r'```python\n(.*?)```', text, re.DOTALL)


def check_code_blocks(blocks):
    """对每个 python 代码块做 ast.parse 语法验证 + imports 白名单检查. 不执行."""
    if not blocks:
        return False, "no_python_blocks"
    for i, b in enumerate(blocks):
        try:
            tree = ast.parse(b)
        except SyntaxError as e:
            return False, f"block{i}_syntax_error: {e.msg}(line {e.lineno})"
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                for alias in node.names:
                    root = alias.name.split(".")[0].lower()
                    if root in FORBIDDEN_IMPORTS:
                        return False, f"block{i}_forbidden_import: {alias.name}"
                    if root not in ALLOWED_IMPORTS:
                        return False, f"block{i}_non_whitelisted_import: {alias.name}"
            elif isinstance(node, ast.ImportFrom):
                if node.module:
                    root = node.module.split(".")[0].lower()
                    if root in FORBIDDEN_IMPORTS:
                        return False, f"block{i}_forbidden_import: {node.module}"
                    if root not in ALLOWED_IMPORTS:
                        return False, f"block{i}_non_whitelisted_import: {node.module}"
    return True, f"all_{len(blocks)}_blocks_ok"


def check(D):
    R = []
    f = read(os.path.join(D, "from_scratch.md"))

    # ---- 18. from_scratch.md ----
    has_topic = ("scratch_topic" in f.lower() or "从零构建" in f or "手写实现" in f
                 or "手写" in f or "from scratch" in f.lower() or "从零" in f)

    # core_algorithm: 含数学公式 + ≥150字
    ca_body = section_body(f, ["core_algorithm", "核心算法", "算法推导", "数学推导", "算法"])
    has_math = ("$$" in ca_body or re.search(r'(?<!\$)\$[^\s$][^$]*\$', ca_body) is not None
                or "公式" in ca_body or "推导" in ca_body or "derivation" in ca_body.lower()
                or "softmax" in ca_body.lower() or "梯度" in ca_body)
    has_ca_len = len(ca_body.strip()) >= 150

    # code_artifact: python代码块 + ast.parse + imports白名单 + verification_property
    blocks = extract_python_blocks(f)
    n_blocks = len(blocks)
    code_ok, code_detail = check_code_blocks(blocks)
    has_vp = ("verification_property" in f.lower() or "验证属性" in f
              or "不变量" in f or "期望输出" in f or "expected" in f.lower()
              or "shape" in f.lower())

    # connection_to_unit: ≥3 delta
    ctu_body = section_body(f, ["connection_to_unit", "与单元", "单元连接", "对比", "连接"])
    n_delta = len(re.findall(r'^\s*\d+\.', ctu_body, re.MULTILINE))
    has_delta_kw = ("对比" in ctu_body or "delta" in ctu_body.lower() or "vs" in ctu_body.lower()
                    or "库" in ctu_body or "solution" in ctu_body.lower())
    has_conn = n_delta >= 3 or (has_delta_kw and len(ctu_body.strip()) >= 120)

    # deep_dive_links: rohitg00 链接 ≥1
    rohitg_links = re.findall(r'github\.com/rohitg00/ai-engineering-from-scratch', f, re.IGNORECASE)
    has_links = len(rohitg_links) >= 1

    # exercises: ≥3 编号 + ≥1 绑定 TODO
    ex_body = section_body(f, ["exercise", "练习", "习题", "作业"])
    n_ex = len(re.findall(r'^\s*\d+\.', ex_body, re.MULTILINE))
    has_todo_bind = ("starter.ipynb" in ex_body or "practice.md" in ex_body
                     or "TODO" in ex_body or "todo" in ex_body.lower()
                     or "既有" in ex_body or "本单元" in ex_body)
    has_ex = n_ex >= 3 and has_todo_bind

    c18 = (has_topic and has_math and has_ca_len and n_blocks >= 1 and code_ok and has_vp
           and has_conn and has_links and has_ex)
    R.append(("18. from_scratch.md: 从零构建(topic+core_algorithm含公式≥150字+code_artifact ast.parse验证+imports白名单+verification_property+connection≥3+rohitg00链接+exercises≥3绑TODO)",
              c18, f"topic={has_topic}, math={has_math}(ca_len={len(ca_body.strip())}), "
                   f"blocks={n_blocks}(code={code_ok}:{code_detail[:50]}), vp={has_vp}, "
                   f"conn={has_conn}(n_delta={n_delta}), links={len(rohitg_links)}, "
                   f"ex={has_ex}(n_ex={n_ex},todo_bind={has_todo_bind}), len={len(f)}"))

    # ---- 19. notes.md v11.0 关键词 ----
    n = read(os.path.join(D, "notes.md"))
    kws = ["从零构建", "from scratch", "手写实现", "手写", "工程底座", "numpy", "数学推导",
           "rohitg00", "AI工程", "verification_property", "验证属性", "scratch_topic",
           "code_artifact", "core_algorithm", "从零", "工程从零", "ai-engineering-from-scratch"]
    hits = sum(1 for k in kws if k.lower() in n.lower())
    c19 = hits >= 4
    R.append(("19. notes.md: v11.0从零构建关键词(>=4命中)", c19, f"hits={hits}"))
    return R


if __name__ == "__main__":
    d = sys.argv[1]
    R = check(d)
    print("=" * 70)
    print(f"LOOP ENGINEERING v11.0 验证: {d}")
    print("=" * 70)
    allok = True
    for name, ok, detail in R:
        if not ok: allok = False
        print(f"{'PASS' if ok else 'FAIL'}  {name}\n         {detail}")
    print("=" * 70)
    print(f"结果: {'v11.0层全部2条通过 (18-19) - 收敛' if allok else '有失败，需修复'}")
    print("注: v5.0(1-7) verify_unit.py; v6.0(8-12) verify_v6_unit.py; v7.0(13-15) verify_v7_unit.py; v9.0(16-17) verify_v9_unit.py")
    sys.exit(0 if allok else 1)
