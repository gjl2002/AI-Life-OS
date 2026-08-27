#!/usr/bin/env bash
set -euo pipefail

script_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
codex_root="${CODEX_HOME:-$HOME/.codex}"
skills_dir="${CODEX_SKILLS_DIR:-$codex_root/skills}"

mkdir -p "$skills_dir"

skill_count=0
for skill_dir in "$script_dir"/skills/*; do
  if [ -d "$skill_dir" ]; then
    cp -R "$skill_dir" "$skills_dir/"
    skill_count=$((skill_count + 1))
  fi
done

printf '已安装 %d 个 AI Life OS Skill/共享依赖到：%s\n' "$skill_count" "$skills_dir"
printf '请重新打开 Codex 或新建任务，然后运行：$ai-life-system-init\n'
