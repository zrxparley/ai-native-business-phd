#!/usr/bin/env python3
"""v11.0 全景验证: 跑所有 day-* 目录 × 5 验证器 (v5+v6+v7+v9+v11) = 19/19.
用法: python3 v11_panorama.py
"""
import os, sys, subprocess

TM_DIR = "/Users/aha.gare.mbp/WorkBuddy/20260504101638/teaching-materials"
VER_DIR = os.path.dirname(os.path.abspath(__file__))
VERIFIERS = [
    (os.path.join(VER_DIR, "verify_unit.py"), "v5(1-7)"),
    (os.path.join(VER_DIR, "verify_v6_unit.py"), "v6(8-12)"),
    (os.path.join(VER_DIR, "verify_v7_unit.py"), "v7(13-15)"),
    (os.path.join(VER_DIR, "verify_v9_unit.py"), "v9(16-17)"),
    (os.path.join(VER_DIR, "verify_v11_unit.py"), "v11(18-19)"),
]
SKIP_DIRS = {"_frontier_corpus", "_from_scratch_map", "_shared", "frontier-deep-dives", "_verifiers"}


def find_units():
    units = []
    for mod in sorted(os.listdir(TM_DIR)):
        modp = os.path.join(TM_DIR, mod)
        if not os.path.isdir(modp) or mod.startswith("_") or mod in SKIP_DIRS:
            continue
        for day in sorted(os.listdir(modp)):
            dayp = os.path.join(modp, day)
            if os.path.isdir(dayp) and day.startswith("day-"):
                units.append(dayp)
    return units


def run_verifier(verifier, unit):
    try:
        r = subprocess.run(["python3", verifier, unit], capture_output=True, text=True, timeout=30)
        return r.returncode == 0
    except Exception as e:
        return False


def main():
    units = find_units()
    print(f"发现 {len(units)} 个单元")
    total = 0; full_19 = 0; partial = 0; no_v11 = 0
    no_v11_list = []
    for u in units:
        total += 1
        results = [run_verifier(v[0], u) for v in VERIFIERS]
        all_ok = all(results)
        v11_pass = results[4] if len(results) > 4 else False
        if all_ok:
            full_19 += 1
        elif v11_pass:
            partial += 1
        else:
            no_v11 += 1
            no_v11_list.append(os.path.relpath(u, TM_DIR))
    print("=" * 70)
    print(f"TOTAL: {total} | v11 19/19: {full_19} | PARTIAL: {partial} | NO-V11: {no_v11}")
    if no_v11_list:
        print(f"NO-V11 单元 ({len(no_v11_list)}):")
        for x in no_v11_list[:30]:
            print(f"  {x}")
        if len(no_v11_list) > 30:
            print(f"  ...还有 {len(no_v11_list)-30} 个")
    print("=" * 70)
    print(f"结果: {'v11.0 全景收敛 58/58 19/19' if full_19 == total and total > 0 else '需修复'}")
    sys.exit(0 if full_19 == total and total > 0 else 1)


if __name__ == "__main__":
    main()
