import cadquery as cq
from ocp_vscode import show

w=88
h=50
t=56

v1 = (
    cq.Workplane("XY")

    # Base block
    .box(w, h, 18, centered=False)

    # X-hwise bar
    .faces(">Z")
    .workplane().tag("base")
    .workplane(origin=(0,28))
    .box(w, 12, t-18, centered=False)

    # Y-base bar
    .workplaneFromTagged("base")
    .workplane(origin=(38, 0))
    .box(12, h, t-18, centered=False)
)

# Slice plane
A = cq.Vector(88-10 ,0, 10)
B = cq.Vector(88, 50, 56)
C = cq.Vector(88, 0, 0)
x = (A-C).cross(B-C)
x = x.normalized()

p = (
    cq.Face.makePlane(
        200,
        200,
        cq.Vector(w,0,0), 
        x)
)

res = (
    v1
    .split(p)
    .solids(cq.selectors.DirectionMinMaxSelector(x))
)

show(res)