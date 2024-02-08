import cadquery as cq
from ocp_vscode import show

w = 60.0
h = 120.0
t = 35.0
d=20

v3 = (
    cq.Workplane("XY")
    .box(w, 60, 20, centered=False)
    .workplane()
    .box(w, h, 15, centered=False)
    .faces("<Z")
    .workplane()
    .move(w/2,-20-15)
    .line(0,-45)
    .vertices()
    .hole(d)
    .faces(">Z")
    .workplane()
    .tag("base")
    .box(w, 15, 10, centered=False)
    .workplaneFromTagged("base")
    .move(0,h-15)
    .box(15, 15, 20, centered=False)
    .workplaneFromTagged("base")
    .move(w-15,h-15)
    .box(15, 15, 20, centered=False)
)

# Rotate for viewing
v3 = v3.rotate((0, 0, 0), (0, 0, 1), -90)
show(v3)
