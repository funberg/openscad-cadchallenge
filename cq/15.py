import cadquery as cq
from ocp_vscode import show, Camera
import watch_import

eps=0.000001
r=6/2
r2=4/2
r3=7/2
r4=1.5
a=7-r
b=11
c=4
d=3
base = (
    cq.Workplane("XY")
    .tag("base")
    .workplane(offset=25-r-r)
    .sphere(r, centered=False)

    .workplaneFromTagged("base")
    .workplane(offset=25-a-r)
    .cylinder(a, r, centered=False)

    .faces("<Z").workplane(invert=True, offset=-b)
    .move(r-r2,r-r2)
    .cylinder(b, r2, centered=False)

    .faces("<Z").workplane(invert=True, offset=-c)
    .cylinder(c, r, centered=False)

    .faces("<Z").workplane(invert=True, offset=-d)
    .move(r-r3,r-r3)
    .cylinder(d, r3, centered=False)

    .faces("<Z").workplane(invert=True, offset=-r4)
    .move(r-r4,r-r4)
    .sphere(r4, centered=False, combine="cut")

    .faces("<Z[1]")
    .edges().all()[1].fillet(1-eps)

    .faces("<Z[0]")
    .edges().all()[1]
    .fillet(1-eps)

)

show(base, reset_camera=Camera.KEEP)
watch_import.watch_me()