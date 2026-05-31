#!/usr/bin/env python3
"""
Financial-Services-CN — 全量校验脚本

校验项：
1. 所有 -cn skill 目录命名规范（必须 -cn 后缀）
2. 每个 skill 必有 SKILL.md
3. SKILL.md 含合法 YAML frontmatter（name + description）
4. name 字段必须以 -cn 结尾
5. description 必须含 "适用范围" 字段
6. references/ 目录至少含 3 个 .md（workflow / report-structure / best-practices）
7. SKILL.md 行数 ≥ 400（compliance-watcher-cn 例外，≥ 500）

返回码 0 = 通过；非 0 = 失败。
"""
from pathlib import Path
import re
import sys


ROOT = Path(__file__).resolve().parents[1]
VERTICAL_PLUGINS = ROOT / "plugins" / "vertical-plugins"

# 行数基线
LINE_BASELINE = 400
LINE_BASELINE_COMPLIANCE = 500


def parse_frontmatter(content: str) -> dict:
    """提取 YAML frontmatter（首段 --- ... ---）"""
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n", content, re.DOTALL)
    if not m:
        return {}
    fm = {}
    for line in m.group(1).split("\n"):
        kv = re.match(r"^(\w+):\s*(.*)$", line)
        if kv:
            fm[kv.group(1)] = kv.group(2).strip()
    return fm


def main():
    issues = []
    skill_count = 0
    line_total = 0

    for skill_dir in VERTICAL_PLUGINS.glob("*/skills/*"):
        if not skill_dir.is_dir():
            continue
        skill_name = skill_dir.name
        # 仅校验 -cn 技能
        if not skill_name.endswith("-cn"):
            continue
        skill_count += 1

        # 校验 SKILL.md 存在
        skill_md = skill_dir / "SKILL.md"
        if not skill_md.exists():
            issues.append(f"❌ {skill_name}: 缺 SKILL.md")
            continue

        # 校验 YAML frontmatter
        content = skill_md.read_text(encoding="utf-8")
        fm = parse_frontmatter(content)
        if not fm:
            issues.append(f"❌ {skill_name}: SKILL.md 无 YAML frontmatter")
            continue

        # name 字段必须以 -cn 结尾
        name = fm.get("name", "")
        if not name.endswith("-cn"):
            issues.append(f"❌ {skill_name}: name 字段 '{name}' 不以 -cn 结尾")

        # description 必须含 "适用范围"
        desc = fm.get("description", "")
        if "适用范围" not in desc:
            issues.append(f"⚠️ {skill_name}: description 缺 '适用范围' 字段")

        # references 目录至少 3 个 .md
        refs_dir = skill_dir / "references"
        if refs_dir.exists():
            ref_files = list(refs_dir.glob("*.md"))
            if len(ref_files) < 3:
                issues.append(f"⚠️ {skill_name}: references/ 仅 {len(ref_files)} 个 .md（推荐 ≥3）")
        else:
            issues.append(f"⚠️ {skill_name}: 无 references/ 目录")

        # 行数基线
        lines = len(content.splitlines())
        line_total += lines
        baseline = LINE_BASELINE_COMPLIANCE if "compliance-watcher" in skill_name else LINE_BASELINE
        if lines < baseline * 0.85:  # 允许 15% 容差
            issues.append(f"⚠️ {skill_name}: SKILL.md 仅 {lines} 行（基线 {baseline}）")

    # 输出报告
    print(f"\n{'=' * 60}")
    print(f"Financial-Services-CN 校验报告")
    print(f"{'=' * 60}")
    print(f"检查的 -cn 技能数：{skill_count}")
    print(f"SKILL.md 总行数：{line_total:,}")
    print(f"平均行数：{line_total // skill_count if skill_count else 0}")
    print(f"问题数：{len(issues)}")
    print()

    if issues:
        for issue in issues:
            print(issue)
        print()
        # 严重错误（❌）才返回失败
        fatal = [i for i in issues if i.startswith("❌")]
        if fatal:
            print(f"❌ 发现 {len(fatal)} 个严重错误，请修复后再提交")
            sys.exit(1)
        else:
            print(f"⚠️ 仅发现 {len(issues)} 个警告（非阻断）")
            sys.exit(0)
    else:
        print(f"✅ 全部 {skill_count} 个 -cn 技能通过校验")
        sys.exit(0)


if __name__ == "__main__":
    main()
