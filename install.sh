#!/usr/bin/env bash
set -euo pipefail

usage() {
  cat <<'USAGE'
用法
  ./install.sh --codex           安装到 Codex 的用户 Skill 目录
  ./install.sh --skills-dir DIR  安装到指定 Agent 的 Skill 目录
  ./install.sh --zip-dir DIR     为每个 Skill 导出一个 ZIP（需要 Python 3）
  ./install.sh --help            显示帮助
USAGE
}

case "${1:-}" in
  --help|-h)
    usage
    exit 0
    ;;
  --codex)
    if [[ $# -ne 1 ]]; then
      usage >&2
      exit 2
    fi
    destination="${CODEX_SKILLS_DIR:-${CODEX_HOME:-$HOME/.codex}/skills}"
    ;;
  --skills-dir|--zip-dir)
    if [[ $# -ne 2 || -z "$2" ]]; then
      usage >&2
      exit 2
    fi
    destination="$2"
    ;;
  "")
    # Keep existing callers that already provide an explicit destination working.
    if [[ $# -ne 0 || -z "${CODEX_SKILLS_DIR:-}" ]]; then
      usage >&2
      exit 2
    fi
    destination="$CODEX_SKILLS_DIR"
    ;;
  *)
    usage >&2
    exit 2
    ;;
esac

script_dir="$(CDPATH= cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd -P)"
source_dir="$script_dir/skills"
if [[ "${1:-}" == "--zip-dir" ]] && ! command -v python3 >/dev/null 2>&1; then
  printf '导出 ZIP 需要 Python 3。\n' >&2
  exit 1
fi

# Resolve physical paths before creating a destination inside a Skill package.
target_parent="$destination"
while [[ ! -d "$target_parent" ]]; do
  target_parent="$(dirname -- "$target_parent")"
done
target_parent="$(CDPATH= cd -- "$target_parent" && pwd -P)"
case "$target_parent" in
  "$source_dir"|"$source_dir"/*)
    printf '请选择仓库 skills/ 以外的目录。\n' >&2
    exit 2
    ;;
esac
mkdir -p -- "$destination"
destination="$(CDPATH= cd -- "$destination" && pwd -P)"

if [[ "${1:-}" == "--zip-dir" ]]; then
  python3 - "$source_dir" "$destination" <<'PY'
import sys
from pathlib import Path
from tempfile import NamedTemporaryFile
from zipfile import ZIP_DEFLATED, ZipFile

source_dir, output_dir = map(Path, sys.argv[1:])
skills = sorted(path.parent for path in source_dir.glob("*/SKILL.md"))
ignored = {".DS_Store", ".git", "__pycache__", "season_state.json"}

for skill in skills:
    with NamedTemporaryFile(dir=output_dir, suffix=".zip", delete=False) as temporary:
        temporary_path = Path(temporary.name)
    try:
        with ZipFile(temporary_path, "w", compression=ZIP_DEFLATED) as archive:
            for file in sorted(skill.rglob("*")):
                name = file.relative_to(skill)
                if file.is_file() and not file.is_symlink() and not ignored.intersection(name.parts):
                    archive.write(file, name.as_posix())
        temporary_path.replace(output_dir / f"{skill.name}.zip")
    finally:
        if temporary_path.exists():
            temporary_path.unlink()

print(f"已导出 {len(skills)} 个独立 Skill ZIP 到 {output_dir}")
PY
  exit 0
fi

skill_count=0
for skill_dir in "$source_dir"/*; do
  if [[ -f "$skill_dir/SKILL.md" ]]; then
    cp -R -- "$skill_dir" "$destination/"
    skill_count=$((skill_count + 1))
  fi
done

printf '已安装 %d 个 AI Life OS Skill 到 %s\n' "$skill_count" "$destination"
printf '在你的 Agent 中刷新技能列表或新建会话。需要连接 Notion 时，调用 ai-life-system-init。\n'
