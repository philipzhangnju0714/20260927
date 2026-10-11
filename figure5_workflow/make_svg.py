"""Generate figure5_workflow.svg (research workflow, Scientific-Reports style).
Edit the text in the lists below and run:  python3 make_svg.py
"""
from pathlib import Path

W, H = 1000, 420
FONT = "Arial, 'Liberation Sans', Helvetica, sans-serif"
INK, SUB, BOX, DASH = "#222", "#555", "#5a5a5a", "#8a8a8a"
CW, X1, X2, X3 = 250, 40, 375, 710          # column width and left edges
BH, GAP = 40, 16                              # box height, vertical gap inside groups

out = []
def add(s): out.append(s)

def box(x, y, w, h, lines, bold=False, sub=None):
    add(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="#fff" stroke="{INK if bold else BOX}" '
        f'stroke-width="{1.4 if bold else 1}"/>')
    n = len(lines) + (1 if sub else 0)
    lh = 14.5
    y0 = y + h / 2 - (n - 1) * lh / 2 + 4.3
    for i, t in enumerate(lines):
        add(f'<text x="{x + w/2}" y="{y0 + i*lh:.1f}" text-anchor="middle" font-size="{13 if bold else 12.5}" '
            f'font-weight="{"bold" if bold else "normal"}" fill="{INK}">{t}</text>')
    if sub:
        add(f'<text x="{x + w/2}" y="{y0 + len(lines)*lh:.1f}" text-anchor="middle" font-size="11" fill="{SUB}">{sub}</text>')

def group(x, y, w, h):
    add(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="none" stroke="{DASH}" stroke-width="1" stroke-dasharray="2.5 2"/>')

def arrow(pts):
    d = "M" + " L".join(f"{a},{b}" for a, b in pts)
    add(f'<path d="{d}" fill="none" stroke="{INK}" stroke-width="1.1" marker-end="url(#ah)"/>')

def column(x, items, chain):
    """dashed group of boxes starting at y=20; returns bottom y of group."""
    gy, pad = 20, 10
    y = gy + pad
    for i, (lines, sub) in enumerate(items):
        box(x + pad, y, CW - 2*pad, BH, lines, sub=sub)
        if chain and i < len(items) - 1:
            arrow([(x + CW/2, y + BH), (x + CW/2, y + BH + GAP - 1)])
        y += BH + GAP
    bottom = y - GAP + pad
    group(x, gy, CW, bottom - gy)
    return bottom

# ---------------- content ----------------
COL1_TOP = (["Literature Review"],)
COL1 = [(["AI-Assisted Situated", "Storytelling Systems"], None),
        (["SOR Model and Cognitive", "Appraisal Theory"], None),
        (["Six Perceived Attributes"], "content · expression · interaction")]
COL1_END = ["Develop Research Hypotheses", "(H1–H15) and Model"]

COL2 = [(["Research Case"], "GeoDrama, historic urban Nanjing"),
        (["Questionnaire Design"], "27 items · 9 constructs"),
        (["On-site Walking Experience"], "approx. 10–15 min"),
        (["Data Collection"], "valid N = 548")]
COL2_END = ["SPSS 27.0", "+", "AMOS 27.0"]

COL3 = [(["Measurement Model Evaluation"], "CFA: reliability and validity"),
        (["Structural Model Analysis"], "SEM: H1–H14"),
        (["Alternative Models and", "Mediation Effects"], None),
        (["SEM–ANN Analysis"], "ten-fold cross-validation")]
COL3_END = ["Results &amp; Discussion"]

BOTTOM = ["Theoretical Contributions", "Practical Implications", "Limitations and Future Research"]

# ---------------- layout ----------------
add(f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" font-family="{FONT}">')
add('<defs><marker id="ah" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto">'
    f'<path d="M0,1 L10,5 L0,9 z" fill="{INK}"/></marker></defs>')
add(f'<rect width="{W}" height="{H}" fill="#fff"/>')

# column 1: literature review, themes, hypotheses
box(X1, 20, CW, 36, COL1_TOP[0], bold=True)
g1y = 76
y = g1y + 10
for lines, sub in COL1:
    box(X1 + 10, y, CW - 20, BH, lines, sub=sub)
    y += BH + 12
g1b = y - 12 + 10
group(X1, g1y, CW, g1b - g1y)
arrow([(X1 + CW/2, 56), (X1 + CW/2, g1y - 1)])

b2 = column(X2, COL2, chain=True)
b3 = column(X3, COL3, chain=True)

ENDY, ENDH = max(g1b, b2, b3) + 22, 58
arrow([(X1 + CW/2, g1b), (X1 + CW/2, ENDY - 1)])
box(X1, ENDY, CW, ENDH, COL1_END, bold=True)
arrow([(X2 + CW/2, b2), (X2 + CW/2, ENDY - 1)])
box(X2, ENDY, CW, ENDH, COL2_END, bold=True)
arrow([(X3 + CW/2, b3), (X3 + CW/2, ENDY - 1)])
box(X3, ENDY, CW, ENDH, COL3_END, bold=True)

# cross-column connectors: bottom box -> top of next column
mid12, mid23 = (X1 + CW + X2) / 2, (X2 + CW + X3) / 2
top_box_y = 20 + 10 + BH / 2
arrow([(X1 + CW, ENDY + ENDH/2), (mid12, ENDY + ENDH/2), (mid12, top_box_y), (X2 + 9, top_box_y)])
arrow([(X2 + CW, ENDY + ENDH/2), (mid23, ENDY + ENDH/2), (mid23, top_box_y), (X3 + 9, top_box_y)])

# bottom group: implications
by = ENDY + ENDH + 26
bgap = 14
gx, gw = X1, (X3 - 40) - X1                    # span from column 1 to just left of column 3
bw = (gw - 20 - (len(BOTTOM) - 1) * bgap) / len(BOTTOM)
group(gx, by, gw, 54)
for i, t in enumerate(BOTTOM):
    box(gx + 10 + i * (bw + bgap), by + 10, bw, 34, [t])
arrow([(X3 + CW/2, ENDY + ENDH), (X3 + CW/2, by + 27), (gx + gw + 1, by + 27)])

add('</svg>')
H_real = by + 54 + 16
svg = "\n".join(out).replace(f'height="{H}" viewBox="0 0 {W} {H}"', f'height="{H_real}" viewBox="0 0 {W} {H_real}"', 1)
svg = svg.replace(f'<rect width="{W}" height="{H}"', f'<rect width="{W}" height="{H_real}"', 1)
Path(__file__).with_name("figure5_workflow.svg").write_text(svg, encoding="utf-8")
print("wrote figure5_workflow.svg", W, "x", H_real)
