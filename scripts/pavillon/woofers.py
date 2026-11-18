"""Simple directivity model of the two 12-inch drivers under the horn.

Each cone is a rigid piston in an infinite baffle (effective radius A_EFF);
the two are stacked vertically, centres SPACING apart, and play in phase.
Good enough to compare beamwidths with the horn around the crossover; the
real cabinet, cone break-up and the horn-to-woofer offset are not modelled.
"""
import numpy as np
from scipy.special import j1

C = 343.0
A_EFF = 0.13      # effective cone radius of a 12" driver (m)
SPACING = 0.33    # centre-to-centre distance of the two stacked 12" (m)


def piston(f, theta):
    x = 2 * np.pi * f / C * A_EFF * np.sin(theta)
    with np.errstate(invalid="ignore", divide="ignore"):
        d = np.where(np.abs(x) < 1e-9, 1.0, 2 * j1(x) / x)
    return np.abs(d)


def pair(f, theta):
    return np.abs(np.cos(np.pi * f / C * SPACING * np.sin(theta))) * piston(f, theta)


def beamwidth(f, plane):
    """-6 dB beamwidth (deg) of the woofer pair: 'h' = one cone wide, 'v' = the stacked pair."""
    th = np.radians(np.linspace(0, 90, 9001))
    p = piston(f, th) if plane == "h" else pair(f, th)
    below = np.nonzero(20 * np.log10(np.maximum(p, 1e-12)) < -6)[0]
    return 180.0 if len(below) == 0 else 2 * np.degrees(th[below[0]])


if __name__ == "__main__":
    for f in (630, 800, 1000, 1200, 1600, 2000, 2400):
        print(f, round(beamwidth(f, "h")), round(beamwidth(f, "v")))
