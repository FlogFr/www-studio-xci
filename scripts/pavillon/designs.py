"""Candidate horns compared in the article, and the retained design.

All share the 2-inch throat (r0 = 25.4 mm) and a straight driver exit (a0 = 0).
"""
from horn import Horn

DESIGNS = {
    # Plain OS waveguide, 80 x 40 walls, no mouth flare: the reference shape.
    "os-pur": Horn(name="os-pur", L=0.20, ah=40, av=20, sh=0.0, sv=0.0),
    # Strong vertical flare up to the 50-degree printing limit (taller mouth).
    "flare-fort": Horn(name="flare-fort", L=0.195, ah=45, av=20, sh=0.0, sv=2.0, n=2, max_angle=50),
    # Retained: OS-SE, horizontal walls opened to 90 deg, moderate flare near the mouth.
    "pavillon-80x40": Horn(name="pavillon-80x40", L=0.195, ah=45, av=20, sh=0.1, sv=0.6, n=4, max_angle=50),
}
RETAINED = "pavillon-80x40"
COMPARED = "os-pur"
