import cadquery as cq

w = 60.0
h = 120.0
t = 35.0
d=20

v3 = (
cq.Workplane("XY")
.box(w, 60, 20, centered=False)
.workplane()
.box(w, h, 15, centered=False)
.faces("<Z")
.workplane()
.move(w/2,-20-15)
.line(0,-45)
.vertices()
.hole(d)
.faces(">Z")
.workplane()
.tag("base")
.box(w, 15, 10, centered=False)
.workplaneFromTagged("base")
.move(0,h-15)
.box(15, 15, 20, centered=False)
.workplaneFromTagged("base")
.move(w-15,h-15)
.box(15, 15, 20, centered=False)
)

show_object(v3)
