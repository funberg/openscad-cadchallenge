import cadquery as cq
import math
from ocp_vscode import show, set_port, show_object, Camera
set_port(3939)

taper = math.degrees(math.atan(.156/.125))
base = (
    cq.Workplane("XZ")
    .tag("base")
    .cylinder(.3125, 2.1875/2)
)

back = (
    base
    .faces(">Y")
    .workplane(offset=0.2)
    .cylinder(.75-.3125, 2.0625/2, combine=False)
)

front = (
    base
    .faces("<Y")
    .workplane()
    .circle(2.1875/2)
    .extrude(-.125, taper=taper, combine="cut")
)

v1 = (
    front
    .union(back)
    .faces("<Y[2]")
    .cboreHole(.25, .4375, .3125)
    .faces(">Y")
    .workplane()
    .move(0,.5)
    .hole(.1640, .45)
)

hole = (
    v1
    .faces(">Y[1]")
    .workplane()
    .move(0,.5)
    .circle(.1640/2)
    .extrude(-2, taper=50, combine="cut")
)

#res = res.rotate((0, 0, 0), (0, 0, 1), 90)
show(v1, hole, measure_tools=True, reset_camera=Camera.KEEP)
