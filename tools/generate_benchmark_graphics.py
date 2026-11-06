#!/usr/bin/env python3
"""Generate benchmark leaderboard graphics in the exact visual style of frontier AI leaderboards.
Produces standalone SVGs, high-resolution PNGs via Chrome headless, and an interactive HTML report.
"""

from __future__ import annotations

import os
import shutil
import subprocess
from pathlib import Path

# Paths
ROOT = Path(__file__).resolve().parents[1]
RESULTS_DIR = ROOT / "benchmarks" / "results"
PUBLIC_DIR = ROOT / "PUBLIC"
DOCS_ASSETS = ROOT / "docs" / "assets"
_env_artifact = os.environ.get("ARTIFACT_DIR")
ARTIFACT_DIR = Path(_env_artifact) if _env_artifact else None

_all_targets = [p for p in [PUBLIC_DIR, DOCS_ASSETS, RESULTS_DIR, ARTIFACT_DIR] if p is not None]
for p in _all_targets:
    p.mkdir(parents=True, exist_ok=True)

# -----------------------------------------------------------------------------
# VECTOR LOGO DEFINITIONS (24x24 viewBox, crisp and scalable)
# -----------------------------------------------------------------------------

LOGOS = {
    "google": """
    <g transform="scale(0.8) translate(3, 3)">
      <path d="M22.56 12.25c0-.78-.07-1.53-.2-2.25H12v4.26h5.92c-.26 1.37-1.04 2.53-2.21 3.31v2.77h3.57c2.08-1.92 3.28-4.74 3.28-8.09z" fill="#4285F4"/>
      <path d="M12 23c2.97 0 5.46-.98 7.28-2.66l-3.57-2.77c-.98.66-2.23 1.06-3.71 1.06-2.86 0-5.29-1.93-6.16-4.53H2.18v2.84C3.99 20.53 7.7 23 12 23z" fill="#34A853"/>
      <path d="M5.84 14.09c-.22-.66-.35-1.36-.35-2.09s.13-1.43.35-2.09V7.06H2.18C1.43 8.55 1 10.22 1 12s.43 3.45 1.18 4.94l2.85-2.22.81-.63z" fill="#FBBC05"/>
      <path d="M12 5.38c1.62 0 3.06.56 4.21 1.64l3.15-3.15C17.45 2.09 14.97 1 12 1 7.7 1 3.99 3.47 2.18 7.06l3.66 2.84c.87-2.6 3.3-4.52 6.16-4.52z" fill="#EA4335"/>
    </g>
    """,
    "anthropic": """
    <g fill="#CC785C">
      <path d="M13.827 3.518h3.918L24 20.482h-3.918l-6.255-16.964zm-7.654 0h3.918L16.346 20.482h-3.918L10.59 15.5H5.41l-1.838 4.982H0L6.173 3.518zm1.838 8.964h2.576l-1.288-3.489-1.288 3.489z"/>
    </g>
    """,
    "openai": """
    <g fill="#1F1F1F">
      <path d="M22.282 9.821a5.985 5.985 0 0 0-.516-4.91 6.046 6.046 0 0 0-6.51-2.9A6.065 6.065 0 0 0 4.981 4.18a5.985 5.985 0 0 0-3.998 2.9 6.046 6.046 0 0 0 .743 7.097 5.98 5.98 0 0 0 .51 4.911 6.051 6.051 0 0 0 6.515 2.9A5.985 5.985 0 0 0 13.26 24a6.056 6.056 0 0 0 5.772-4.206 5.99 5.99 0 0 0 3.997-2.9 6.056 6.056 0 0 0-.747-7.073zM13.26 22.43a4.476 4.476 0 0 1-2.876-1.04l.141-.081 4.779-2.758a.795.795 0 0 0 .392-.681v-6.737l2.02 1.168a.071.071 0 0 1 .038.052v5.583a4.504 4.504 0 0 1-4.494 4.494zm-9.33-4.52a4.467 4.467 0 0 1-.535-3.003l.142.085 4.783 2.755a.793.793 0 0 0 .78 0l5.836-3.367v2.332a.08.08 0 0 1-.033.064l-4.835 2.793a4.505 4.505 0 0 1-6.138-1.659zm-1.802-8.318a4.484 4.484 0 0 1 2.34-1.961v5.673a.79.79 0 0 0 .388.682l5.836 3.368-2.02 1.166a.08.08 0 0 1-.073.004l-4.84-2.793a4.505 4.505 0 0 1-1.631-6.139zm15.717 1.942l-5.836-3.368 2.02-1.166a.08.08 0 0 1 .073-.004l4.84 2.793a4.505 4.505 0 0 1 1.631 6.139 4.484 4.484 0 0 1-2.34 1.961v-5.673a.79.79 0 0 0-.388-.682zm2.02-3.136l-.142-.085-4.783-2.755a.793.793 0 0 0-.78 0l-5.836 3.367v-2.332a.08.08 0 0 1 .033-.064l4.835-2.793a4.505 4.505 0 0 1 6.673 4.662zm-9.141 4.52a1.593 1.593 0 1 0-1.593-1.593 1.593 1.593 0 0 0 1.593 1.593z"/>
    </g>
    """,
    "meta": """
    <g fill="#0081FB">
      <path d="M12 6.5C7.5 6.5 4 10 4 13.5c0 3.2 2.5 5.5 5 5.5 2.5 0 4-2.2 4-4.5 0-2.3 1.5-4.5 4-4.5 2.5 0 5 2.3 5 5.5 0 3.5-3.5 7-8 7-4.5 0-9-3.5-9-9S7.5 4.5 12 4.5c4.5 0 9 3.5 9 9s-4.5 9-9 9c-2.8 0-5.2-1.4-6.8-3.6 1.4-1.2 2.8-2.9 3.8-4.9C10.2 12.5 11 11 12 11c1 0 1.8 1.5 2.8 3 1 2 2.4 3.7 3.8 4.9-1.6 2.2-4 3.6-6.6 3.6-3.8 0-6.5-2.8-6.5-6.5 0-3.7 2.7-6.5 6.5-6.5z"/>
    </g>
    """,
    "kimi": """
    <g>
      <rect width="24" height="24" rx="5" fill="#0066FF"/>
      <path d="M7 6h3v5.2l4.8-5.2h3.8L12.7 12l6.1 6H15l-5-5.2V18H7V6z" fill="#FFFFFF"/>
    </g>
    """,
    "xai": """
    <g fill="#1F1F1F">
      <path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-5.214-6.817L4.99 21.75H1.68l7.73-8.835L1.254 2.25H8.08l4.713 6.231zm-1.161 17.52h1.833L7.084 4.126H5.117z"/>
    </g>
    """,
    "tencent": """
    <g>
      <circle cx="12" cy="12" r="10" fill="#00A4FF"/>
      <path d="M7 12a5 5 0 0 1 10 0v2a3 3 0 0 1-6 0v-2a1 1 0 0 0-2 0v1a1 1 0 0 1-2 0v-1z" fill="#FFFFFF"/>
      <circle cx="9.5" cy="10" r="1.2" fill="#1E293B"/>
      <circle cx="14.5" cy="10" r="1.2" fill="#1E293B"/>
    </g>
    """,
    "qwen": """
    <g>
      <circle cx="12" cy="12" r="10" fill="#FF6A00"/>
      <path d="M12 6a6 6 0 1 0 4.2 10.2L18 18l-1.8-1.8A5.96 5.96 0 0 0 12 6zm0 2.5a3.5 3.5 0 1 1 0 7 3.5 3.5 0 0 1 0-7z" fill="#FFFFFF"/>
    </g>
    """,
    "deepseek": """
    <g>
      <circle cx="12" cy="12" r="10" fill="#2444E5"/>
      <path d="M7 15c2-4 6-5 9-4 2 .7 3 2 3 2s-1.5-1-4-1c-3 0-5.5 1.5-7 3.5l-1-.5zm1-5c1.5-2 4-3 6.5-2.5 1.5.3 2.5 1 2.5 1s-1-.8-3-.8c-2.5 0-4.5 1-6 2.3z" fill="#FFFFFF"/>
    </g>
    """,
    "zhipu": """
    <g>
      <rect width="24" height="24" rx="5" fill="#1E40AF"/>
      <path d="M7 7h10l-6.5 7H17v3H7l6.5-7H7V7z" fill="#FFFFFF"/>
    </g>
    """,
    "xiaomi": """
    <g>
      <rect width="24" height="24" rx="6" fill="#FF6700"/>
      <path d="M6.5 8h2v8h-2V8zm4 0h3.5c1.4 0 2.5 1.1 2.5 2.5V16h-2v-5c0-.3-.2-.5-.5-.5H12.5V16h-2V8zm8 0h2v8h-2V8z" fill="#FFFFFF"/>
    </g>
    """,
    "ling": """
    <g>
      <rect width="24" height="24" rx="5" fill="#0EA5E9"/>
      <circle cx="12" cy="12" r="6" fill="none" stroke="#FFFFFF" stroke-width="2.5"/>
      <circle cx="12" cy="12" r="2" fill="#FFFFFF"/>
    </g>
    """,
    "minimax": """
    <g>
      <rect width="24" height="24" rx="5" fill="#EC4899"/>
      <path d="M6 12v3m3-6v9m3-12v15m3-12v9m3-6v3" stroke="#FFFFFF" stroke-width="2" stroke-linecap="round"/>
    </g>
    """,
    "mistral": """
    <g fill="#EA580C">
      <rect x="3" y="4" width="3.6" height="16" rx="0.5"/>
      <rect x="17.4" y="4" width="3.6" height="16" rx="0.5"/>
      <rect x="6.6" y="8" width="3.6" height="8" rx="0.5"/>
      <rect x="13.8" y="8" width="3.6" height="8" rx="0.5"/>
      <rect x="10.2" y="11" width="3.6" height="5" rx="0.5"/>
    </g>
    """,
    "k2": """
    <g>
      <rect width="24" height="24" rx="5" fill="#1E3A8A"/>
      <path d="M7 6h3v4.5l4-4.5h3.5L12.5 11l5.5 7H14.5l-4.5-5.5V18H7V6z" fill="#FFFFFF"/>
    </g>
    """,
    "beam": """
    <g fill="#166534">
      <circle cx="8" cy="12" r="4"/>
      <circle cx="16" cy="12" r="4"/>
      <path d="M8 10h8v4H8z"/>
    </g>
    """,
    "nvidia": """
    <g fill="#76B900">
      <path d="M12 4c-4.4 0-8 3.6-8 8 0 3.5 2.3 6.5 5.5 7.6V17c-2-.9-3.5-3-3.5-5 0-3.3 2.7-6 6-6s6 2.7 6 6c0 2-1.5 4.1-3.5 5v2.6c3.2-1.1 5.5-4.1 5.5-7.6 0-4.4-3.6-8-8-8zm0 4c-2.2 0-4 1.8-4 4 0 1.8 1.2 3.3 2.8 3.8V13.5c-.5-.4-.8-1-.8-1.5 0-1.1.9-2 2-2s2 .9 2 2c0 .5-.3 1.1-.8 1.5v2.3c1.6-.5 2.8-2 2.8-3.8 0-2.2-1.8-4-4-4z"/>
    </g>
    """,
    "inkling": """
    <g fill="#334155">
      <rect width="24" height="24" rx="5"/>
      <path d="M7 8h10v2.5H7V8zm0 5h10v2.5H7V13z" fill="#FFFFFF"/>
    </g>
    """,
    # Academic & Scientific badges
    "acm": """
    <g>
      <rect width="24" height="24" rx="4" fill="#0077C8"/>
      <text x="12" y="16.5" font-family="'Helvetica Neue', Arial, sans-serif" font-weight="900" font-size="10.5" fill="#FFFFFF" text-anchor="middle">ACM</text>
    </g>
    """,
    "nature": """
    <g>
      <rect width="24" height="24" rx="4" fill="#D32F2F"/>
      <text x="12" y="17.5" font-family="Georgia, serif" font-weight="900" font-size="16" fill="#FFFFFF" text-anchor="middle">N</text>
    </g>
    """,
    "cell": """
    <g>
      <rect width="24" height="24" rx="4" fill="#0288D1"/>
      <text x="12" y="17" font-family="'Arial Black', sans-serif" font-weight="900" font-size="15" fill="#FFFFFF" text-anchor="middle">C</text>
    </g>
    """,
    "ieee": """
    <g>
      <rect width="24" height="24" rx="4" fill="#00629B"/>
      <path d="M12 4l6 8-6 8-6-8z" fill="#FFFFFF"/>
      <path d="M12 7l3.5 5-3.5 5-3.5-5z" fill="#00629B"/>
    </g>
    """,
    "science": """
    <g>
      <rect width="24" height="24" rx="4" fill="#D32F2F"/>
      <text x="12" y="17" font-family="Georgia, serif" font-style="italic" font-weight="900" font-size="15" fill="#FFFFFF" text-anchor="middle">S</text>
    </g>
    """,
    "apa": """
    <g>
      <rect width="24" height="24" rx="4" fill="#2E7D32"/>
      <text x="12" y="16" font-family="sans-serif" font-weight="800" font-size="9" fill="#FFFFFF" text-anchor="middle">APA</text>
    </g>
    """,
    "elsevier": """
    <g>
      <rect width="24" height="24" rx="4" fill="#FF6D00"/>
      <circle cx="12" cy="10" r="5" fill="#FFFFFF"/>
      <path d="M12 11v6m-3 0h6" stroke="#FFFFFF" stroke-width="2"/>
    </g>
    """,
    "arxiv": """
    <g>
      <rect width="24" height="24" rx="4" fill="#B31B1B"/>
      <text x="12" y="16.5" font-family="sans-serif" font-weight="800" font-size="8.5" fill="#FFFFFF" text-anchor="middle">arXiv</text>
    </g>
    """,
    "springer": """
    <g>
      <rect width="24" height="24" rx="4" fill="#003366"/>
      <circle cx="12" cy="12" r="7" fill="none" stroke="#FFFFFF" stroke-width="2"/>
      <path d="M12 7v10M7 12h10" stroke="#FFFFFF" stroke-width="1.8"/>
    </g>
    """,
    "plos": """
    <g>
      <rect width="24" height="24" rx="4" fill="#5C2D91"/>
      <circle cx="8" cy="12" r="2.5" fill="#FFFFFF"/>
      <circle cx="16" cy="12" r="2.5" fill="#FFFFFF"/>
    </g>
    """,
    "crossref": """
    <g>
      <rect width="24" height="24" rx="4" fill="#3F51B5"/>
      <path d="M6 12l5-5m-5 5l5 5M18 12l-5-5m5 5l-5 5" stroke="#FFFFFF" stroke-width="2.2" stroke-linecap="round"/>
    </g>
    """,
    "kalaris": """
    <g>
      <rect width="24" height="24" rx="4" fill="#10B981"/>
      <path d="M7 6h3v4l4-4h4l-5 5 5.5 7H14.5l-4-5.2V18H7V6z" fill="#FFFFFF"/>
    </g>
    """,
    "dna": """
    <g>
      <rect width="24" height="24" rx="4" fill="#059669"/>
      <path d="M7 6c5 3 5 9 10 12M17 6c-5 3-5 9-10 12M8 9h8M8 15h8M9 12h6" stroke="#FFFFFF" stroke-width="1.6" stroke-linecap="round"/>
    </g>
    """,
    "flask": """
    <g>
      <rect width="24" height="24" rx="4" fill="#D97706"/>
      <path d="M10 5h4v4l4 8a1 1 0 0 1-.9 1.5H6.9A1 1 0 0 1 6 17l4-8V5z" fill="none" stroke="#FFFFFF" stroke-width="1.8"/>
      <path d="M8 14h8" stroke="#FFFFFF" stroke-width="1.5"/>
    </g>
    """,
    "atom": """
    <g>
      <rect width="24" height="24" rx="4" fill="#4F46E5"/>
      <ellipse cx="12" cy="12" rx="8" ry="3" fill="none" stroke="#FFFFFF" stroke-width="1.4" transform="rotate(30 12 12)"/>
      <ellipse cx="12" cy="12" rx="8" ry="3" fill="none" stroke="#FFFFFF" stroke-width="1.4" transform="rotate(-30 12 12)"/>
      <circle cx="12" cy="12" r="2" fill="#FFFFFF"/>
    </g>
    """,
    "brain": """
    <g>
      <rect width="24" height="24" rx="4" fill="#8B5CF6"/>
      <circle cx="9" cy="10" r="3.5" fill="none" stroke="#FFFFFF" stroke-width="1.6"/>
      <circle cx="15" cy="10" r="3.5" fill="none" stroke="#FFFFFF" stroke-width="1.6"/>
      <path d="M8 13.5c1 2 2 3.5 4 3.5s3-1.5 4-3.5" stroke="#FFFFFF" stroke-width="1.6" fill="none"/>
    </g>
    """,
    "book": """
    <g>
      <rect width="24" height="24" rx="4" fill="#2563EB"/>
      <path d="M6 7a2 2 0 0 1 2-2h4v13H8a2 2 0 0 0-2 2V7zm12 0a2 2 0 0 0-2-2h-4v13h4a2 2 0 0 1 2 2V7z" fill="none" stroke="#FFFFFF" stroke-width="1.6"/>
    </g>
    """,
    "shield": """
    <g>
      <rect width="24" height="24" rx="4" fill="#0EA5E9"/>
      <path d="M12 5l6 2.5v5c0 4-2.8 7-6 8-3.2-1-6-4-6-8v-5L12 5z" fill="none" stroke="#FFFFFF" stroke-width="1.8"/>
      <path d="M9.5 12.5l2 2 4-4" stroke="#FFFFFF" stroke-width="1.8" stroke-linecap="round"/>
    </g>
    """
}

# -----------------------------------------------------------------------------
# SVG BUILDER ENGINE
# -----------------------------------------------------------------------------

def build_leaderboard_svg(
    items: list[dict],
    max_score: float = 65,
    y_ticks: list[int] = None,
    width: int = 1140,
    height: int = 370,
    bar_width: int = 26,
    bar_spacing: float = 36.5,
    margin_left: float = 70.0,
    baseline_y: float = 180.0,
    top_y: float = 44.0,
) -> str:
    """Builds a pixel-perfect, self-contained SVG leaderboard matching the reference image."""
    if y_ticks is None:
        y_ticks = [10, 20, 30, 40, 50, 60]

    chart_height = baseline_y - top_y
    scale = chart_height / max_score

    svg_parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" height="auto" style="background: #FFFFFF; font-family: -apple-system, BlinkMacSystemFont, \'Segoe UI\', Roboto, Helvetica, Arial, sans-serif;">',
        '<defs>',
        '  <!-- Checkered green pattern for #1 top rank -->',
        '  <pattern id="checkered-green" width="6" height="6" patternUnits="userSpaceOnUse">',
        '    <rect width="6" height="6" fill="#22C55E"/>',
        '    <rect width="3" height="3" fill="#15803D"/>',
        '    <rect x="3" y="3" width="3" height="3" fill="#15803D"/>',
        '  </pattern>',
        '  <!-- Checkered blue pattern for Meta special variant -->',
        '  <pattern id="checkered-blue" width="6" height="6" patternUnits="userSpaceOnUse">',
        '    <rect width="6" height="6" fill="#0081FB"/>',
        '    <rect width="3" height="3" fill="#0058B6"/>',
        '    <rect x="3" y="3" width="3" height="3" fill="#0058B6"/>',
        '  </pattern>',
        '</defs>',
        '<!-- Background -->',
        f'<rect width="{width}" height="{height}" fill="#FFFFFF"/>',
    ]

    # Horizontal Dotted Gridlines across the chart area
    grid_start_x = margin_left - 15
    grid_end_x = margin_left + len(items) * bar_spacing + 8
    for tick in y_ticks:
        tick_y = baseline_y - (tick * scale)
        svg_parts.append(
            f'<line x1="{grid_start_x:.1f}" y1="{tick_y:.1f}" x2="{grid_end_x:.1f}" y2="{tick_y:.1f}" stroke="#E2E8F0" stroke-width="1.2" stroke-dasharray="2,3"/>'
        )

    # Render Bars, Numbers, Logos, and Labels
    r = 5.0  # rounded top radius
    for i, item in enumerate(items):
        cx = margin_left + i * bar_spacing + (bar_width / 2.0)
        bx = cx - (bar_width / 2.0)
        score = item["score"]
        h = max(12.0, score * scale)
        b_top = baseline_y - h

        # Determine Fill
        fill = item.get("fill")
        if not fill:
            if item.get("pattern"):
                fill = f"url(#{item['pattern']})"
            else:
                fill = item.get("color", "#CC785C")

        # SVG Path for Bar with Rounded Top Corners and Flat Bottom
        bar_path = (
            f"M {bx:.2f} {baseline_y:.2f} "
            f"V {b_top + r:.2f} "
            f"Q {bx:.2f} {b_top:.2f} {bx + r:.2f} {b_top:.2f} "
            f"H {bx + bar_width - r:.2f} "
            f"Q {bx + bar_width:.2f} {b_top:.2f} {bx + bar_width:.2f} {b_top + r:.2f} "
            f"V {baseline_y:.2f} Z"
        )
        svg_parts.append(f'<path d="{bar_path}" fill="{fill}"/>')

        # Score Number inside Bar
        score_val = item.get("score_display", str(int(round(score))))
        if h > 50:
            text_y = b_top + (h * 0.58)
        else:
            text_y = b_top + (h * 0.52)

        svg_parts.append(
            f'<text x="{cx:.2f}" y="{text_y:.2f}" fill="#FFFFFF" font-size="11" font-weight="700" text-anchor="middle" dominant-baseline="central">{score_val}</text>'
        )

        # Logo / Icon below the baseline
        logo_key = item.get("logo", "anthropic").lower()
        logo_svg = LOGOS.get(logo_key, LOGOS["anthropic"])
        logo_x = cx - 10.0
        logo_y = baseline_y + 8.0
        svg_parts.append(f'<g transform="translate({logo_x:.2f}, {logo_y:.2f}) scale(0.83)">{logo_svg}</g>')

        # Rotated Label below Logo
        label = item.get("label", "")
        label_y = baseline_y + 36.0
        svg_parts.append(
            f'<text transform="translate({cx:.2f}, {label_y:.2f}) rotate(-58)" text-anchor="end" font-size="10.5" font-weight="500" fill="#1E293B">{label}</text>'
        )

    svg_parts.append('</svg>')
    return "\n".join(svg_parts)


# -----------------------------------------------------------------------------
# HIGH-RES PNG RENDERER VIA CHROME HEADLESS
# -----------------------------------------------------------------------------

def render_svg_to_png(svg_path: Path, png_path: Path, width: int = 1140, height: int = 370, scale: int = 2):
    """Renders the SVG to high-resolution PNG using Chrome headless."""
    chrome_exe = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
    if not os.path.exists(chrome_exe):
        chrome_exe = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"

    cmd = [
        chrome_exe,
        "--headless=new",
        "--disable-gpu",
        f"--force-device-scale-factor={scale}",
        f"--window-size={width},{height}",
        f"--screenshot={png_path.resolve()}",
        str(svg_path.resolve()),
    ]
    try:
        subprocess.run(cmd, capture_output=True, check=True)
        print(f"Rendered High-DPI PNG: {png_path} ({width*scale}x{height*scale})")
    except Exception as e:
        print(f"Failed to render PNG via Chrome: {e}")


# -----------------------------------------------------------------------------
# DATASET DEFINITIONS
# -----------------------------------------------------------------------------

def get_frontier_models_data() -> list[dict]:
    """The 28 frontier AI models evaluated on research tasks (exact 1:1 match to reference)."""
    return [
        {"label": "Gemini 4 Carbon (high)", "score": 60, "color": "#22C55E", "pattern": "checkered-green", "logo": "google"},
        {"label": "Claude Opus 5.5 (max)", "score": 59, "color": "#CC785C", "logo": "anthropic"},
        {"label": "GPT-6 Astra (max)", "score": 57, "color": "#1F1F1F", "logo": "openai"},
        {"label": "GPT-6.1 Sol (max)", "score": 55, "color": "#1F1F1F", "logo": "openai"},
        {"label": "Claude Sonnet 5.5 (max)", "score": 55, "color": "#CC785C", "logo": "anthropic"},
        {"label": "GPT-6.1 Terra (max)", "score": 51, "color": "#1F1F1F", "logo": "openai"},
        {"label": "Muse Wonder Full (max)", "score": 50, "color": "#0081FB", "pattern": "checkered-blue", "logo": "meta"},
        {"label": "Claude Fable 5.1 (max)", "score": 49, "color": "#CC785C", "logo": "anthropic"},
        {"label": "Kimi K3.1 Pro", "score": 46, "color": "#0066FF", "logo": "kimi"},
        {"label": "Muse Wonder (max)", "score": 44, "color": "#0088F4", "logo": "meta"},
        {"label": "Claude Haiku 5.5 (max)", "score": 36, "color": "#C57B5E", "logo": "anthropic"},
        {"label": "Grok 4.7 (xhigh)", "score": 35, "color": "#726DD1", "logo": "xai"},
        {"label": "Tencent Hy4", "score": 35, "color": "#59B5FE", "logo": "tencent"},
        {"label": "Qwen 3.8 Max (0902)", "score": 34, "color": "#FF6D10", "logo": "qwen"},
        {"label": "DeepSeek V4.1 Flash 1017 (max)", "score": 33, "color": "#2444E5", "logo": "deepseek"},
        {"label": "GLM-5.3 (max)", "score": 32, "color": "#2681FF", "logo": "zhipu"},
        {"label": "Gemini 3.8 Flash (high)", "score": 31, "color": "#45A75A", "logo": "google"},
        {"label": "MiMo-V2.6-Pro", "score": 30, "color": "#F46E19", "logo": "xiaomi"},
        {"label": "Ling 3.1 Flash 1019", "score": 30, "color": "#5CA8DC", "logo": "ling"},
        {"label": "MiniMax-M3.1-Flash", "score": 29, "color": "#DB3968", "logo": "minimax"},
        {"label": "GPT-6 Luna (max)", "score": 28, "color": "#1F1F1F", "logo": "openai"},
        {"label": "Mistral Large 4 (high)", "score": 26, "color": "#D46240", "logo": "mistral"},
        {"label": "Muse Spark Open (xhigh)", "score": 25, "color": "#499DDB", "logo": "meta"},
        {"label": "Qwen 3.8 27B (xhigh)", "score": 20, "color": "#FF6C1A", "logo": "qwen"},
        {"label": "K2 Horizon 375B A23B", "score": 18, "color": "#1520AE", "logo": "k2"},
        {"label": "Beam 1.0", "score": 18, "color": "#175524", "logo": "beam"},
        {"label": "Nemotron 3.5 Super VL", "score": 14, "color": "#7CB409", "logo": "nvidia"},
        {"label": "Inkling (xhigh)", "score": 12, "color": "#6C7175", "logo": "inkling"},
    ]


def get_research_skills_data() -> list[dict]:
    """The 22 core scientific skills ranked by Task Outcome Win Rate & Mechanical Reliability."""
    return [
        {"label": "acm-sigconf (ACM)", "score": 100, "color": "#22C55E", "pattern": "checkered-green", "logo": "acm"},
        {"label": "nature-portfolio (Nature)", "score": 96, "color": "#D32F2F", "logo": "nature"},
        {"label": "cell-press (Cell)", "score": 95, "color": "#0288D1", "logo": "cell"},
        {"label": "research-skill-creator", "score": 94, "color": "#10B981", "logo": "kalaris"},
        {"label": "unslop-academic-writing", "score": 92, "color": "#10B981", "logo": "kalaris"},
        {"label": "citation-verification", "score": 91, "color": "#3F51B5", "logo": "crossref"},
        {"label": "springer-lncs (Springer)", "score": 89, "color": "#003366", "logo": "springer"},
        {"label": "ieee-transactions (IEEE)", "score": 88, "color": "#00629B", "logo": "ieee"},
        {"label": "science-aaas (Science)", "score": 86, "color": "#CC785C", "logo": "science"},
        {"label": "bibtex-hygiene", "score": 85, "color": "#FF6D10", "logo": "book"},
        {"label": "reproducibility-statement", "score": 84, "color": "#2444E5", "logo": "shield"},
        {"label": "arxiv-submission (arXiv)", "score": 82, "color": "#B31B1B", "logo": "arxiv"},
        {"label": "apa7 (APA)", "score": 79, "color": "#2E7D32", "logo": "apa"},
        {"label": "cover-letter-to-editor", "score": 77, "color": "#C57B5E", "logo": "book"},
        {"label": "systematic-review-prisma", "score": 76, "color": "#5C2D91", "logo": "shield"},
        {"label": "research-knowledge-graph", "score": 74, "color": "#4F46E5", "logo": "brain"},
        {"label": "elsevier-cas (Elsevier)", "score": 72, "color": "#FF6D00", "logo": "elsevier"},
        {"label": "paper-corpus-rag", "score": 68, "color": "#0EA5E9", "logo": "book"},
        {"label": "reference-manager-interop", "score": 65, "color": "#DB3968", "logo": "crossref"},
        {"label": "plos (PLOS ONE)", "score": 62, "color": "#5C2D91", "logo": "plos"},
        {"label": "abstract-and-title", "score": 58, "color": "#6C7175", "logo": "book"},
        {"label": "rebuttal-and-response", "score": 54, "color": "#D46240", "logo": "shield"},
    ]


def get_disciplines_data() -> list[dict]:
    """The 19 scientific disciplines ranked by Quality & Compliance Rubric score."""
    return [
        {"label": "chemistry-drug-discovery (12)", "score": 98.7, "score_display": "99", "color": "#22C55E", "pattern": "checkered-green", "logo": "flask"},
        {"label": "ml-training (32 skills)", "score": 96.8, "score_display": "97", "color": "#EA580C", "logo": "brain"},
        {"label": "life-sciences (33 skills)", "score": 96.6, "score_display": "97", "color": "#059669", "logo": "dna"},
        {"label": "ml-inference-and-ops (13)", "score": 96.1, "score_display": "96", "color": "#1E3A8A", "logo": "brain"},
        {"label": "knowledge-and-rag (7 skills)", "score": 95.9, "score_display": "96", "color": "#0284C7", "logo": "book"},
        {"label": "journal-formats (11 skills)", "score": 95.8, "score_display": "96", "color": "#D32F2F", "logo": "nature"},
        {"label": "lab-automation (11 skills)", "score": 95.6, "score_display": "96", "color": "#0D9488", "logo": "flask"},
        {"label": "multimodal-and-emerging (18)", "score": 95.6, "score_display": "96", "color": "#9333EA", "logo": "atom"},
        {"label": "data-science-and-ml (30)", "score": 95.3, "score_display": "95", "color": "#4F46E5", "logo": "brain"},
        {"label": "literature-review (18 skills)", "score": 94.8, "score_display": "95", "color": "#2563EB", "logo": "book"},
        {"label": "physical-sciences (10 skills)", "score": 94.6, "score_display": "95", "color": "#7C3AED", "logo": "atom"},
        {"label": "visualization-presentation (11)", "score": 94.4, "score_display": "94", "color": "#E11D48", "logo": "nature"},
        {"label": "research-automation (9 skills)", "score": 94.3, "score_display": "94", "color": "#10B981", "logo": "kalaris"},
        {"label": "ml-evaluation-safety (11)", "score": 94.3, "score_display": "94", "color": "#DB2777", "logo": "shield"},
        {"label": "scientific-databases (12)", "score": 94.1, "score_display": "94", "color": "#475569", "logo": "crossref"},
        {"label": "clinical-and-health (7 skills)", "score": 93.8, "score_display": "94", "color": "#DC2626", "logo": "shield"},
        {"label": "research-writing (15 skills)", "score": 93.4, "score_display": "93", "color": "#CC785C", "logo": "kalaris"},
        {"label": "llm-applications (9 skills)", "score": 91.5, "score_display": "92", "color": "#2563EB", "logo": "brain"},
        {"label": "ideation-and-design (12)", "score": 91.2, "score_display": "91", "color": "#F59E0B", "logo": "book"},
    ]


def get_verification_guardrails_data() -> list[dict]:
    """Hallucination detection, citation verification, and anti-slop accuracy."""
    return [
        {"label": "Crossref DOI Verified", "score": 100, "score_display": "100%", "color": "#22C55E", "pattern": "checkered-green", "logo": "crossref"},
        {"label": "DOI-less Preprints Verified", "score": 100, "score_display": "100%", "color": "#22C55E", "logo": "arxiv"},
        {"label": "Fabricated Citations Caught", "score": 100, "score_display": "100%", "color": "#10B981", "logo": "shield"},
        {"label": "Corrupted Metadata Caught", "score": 100, "score_display": "100%", "color": "#10B981", "logo": "shield"},
        {"label": "Wrong First Author Flagged", "score": 100, "score_display": "100%", "color": "#059669", "logo": "shield"},
        {"label": "Claude Haiku Router (hit@3)", "score": 96, "score_display": "96%", "color": "#CC785C", "logo": "anthropic"},
        {"label": "Claude Haiku Router (hit@1)", "score": 92, "score_display": "92%", "color": "#CC785C", "logo": "anthropic"},
        {"label": "Unslop Academic Clean Rate", "score": 89, "score_display": "89%", "color": "#2563EB", "logo": "kalaris"},
        {"label": "Slop Index Reduction", "score": 83, "score_display": "83%", "color": "#0284C7", "logo": "kalaris"},
        {"label": "Human Abstract Clean Base", "score": 78, "score_display": "78%", "color": "#475569", "logo": "book"},
        {"label": "Model Vanilla Clean Rate", "score": 68, "score_display": "68%", "color": "#64748B", "logo": "openai"},
        {"label": "BM25 Router (all 281 evals)", "score": 65, "score_display": "65%", "color": "#94A3B8", "logo": "book"},
    ]


# -----------------------------------------------------------------------------
# HTML DASHBOARD BUILDER
# -----------------------------------------------------------------------------

def build_dashboard_html(benchmarks: list[dict]) -> str:
    """Build dashboard html."""
    tabs_nav = []
    tabs_content = []
    for idx, b in enumerate(benchmarks):
        active_cls = "active" if idx == 0 else ""
        tabs_nav.append(
            f'<button class="tab-btn {active_cls}" onclick="switchTab(\'{b["name"]}\', this)">{b["title"]}</button>'
        )

        rows = []
        for rank, item in enumerate(b["items"], 1):
            score_disp = item.get("score_display", str(int(round(item["score"]))))
            rows.append(
                f'<tr><td style="color:#64748B; font-weight:600;">#{rank}</td>'
                f'<td style="font-weight:600; color:#0F172A;">{item["label"]}</td>'
                f'<td style="text-align:right; font-weight:700; color:{item.get("color", "#0F172A")};">{score_disp}</td></tr>'
            )
        table_html = "".join(rows)

        display_style = "block" if idx == 0 else "none"
        tabs_content.append(f"""
        <div id="tab-{b['name']}" class="tab-pane" style="display:{display_style};">
            <div class="card-header">
                <div>
                    <h2 class="card-title">{b['title']}</h2>
                    <p class="card-desc">{b['subtitle']}</p>
                </div>
                <div class="actions">
                    <a href="{b['png_filename']}" download class="btn btn-primary">Download High-Res PNG</a>
                    <a href="{b['svg_filename']}" download class="btn btn-secondary">Download Scalable SVG</a>
                </div>
            </div>
            <div class="graphic-container">
                <img src="{b['png_filename']}" alt="{b['title']}" class="leaderboard-img" />
            </div>
            <div class="table-container">
                <table class="data-table">
                    <thead>
                        <tr>
                            <th style="width: 80px;">Rank</th>
                            <th>Entry / Benchmark Target</th>
                            <th style="text-align: right; width: 140px;">Score</th>
                        </tr>
                    </thead>
                    <tbody>
                        {table_html}
                    </tbody>
                </table>
            </div>
        </div>
        """)

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Research Agent Skills - Benchmark Suite</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
    <style>
        :root {{
            --bg: #F8FAFC;
            --card-bg: #FFFFFF;
            --border: #E2E8F0;
            --text-main: #0F172A;
            --text-muted: #64748B;
            --primary: #0F172A;
            --accent: #22C55E;
        }}
        * {{ box-sizing: border-box; margin: 0; padding: 0; }}
        body {{
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
            background-color: var(--bg);
            color: var(--text-main);
            padding: 32px 24px;
            line-height: 1.5;
        }}
        .container {{
            max-width: 1240px;
            margin: 0 auto;
        }}
        header {{
            margin-bottom: 28px;
        }}
        h1 {{
            font-size: 26px;
            font-weight: 800;
            color: var(--text-main);
            letter-spacing: -0.02em;
            margin-bottom: 6px;
        }}
        .header-desc {{
            color: var(--text-muted);
            font-size: 14px;
        }}
        .tabs {{
            display: flex;
            gap: 8px;
            border-bottom: 1px solid var(--border);
            margin-bottom: 24px;
            overflow-x: auto;
        }}
        .tab-btn {{
            background: none;
            border: none;
            padding: 10px 18px;
            font-size: 13.5px;
            font-weight: 600;
            color: var(--text-muted);
            cursor: pointer;
            border-bottom: 2px solid transparent;
            transition: all 0.15s ease;
            white-space: nowrap;
        }}
        .tab-btn:hover {{
            color: var(--text-main);
        }}
        .tab-btn.active {{
            color: var(--primary);
            border-bottom-color: var(--primary);
        }}
        .card {{
            background: var(--card-bg);
            border: 1px solid var(--border);
            border-radius: 12px;
            box-shadow: 0 1px 3px rgba(0,0,0,0.04);
            overflow: hidden;
            margin-bottom: 32px;
        }}
        .card-header {{
            display: flex;
            justify-content: space-between;
            align-items: flex-start;
            padding: 24px 28px 18px;
            border-bottom: 1px solid var(--border);
            flex-wrap: wrap;
            gap: 16px;
        }}
        .card-title {{
            font-size: 18px;
            font-weight: 700;
            letter-spacing: -0.01em;
            margin-bottom: 4px;
        }}
        .card-desc {{
            color: var(--text-muted);
            font-size: 13px;
        }}
        .actions {{
            display: flex;
            gap: 8px;
        }}
        .btn {{
            display: inline-flex;
            align-items: center;
            padding: 7px 14px;
            font-size: 12px;
            font-weight: 600;
            border-radius: 6px;
            text-decoration: none;
            transition: all 0.15s ease;
            cursor: pointer;
        }}
        .btn-primary {{
            background: var(--primary);
            color: #FFFFFF;
        }}
        .btn-primary:hover {{ background: #1E293B; }}
        .btn-secondary {{
            background: #FFFFFF;
            border: 1px solid var(--border);
            color: var(--text-main);
        }}
        .btn-secondary:hover {{ background: #F1F5F9; }}
        .graphic-container {{
            padding: 24px 28px;
            background: #FFFFFF;
            text-align: center;
            border-bottom: 1px solid var(--border);
            overflow-x: auto;
        }}
        .leaderboard-img {{
            max-width: 100%;
            height: auto;
            border-radius: 4px;
            display: inline-block;
        }}
        .table-container {{
            padding: 20px 28px 28px;
        }}
        .data-table {{
            width: 100%;
            border-collapse: collapse;
            font-size: 13px;
        }}
        .data-table th {{
            text-align: left;
            padding: 10px 14px;
            background: #F8FAFC;
            color: var(--text-muted);
            font-weight: 600;
            border-bottom: 1px solid var(--border);
        }}
        .data-table td {{
            padding: 10px 14px;
            border-bottom: 1px solid #F1F5F9;
        }}
        .data-table tr:hover td {{
            background: #F8FAFC;
        }}
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>Research Agent Skills · Benchmark Suite</h1>
            <p class="header-desc">Frontier AI model evaluations, academic task win rates, domain quality scores, and verification guardrails.</p>
        </header>

        <div class="tabs">
            {"".join(tabs_nav)}
        </div>

        <div class="card">
            {"".join(tabs_content)}
        </div>
    </div>

    <script>
        function switchTab(tabName, btn) {{
            document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
            document.querySelectorAll('.tab-pane').forEach(p => p.style.display = 'none');
            btn.classList.add('active');
            document.getElementById('tab-' + tabName).style.display = 'block';
        }}
    </script>
</body>
</html>
"""


# -----------------------------------------------------------------------------
# MAIN GENERATOR
# -----------------------------------------------------------------------------

def main():
    """Run the command-line interface."""
    print("Generating Benchmark Graphics matching reference style...")

    benchmarks = [
        {
            "name": "models",
            "items": get_frontier_models_data(),
            "max_score": 65,
            "y_ticks": [10, 20, 30, 40, 50, 60],
            "title": "Frontier AI Models Benchmark Leaderboard",
            "subtitle": "Performance on Held-out Scientific Research Tasks & Format Constraint Verification",
            "svg_filename": "benchmark_leaderboard_models.svg",
            "png_filename": "benchmark_leaderboard_models.png",
            "width": 1140,
            "height": 370,
            "bar_spacing": 36.5,
            "bar_width": 26,
            "margin_left": 70.0,
            "baseline_y": 180.0,
            "top_y": 44.0,
        },
        {
            "name": "skills",
            "items": get_research_skills_data(),
            "max_score": 105,
            "y_ticks": [20, 40, 60, 80, 100],
            "title": "Research Agent Skills - Task Outcomes Leaderboard",
            "subtitle": "Head-to-head win rate vs baseline model across 22 scientific journal & academic skills",
            "svg_filename": "benchmark_leaderboard_skills.svg",
            "png_filename": "benchmark_leaderboard_skills.png",
            "width": 1120,
            "height": 370,
            "bar_spacing": 45.0,
            "bar_width": 28,
            "margin_left": 72.0,
            "baseline_y": 180.0,
            "top_y": 44.0,
        },
        {
            "name": "disciplines",
            "items": get_disciplines_data(),
            "max_score": 105,
            "y_ticks": [20, 40, 60, 80, 100],
            "title": "Research Agent Skills - Scientific Disciplines Quality Score",
            "subtitle": "Static quality & strict policy compliance across all 19 research fields (281 skills)",
            "svg_filename": "benchmark_leaderboard_disciplines.svg",
            "png_filename": "benchmark_leaderboard_disciplines.png",
            "width": 1100,
            "height": 370,
            "bar_spacing": 51.0,
            "bar_width": 30,
            "margin_left": 75.0,
            "baseline_y": 180.0,
            "top_y": 44.0,
        },
        {
            "name": "verification",
            "items": get_verification_guardrails_data(),
            "max_score": 105,
            "y_ticks": [20, 40, 60, 80, 100],
            "title": "Research Integrity & Hallucination Guardrails Benchmark",
            "subtitle": "Citation verification accuracy, router trigger precision, and AI slop reduction",
            "svg_filename": "benchmark_leaderboard_verification.svg",
            "png_filename": "benchmark_leaderboard_verification.png",
            "width": 1060,
            "height": 370,
            "bar_spacing": 78.0,
            "bar_width": 36,
            "margin_left": 80.0,
            "baseline_y": 180.0,
            "top_y": 44.0,
        },
    ]

    for b in benchmarks:
        print(f"\nProcessing {b['name']} ({len(b['items'])} items)...")
        # Build SVG
        svg_content = build_leaderboard_svg(
            items=b["items"],
            max_score=b["max_score"],
            y_ticks=b["y_ticks"],
            width=b["width"],
            height=b["height"],
            bar_width=b["bar_width"],
            bar_spacing=b["bar_spacing"],
            margin_left=b["margin_left"],
            baseline_y=b["baseline_y"],
            top_y=b["top_y"],
        )

        # Save SVG
        svg_targets = [p for p in [PUBLIC_DIR, RESULTS_DIR, DOCS_ASSETS, ARTIFACT_DIR] if p is not None]
        for target_dir in svg_targets:
            p = target_dir / b["svg_filename"]
            p.write_text(svg_content, encoding="utf-8")

        # Render High-DPI PNG via Chrome headless
        primary_svg = PUBLIC_DIR / b["svg_filename"]
        primary_png = PUBLIC_DIR / b["png_filename"]
        render_svg_to_png(primary_svg, primary_png, width=b["width"], height=b["height"], scale=2)

        # Copy high-DPI PNG to all target directories
        png_targets = [p for p in [RESULTS_DIR, DOCS_ASSETS, ARTIFACT_DIR] if p is not None]
        for target_dir in png_targets:
            dest = target_dir / b["png_filename"]
            if primary_png.exists() and dest != primary_png:
                shutil.copy2(primary_png, dest)

    # Build and save HTML Dashboard
    html_dashboard = build_dashboard_html(benchmarks)
    dash_targets = [p for p in [PUBLIC_DIR, RESULTS_DIR, ARTIFACT_DIR] if p is not None]
    for target_dir in dash_targets:
        p = target_dir / "benchmark_dashboard.html"
        p.write_text(html_dashboard, encoding="utf-8")
        print(f"Saved Dashboard: {p}")

    print("\nAll benchmark graphics and dashboards successfully generated!")

if __name__ == "__main__":
    main()
