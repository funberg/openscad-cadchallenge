import cadquery as cq
from ocp_vscode import show, Camera
import math

w=39+7+7
h=26
t=21+5

# Slice plane
A = cq.Vector(11 ,26-5, t)
B = cq.Vector(11+31, 26-5, t)
x = A.cross(B)
x = x.normalized()

p = cq.Face.makePlane(300, 300, cq.Vector(0,0,0), x)
a = math.atan((21+5)/(26-5))
v1 = (
    cq.Workplane("XY")
    .tag("base")
    # Base block
    .box(w/2, h, t, centered=False)
    
    # Option 1 use split plane
    .split(p)
    .solids(cq.selectors.DirectionMinMaxSelector(x))
    # Option 2 cut with rotated box
    # .cut(
    #     cq.Workplane("XY")
    #     .box(w/2, h*2, t, centered=False)
    #     .rotate((0,0,0), (w,0,0), math.degrees(a))
    # )

    .workplaneFromTagged("base")
    .box(7, h, 16.7, centered=False)
    
    .workplaneFromTagged("base")
    .workplane(offset=21)
    .box(11, h, 5, centered=False, combine="cut")

    .workplaneFromTagged("base")
    .workplane(offset=7*math.sin(a))
    .move(7+11,0)
    .box(17, h, 17*math.sin(a), centered=False, combine="cut")

    .mirror("YZ", basePointVector=(w/2,0,0), union=True)
)

res = (
    v1
)

show(res, measure_tools=False, reset_camera=Camera.KEEP)
