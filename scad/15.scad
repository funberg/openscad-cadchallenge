$fn = 100;

translate([0,0,3])
sphere(r=3);

translate([0,0,3])
cylinder(d=6, h=7-3);
    
translate([0,0,7])
rotate_extrude()
{
    difference() {
        square([3, 1]);
        translate([3,1])
        circle(r=1);
    }
}

translate([0,0,8])
cylinder(d=4, h=11-2);

translate([0,0,7+11-1])
rotate_extrude()
{
    difference() {
        square([3, 1]);
        translate([3,0])
        circle(r=1);
    }
}

translate([0,0,7+11])
cylinder(d=6, h=4);

translate([0,0,7+11+4])
difference() {
    cylinder(d=7, h=3);
    translate([0,0,3])
    sphere(d=3);
}