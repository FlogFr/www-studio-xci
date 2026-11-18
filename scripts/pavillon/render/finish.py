"""Crops the renders to their content (plus a margin) and saves them as WebP."""
import sys
from pathlib import Path
import numpy as np
from PIL import Image

BG = np.array([0x1c, 0x1c, 0x1c])


def finish(src, dst, width=1600, ratio=None, pad=0.06):
    im = np.asarray(Image.open(src).convert("RGB")).astype(int)
    mask = np.abs(im - BG).sum(axis=2) > 12
    ys, xs = np.nonzero(mask)
    x0, x1, y0, y1 = xs.min(), xs.max(), ys.min(), ys.max()
    w, h = x1 - x0, y1 - y0
    p = int(pad * max(w, h))
    x0, x1, y0, y1 = x0 - p, x1 + p, y0 - p, y1 + p
    if ratio:  # grow the short side to the requested width / height ratio
        w, h = x1 - x0, y1 - y0
        if w / h < ratio:
            d = int((h * ratio - w) / 2); x0, x1 = x0 - d, x1 + d
        else:
            d = int((w / ratio - h) / 2); y0, y1 = y0 - d, y1 + d
    canvas = Image.new("RGB", (x1 - x0, y1 - y0), tuple(BG))
    canvas.paste(Image.open(src).convert("RGB"), (-x0, -y0))
    height = round(width / ratio) if ratio else round(width * canvas.height / canvas.width)
    out = canvas.resize((width, height), Image.LANCZOS)
    out.save(dst, "WEBP", quality=86, method=6)
    return out.size


if __name__ == "__main__":
    dest = Path(sys.argv[1])
    dest.mkdir(parents=True, exist_ok=True)
    for name, ratio in (("rendu-3-4", 16 / 11), ("rendu-arriere", 16 / 11), ("eclate", 16 / 11), ("impression", 16 / 11)):
        print(name, finish(f"{name}.png", dest / f"{name}.webp", ratio=ratio))
