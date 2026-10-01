#!/usr/bin/env sh
# Research Agent Skills installer (macOS / Linux / WSL) - Kalaris Labs
#
#   curl -fsSL https://raw.githubusercontent.com/KalarisLabs/research-agent-skills/main/install.sh | sh
#
# Options (environment variables):
#   RAS_VERSION   release to install, e.g. 1.0.0 (default: latest)
#   RAS_BUNDLE    bundle or category to install (default: research-essentials; "all" for everything)
#   RAS_HARNESS   auto | all | comma list: claude-code,codex,cursor,gemini-cli,copilot,opencode,windsurf,agents
#   RAS_NO_NODE   set to 1 to force the standalone (no Node.js) installer
#   RAS_BASE_URL  release download base URL (testing/mirrors); default GitHub Releases
#
# With Node.js >= 18 this delegates to the npm CLI (published with provenance).
# Without Node it downloads the release tarball, verifies it against the
# release SHA256SUMS, and copies the selected skills into place.
set -eu

REPO="KalarisLabs/research-agent-skills"
VERSION="${RAS_VERSION:-latest}"
BUNDLE="${RAS_BUNDLE:-research-essentials}"
HARNESS="${RAS_HARNESS:-auto}"

say() { printf '%s\n' "$*"; }
die() { printf 'error: %s\n' "$*" >&2; exit 1; }

case "$VERSION" in latest|[0-9]*) ;; *) die "invalid RAS_VERSION '$VERSION'" ;; esac
case "$BUNDLE" in *[!a-z0-9-]*) die "invalid RAS_BUNDLE '$BUNDLE'" ;; esac

if [ "${RAS_NO_NODE:-0}" != "1" ] && command -v node >/dev/null 2>&1 && command -v npx >/dev/null 2>&1 &&
  node -e 'process.exit(Number(process.versions.node.split(".")[0]) >= 18 ? 0 : 1)' 2>/dev/null; then
  case "$BUNDLE" in
    all) SEL="--all" ;;
    research-essentials|ml-research|ai-research|biology-research|chemistry-research|medicine-research|physics-research) SEL="--bundle $BUNDLE" ;;
    *) SEL="--category $BUNDLE" ;;
  esac
  say "Installing with the research-agent-skills CLI (npm)..."
  # shellcheck disable=SC2086
  exec npx -y "research-agent-skills@${VERSION}" install $SEL --harness "$HARNESS" --yes
fi

say "Node.js 18+ not found; using the standalone installer."
command -v curl >/dev/null 2>&1 || die "curl is required"
command -v tar >/dev/null 2>&1 || die "tar is required"
if command -v sha256sum >/dev/null 2>&1; then SHA="sha256sum"; elif command -v shasum >/dev/null 2>&1; then SHA="shasum -a 256"; else die "sha256sum or shasum is required"; fi

if [ "$VERSION" = "latest" ] && [ -z "${RAS_BASE_URL:-}" ]; then
  VERSION=$(curl -fsSL "https://api.github.com/repos/$REPO/releases/latest" | sed -n 's/.*"tag_name": *"v\{0,1\}\([^"]*\)".*/\1/p' | head -n1)
  [ -n "$VERSION" ] || die "could not resolve the latest release"
fi

TMP=$(mktemp -d)
trap 'rm -rf "$TMP"' EXIT INT TERM
ASSET="research-agent-skills-${VERSION}.tar.gz"
BASE="${RAS_BASE_URL:-https://github.com/$REPO/releases/download/v${VERSION}}"
say "Downloading $ASSET ..."
curl -fsSL -o "$TMP/$ASSET" "$BASE/$ASSET"
curl -fsSL -o "$TMP/SHA256SUMS" "$BASE/SHA256SUMS"
EXPECTED=$(grep " \*\{0,1\}$ASSET\$" "$TMP/SHA256SUMS" | cut -d' ' -f1)
ACTUAL=$($SHA "$TMP/$ASSET" | cut -d' ' -f1)
[ -n "$EXPECTED" ] && [ "$EXPECTED" = "$ACTUAL" ] || die "checksum mismatch for $ASSET"
say "Verified SHA-256 $ACTUAL"

mkdir -p "$TMP/x"
tar -xzf "$TMP/$ASSET" -C "$TMP/x" --strip-components=1 --no-same-owner
LIST="$TMP/x/catalog/lists/$BUNDLE.txt"
[ -f "$LIST" ] || die "unknown bundle or category '$BUNDLE'"

targets=""
add() { case " $targets " in *" $1 "*) ;; *) targets="$targets $1" ;; esac; }
for h in $(printf '%s' "$HARNESS" | tr ',' ' '); do
  case "$h" in
    auto)
      [ -d "$HOME/.claude" ] && add "$HOME/.claude/skills"
      [ -d "$HOME/.codex" ] && add "$HOME/.codex/skills"
      [ -d "$HOME/.cursor" ] && add "$HOME/.cursor/skills"
      [ -d "$HOME/.gemini" ] && add "$HOME/.gemini/skills"
      [ -d "$HOME/.copilot" ] && add "$HOME/.copilot/skills"
      [ -d "$HOME/.config/opencode" ] && add "$HOME/.config/opencode/skills"
      [ -d "$HOME/.codeium/windsurf" ] && add "$HOME/.codeium/windsurf/skills"
      [ -n "$targets" ] || add "$HOME/.claude/skills" ;;
    all) for d in .claude/skills .codex/skills .cursor/skills .gemini/skills .copilot/skills .config/opencode/skills .codeium/windsurf/skills .agents/skills; do add "$HOME/$d"; done ;;
    claude-code) add "$HOME/.claude/skills" ;;
    codex) add "$HOME/.codex/skills" ;;
    cursor) add "$HOME/.cursor/skills" ;;
    gemini-cli) add "$HOME/.gemini/skills" ;;
    copilot) add "$HOME/.copilot/skills" ;;
    opencode) add "$HOME/.config/opencode/skills" ;;
    windsurf) add "$HOME/.codeium/windsurf/skills" ;;
    agents) add "$HOME/.agents/skills" ;;
    *) die "unknown harness '$h'" ;;
  esac
done

count=0
for dir in $targets; do
  mkdir -p "$dir"
  while IFS= read -r name; do
    case "$name" in ""|*[!a-z0-9-]*) continue ;; esac
    rm -rf "${dir:?}/$name"
    cp -R "$TMP/x/skills/$name" "$dir/$name"
    count=$((count + 1))
  done < "$LIST"
  say "  installed into $dir"
done
say "Installed $count skill copies (v$VERSION, $BUNDLE). Restart your agent to load them."
