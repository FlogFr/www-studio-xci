"""Charts for the article (WebP, 1600 px wide) from the BEM results.

    python3 plots.py <outdir>
"""
import sys
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap

import style as st
from horn import keele_dimension, keele_frequency
from designs import DESIGNS, RETAINED, COMPARED

HERE = Path(__file__).parent
RES = HERE / "results"


def load(name, hf=True):
    """Results of a design, with its high-frequency run appended when present."""
    d = np.load(RES / f"{name}.npz")
    r = {k: d[k] for k in d.files if k != "params"}
    if hf and (RES / f"{name}-hf.npz").exists():
        h = np.load(RES / f"{name}-hf.npz")
        for k in ("freqs", "ph", "pv", "di", "z", "nel"):
            r[k] = np.concatenate([r[k], h[k]])
    return r


def table(res, freqs=(630, 800, 1000, 1250, 1600, 2000, 2500, 3150, 4000, 5000, 6300, 8000, 10000)):
    """Markdown rows: frequency, horizontal and vertical -6 dB beamwidth, DI (nearest computed points)."""
    bh, bv = beamwidth(res["ph"], res["angles"]), beamwidth(res["pv"], res["angles"])
    rows = []
    for f in freqs:
        i = int(np.argmin(np.abs(np.log(res["freqs"] / f))))
        if abs(np.log2(res["freqs"][i] / f)) > 0.1:
            continue
        lab = f"{f / 1000:g} kHz".replace(".", ",") if f >= 1000 else f"{f} Hz"
        rows.append(f"| {lab} | {bh[i]:.0f}° | {bv[i]:.0f}° | {res['di'][i]:.1f} dB |".replace(".", ","))
    return "\n".join(rows)


def norm_db(p):
    """dB relative to on-axis, per frequency (rows)."""
    a = np.abs(p)
    c = a.shape[1] // 2
    return 20 * np.log10(np.maximum(a, 1e-12) / a[:, c:c + 1])


def beamwidth(p, ang, level=-6.0):
    """-6 dB beamwidth (deg) per frequency, linear interpolation between samples."""
    db = norm_db(p)
    c = len(ang) // 2
    out = []
    for row in db:
        edges = []
        for rng in (range(c, len(ang) - 1), range(c, 0, -1)):
            step = 1 if rng.step == 1 else -1
            e = ang[-1] if step == 1 else ang[0]
            for i in rng:
                j = i + step
                if row[j] < level <= row[i]:
                    t = (row[i] - level) / (row[i] - row[j])
                    e = ang[i] + t * (ang[j] - ang[i])
                    break
            edges.append(e)
        out.append(edges[0] - edges[1])
    return np.asarray(out)


def fig_keele(out, retained):
    f = np.geomspace(400, 10000, 300)
    fig, ax = plt.subplots(figsize=(8, 4.6))
    for i, (ang, lab) in enumerate(((80, "80° (horizontal)"), (40, "40° (vertical)"))):
        ax.plot(f, keele_dimension(ang, f) * 100, color=st.SERIES[i], label=lab)
    ax.axvline(800, color=st.AMBER, lw=1.2, ls=(0, (4, 3)))
    ax.text(820, 92, "coupure 800 Hz", color=st.INK_SOFT, fontsize=13)
    for i, (ang, dim) in enumerate(((80, 39.7), (40, 79.4))):
        ax.plot([800], [dim], "o", ms=8, color=st.SERIES[i], mec=st.SURFACE, mew=2)
        ax.annotate(f"{dim:.0f} cm", (800, dim), xytext=(-62, 2), textcoords="offset points",
                    color=st.INK, fontsize=14, fontfamily=st.MONO)
    W, H = retained.mouth_width * 100, retained.mouth_height * 100
    for i, (ang, dim, lab) in enumerate(((80, W, "largeur"), (40, H, "hauteur"))):
        fk = keele_frequency(ang, dim / 100)
        ax.plot([fk], [dim], "s", ms=8, color=st.SERIES[i], mec=st.SURFACE, mew=2)
        ax.annotate(f"{lab} retenue {dim:.0f} cm : {fk/1000:.1f} kHz".replace(".", ","), (fk, dim),
                    xytext=(10, 6), textcoords="offset points", color=st.INK, fontsize=13)
    st.hz_axis(ax, 400, 10000)
    ax.set_ylim(0, 100)
    ax.set_ylabel("Dimension de bouche (cm)")
    ax.legend(loc="upper right", handlelength=1.6)
    st.mono_ticks(ax)
    fig.tight_layout()
    return st.save(fig, out)


def fig_profiles(out, horns):
    """Half-profiles of the wall in both planes (colour = plane, line style = design)."""
    fig, ax = plt.subplots(figsize=(8, 4.6))
    styles = ["-", (0, (5, 3))]
    for j, (h, lab) in enumerate(horns):
        z = np.linspace(0, h.L, 400)
        for i, (phi, plane) in enumerate(((0.0, "horizontal"), (np.pi / 2, "vertical"))):
            ax.plot(z * 1000, h.radius(z, phi) * 1000, color=st.SERIES[i], ls=styles[j], label=f"{plane} · {lab}")
    ax.set_aspect("equal")
    ax.set_xlim(0, max(h.L for h, _ in horns) * 1000 + 5)
    ax.set_ylim(0, 220)
    ax.set_xlabel("Profondeur depuis la gorge (mm)")
    ax.set_ylabel("Distance à l'axe (mm)")
    ax.legend(loc="upper left", fontsize=12, bbox_to_anchor=(1.02, 1), borderaxespad=0)
    st.mono_ticks(ax)
    fig.tight_layout()
    return st.save(fig, out)


CMAP = LinearSegmentedColormap.from_list(
    "amber", ["#1c1c1c", "#3a2a06", "#6b4a00", "#a87400", "#e09a00", "#ffc040", "#fff0c8"])


def fig_polar_map(out, res, plane, title):
    p = res["ph"] if plane == "h" else res["pv"]
    f, ang = res["freqs"], res["angles"]
    db = norm_db(p)
    keep = np.abs(ang) <= 90
    fig, ax = plt.subplots(figsize=(8, 4.4))
    levels = np.arange(-24, 1, 3)
    cs = ax.contourf(f, ang[keep], np.clip(db[:, keep].T, -24, 0), levels=levels, cmap=CMAP, extend="min")
    ax.contour(f, ang[keep], db[:, keep].T, levels=[-6], colors=[st.INK], linewidths=1.6)
    target = 40 if plane == "h" else 20
    for s in (1, -1):
        ax.axhline(s * target, color=st.SERIES[0], lw=1.4, ls=(0, (4, 3)))
    ax.text(f[0] * 1.03, target + 3, f"cible ±{target}°", color=st.INK, fontsize=12,
            bbox=dict(fc=st.SURFACE, ec="none", alpha=0.85, pad=2))
    st.hz_axis(ax, f[0], f[-1])
    ax.set_ylim(-90, 90)
    ax.set_yticks(range(-90, 91, 30))
    ax.set_ylabel("Angle hors axe (°)")
    ax.grid(False)
    cb = fig.colorbar(cs, ax=ax, pad=0.02, ticks=levels[::2])
    cb.set_label("dB / axe", color=st.INK_SOFT)
    cb.ax.tick_params(colors=st.MUTED)
    cb.outline.set_edgecolor(st.LINE)
    for lab in cb.ax.get_yticklabels():
        lab.set_fontfamily(st.MONO)
    ax.set_title(title, fontsize=14, loc="left", color=st.INK_SOFT)
    st.mono_ticks(ax)
    fig.tight_layout()
    return st.save(fig, out)


def fig_beamwidth(out, runs):
    """runs: list of (label, res, linestyle)."""
    fig, ax = plt.subplots(figsize=(8, 4.6))
    for label, res, ls in runs:
        f = res["freqs"]
        for i, (key, plane) in enumerate((("ph", "horizontal"), ("pv", "vertical"))):
            bw = beamwidth(res[key], res["angles"])
            ax.plot(f, bw, color=st.SERIES[i], ls=ls, marker="o" if ls == "-" else None, ms=4,
                    label=f"{plane} · {label}")
    for t in (80, 40):
        ax.axhline(t, color=st.MUTED, lw=1.0, ls=(0, (1, 3)))
        ax.text(0.995, t + 2, f"cible {t}°", transform=ax.get_yaxis_transform(), ha="right", va="bottom",
                fontsize=12, color=st.MUTED)
    ax.axvline(800, color=st.AMBER, lw=1.2, ls=(0, (4, 3)))
    f_all = np.concatenate([r["freqs"] for _, r, _ in runs])
    st.hz_axis(ax, f_all.min(), f_all.max())
    ax.set_ylim(0, 180)
    ax.set_yticks(range(0, 181, 20))
    ax.set_ylabel("Largeur à −6 dB (°)")
    ax.legend(loc="upper right", fontsize=12, ncol=1, bbox_to_anchor=(1, 1.0))
    st.mono_ticks(ax)
    fig.tight_layout()
    return st.save(fig, out)


def fig_impedance(out, res):
    f, z = res["freqs"], res["z"]
    fig, ax = plt.subplots(figsize=(8, 4.2))
    ax.plot(f, z.real, color=st.SERIES[0], marker="o", ms=4, label="résistance")
    ax.plot(f, z.imag, color=st.SERIES[1], marker="o", ms=4, label="réactance")
    ax.axhline(0, color=st.MUTED, lw=1)
    ax.axvline(800, color=st.AMBER, lw=1.2, ls=(0, (4, 3)))
    st.hz_axis(ax, f[0], f[-1])
    ax.set_ylabel("Impédance de gorge (normalisée)")
    ax.legend(loc="lower right")
    st.mono_ticks(ax)
    fig.tight_layout()
    return st.save(fig, out)


if __name__ == "__main__":
    out = Path(sys.argv[1] if len(sys.argv) > 1 else HERE / "out")
    out.mkdir(parents=True, exist_ok=True)
    ret = DESIGNS[RETAINED]
    print("keele", fig_keele(out / "keele.webp", ret))
    cmp_name = COMPARED
    print("profils", fig_profiles(out / "profils.webp", [(ret, "retenu"), (DESIGNS[cmp_name], "guide d'onde OS pur")]))
    r = load(RETAINED)
    print("polaire-h", fig_polar_map(out / "polaire-h.webp", r, "h", "Plan horizontal"))
    print("polaire-v", fig_polar_map(out / "polaire-v.webp", r, "v", "Plan vertical"))
    print("largeur", fig_beamwidth(out / "largeur.webp", [("retenu", r, "-"), ("OS pur", load(cmp_name), (0, (5, 3)))]))
    print("impedance", fig_impedance(out / "impedance.webp", r))
    for name in (RETAINED, cmp_name, "flare-fort"):
        print(f"\n{name}\n" + table(load(name)))
