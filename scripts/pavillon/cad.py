"""Printable horn: four quadrants to bolt together, exported as STL (millimetres).

Each quadrant prints mouth-down, flange on the bed, without supports: the
inside never leans more than the profile's `max_angle` (50 deg), the outside
always faces up, the throat flange sits on a 45-degree collar. The body is the
horn wall (thickness t), a fillet on the mouth flange, the throat flange for
the driver (4 x M6 on a 101.6 mm circle, one bolt per quadrant, reached
through a notch in the collar), seam ribs with M4 bolts along the two split
planes, and screw holes in the mouth flange for mounting behind the baffle.

    python3 cad.py [design] [outdir]
"""
import sys
from dataclasses import dataclass
from pathlib import Path
import numpy as np
import trimesh
from manifold3d import Manifold, Mesh

from designs import DESIGNS, RETAINED


@dataclass(frozen=True)
class Mech:
    t: float = 4.0            # wall thickness (mm)
    t_throat: float = 7.0     # wall thickness at the throat, tapering to t
    taper: float = 60.0       # depth over which the throat thickening fades
    flange_margin: float = 14.0   # mouth flange beyond the mouth contour (min)
    t_mouth: float = 8.0      # mouth flange thickness
    fillet: float = 8.0       # 45-degree fillet between wall and mouth flange
    screw_d: float = 4.6      # mouth screw clearance (wood screw 4 mm)
    throat_r: float = 68.0    # throat flange radius
    t_throat_flange: float = 12.0
    bolt_circle: float = 101.6    # driver bolt circle diameter (4 x M6 at 90 deg)
    bolt_d: float = 6.6
    notch_w: float = 18.0     # access notch for the M6 heads, tangential width
    notch_h: float = 24.0     # and height under the throat flange
    rib_w: float = 6.0        # seam rib thickness on each side of the split plane
    rib_e: float = 16.0       # rib protrusion beyond the wall
    rib_bolt_d: float = 4.5   # M4 clearance
    rib_pitch: float = 45.0   # spacing of rib bolts along the depth


def _phi_samples(corner, n_quadrant=120):
    """Azimuths with both symmetry planes and the flange corners as samples."""
    n1 = max(8, int(round(n_quadrant * corner / (np.pi / 2))))
    q = np.concatenate([np.linspace(0, corner, n1, endpoint=False),
                        np.linspace(corner, np.pi / 2, n_quadrant - n1, endpoint=False)])
    q2 = np.pi - q[::-1][:-1]
    half = np.concatenate([q, [np.pi / 2], q2])
    return np.concatenate([half, np.pi + half])


def _rect_radius(phi, w, h):
    c, s = np.abs(np.cos(phi)), np.abs(np.sin(phi))
    with np.errstate(divide="ignore"):
        return np.minimum(np.where(c > 1e-12, (w / 2) / c, np.inf), np.where(s > 1e-12, (h / 2) / s, np.inf))


def _loft(rings):
    """Closed solid from a list of rings (each (N, 3), same N), capped at both ends."""
    R, N = len(rings), len(rings[0])
    V = np.concatenate(rings + [rings[0].mean(0, keepdims=True), rings[-1].mean(0, keepdims=True)])
    j = np.arange(N)
    j2 = (j + 1) % N
    tris = []
    for k in range(R - 1):
        a, b = k * N, (k + 1) * N
        tris.append(np.stack([a + j, b + j, b + j2], 1))
        tris.append(np.stack([a + j, b + j2, a + j2], 1))
    c0, c1 = R * N, R * N + 1
    tris.append(np.stack([np.full(N, c0), j, j2], 1))
    tris.append(np.stack([np.full(N, c1), (R - 1) * N + j2, (R - 1) * N + j], 1))
    F = np.concatenate(tris)
    # orient outwards
    vol = np.einsum("ij,ij->i", V[F[:, 0]], np.cross(V[F[:, 1]], V[F[:, 2]])).sum() / 6
    if vol < 0:
        F = F[:, ::-1]
    m = Manifold(Mesh(vert_properties=V.astype(np.float32), tri_verts=F.astype(np.uint32)))
    assert m.status().name == "NoError", m.status()
    return m


def _cyl(p0, p1, d, seg=40):
    """Cylinder of diameter d from point p0 to point p1."""
    p0, p1 = np.asarray(p0, float), np.asarray(p1, float)
    v = p1 - p0
    L = np.linalg.norm(v)
    c = Manifold.cylinder(L, d / 2, d / 2, seg)
    # rotate +z onto v
    z = np.array([0, 0, 1.0])
    u = v / L
    axis = np.cross(z, u)
    s, cth = np.linalg.norm(axis), np.dot(z, u)
    if s < 1e-9:
        R = np.eye(3) if cth > 0 else np.diag([1, -1, -1.0])
    else:
        k = axis / s
        K = np.array([[0, -k[2], k[1]], [k[2], 0, -k[0]], [-k[1], k[0], 0]])
        R = np.eye(3) + s * K + (1 - cth) * K @ K
    M = np.hstack([R, p0[:, None]])
    return c.transform(M.tolist())


class HornCAD:
    def __init__(self, horn, mech=Mech()):
        self.h, self.m = horn, mech
        L = horn.L * 1000
        self.L = L
        self.W = horn.mouth_width * 1000
        self.H = horn.mouth_height * 1000
        # flange: rectangle around the mouth contour with at least `flange_margin`
        self.Wf = self.W + 2 * mech.flange_margin
        self.Hf = self.H + 2 * mech.flange_margin
        self.corner = np.arctan2(self.Hf, self.Wf)
        self.phi = _phi_samples(self.corner)

    # inner wall radius (mm) and slope on a z grid (mm), per azimuth
    def inner(self, z):
        r = np.stack([self.h.radius(z / 1000, p) for p in self.phi], 1) * 1000  # (nz, nphi)
        return r

    def z_grid(self):
        zs = self.h.z_samples(0.002) * 1000
        return np.unique(np.concatenate([zs, np.linspace(0, self.L, 120)]))

    def cavity(self):
        z = self.z_grid()
        r = self.inner(z)
        rings = [self._ring(-6.0, np.full(len(self.phi), self.h.r0 * 1000))]
        rings += [self._ring(zz, rr) for zz, rr in zip(z, r)]
        rings.append(self._ring(self.L + 6.0, r[-1]))
        return _loft(rings)

    def _ring(self, z, r):
        return np.column_stack([r * np.cos(self.phi), r * np.sin(self.phi), np.full(len(self.phi), z)])

    def envelope(self, extra=0.0):
        """Outer solid: wall offset along the normal, with a 45-degree fillet onto the mouth flange."""
        m = self.m
        zf = self.L - m.t_mouth
        z = self.z_grid()
        z = np.unique(np.concatenate([z[z < zf], [zf]]))
        r = self.inner(z)
        slope = np.gradient(r, z, axis=0)
        t = m.t + (m.t_throat - m.t) * np.clip(1 - z / m.taper, 0, 1)
        r_out = r + (t[:, None] + extra) * np.sqrt(1 + slope ** 2)
        r_e = np.maximum(r_out, r_out[-1] + m.fillet - (zf - z)[:, None])
        rings = [self._ring(zz, rr) for zz, rr in zip(z, r_e)]
        rings.append(self._ring(self.L, r_e[-1]))
        return _loft(rings), z, r_out, r_e

    def body(self):
        m = self.m
        outer, z, r_out, r_e = self.envelope()
        solid = outer
        # mouth flange (on the bed when printing)
        solid = solid + Manifold.cube([self.Wf, self.Hf, m.t_mouth], True).translate([0, 0, self.L - m.t_mouth / 2])
        # throat flange on a 45-degree collar
        solid = solid + Manifold.cylinder(m.t_throat_flange, m.throat_r, m.throat_r, 128)
        solid = solid + Manifold.cylinder(m.throat_r, m.throat_r, 0, 128).translate([0, 0, m.t_throat_flange])
        # seam ribs along the split planes
        rib_env, _, _, _ = self.envelope(extra=m.rib_e)
        big = 2 * max(self.Wf, self.Hf, 2 * self.L)
        slab_v = Manifold.cube([2 * m.rib_w, big, self.L], True).translate([0, 0, self.L / 2])
        slab_h = Manifold.cube([big, 2 * m.rib_w, self.L], True).translate([0, 0, self.L / 2])
        inside = Manifold.cube([self.Wf, self.Hf, self.L], True).translate([0, 0, self.L / 2])
        solid = solid + (rib_env ^ (slab_v + slab_h) ^ inside)
        solid = solid - self.cavity()
        # driver bolts, one per quadrant at 45 degrees, heads reached through a notch
        rb = m.bolt_circle / 2
        inner_notch = rb - m.notch_w / 2
        k45 = int(np.argmin(np.abs(self.phi - np.pi / 4)))
        z_top = m.t_throat_flange + m.notch_h
        assert np.interp(z_top, z, r_out[:, k45]) < inner_notch - 1, "notch would cut the wall"
        for k in range(4):
            a = np.pi / 4 + k * np.pi / 2
            p = rb * np.array([np.cos(a), np.sin(a)])
            solid = solid - _cyl([*p, -1], [*p, m.t_throat_flange + 1], m.bolt_d)
            notch = Manifold.cube([m.throat_r + 10 - inner_notch, m.notch_w, m.notch_h], False)
            notch = notch.translate([inner_notch, -m.notch_w / 2, m.t_throat_flange]).rotate([0, 0, np.degrees(a)])
            solid = solid - notch
        # rib bolts: along x through the vertical-plane ribs, along y through the horizontal ones
        self.rib_bolts = []
        k90 = len(self.phi) // 4
        for k_phi, axis in ((0, 1), (k90, 0)):
            zs = np.arange(m.t_throat_flange + 30, self.L - m.t_mouth - m.fillet - 8, m.rib_pitch)
            for zz in zs:
                rr = np.interp(zz, z, r_out[:, k_phi]) + m.rib_e / 2
                for sgn in (1, -1):
                    c = [0.0, 0.0, zz]
                    c[1 - axis] = sgn * rr
                    a0, a1 = list(c), list(c)
                    a0[axis], a1[axis] = -m.rib_w - 1, m.rib_w + 1
                    solid = solid - _cyl(a0, a1, m.rib_bolt_d, 24)
                    self.rib_bolts.append((tuple(c), axis))
        # mouth screws: 3 per quadrant
        self.screws = []
        inset = 10.0
        for sx in (1, -1):
            for sy in (1, -1):
                for (x, y) in ((self.Wf / 2 - inset, self.Hf / 2 - inset),
                               (self.Wf / 4, self.Hf / 2 - inset),
                               (self.Wf / 2 - inset, self.Hf / 4)):
                    p = (sx * x, sy * y)
                    solid = solid - _cyl([*p, self.L - m.t_mouth - 1], [*p, self.L + 1], m.screw_d)
                    self.screws.append(p)
        return solid

    def quadrants(self, solid):
        """Top-right and top-left quadrants (the bottom ones are the same parts turned 180 deg)."""
        a = solid.trim_by_plane([1, 0, 0], 0).trim_by_plane([0, 1, 0], 0)
        b = solid.trim_by_plane([-1, 0, 0], 0).trim_by_plane([0, 1, 0], 0)
        return a, b


def to_trimesh(m):
    mesh = m.to_mesh()
    return trimesh.Trimesh(np.asarray(mesh.vert_properties)[:, :3], np.asarray(mesh.tri_verts), process=True)


def check_overhangs(tm, limit=51.0):
    """Area of downward faces steeper than `limit` degrees from vertical, outside the bed plane."""
    n = tm.face_normals
    down = n[:, 2] < -np.sin(np.radians(limit))
    on_bed = tm.triangles_center[:, 2] < tm.bounds[0, 2] + 0.05
    return tm.area_faces[down & ~on_bed].sum()


if __name__ == "__main__":
    name = sys.argv[1] if len(sys.argv) > 1 else RETAINED
    out = Path(sys.argv[2]) if len(sys.argv) > 2 else Path(__file__).parent / "out"
    out.mkdir(parents=True, exist_ok=True)
    horn = DESIGNS[name]
    cad = HornCAD(horn)
    body = cad.body()
    full = to_trimesh(body)
    print(horn.summary())
    print(f"flange {cad.Wf:.0f} x {cad.Hf:.0f} mm, depth {cad.L:.0f} mm, volume {full.volume/1000:.0f} cm3, "
          f"watertight {full.is_watertight}")
    full.export(out / f"{name}-assemble.stl")
    for tag, q in zip("AB", cad.quadrants(body)):
        tm = to_trimesh(q)
        tm.apply_transform(trimesh.transformations.rotation_matrix(np.pi, [1, 0, 0]))  # mouth down
        tm.apply_translation(-tm.bounds[0])
        ext = tm.bounds[1] - tm.bounds[0]
        print(f"quart {tag}: {ext[0]:.0f} x {ext[1]:.0f} x {ext[2]:.0f} mm, {tm.volume/1000:.0f} cm3, "
              f"overhang > 51 deg: {check_overhangs(tm):.0f} mm2, watertight {tm.is_watertight}")
        tm.export(out / f"{name}-quart-{tag}.stl")
