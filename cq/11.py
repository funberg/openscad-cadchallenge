import cadquery as cq
from ocp_vscode import show, Camera

b = cq.selectors.BoxSelector

w=12+40+12
h=75
t=12
eps=0.00000001

base = (
    cq.Workplane("XY")
    .tag("base")
    # Base block
    .box(w, h, t, centered=False)
    
    # Body holes
    .faces(">Z").workplane()
    .move(27+5, (75-34)/2-5)
    .line(0,34+5+5)
    .vertices()
    .hole(5*2)
)

# Handle should most likely be translated to make the manual fillet hit the corner of the body
mid_y=75/2
handle = (
    cq.Workplane("XY")
    .tag("base")
    .move(w,(75-40)/2)
    .box(70-20, 40, 12, centered=False)
    
    .workplaneFromTagged("base")
    .move(w+70-40,(75-40)/2)
    .cylinder(12, 20, centered=False)

    # handle hole
    .faces(">Z").workplane()
    .move(w+70-20,75/2)
    .hole(6*2)

    # handle base ext
    .workplaneFromTagged("base")
    .move(w,0)
    .box(20, h, t, centered=False)

    # cut R20 handle left
    .workplaneFromTagged("base")
    .move(w,mid_y-20-40)
    .cylinder(20, 20, centered=False, combine="cut")

    # cut R20 handle right
    .workplaneFromTagged("base")
    .move(w,mid_y+20)
    .cylinder(20, 20, centered=False, combine="cut")
)

# Pure speculation on the R, how to read it from the spec?
r=5
ext = (
    cq.Workplane("XY")
    .tag("base")
    .box(12, h, 52, centered=False)
    .faces(">Z")
    .edges("|X")
    .fillet(14)
    .cut(
        cq.Workplane("YZ")
        .move(7,52-7-2*r)
        .box(75-14, 2*r, 12, centered=False)
        .edges("|X")
        .fillet(r-0.001)
    )
)

show(base, handle, ext, ext.translate((40+12,0,0)), measure_tools=False, reset_camera=Camera.KEEP)
