import cadquery as cq
from ocp_vscode import show

v1 = (
    cq.Workplane("XY")
    .tag("base")
    .box(120, 80, 15, centered=False)

    .workplaneFromTagged("base")
    .move(30,0)
    .box(60, 80, 5, centered=False, combine="cut")

    .faces(">Z")
    .workplane(origin=(60, 40))
    .rect(90, 50)
    .vertices()
    .hole(10)
)

cyl = (
    cq.Workplane("XZ")
    .workplane(origin=(90-70/2,0,0), offset=-70)
    .move(0,60-70/2+15)
    .cylinder(60, 70/2, centered=False)
)

cyl2 = (
    cyl
    .faces(">Y")
    .workplane(centerOption="CenterOfBoundBox")
    .hole(50)
)

# bracket 1
b1 = (
    v1
    .faces(">Z")
    .workplane(origin=(120-30-5, 10))
    .box(10, 60, 60, centered=False)
    .cut(cyl)
)

# bracket 2
b2 = (
    cq.Workplane("XZ")
    .workplane(offset=-80/2)
    .tag("base")
    .sketch()
    .arc((120-30, 60+15), 70/2, 0.0, 360.0)
    .segment((35, 15), (120, 15))
    .hull()
    .finalize()
    .extrude(10/2,  both=True)
    .cut(cyl)
)

res = v1.union(b1).union(b2).union(cyl2)
res = res.rotate((0, 0, 0), (0, 0, 1), 90)

show(res)
