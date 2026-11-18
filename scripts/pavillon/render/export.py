"""Exports the render inputs into stl/: the assembled horn and its four quadrants in place."""
import sys
from pathlib import Path
import numpy as np
import trimesh

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from cad import HornCAD, to_trimesh  # noqa: E402
from designs import DESIGNS, RETAINED  # noqa: E402

out = Path(__file__).parent / "stl"
out.mkdir(exist_ok=True)
cad = HornCAD(DESIGNS[sys.argv[1] if len(sys.argv) > 1 else RETAINED])
body = cad.body()
to_trimesh(body).export(out / "assemble.stl")
a, b = cad.quadrants(body)
ta, tb = to_trimesh(a), to_trimesh(b)
turn = trimesh.transformations.rotation_matrix(np.pi, [0, 0, 1])
ta.export(out / "q-tr.stl")
tb.export(out / "q-tl.stl")
tb.copy().apply_transform(turn).export(out / "q-br.stl")
ta.copy().apply_transform(turn).export(out / "q-bl.stl")
print(f"flange {cad.Wf:.0f} x {cad.Hf:.0f} mm, depth {cad.L:.0f} mm")
