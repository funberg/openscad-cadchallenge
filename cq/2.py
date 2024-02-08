import cadquery as cq
from ocp_vscode import show

p2 = (
    cq.Workplane("XY")
    .cylinder(30, 30/2, centered=False)

    .faces(">Z")
    .workplane(offset=-30)
    .move(15,0)
    .box(18, 30, 30, centered=False)

    .faces(">Z")
    .workplane()
    .move(15,15)
    .hole(7.5*2)
)

bw = 60-18
base = [(0,0), (bw-9, 0), (bw, 9), (bw, 9+12), (bw-9, 30), (0, 30)]

bse = (
    cq.Workplane("XY")
    .move(18+15,0)
    .polyline(base).close()
    .extrude(9)
    .translate([15+18,0])
)

pts=[(0,30), (bw, 9), (0, 9)]

dia = (
    cq.Workplane("XZ")
    .workplane(offset=-(9+12/2))
    .polyline(pts).close()
    .extrude(7/2, both=True)
    .translate([15+18,0])
)

res = p2.union(bse).union(dia)
show(res)
