difference() {
    union() {
    cylinder(h=20, d=60);
    translate([-30,0,0])
    cube([60, 38, 20]);
    }

    translate([0,0,-1])
    cylinder(h=22, r=15);
    
    translate([-15, 28, -1])
    cube([30, 11, 22]);
}