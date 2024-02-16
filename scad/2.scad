difference() {
    union() {
        cylinder(h=30, d=30);
        translate([-15,0,0]) {
            cube([30, 18, 30]);
            cube([30, 60, 9]);
        }
        hull()
        translate([-7/2,0,0]) {
            translate([0,18-1,0])
            cube([7, 1, 30]);
            translate([0,60-1,0])
            cube([7, 1, 9]);
        }
    }
    translate([0,0,-1])
    cylinder(h=32, r=7.5);
    
    translate([0,0,-1])
    linear_extrude(11) {
        translate([6,60,0])
        rotate([0,0,-45])
        square(20);
        
        mirror([1,0,0])
        translate([6,60,0])
        rotate([0,0,-45])
        square(20);
    }
}