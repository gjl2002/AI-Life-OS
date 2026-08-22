#!/usr/bin/env bash
set -euo pipefail

script_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
codex_root="${CODEX_HOME:-$HOME/.codex}"
skills_dir="${CODEX_SKILLS_DIR:-$codex_root/skills}"

mkdir -p "$skills_dir"

for skill_dir in "$script_dir"/skills/*; do
  if [ -d "$skill_dir" ]; then
    cp -R "$skill_dir" "$skills_dir/"
  fi
done

printf '已安装 8 个 AI 人生系统 Skill 到：%s\n' "$skills_dir"
printf '请重新打开 Codex 或新建任务，然后运行：$ai-life-system-init\n'
