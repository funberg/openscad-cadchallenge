import cadquery as cq
from ocp_vscode import show

v1 = (
    cq.Workplane("XY")
    .tag("base")
    .cylinder(20, 30, centered=False)

    .workplaneFromTagged("base")
    .move(30,0)
    .box(38, 60, 20, centered=False)

    .faces(">Z")
    .workplane()
    .move(30,30)
    .hole(30)

    .workplaneFromTagged("base")
    .move(30+38-10, 15)
    .box(10, 30, 20, centered=False, combine="cut")
)

v1 = v1.rotate((0, 0, 0), (0, 0, 1), -90)

show(v1)
