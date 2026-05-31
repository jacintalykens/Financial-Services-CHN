#!/usr/bin/env python3
"""
Financial-Services-CN — 同步脚本

将 plugins/vertical-plugins/<vertical>/skills/<skill>/ 全量复制到
plugins/agent-plugins/<agent>/skills/<skill>/ 位置（按 Anthropic 原架构）。

⚠️ 本项目作为独立分支，默认不含 agent-plugins/ 目录。
本脚本仅在你将本项目合并到 Anthropic 官方 financial-services 仓库时才有用。

合并到 Anthropic 官方仓库后，使用 Anthropic 官方的 scripts/sync-agent-skills.py
即可。本脚本为兼容性占位。
"""
import shutil
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
AGENTS = ROOT / "plugins" / "agent-plugins"
VERTICALS = ROOT / "plugins" / "vertical-plugins"


def main():
    if not AGENTS.exists():
        print("ℹ️ 未发现 plugins/agent-plugins/ 目录")
        print("   本项目作为独立分支不含 agent-plugins/，无需同步")
        print("   如要合并到 Anthropic 官方仓库，请用官方的 sync-agent-skills.py")
        sys.exit(0)

    # 索引所有源 skill
    src_by_name: dict[str, Path] = {}
    for sk in VERTICALS.glob("*/skills/*"):
        if sk.is_dir():
            src_by_name[sk.name] = sk

    synced = 0
    missing: list[str] = []
    for bundled in sorted(AGENTS.glob("*/skills/*")):
        if not bundled.is_dir():
            continue
        src = src_by_name.get(bundled.name)
        if not src:
            missing.append(str(bundled.relative_to(ROOT)))
            continue
        shutil.rmtree(bundled)
        shutil.copytree(src, bundled)
        synced += 1

    print(f"✅ synced {synced} bundled skill dir(s) from vertical-plugins/")
    if missing:
        print("⚠️ no vertical source found for:", file=sys.stderr)
        for m in missing:
            print(f"  - {m}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
