#!/usr/bin/env bash
set -euo pipefail

# Overlay applier: blindly applies canonical files from scripts/overlay/
# Usage: ./scripts/apply_overlay.sh

OVERLAY_DIR="scripts/overlay"

write_if_absent() {
  local target="$1"
  local src="$2"
  if [ ! -e "$target" ]; then
    cp "$src" "$target"
    echo "Created $target"
  fi
}

write_canonical() {
  local target="$1"
  local src="$2"
  cp "$src" "$target"
  echo "Replaced $target with canonical version"
}

# Example: apply overlays for CI scripts
for file in "$OVERLAY_DIR"/ci/*; do
  [ -f "$file" ] || continue
  target="ci/$(basename "$file")"
  write_canonical "$target" "$file"
done

# Example: apply overlays for .github workflows
for file in "$OVERLAY_DIR"/github/*; do
  [ -f "$file" ] || continue
  target=".github/workflows/$(basename "$file")"
  write_canonical "$target" "$file"
done

echo "Overlay application complete."
