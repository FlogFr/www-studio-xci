#!/usr/bin/env bash
# Regenerates the raster brand images with ImageMagick:
#   favicon.ico, assets/img/favicon-32.png, apple-touch-icon.png, logo.png
#   assets/img/og/<universe>.png  (1200×630 social cards)
# Fonts default to DejaVu / JetBrains Mono system files; override with
# FONT_BOLD, FONT_COND, FONT_SERIF, FONT_MONO.
set -euo pipefail

cd "$(dirname "$0")/.."
command -v convert >/dev/null || { echo "ImageMagick (convert) is required" >&2; exit 1; }

FONT_BOLD=${FONT_BOLD:-/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf}
FONT_COND=${FONT_COND:-/usr/share/fonts/truetype/dejavu/DejaVuSansCondensed-Bold.ttf}
FONT_SERIF=${FONT_SERIF:-/usr/share/fonts/truetype/dejavu/DejaVuSerif-BoldItalic.ttf}
FONT_MONO=${FONT_MONO:-/usr/share/fonts/truetype/jetbrainnerd/JetBrainsMonoNerdFont-Medium.ttf}

mkdir -p assets/img/og

# Brand mark: "XCI" in a black square.
mark() { # size output
  local s=$1 out=$2
  convert -size "${s}x${s}" xc:'#121212' -fill '#f3f1ec' -font "$FONT_MONO" \
    -pointsize "$(( s * 36 / 100 ))" -gravity center -annotate +0+0 'XCI' "$out"
}
mark 32 assets/img/favicon-32.png
mark 180 assets/img/apple-touch-icon.png
mark 512 assets/img/logo.png
convert assets/img/favicon-32.png favicon.ico

# Social card: id bg ink muted accent numeral_font numeral name tagline [numeral_size]
card() {
  local id=$1 bg=$2 ink=$3 muted=$4 accent=$5 nfont=$6 numeral=$7 name=$8 tagline=$9 nsize=${10:-300}
  convert -size 1200x630 "xc:$bg" \
    -fill "$accent" -font "$nfont" -pointsize "$nsize" -gravity west -annotate +70+10 "$numeral" \
    -fill "$ink" -font "$FONT_COND" -pointsize 96 -gravity northwest -annotate +520+190 "$name" \
    -fill "$muted" -font "$FONT_MONO" -pointsize 34 -annotate +524+320 "$tagline" \
    -fill "$muted" -font "$FONT_MONO" -pointsize 26 -annotate +70+56 'studio-xci.fr' \
    -fill none -stroke "$ink" -strokewidth 3 -draw 'rectangle 1030,520 1130,574' \
    -stroke none -fill "$ink" -font "$FONT_MONO" -pointsize 30 -gravity southeast -annotate +86+64 'XCI' \
    "assets/img/og/$id.png"
}

card studio   '#f3f1ec' '#121212' '#67635b' '#121212' "$FONT_BOLD"  'XCI' 'STUDIO'   'Projets & documentation' 180
card son      '#121212' '#ededed' '#a4a4a4' '#ffb000' "$FONT_COND"  'I'   'SON'      'Sono, DSP, enceintes'
card logiciel '#ffffff' '#0f172a' '#64748b' '#2448c9' "$FONT_MONO"  'II'  'LOGICIEL' 'Linux, Kubernetes, libre'
card motion   '#0d0b14' '#f4f0ff' '#9c93b5' '#ff4d8d' "$FONT_BOLD"  'III' 'MOTION'   'Blender, 2D, 3D'
card web      '#f5efe4' '#1b1a17' '#6b655b' '#c2410c' "$FONT_SERIF" 'IV'  'WEB'      'Sites et références'
card others   '#e6eeec' '#0b2a2f' '#4c6669' '#0a6e65' "$FONT_BOLD"  'V'   'OTHERS'   'Shape, composites…'

echo "Images written to assets/img/"
