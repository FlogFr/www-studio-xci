"""Closed boundary mesh of a horn mounted in a rectangular box, for the BEM.

The body is a single sequence of closed rings, stitched together:
throat disk (vibrating) -> horn wall -> front baffle -> box sides -> box back.
Rings are sampled by arc length (target element size h) and mirrored so the
mesh keeps both symmetry planes of the horn.
"""
import numpy as np
import trimesh


def _quadrant_params(curve, h, corners=(), nmin=4):
    """Azimuths in [0, pi/2] sampling curve(phi) about h apart (corners kept)."""
    knots = [0.0, *sorted(corners), np.pi / 2]
    out = []
    for a, b in zip(knots[:-1], knots[1:]):
        t = np.linspace(a, b, 400)
        pts = curve(t)
        s = np.concatenate([[0], np.cumsum(np.linalg.norm(np.diff(pts, axis=0), axis=1))])
        n = max(nmin, int(np.ceil(s[-1] / h)))
        out.append(np.interp(np.linspace(0, s[-1], n + 1), s, t)[:-1])
    return np.concatenate(out)


def ring_params(curve, h, corners=(), nmin=4):
    """Full-turn azimuths, symmetric about both axes, starting at 0."""
    q = _quadrant_params(curve, h, corners, nmin)          # [0, pi/2)
    q2 = np.pi - q[::-1][:-1]                               # (pi/2, pi)
    half = np.concatenate([q, [np.pi / 2], q2])             # [0, pi)
    return np.concatenate([half, np.pi + half])             # [0, 2pi)


def zipper(ia, pa, ib, pb):
    """Triangulate the band between two closed rings (index and azimuth arrays)."""
    tris = []
    na, nb = len(ia), len(ib)
    i = j = 0
    while i < na or j < nb:
        a_next = pa[(i + 1) % na] + (2 * np.pi if i + 1 >= na else 0)
        b_next = pb[(j + 1) % nb] + (2 * np.pi if j + 1 >= nb else 0)
        if j >= nb or (i < na and a_next <= b_next):
            tris.append((ia[i % na], ib[j % nb], ia[(i + 1) % na]))
            i += 1
        else:
            tris.append((ia[i % na], ib[j % nb], ib[(j + 1) % nb]))
            j += 1
    return tris


def rect_point(phi, w, hgt):
    c, s = np.cos(phi), np.sin(phi)
    with np.errstate(divide="ignore"):
        k = np.minimum(np.where(np.abs(c) > 1e-12, (w / 2) / np.abs(c), np.inf),
                       np.where(np.abs(s) > 1e-12, (hgt / 2) / np.abs(s), np.inf))
    return k * c, k * s


def build(horn, h_horn, h_box, margin=0.03, back=0.12):
    """Return (vertices, triangles, throat_mask) of the closed body."""
    verts, tris, throat_tris = [], [], []
    rings = []  # list of (index array, phi array)

    def add_ring(points, phi):
        start = len(verts)
        verts.extend(points)
        rings.append((np.arange(start, start + len(points)), phi))

    # throat disk: centre point then rings out to the throat circle
    centre = len(verts)
    verts.append((0.0, 0.0, 0.0))
    r0 = horn.r0
    nr = 3
    for k in range(1, nr + 1):
        rr = r0 * k / nr
        phi = ring_params(lambda t: np.stack([rr * np.cos(t), rr * np.sin(t)], 1), h_horn / 2, nmin=2 * k)
        add_ring(np.stack([rr * np.cos(phi), rr * np.sin(phi), np.zeros_like(phi)], 1), phi)
    # fan from the centre
    ia, pa = rings[0]
    for i in range(len(ia)):
        tris.append((centre, ia[i], ia[(i + 1) % len(ia)]))
    throat_rings = len(rings)

    # horn wall
    zs = horn.z_samples(h_horn)
    for z in zs[1:]:
        curve = lambda t, z=z: horn.point(z, t)[:, :2]
        phi = ring_params(curve, h_horn, nmin=6)
        add_ring(horn.point(z, phi), phi)
    mouth_ring = len(rings) - 1

    # front baffle: rays from the mouth contour to the box outline
    W = horn.mouth_width + 2 * margin
    H = horn.mouth_height + 2 * margin
    corner = np.arctan2(H, W)
    nb = max(2, int(np.ceil((max(W - horn.mouth_width, H - horn.mouth_height) / 2 + 0.05) / h_box)))
    for k in range(1, nb + 1):
        t = k / nb

        def curve(ph, t=t):
            m = horn.point(horn.L, ph)[:, :2]
            rx, ry = rect_point(ph, W, H)
            return (1 - t) * m + t * np.stack([rx, ry], 1)
        hh = h_horn + (h_box - h_horn) * t
        phi = ring_params(curve, hh, corners=(corner,) if k == nb else (), nmin=6)
        xy = curve(phi)
        add_ring(np.column_stack([xy, np.full(len(phi), horn.L)]), phi)

    # box sides
    z_back = -back
    depth = horn.L - z_back
    ns = max(2, int(np.ceil(depth / h_box)))
    rect_curve = lambda ph: np.stack(rect_point(ph, W, H), 1)
    phi_r = ring_params(rect_curve, h_box, corners=(corner,), nmin=4)
    rx, ry = rect_point(phi_r, W, H)
    for k in range(1, ns + 1):
        z = horn.L - depth * k / ns
        add_ring(np.column_stack([rx, ry, np.full(len(phi_r), z)]), phi_r)

    # back face, shrinking to a centre point
    nbk = max(2, int(np.ceil(0.5 * max(W, H) / h_box)))
    for k in range(1, nbk):
        t = 1 - k / nbk

        def curve(ph, t=t):
            return t * np.stack(rect_point(ph, W, H), 1)
        phi = ring_params(curve, h_box, corners=(corner,), nmin=2)
        xy = curve(phi)
        add_ring(np.column_stack([xy, np.full(len(phi), z_back)]), phi)

    # stitch consecutive rings
    for k in range(len(rings) - 1):
        (ia, pa), (ib, pb) = rings[k], rings[k + 1]
        band = zipper(ia, pa, ib, pb)
        if k < throat_rings - 1:
            throat_tris.extend(range(len(tris), len(tris) + len(band)))
        tris.extend(band)
    throat_tris.extend(range(0, len(rings[0][0])))  # the centre fan
    last = len(verts)
    verts.append((0.0, 0.0, z_back))
    ia, pa = rings[-1]
    for i in range(len(ia)):
        tris.append((ia[i], last, ia[(i + 1) % len(ia)]))

    v = np.asarray(verts, dtype=float)
    f = np.asarray(tris, dtype=np.int64)
    mesh = trimesh.Trimesh(v, f, process=False)
    mesh.fix_normals()
    assert mesh.is_watertight, "BEM body is not watertight"
    assert mesh.volume > 0
    throat = np.zeros(len(f), dtype=bool)
    throat[np.asarray(throat_tris)] = True
    return np.asarray(mesh.vertices), np.asarray(mesh.faces), throat


if __name__ == "__main__":
    import sys
    from horn import Horn
    h = Horn()
    v, f, th = build(h, 0.02, 0.05)
    m = trimesh.Trimesh(v, f, process=False)
    print(h.summary())
    print("vertices", len(v), "triangles", len(f), "throat", th.sum(), "watertight", m.is_watertight,
          "volume", m.volume)
    # throat normals must point +z (into the horn)
    n = m.face_normals[th]
    print("throat normal z mean", n[:, 2].mean())
    print("throat area", m.area_faces[th].sum(), "expected", np.pi * h.r0 ** 2)
    if len(sys.argv) > 1:
        m.export(sys.argv[1])
