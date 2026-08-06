#!/bin/bash
# E13 v6.1 + E15 推送脚本
# 在 macOS 终端中运行: cd ~/WorkBuddy/20260504101638 && bash push_to_github.sh

set -e

echo "=== 1. 清理 stale lock 文件 ==="
rm -f .git/index.lock .git/HEAD.lock .git/HEAD.lock.bak
echo "Lock files cleaned."

echo ""
echo "=== 2. 暂存所有变更 ==="
git add -A
git status --short

echo ""
echo "=== 3. 提交 ==="
git commit -m "feat: v18.0 - E15芒格100思维模型 + E13扩展至100工具 + 质量增强

v16.0: 新增选修E15查理·芒格100个思维模型与AI时代应用
- 6h/3天/3538行/412KB
- 100个模型覆盖8学科: 数学/统计(14)+物理/工程(12)+生物(8)+
  心理学(25,含芒格完整人类误判心理学)+经济学(12)+商业/战略(10)+
  决策科学(10)+哲学(9,含格栅理论)

v17.0: E13战略思维画布工具集100工具全量补全
- 4天8h -> 7天14h, 4416->6106行(281KB->472KB)
- Day 5: BMC衍生画布16个 + 战略分析11个
- Day 6: 产品增长11个 + 客户体验10个
- Day 7: 组织运营11个 + 创新思维12个
- 速查矩阵从29扩展至100工具

v18.0: E13 v6.1质量增强
- 格式修复: 编号/分隔线/冒号统一
- 补充Section十六的11个结构化对比表格
- 新增15条跨教材交叉引用
- 6个新章节各添加选型指南表
- 去模板化8个AI时代应用段落

同步更新: 技能2/4/5交叉引用 + README v18.0 + .gitignore"

echo ""
echo "=== 4. 推送到 GitHub ==="
git push origin main

echo ""
echo "=== 推送完成! ==="
echo "GitHub: https://github.com/zrxparley/ai-native-business-phd"
