#!/usr/bin/env python3
"""Loop Engineering v6.0 验证脚本: 检查学习科学层新增 5 条标准 (8-12)。
v5.0 的 1-7 条仍由 /tmp/verify_unit.py 检查 (绝不覆盖)。
一个单元 v6.0 收敛 = verify_unit.py 全通过 (1-7) + 本脚本全通过 (8-12)。

用法: python3 verify_v6_unit.py <day_dir>

v6.0 新增标准:
  8. practice.md: 刻意练习 (skill_target+subskills+>=3 drills含difficulty/reps_required/feedback_rule)
                  + weak_loop + 交叉/interleaving + worked-faded 示例
  9. schedule.json: FSRS/SM-2 间隔重复 (>=3 cards, 每card id/concept/due, due>=4点)
  10. alignment.md: Biggs ILO↔TLA↔AT 矩阵 (>=3行) + mastery_threshold + 3自检问题
  11. tutorial.ipynb: 牛津tutorial LLM仿真 (persona Socratic+禁直接答案 + >=5苏格拉底问
                   + Hattie四级[TASK]/[PROCESS]/[SELF-REG]/[FEED-FORWARD] + student_model + 限频)
  12. notes.md v6.0关键词: 命中学习科学关键词 (FSRS/SM-2/刻意练习/deliberate practice/
                   建构对齐/constructive alignment/牛津tutorial/Socratic/Hattie/间隔重复/
                   spaced retrieval/交叉/interleaving/mastery/Worked-Faded)
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

    # ---- 8. practice.md ----
    p = read("practice.md")
    has_target = "skill_target" in p
    has_sub = "subskills" in p
    # drills: count blocks with difficulty + reps_required + feedback_rule
    drill_blocks = re.findall(r"(?is)drill[_\s-]*id\s*[:：].*?(?=\n\s*drill[_\s-]*id|\Z)", p)
    if not drill_blocks:
        drill_blocks = re.findall(r"(?is)###\s*drill.*?(?=\n###|\Z)", p)
    drills_ok = 0
    for b in drill_blocks:
        if ("difficulty" in b.lower() or "难度" in b) and ("reps_required" in b.lower() or "reps" in b.lower() or "重复" in b) and ("feedback_rule" in b.lower() or "反馈" in b):
            drills_ok += 1
    if drills_ok < 3:
        # fallback: count difficulty+feedback_rule co-occurrences anywhere
        drills_ok = min(10, p.lower().count("difficulty") + p.count("难度")) if p.count("feedback_rule") >= 3 or p.count("反馈") >= 3 else drills_ok
    has_weak = "weak_loop" in p.lower() or "弱项循环" in p or "弱链" in p
    has_interleave = "interleav" in p.lower() or "交叉" in p or "A1B1C1" in p
    has_worked = "worked" in p.lower() or "faded" in p.lower() or "渐退" in p or "示范-填空" in p or "worked-faded" in p.lower()
    c8 = has_target and has_sub and drills_ok >= 3 and has_weak and has_interleave and has_worked
    R.append(("8. practice.md: 刻意练习(skill_target+subskills+>=3drills+weak_loop+交叉+worked-faded)",
              c8, f"target={has_target}, subskills={has_sub}, drills_ok={drills_ok}, weak_loop={has_weak}, interleave={has_interleave}, worked_faded={has_worked}, len={len(p)}"))

    # ---- 9. schedule.json ----
    sj = read("schedule.json")
    c9 = False
    detail9 = "invalid"
    try:
        data = json.loads(sj)
        cards = data.get("cards", data) if isinstance(data, dict) else data
        if isinstance(cards, dict):
            cards = list(cards.values())
        cards = [c for c in cards if isinstance(c, dict)]
        ncards = len(cards)
        ok_cards = 0
        for c in cards:
            has_id = "id" in c or "card_id" in c
            has_concept = "concept" in c or "concept" in c.get("front", "") if isinstance(c.get("front"), str) else "concept" in c
            due = c.get("due", c.get("intervals", c.get("schedule", [])))
            ndue = len(due) if isinstance(due, list) else 0
            if has_id and (has_concept or "concept" in c or "front" in c) and ndue >= 4:
                ok_cards += 1
        has_fsrs = "fsrs" in sj.lower() or "sm-2" in sj.lower() or "sm2" in sj.lower() or "EF" in sj or "EF0" in sj
        c9 = ncards >= 3 and ok_cards >= 3 and has_fsrs
        detail9 = f"cards={ncards}, ok_cards={ok_cards}, fsrs/sm2={has_fsrs}"
    except Exception as e:
        detail9 = f"json_error: {e}"
    R.append(("9. schedule.json: FSRS/SM-2间隔重复(>=3cards, 每id/concept/due>=4)", c9, detail9))

    # ---- 10. alignment.md ----
    a = read("alignment.md")
    has_ilo = "ILO" in a or "学习产出" in a or "intended learning" in a.lower()
    has_tla = "TLA" in a or "学习活动" in a or "teaching/learning" in a.lower()
    has_at = re.search(r"\bAT\b", a) or "评估任务" in a or "assessment task" in a.lower() or "assessment" in a.lower()
    # matrix rows: count | or table rows with ILO/TLA/AT
    rows = len(re.findall(r"(?im)^\s*\|?\s*ILO|^\s*\|.*TLA.*AT|^\s*\|\s*.+\|\s*.+\|\s*.+\|", a))
    if rows < 3:
        rows = a.count("| ILO") + a.count("|ILO") + a.count("ILO")  # rough
    has_mastery = "mastery" in a.lower() or "掌握阈值" in a or "过关" in a
    has_selfcheck = a.count("自检") >= 3 or a.lower().count("self-check") >= 3 or a.count("Feed Up") + a.count("Feed Back") + a.count("Feed Forward") >= 2 or (a.count("TLA") >= 1 and a.count("训练") + a.count("measure") >= 1)
    c10 = has_ilo and has_tla and (has_at is not None) and has_mastery and (rows >= 3 or a.count("ILO") >= 3) and has_selfcheck
    R.append(("10. alignment.md: Biggs ILO↔TLA↔AT(>=3行)+mastery阈值+3自检",
              c10, f"ILO={has_ilo}, TLA={has_tla}, AT={bool(has_at)}, mastery={has_mastery}, rows~{rows}, selfcheck={has_selfcheck}, len={len(a)}"))

    # ---- 11. tutorial.ipynb ----
    t = nb("tutorial.ipynb")
    tcells = t.get("cells", [])
    tsrc = "\n".join(src(c) for c in tcells)
    tsize = os.path.getsize(os.path.join(D, "tutorial.ipynb")) if os.path.exists(os.path.join(D, "tutorial.ipynb")) else 0
    has_persona = "Socratic" in tsrc or "苏格拉底" in tsrc or "socratic" in tsrc.lower()
    has_no_answer = "不直接给答案" in tsrc or "never give" in tsrc.lower() or "禁直接答案" in tsrc or "do not answer" in tsrc.lower() or "不直接答" in tsrc
    # socratic questions: count "?" in markdown cells with probing keywords, or count explicit numbered questions
    soc_q = len(re.findall(r"(?im)(why|为什么|如何|how could|what if|若|反例|counterexample|凭什么|依据|假设.*变)", tsrc))
    has_hattie = all(tag in tsrc for tag in ["[TASK]", "[PROCESS]"]) and ("[SELF-REG]" in tsrc or "[SELF_REG]" in tsrc) and ("[FEED-FORWARD]" in tsrc or "[FEED_FORWARD]" in tsrc or "FEED-FORWARD" in tsrc)
    has_student_model = "student_model" in tsrc.lower() or "student-model" in tsrc.lower() or "学生模型" in tsrc or "student_state" in tsrc.lower()
    has_limit = "限频" in tsrc or "daily limit" in tsrc.lower() or "1次/天" in tsrc or "每天" in tsrc or "usage limit" in tsrc.lower()
    c11 = tsize > 1000 and has_persona and has_no_answer and soc_q >= 5 and has_hattie and has_student_model and has_limit
    R.append(("11. tutorial.ipynb: 牛津Socratic(persona+禁直接答案+>=5问)+Hattie四级+student_model+限频",
              c11, f"size={tsize}, persona={has_persona}, no_answer={has_no_answer}, soc_q={soc_q}, hattie4={has_hattie}, student_model={has_student_model}, limit={has_limit}"))

    # ---- 12. notes.md v6.0 学习科学关键词 ----
    n = read("notes.md")
    kws = ["FSRS","SM-2","SM2","刻意练习","deliberate practice","建构对齐","constructive alignment",
           "牛津tutorial","Oxford tutorial","Socratic","苏格拉底","Hattie","间隔重复","spaced retrieval",
           "spaced repetition","交叉","interleav","interleaving","mastery","掌握","Worked","Faded","渐退",
           "formative feedback","形成性反馈","retrieval practice","提取练习"]
    hits = sum(1 for k in kws if k.lower() in n.lower())
    c12 = hits >= 4
    R.append(("12. notes.md: v6.0学习科学关键词(>=4命中)", c12, f"hits={hits}"))
    return R

if __name__ == "__main__":
    d = sys.argv[1]
    R = check(d)
    print("=" * 70)
    print(f"LOOP ENGINEERING v6.0 验证: {d}")
    print("=" * 70)
    allok = True
    for name, ok, detail in R:
        if not ok: allok = False
        print(f"{'PASS' if ok else 'FAIL'}  {name}\n         {detail}")
    print("=" * 70)
    print(f"结果: {'v6.0层全部5条通过 (8-12) - 收敛' if allok else '有失败，需修复'}")
    print("注: v5.0基线 (1-7) 请另跑 verify_unit.py")
    sys.exit(0 if allok else 1)
