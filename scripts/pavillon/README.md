# Constant-directivity horn — design scripts

Everything behind `/son/pavillon-directivite-constante/`: the horn geometry, the
BEM simulation, the charts, the dimensioned drawing and the printable STL parts.
Excluded from the Jekyll build (`scripts/` is in `exclude`).

| File | Role |
|------|------|
| `horn.py` | OS-SE profile (`Horn` dataclass), Keele and Molloy formulas |
| `designs.py` | the compared candidates and the retained design (`RETAINED`) |
| `woofers.py` | piston model of the two stacked 12″ (directivity around the crossover) |
| `mesh.py` | closed BEM body: horn in a rectangular box, symmetric rings |
| `bem.py` | bempp-cl solver (Burton-Miller, dense LU): polars, DI, throat impedance → `results/<design>.npz` |
| `plots.py` | article charts (WebP) from `results/` |
| `cad.py` | printable quadrants (manifold3d) → STL |
| `plan.py` | dimensioned drawing (WebP) and 1:1 baffle template (SVG) |
| `style.py` | chart style (I · Son colours, Barlow / JetBrains Mono) |
| `render/` | three.js renders: `export.py` (STL inputs), `index.html` + `shoot.js` + `views.json` (headless Chromium), `finish.py` (crop, WebP) |
| `results/` | BEM results (`.npz`): retained design (1/6 octave + `-hf`), compared candidates (1/3 octave) |

## Constraints

- Printer bed 220 × 220 × 220 mm: a quadrant must stay within 220 × 220 mm
  and 220 mm high (it is 219 × 133 × 195 mm).
- Inner walls ≤ 50° from the axis (`max_angle`), so a quadrant prints
  mouth-down without supports.

## Setup

```
pip install numpy scipy matplotlib bempp-cl numba manifold3d trimesh networkx shapely
```

`bempp-cl` installs as the `bempp_cl` module. Charts use Barlow / Barlow
Condensed when their TTF files are in `$FONT_DIR` (otherwise the default sans).

## Commands

```
python3 bem.py <design> 500 5040 6       # 1/6-octave BEM run, ~20 min on 4 cores
python3 bem.py <design> --hf             # 6.3, 8, 10 kHz (finer horn mesh), ~20 min
python3 plots.py ../../assets/img/pavillon
python3 plan.py  ../../assets/img/pavillon
python3 cad.py   <design> out/           # STL, then zip the two quadrants
cd render && npm install && python3 export.py && python3 -m http.server 8765 &
node shoot.js views.json && python3 finish.py ../../../assets/img/pavillon
```

## Model and its limits

- Exterior Helmholtz problem, P1 pressure, Burton-Miller coupling `i/k`,
  checked against the pulsating sphere (error < 0.2 %) and a mesh-convergence
  run (coarse vs fine: DI within 0.05 dB, beamwidths identical).
- Mesh: λ/6 on the horn (20 mm max), λ/5 on the box (50 mm max, 15 mm min).
- The throat is a flat piston with a uniform velocity: the driver's phase plug
  and its own response are not modelled. Levels are relative (normalised on
  axis); the impedance is normalised to ρc/S at the throat.
- The horn sits in a box 30 mm larger than its mouth on every side and 120 mm
  deeper than the throat: the real cabinet will change the response below
  ~1 kHz.
