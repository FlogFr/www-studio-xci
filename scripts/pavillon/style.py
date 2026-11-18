"""Chart style in the I · Son identity (dark surface, Barlow, JetBrains Mono).

Categorical series use the first three slots of the validated dark palette
(blue, orange, aqua: all-pairs CVD-safe on #1c1c1c); the site amber is kept for
annotations. Fonts: put Barlow / Barlow Condensed TTFs in $FONT_DIR to match
the site; otherwise matplotlib's default sans is used.
"""
import os
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import font_manager
from PIL import Image

SURFACE = "#1c1c1c"
INK = "#ededed"
INK_SOFT = "#cfcfcf"
MUTED = "#a4a4a4"
LINE = "#2c2c2c"
GRID = "#2a2a2a"
AMBER = "#ffb000"
SERIES = ["#3987e5", "#d95926", "#199e70"]

for d in filter(None, [os.environ.get("FONT_DIR"), "/usr/share/fonts/truetype/jetbrains-mono"]):
    for f in Path(d).glob("*.ttf"):
        font_manager.fontManager.addfont(str(f))
names = {f.name for f in font_manager.fontManager.ttflist}
BODY = "Barlow" if "Barlow" in names else "DejaVu Sans"
MONO = "JetBrains Mono" if "JetBrains Mono" in names else "DejaVu Sans Mono"

plt.rcParams.update({
    "figure.facecolor": SURFACE, "axes.facecolor": SURFACE, "savefig.facecolor": SURFACE,
    "axes.edgecolor": LINE, "axes.labelcolor": INK_SOFT, "axes.titlecolor": INK,
    "xtick.color": MUTED, "ytick.color": MUTED, "text.color": INK_SOFT,
    "font.family": BODY, "font.size": 15, "axes.labelsize": 15,
    "xtick.labelsize": 13, "ytick.labelsize": 13, "legend.fontsize": 14,
    "axes.grid": True, "grid.color": GRID, "grid.linewidth": 1.0,
    "axes.spines.top": False, "axes.spines.right": False,
    "lines.linewidth": 2.4, "lines.solid_capstyle": "round",
    "legend.frameon": False, "legend.labelcolor": INK_SOFT,
})


def mono_ticks(ax):
    for lab in ax.get_xticklabels() + ax.get_yticklabels():
        lab.set_fontfamily(MONO)


def hz_axis(ax, fmin, fmax, ticks=(500, 800, 1000, 2000, 3000, 5000, 10000)):
    ax.set_xscale("log")
    ax.set_xlim(fmin, fmax)
    t = [f for f in ticks if fmin <= f <= fmax]
    ax.set_xticks(t)
    ax.set_xticklabels([f"{f/1000:g} k" if f >= 1000 else f"{f:g}" for f in t])
    ax.minorticks_off()
    ax.set_xlabel("Fréquence (Hz)")


def save(fig, path, width=1600):
    """Save as WebP at `width` px (figures are drawn at 2x their display size)."""
    path = Path(path)
    png = path.with_suffix(".png")
    fig.savefig(png, dpi=width / fig.get_figwidth())
    plt.close(fig)
    im = Image.open(png).convert("RGB")
    im.save(path, "WEBP", quality=88, method=6)
    png.unlink()
    return im.size
