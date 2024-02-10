import cadquery as cq
from ocp_vscode import show

base = (
    cq.Workplane("XY")
    .tag("base")
    .box(62, 100, 20, centered=False)

    .workplaneFromTagged("base")
    .move((62-50)/2, 0)
    .box(50, 100, 6, centered=False, combine="cut")
    .faces(">Z")
    .workplane()
    .sketch()
    .arc((62/2,100-37-20-20), 8, 0, 360)
    .arc((62/2,100-37-20), 8, 0, 360)
    .hull()
    .finalize()
    .extrude(-20, combine="cut")
)

top = (
    base
    .faces(">Z")
    .workplane(origin=(0, 100-37))
    .box(62, 37, 44-20, centered=False, combine=False)
    
    .faces(">Z")
    .workplane()
    .moveTo((62-44)/2, 37-12)
    .line(44, 0)
    .vertices()
    .hole(6, 20)

    .faces(">Z")
    .workplane(offset=-12)
    .sketch()
    .segment(((62-37)/2, 0), ((62-37)/2+37, 0))
    .segment(((62-25)/2, 37), ((62-25)/2+25, 37))
    .hull()
    .finalize()
    .extrude(20, combine="cut")
)

res = (
    base.union(top)
    .faces("<Z[1]")
    .workplane()
    .move(62/2, 100-37+20)
    .hole(10)
)

show(res)
