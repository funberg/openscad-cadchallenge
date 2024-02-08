import cadquery as cq
from ocp_vscode import show, show_object, reset_show, Camera

s = cq.selectors.StringSyntaxSelector

base = (
    cq.Workplane("XY")
    .box(3, 4, .625, centered=False)
    .edges("|Z")
    .fillet(.655)
    
    # holes
    .faces(">Z")
    .workplane()
    .move(.655, 4-.655)
    .line(2.345-.655, 0)
    .vertices()
    .hole(.312)

    # bottom slot
    .faces("<Z")
    .workplane(invert=True)
    .move(0,.875)
    .box(3, .25, .2, centered=False, combine="cut")

    # top bit
    .faces(">Z")
    .workplane()
    .move((3-1.25*2)/2, 2-.5/2)
    .box(2.5, .5, 2.625-.625, centered=False)
    .faces(">Z")
    .edges("|Y")
    .fillet(.5)

    # hole
    .faces("<Y[2]")
    .workplane()
    .move(1.5,2.625-.625-1)
    .hole(1)

    # top-base fillet
    .faces("<Z[1]")
    .edges(s("+Y")+s("+X")-s("<X")-s(">X")-s(">Y")-s("<Y"))
    .fillet(.1)
)
base = base.rotate((0,0,0), (0,0,1), 90)
show(base, reset_camera=Camera.KEEP)