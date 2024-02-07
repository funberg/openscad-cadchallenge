import cadquery as cq
from jupyter_cadquery.viewer.client import show, show_object

bw = 60-18
pts=[(0,30), (bw, 9), (0, 9)]

v2 = (
cq.Workplane("XY")
.box(60+15, 30, 30, centered=False)

.faces(">Z")
.workplane()
.move(15,15)
.hole(15)

.edges("<X").edges("|Z")
.fillet(14.99)
.edges(">X").edges("|Z")
.chamfer(9,9)

.faces("<Y")
.workplane(offset=-30, origin=(15+18,0,9))
.box(50,30-9,30,centered=False, combine='cut')

.faces("<Y")
.workplane(offset=-15, origin=(15+18,-30,0))
.polyline(pts).close()
.extrude(7/2, both=True)
)

show(v2)