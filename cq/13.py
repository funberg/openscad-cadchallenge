import cadquery as cq
from ocp_vscode import show, Camera
import math

w=50
w2=30

# Slice plane
A = cq.Vector(-50 ,0, 50)
B = cq.Vector(-50, 50, 50)
x = A.cross(B)
x = x.normalized()

p = cq.Face.makePlane(300, 300, cq.Vector(50,0,0), x)
a = math.atan((21+5)/(26-5))
base = (
    cq.Workplane("XY")
    .tag("base")
    
    # Base block
    .box(w, w, w, centered=False)
    
    # Split cube
    .split(p)
    .solids(cq.selectors.DirectionMinMaxSelector(x))

    .workplaneFromTagged("base").workplane(offset=(w-w2)/2)
    # small block
    .move((w-w2)/2, (w-w2)/2)
    .box(w2, w2, w2, centered=False)
)

show(base, measure_tools=False, reset_camera=Camera.KEEP)
