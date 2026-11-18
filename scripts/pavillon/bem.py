"""BEM simulation of a horn in a box: polar maps, directivity index, throat impedance.

Exterior Helmholtz problem solved with bempp-cl (Burton-Miller formulation,
P1 pressure). The throat disk moves with a uniform normal velocity, every other
surface is rigid. Validated against the pulsating sphere (error < 0.2 %).

    python3 bem.py <design> [fmin fmax points_per_octave]   -> results/<design>.npz
    python3 bem.py <design> --hf                             -> results/<design>-hf.npz
"""
import sys, time
from pathlib import Path
import numpy as np
import bempp_cl.api as bempp
from bempp_cl.api.operators.boundary import helmholtz, sparse
from bempp_cl.api.operators.far_field import helmholtz as ff

import mesh as meshlib
from designs import DESIGNS

C = 343.0  # speed of sound, m/s (20 degC)
HERE = Path(__file__).parent


def fibonacci_sphere(n):
    i = np.arange(n) + 0.5
    phi = np.arccos(1 - 2 * i / n)
    th = np.pi * (1 + 5 ** 0.5) * i
    return np.stack([np.cos(th) * np.sin(phi), np.sin(th) * np.sin(phi), np.cos(phi)])


def mesh_sizes(f):
    """Element size on the horn (lambda/6) and on the box (lambda/5, floored above 5 kHz)."""
    lam = C / f
    return min(0.020, lam / 6), min(0.050, max(lam / 5, 0.015))


def solve(horn, freqs, log=print):
    ang = np.radians(np.arange(-180, 181, 2.5))
    pts_h = np.stack([np.sin(ang), np.zeros_like(ang), np.cos(ang)])   # horizontal plane (x-z)
    pts_v = np.stack([np.zeros_like(ang), np.sin(ang), np.cos(ang)])   # vertical plane (y-z)
    sph = fibonacci_sphere(1200)
    res = {k: [] for k in ("ph", "pv", "di", "z", "nel")}
    cache = {}
    for f in freqs:
        k = 2 * np.pi * f / C
        hh, hb = mesh_sizes(f)
        key = (round(hh, 4), round(hb, 4))
        if key not in cache:
            v, t, throat = meshlib.build(horn, hh, hb)
            grid = bempp.Grid(v.T.copy(), t.T.astype(np.uint32).copy(), domain_indices=throat.astype(np.uint32))
            p1 = bempp.function_space(grid, "P", 1)
            # velocity data lives on the throat only: a DP0 space restricted to it
            dp0 = bempp.function_space(grid, "DP", 0, segments=[1])
            g = bempp.GridFunction(dp0, coefficients=np.ones(dp0.global_dof_count))
            area = np.linalg.norm(np.cross(v[t[:, 1]] - v[t[:, 0]], v[t[:, 2]] - v[t[:, 0]]), axis=1) / 2
            cache = {key: (grid, p1, dp0, g, v, t, throat, area)}
        grid, p1, dp0, g, v, t, throat, area = cache[key]
        t0 = time.time()
        eta = 1j / k
        # dense Galerkin system, solved directly (GMRES stalls on these bodies)
        dense = lambda op: op.weak_form().A if not hasattr(op.weak_form().A, "toarray") else op.weak_form().A.toarray()
        A = dense(helmholtz.double_layer(p1, p1, p1, k))
        A *= -1
        A -= eta * dense(helmholtz.hypersingular(p1, p1, p1, k))
        A += 0.5 * dense(sparse.identity(p1, p1, p1))
        B = (-dense(helmholtz.single_layer(dp0, p1, p1, k))
             + eta * (0.5 * dense(sparse.identity(dp0, p1, p1)) + dense(helmholtz.adjoint_double_layer(dp0, p1, p1, k))))
        pc = np.linalg.solve(A, B @ g.coefficients)
        del A, B
        sol = bempp.GridFunction(p1, coefficients=pc)
        # mean pressure on the throat -> normalised throat impedance z = i k <p>
        pt = pc[t[throat]].mean(axis=1)
        z = 1j * k * np.sum(pt * area[throat]) / np.sum(area[throat])

        def far(points):
            return (ff.double_layer(p1, points, k) * sol - ff.single_layer(dp0, points, k) * g)[0]
        ph, pv, ps = far(pts_h), far(pts_v), far(sph)
        p_axis = ph[len(ang) // 2]
        di = 10 * np.log10(np.abs(p_axis) ** 2 / np.mean(np.abs(ps) ** 2))
        # constant throat velocity: pressure scales with k for unit Neumann data
        res["ph"].append(1j * k * ph)
        res["pv"].append(1j * k * pv)
        res["di"].append(di)
        res["z"].append(z)
        res["nel"].append(len(t))
        log(f"{f:7.0f} Hz  {len(t):6d} el  DI={di:5.1f} dB  z={z.real:.2f}{z.imag:+.2f}j  "
            f"{time.time() - t0:5.1f} s")
    return dict(freqs=np.asarray(freqs), angles=np.degrees(ang),
                **{k: np.asarray(v) for k, v in res.items()})


def octave_freqs(fmin, fmax, ppo):
    n = int(round(np.log2(fmax / fmin) * ppo))
    return fmin * 2 ** (np.arange(n + 1) / ppo)


if __name__ == "__main__":
    name = sys.argv[1]
    horn = DESIGNS[name]
    if "--hf" in sys.argv:
        freqs, tag = octave_freqs(6350, 10080, 3), f"{name}-hf"
    else:
        fmin, fmax, ppo = (float(a) for a in sys.argv[2:5]) if len(sys.argv) > 4 else (500, 5040, 6)
        freqs, tag = octave_freqs(fmin, fmax, ppo), name
    print(horn.summary(), flush=True)
    out = solve(horn, freqs, log=lambda s: print(s, flush=True))
    dest = HERE / "results"
    dest.mkdir(exist_ok=True)
    np.savez_compressed(dest / f"{tag}.npz", **out, params=str(horn.as_dict()))
    print("saved", dest / f"{tag}.npz")
