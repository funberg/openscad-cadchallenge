import cadquery as cq
from cadquery import Selector, Vector, Shape
from typing import Sequence

from ocp_vscode import show, Camera
import math

# Test of custom selector that selects the 2 closest objects to a point
class n2(Selector):
    def __init__(self, pnt):
        self.pnt = pnt

    def filter(self, objectList: Sequence[Shape]):
        def dist(tShape):
            return tShape.Center().sub(Vector(*self.pnt)).Length

        return sorted(objectList, key=dist)[:2]

def makePart(s, ri, ro):
    # (17, 13, 16)
    r = s/2
    off = ri*math.cos(math.asin(r/ri))-r
    off2 = ro*math.cos(math.asin(r/ro))-r

    slot = (
        cq.Workplane("XY")
        .rect(3*ri, s)
        .extrude(1)
        .intersect(
            cq.Workplane("XY")
            .circle(ri)
            .extrude(1)
            .translate((-off,0))
        )
        .union(
            cq.Workplane("XY")
            .rect(s, s)
            .extrude(1)
            .translate((-r,0))
        )
        .translate((-off2, 0))
    )

    outer = (
        cq.Workplane("XY")
        .circle(ro)
        .extrude(1)
    )

    res = (
        outer
        .cut(
            slot
        )
    )

    return (res, outer, slot)

# make the 2 ends
l, r = makePart(17, 13, 16), makePart(13, 9, 15)

# offset and rotate the parts
l = [p.rotate((0,0,0), (0,0,1), 17) for p in l]
r = [p.rotate((0,0,0), (0,0,-1), 165).translate((100, 0)) for p in r]

handle = (
    cq.Workplane("XY")    
    .box(85, 11, 1, centered=False)
    .translate((10,-11/2))
    .cut(l[1])
    .cut(r[1])
)

body = (
    l[0].union(r[0])
    .union(handle)
    .edges(n2((20, 0, 0)))
    # Bounding box selector
    # .edges("|Z").edges(b((10, 16, 2), (40, -16, -2)))
    .fillet(47)
    .edges(n2((80, 0, 0)))
    # Bounding box selector
    # .edges("|Z").edges(b((50, 16, 2), (90, -16, -2)))
    .fillet(23)
)


show(body, handle, measure_tools=False, reset_camera=Camera.RESET)
#show(body, handle, l[1], r[1], measure_tools=False, reset_camera=Camera.KEEP)