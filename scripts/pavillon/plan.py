"""Dimensioned drawing of the printed horn, and a 1:1 SVG template of the baffle cut-out.

    python3 plan.py <outdir>
"""
import sys
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon, Circle, Rectangle

import style as st
from cad import HornCAD, to_trimesh
from designs import DESIGNS, RETAINED

HERE = Path(__file__).parent
FILL = "#2a2a2a"


def dim(ax, p0, p1, text, off, horizontal=True, fs=11):
    """Dimension line between p0 and p1, offset perpendicular by `off` (data units)."""
    (x0, y0), (x1, y1) = p0, p1
    if horizontal:
        y = max(y0, y1) + off if off > 0 else min(y0, y1) + off
        for x, yy in ((x0, y0), (x1, y1)):
            ax.plot([x, x], [yy, y + np.sign(off) * 3], color=st.MUTED, lw=0.8)
        ax.annotate("", (x0, y), (x1, y), arrowprops=dict(arrowstyle="<->", color=st.INK_SOFT, lw=1, shrinkA=0, shrinkB=0))
        ax.text((x0 + x1) / 2, y + (4 if off > 0 else -4), text, ha="center", va="bottom" if off > 0 else "top",
                fontsize=fs, fontfamily=st.MONO, color=st.INK)
    else:
        x = max(x0, x1) + off if off > 0 else min(x0, x1) + off
        for xx, y in ((x0, y0), (x1, y1)):
            ax.plot([xx, x + np.sign(off) * 3], [y, y], color=st.MUTED, lw=0.8)
        ax.annotate("", (x, y0), (x, y1), arrowprops=dict(arrowstyle="<->", color=st.INK_SOFT, lw=1, shrinkA=0, shrinkB=0))
        ax.text(x + (4 if off > 0 else -4), (y0 + y1) / 2, text, ha="left" if off > 0 else "right", va="center",
                rotation=90, fontsize=fs, fontfamily=st.MONO, color=st.INK)


def section(mesh, normal, origin, to2d):
    """Polygons of a plane section, mapped to 2-D with `to2d` (3-D points -> 2-D)."""
    sec = mesh.section(plane_origin=origin, plane_normal=normal)
    return [to2d(np.asarray(c)) for c in sec.discrete]


def draw(out, horn, cad, mesh):
    """First-angle layout (ISO E): front view, side section on its right, top section below."""
    m = cad.m
    W, H = horn.mouth_width * 1000, horn.mouth_height * 1000
    mx, my = 95, 70                      # margins around each view (mm, drawing units)
    cw, ch = cad.Wf + 2 * mx, cad.Hf + 2 * my      # front view cell
    sw, sh = cad.L + 2 * my, cad.L + 2 * my        # side cell width / top cell height
    tw, th = cw + sw, ch + sh
    fig = plt.figure(figsize=(8, 8 * th / tw))

    def axes(x0, y0, w, h):
        return fig.add_axes([x0 / tw, 1 - (y0 + h) / th, w / tw, h / th])

    # front view
    ax = axes(0, 0, cw, ch)
    ax.add_patch(Rectangle((-cad.Wf / 2, -cad.Hf / 2), cad.Wf, cad.Hf, fc=FILL, ec=st.INK_SOFT, lw=1.2))
    phi = np.linspace(0, 2 * np.pi, 721)
    ax.add_patch(Polygon(horn.point(horn.L, phi)[:, :2] * 1000, closed=True, fc=st.SURFACE, ec=st.INK, lw=1.4))
    for zz in np.linspace(0, horn.L, 8)[1:-1]:
        c = horn.point(zz, phi)[:, :2] * 1000
        ax.plot(c[:, 0], c[:, 1], color=st.LINE, lw=0.8)
    ax.add_patch(Circle((0, 0), horn.r0 * 1000, fc="none", ec=st.INK, lw=1.2))
    ax.add_patch(Circle((0, 0), m.bolt_circle / 2, fc="none", ec=st.MUTED, lw=0.8, ls=(0, (4, 3))))
    for k in range(4):
        a = np.pi / 4 + k * np.pi / 2
        ax.add_patch(Circle((m.bolt_circle / 2 * np.cos(a), m.bolt_circle / 2 * np.sin(a)), m.bolt_d / 2,
                            fc="none", ec=st.INK_SOFT, lw=1))
    for (x, y) in cad.screws:
        ax.add_patch(Circle((x, y), m.screw_d / 2, fc=st.SURFACE, ec=st.INK_SOFT, lw=1))
    for xy in (([-cad.Wf / 2 - 10, cad.Wf / 2 + 10], [0, 0]), ([0, 0], [-cad.Hf / 2 - 10, cad.Hf / 2 + 10])):
        ax.plot(*xy, color=st.SERIES[0], lw=1, ls=(0, (8, 3, 2, 3)))
    dim(ax, (-cad.Wf / 2, cad.Hf / 2), (cad.Wf / 2, cad.Hf / 2), f"{cad.Wf:.0f}", 24)
    dim(ax, (-W / 2, 0), (W / 2, 0), f"bouche {W:.0f}", -cad.Hf / 2 - 28)
    dim(ax, (-cad.Wf / 2, -cad.Hf / 2), (-cad.Wf / 2, cad.Hf / 2), f"{cad.Hf:.0f}", -24, horizontal=False)
    dim(ax, (0, -H / 2), (0, H / 2), f"bouche {H:.0f}", -cad.Wf / 2 - 62, horizontal=False)
    ax.text(-cw / 2 + 6, ch / 2 - 8, "Face avant", va="top", fontsize=13, color=st.INK_SOFT)
    ax.set_xlim(-cw / 2, cw / 2)
    ax.set_ylim(-ch / 2, ch / 2)
    ax.axis("off")

    off = m.rib_w + 2   # cut just beside the seam ribs
    # side section, on the right: throat next to the front view, mouth on the far right
    ax = axes(cw, 0, sw, ch)
    for poly in section(mesh, [1, 0, 0], [off, 0, 0], lambda p: p[:, [2, 1]]):
        ax.add_patch(Polygon(poly, closed=True, fc=FILL, ec=st.INK_SOFT, lw=1))
    ax.plot([-12, cad.L + 12], [0, 0], color=st.SERIES[0], lw=1, ls=(0, (8, 3, 2, 3)))
    dim(ax, (0, -cad.Hf / 2), (cad.L, -cad.Hf / 2), f"{cad.L:.0f}", -24, fs=10)
    ax.text(0, cad.Hf / 2 + 10, "moteur", fontsize=10, color=st.MUTED)
    ax.text(cad.L, cad.Hf / 2 + 10, "bouche", ha="right", fontsize=10, color=st.MUTED)
    ax.text(-my + 6, ch / 2 - 8, "Coupe verticale", va="top", fontsize=13, color=st.INK_SOFT)
    ax.set_xlim(-my, cad.L + my)
    ax.set_ylim(-ch / 2, ch / 2)
    ax.axis("off")
    # top section, below: throat next to the front view, mouth at the bottom
    ax = axes(0, ch, cw, sh)
    for poly in section(mesh, [0, 1, 0], [0, off, 0], lambda p: np.column_stack([p[:, 0], -p[:, 2]])):
        ax.add_patch(Polygon(poly, closed=True, fc=FILL, ec=st.INK_SOFT, lw=1))
    ax.plot([0, 0], [12, -cad.L - 12], color=st.SERIES[0], lw=1, ls=(0, (8, 3, 2, 3)))
    dim(ax, (cad.Wf / 2, 0), (cad.Wf / 2, -cad.L), f"{cad.L:.0f}", 24, horizontal=False, fs=10)
    ax.text(-cad.Wf / 2 - 10, -4, "moteur", ha="right", va="top", fontsize=10, color=st.MUTED)
    ax.text(-cad.Wf / 2 - 10, -cad.L, "bouche", ha="right", va="bottom", fontsize=10, color=st.MUTED)
    ax.text(-cw / 2 + 6, my - 8, "Coupe horizontale", va="top", fontsize=13, color=st.INK_SOFT)
    ax.set_xlim(-cw / 2, cw / 2)
    ax.set_ylim(-cad.L - my, my)
    ax.axis("off")
    # notes
    ax = axes(cw, ch, sw, sh)
    ax.axis("off")
    notes = [f"gorge Ø{horn.r0 * 2000:.1f}", f"moteur : 4 × M6", f"  sur Ø{m.bolt_circle:.1f}",
             f"baffle : {len(cad.screws)} vis Ø4", f"paroi {m.t:.0f} mm", "cotes en mm"]
    for i, t in enumerate(notes):
        ax.text(0.08, 0.86 - i * 0.12, t.replace(".", ","), transform=ax.transAxes, fontsize=10.5,
                fontfamily=st.MONO, color=st.INK_SOFT if i < len(notes) - 1 else st.MUTED)
    return st.save(fig, out)


def template_svg(out, horn, cad):
    """1:1 template of the baffle cut-out (mouth contour), flange outline and screw centres."""
    phi = np.linspace(0, 2 * np.pi, 721)[:-1]
    mc = horn.point(horn.L, phi)[:, :2] * 1000
    pad = 15
    w, h = cad.Wf + 2 * pad, cad.Hf + 2 * pad + 20
    tx = lambda x: x + w / 2
    ty = lambda y: cad.Hf / 2 + pad - y
    d = "M " + " L ".join(f"{tx(x):.2f} {ty(y):.2f}" for x, y in mc) + " Z"
    parts = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{w:.1f}mm" height="{h:.1f}mm" viewBox="0 0 {w:.1f} {h:.1f}">',
             '<title>Gabarit de découpe du baffle — pavillon 80 × 40 (échelle 1:1)</title>',
             f'<rect x="{tx(-cad.Wf / 2):.2f}" y="{ty(cad.Hf / 2):.2f}" width="{cad.Wf:.2f}" height="{cad.Hf:.2f}" fill="none" stroke="#888" stroke-width="0.4" stroke-dasharray="4 2"/>',
             f'<path d="{d}" fill="none" stroke="#000" stroke-width="0.5"/>',
             f'<line x1="{tx(-cad.Wf / 2 - 8):.2f}" y1="{ty(0):.2f}" x2="{tx(cad.Wf / 2 + 8):.2f}" y2="{ty(0):.2f}" stroke="#888" stroke-width="0.25"/>',
             f'<line x1="{tx(0):.2f}" y1="{ty(cad.Hf / 2 + 8):.2f}" x2="{tx(0):.2f}" y2="{ty(-cad.Hf / 2 - 8):.2f}" stroke="#888" stroke-width="0.25"/>']
    for (x, y) in cad.screws:
        parts.append(f'<circle cx="{tx(x):.2f}" cy="{ty(y):.2f}" r="1" fill="#000"/>')
        parts.append(f'<circle cx="{tx(x):.2f}" cy="{ty(y):.2f}" r="{cad.m.screw_d / 2:.2f}" fill="none" stroke="#000" stroke-width="0.25"/>')
    parts.append(f'<rect x="{pad:.1f}" y="{h - 14:.1f}" width="100" height="0.6" fill="#000"/>')
    parts.append(f'<text x="{pad:.1f}" y="{h - 4:.1f}" font-family="monospace" font-size="5">100 mm (contrôle d\'échelle) · trait plein : découpe = contour de la bouche ({horn.mouth_width*1000:.0f} × {horn.mouth_height*1000:.0f} mm) · pointillé : bride · points : vis</text>')
    parts.append("</svg>")
    Path(out).write_text("\n".join(parts), encoding="utf-8")


if __name__ == "__main__":
    out = Path(sys.argv[1] if len(sys.argv) > 1 else HERE / "out")
    out.mkdir(parents=True, exist_ok=True)
    horn = DESIGNS[RETAINED]
    cad = HornCAD(horn)
    mesh = to_trimesh(cad.body())
    print("plan", draw(out / "plan.webp", horn, cad, mesh))
    template_svg(out / "gabarit-baffle.svg", horn, cad)
    print("template written")
