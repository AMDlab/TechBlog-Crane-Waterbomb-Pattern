from ghpythonlib.treehelpers import list_to_tree, tree_to_list
from Rhino.Geometry import Line

pts = tree_to_list(P, lambda x: x)

print(len(pts[0]))

line_v = []
line_m = []

vs = []
for i in range(9):
    for j in range(0, 10, 2):
        vs.append(Line(pts[j][i], pts[j][i+1]))
    vs.append(Line(pts[9][i], pts[9][i+1]))
line_v.append(vs)

vs = []
for i in range(1, 10, 2):
    for j in range(0, 9, 4):
        vs.append(Line(pts[j][i], pts[j+1][i]))
line_v.append(vs)
vs = []
for i in range(1, 10, 2):
    for j in range(1, 9, 4):
        vs.append(Line(pts[j][i], pts[j+1][i]))
line_v.append(vs)
vs = []
for i in range(0, 10, 2):
    for j in range(0, 8, 4):
        vs.append(Line(pts[j][i], pts[j+2][i]))
    vs.append(Line(pts[8][i], pts[9][i]))
line_v.append(vs)

vs = []
for i in range(0, 10, 2):
    for j in range(2, 9, 4):
        vs.append(Line(pts[j][i], pts[j+1][i]))
line_v.append(vs)
vs = []
for i in range(2, 10, 2):
    for j in range(3, 9, 4):
        vs.append(Line(pts[j][i], pts[j+1][i]))
line_v.append(vs)
vs = []
for i in range(1, 10, 2):
    for j in range(2, 8, 4):
        vs.append(Line(pts[j][i], pts[j+2][i]))
    vs.append(Line(pts[8][i], pts[9][i]))
line_v.append(vs)


ms = []
for i in range(0, 9, 2):
    for j in range(0, 9, 4):
        ms.append(Line(pts[j][i], pts[j+1][i+1]))
line_m.append(ms)
ms = []
for i in range(1, 9, 2):
    for j in range(1, 9, 4):
        ms.append(Line(pts[j][i], pts[j+1][i+1]))
line_m.append(ms)
ms = []
for i in range(1, 9, 2):
    for j in range(0, 9, 4):
        ms.append(Line(pts[j+1][i], pts[j][i+1]))
line_m.append(ms)
ms = []
for i in range(0, 9, 2):
    for j in range(1, 9, 4):
        ms.append(Line(pts[j+1][i], pts[j][i+1]))
line_m.append(ms)

ms = []
for i in range(0, 9, 2):
    for j in range(3, 9, 4):
        ms.append(Line(pts[j][i], pts[j+1][i+1]))
line_m.append(ms)
ms = []
for i in range(1, 9, 2):
    for j in range(2, 9, 4):
        ms.append(Line(pts[j][i], pts[j+1][i+1]))
line_m.append(ms)
ms = []
for i in range(1, 9, 2):
    for j in range(3, 9, 4):
        ms.append(Line(pts[j+1][i], pts[j][i+1]))
line_m.append(ms)
ms = []
for i in range(0, 9, 2):
    for j in range(2, 9, 4):
        ms.append(Line(pts[j+1][i], pts[j][i+1]))
line_m.append(ms)

m = list_to_tree(line_m)
v = list_to_tree(line_v)
