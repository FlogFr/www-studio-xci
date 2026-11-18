"""Horn geometry: an OS-SE waveguide (oblate spheroid + super-ellipse termination).

Coordinates (metres): z along the axis, from the throat (z = 0) to the mouth
(z = L); x horizontal, y vertical. A wall point at azimuth phi (0 = horizontal
plane, 90 deg = vertical plane) and depth z sits at radius r(z, phi) from the
axis:

    r(z) = sqrt(r0^2 + 2 r0 z tan(a0) + z^2 tan(a)^2)                # OS part
         + s L / q * (1 - (1 - (q z / L)^n)^(1/n))                  # SE termination

a0 is the throat (driver exit) angle, a the asymptotic half-angle in that
direction, s the strength of the mouth flare, n its shape and q < 1 keeps the
wall slope finite at the mouth. The half-angle and the flare strength vary with
phi between the horizontal and vertical values (super-ellipse blend, exponent p).
"""
from dataclasses import dataclass, replace, asdict
import numpy as np


@dataclass(frozen=True)
class Horn:
    name: str = "pavillon-80x40"
    r0: float = 0.0254          # throat radius (2" driver exit)
    a0: float = 0.0             # throat (driver exit) half-angle, degrees
    ah: float = 40.0            # horizontal asymptotic half-angle, degrees
    av: float = 20.0            # vertical asymptotic half-angle, degrees
    L: float = 0.20             # depth, throat to mouth plane
    sh: float = 0.25            # mouth flare strength, horizontal
    sv: float = 0.60            # mouth flare strength, vertical
    n: float = 4.0              # flare shape exponent
    q: float = 0.995            # flare truncation (< 1)
    p: float = 2.0              # azimuth blend exponent (2 = ellipse, > 2 squarer)
    max_angle: float = 0.0      # cap on the wall angle to the axis, degrees (0 = none):
                                # keeps the inside printable mouth-down without supports

    def with_(self, **kw):
        return replace(self, **kw)

    def as_dict(self):
        return asdict(self)

    # -- per-azimuth parameters ------------------------------------------------
    def angle(self, phi):
        """Asymptotic half-angle (rad) at azimuth phi (rad), super-ellipse blend."""
        th, tv = np.tan(np.radians(self.ah)), np.tan(np.radians(self.av))
        c, s = np.abs(np.cos(phi)), np.abs(np.sin(phi))
        t = 1.0 / ((c / th) ** self.p + (s / tv) ** self.p) ** (1.0 / self.p)
        return np.arctan(t)

    def flare(self, phi):
        """Flare strength at azimuth phi, same blend as the angle."""
        c, s = np.abs(np.cos(phi)), np.abs(np.sin(phi))
        w = s ** self.p / (c ** self.p + s ** self.p)
        return self.sh * (1 - w) + self.sv * w

    # -- profile ---------------------------------------------------------------
    def radius(self, z, phi):
        if self.max_angle:
            return self._capped(z, phi)
        return self.radius_raw(z, phi)

    def _table(self):
        # radius on a (z, phi) grid with the wall slope capped, integrated from the throat
        key = "_tab"
        if key not in self.__dict__:
            zz = np.linspace(0, self.L, 3001)
            pp = np.linspace(0, np.pi / 2, 361)
            r = self.radius_raw(zz[:, None], pp[None, :])
            dr = np.minimum(np.diff(r, axis=0), np.tan(np.radians(self.max_angle)) * np.diff(zz)[:, None])
            r = np.vstack([r[:1], r[:1] + np.cumsum(dr, axis=0)])
            object.__setattr__(self, key, (zz, pp, r))
        return self.__dict__[key]

    def _capped(self, z, phi):
        zz, pp, tab = self._table()
        z = np.asarray(z, dtype=float)
        ph = np.abs(np.arctan2(np.abs(np.sin(phi)), np.abs(np.cos(phi))))  # fold to [0, pi/2]
        z, ph = np.broadcast_arrays(z, ph)
        iz = np.clip((z / self.L) * (len(zz) - 1), 0, len(zz) - 1 - 1e-9)
        ip = np.clip(ph / (np.pi / 2) * (len(pp) - 1), 0, len(pp) - 1 - 1e-9)
        i0, j0 = iz.astype(int), ip.astype(int)
        fz, fp = iz - i0, ip - j0
        return ((1 - fz) * (1 - fp) * tab[i0, j0] + fz * (1 - fp) * tab[i0 + 1, j0]
                + (1 - fz) * fp * tab[i0, j0 + 1] + fz * fp * tab[i0 + 1, j0 + 1])

    def radius_raw(self, z, phi):
        z = np.asarray(z, dtype=float)
        a = self.angle(phi)
        ta0 = np.tan(np.radians(self.a0))
        os_ = np.sqrt(self.r0 ** 2 + 2 * self.r0 * z * ta0 + (z * np.tan(a)) ** 2)
        u = np.clip(self.q * z / self.L, 0.0, 1.0)
        se = self.flare(phi) * self.L / self.q * (1 - (1 - u ** self.n) ** (1 / self.n))
        return os_ + se

    def point(self, z, phi):
        r = self.radius(z, phi)
        return np.stack([r * np.cos(phi), r * np.sin(phi), np.broadcast_to(z, np.shape(r))], axis=-1)

    # -- summary -----------------------------------------------------------------
    @property
    def mouth_width(self):
        return 2 * float(self.radius(self.L, 0.0))

    @property
    def mouth_height(self):
        return 2 * float(self.radius(self.L, np.pi / 2))

    def mouth_contour(self, nphi=360):
        phi = np.linspace(0, 2 * np.pi, nphi, endpoint=False)
        return self.point(self.L, phi)

    def mouth_area(self):
        c = self.mouth_contour(720)
        x, y = c[:, 0], c[:, 1]
        return 0.5 * abs(np.dot(x, np.roll(y, 1)) - np.dot(y, np.roll(x, 1)))

    def area(self, z, nphi=360):
        """Cross-section area at depth z (flat section, for 1-D estimates)."""
        phi = np.linspace(0, 2 * np.pi, nphi, endpoint=False)
        r = self.radius(z, phi)
        return 0.5 * np.sum(r ** 2) * (2 * np.pi / nphi)

    def z_samples(self, h):
        """Depth samples about h apart along the wall, denser in the mouth flare."""
        zz = np.linspace(0, self.L, 4001)
        # wall length along the steepest meridian (max over a few azimuths)
        ds = np.zeros_like(zz)
        for phi in (0.0, np.pi / 4, np.pi / 2):
            r = self.radius(zz, phi)
            seg = np.hypot(np.diff(zz), np.diff(r))
            ds = np.maximum(ds, np.concatenate([[0], np.cumsum(seg)]))
        n = max(4, int(np.ceil(ds[-1] / h)))
        return np.interp(np.linspace(0, ds[-1], n + 1), ds, zz)

    def summary(self):
        return (f"{self.name}: L={self.L*1000:.0f} mm, mouth {self.mouth_width*1000:.0f} x "
                f"{self.mouth_height*1000:.0f} mm, angles {2*self.ah:.0f}x{2*self.av:.0f} deg, "
                f"flare sh={self.sh} sv={self.sv}")


# Keele's rule of thumb: mouth dimension (m) needed to hold a coverage angle
# (deg) down to a frequency (Hz): W = K / (angle * f), K = 25 400 m.deg.Hz.
KEELE_K = 25400.0


def keele_dimension(angle_deg, f_hz):
    return KEELE_K / (np.asarray(angle_deg) * np.asarray(f_hz))


def keele_frequency(angle_deg, dim_m):
    return KEELE_K / (np.asarray(angle_deg) * np.asarray(dim_m))


def molloy_q(h_deg, v_deg):
    """Directivity factor Q of a horn with h x v coverage (Molloy)."""
    s = np.sin(np.radians(h_deg) / 2) * np.sin(np.radians(v_deg) / 2)
    return 180.0 / np.degrees(np.arcsin(s))


if __name__ == "__main__":
    h = Horn()
    print(h.summary())
    for L in (0.15, 0.20, 0.25, 0.30):
        for sv in (0.0, 0.3, 0.6, 0.9):
            hh = h.with_(L=L, sv=sv, sh=0.0)
            print(f"L={L:.2f} sv={sv:.1f}: {hh.mouth_width*1000:.0f} x {hh.mouth_height*1000:.0f}")
    print("Keele 80 deg @800:", keele_dimension(80, 800), " 40 deg @800:", keele_dimension(40, 800))
    print("Q 80x40:", molloy_q(80, 40), "DI", 10*np.log10(molloy_q(80, 40)))
    print("Q 90x90:", molloy_q(90, 90), "DI", 10*np.log10(molloy_q(90, 90)))
