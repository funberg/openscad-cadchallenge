$fn=100;
scale([10,10,10]) {
    difference() {
        union() {
            translate([.655, .655, 0])
            hull() {

                cylinder(r=.655, h=.625);
                translate([4-2*.655, 0, 0])
                cylinder(r=.655, h=.625);
                translate([4-2*.655, 3-2*.655, 0])
                cylinder(r=.655, h=.625);
                translate([0, 3-2*.655, 0])
                cylinder(r=.655, h=.625);
            }
            
            translate([2-.25,0,-0.5+.625+2])
            rotate([0,90,0])
            translate([0,.5+.25,0])
            hull() {
                cylinder(r=.5, h=.5);
                translate([0, 2.5-2*.5, 0])
                cylinder(r=.5, h=.5);
                translate([2-1.5, -.5, 0])
                cube([1,2.5,.5]);
            }
            translate([2-(.5+2*.12)/2,0,.625])
            translate([(.5+2*.12)/2, 1.5,.12/2])
            cube([.5+2*.12, 2.5+2*.12, .12], center=true);
        }
        
        translate([.655, .655, -0.001])
        cylinder(d=.312, h=.627);
        translate([.655, 2.345, -0.001])
        cylinder(d=.312, h=.627);
        
        translate([4-1-.25/2,-0.1,-0.01])
        cube([.250, 3.2, .21]);
        
        translate([1.5,1.5,1.625])
        rotate([0,90,0])
        cylinder(d=1, h=1);
        
        translate([0,0,.625+.12])
        rotate([-90,0,0]) {
            translate([2-.25-.12,0,0])
            cylinder(r=.12, h=4);
            translate([2+.25+.12,0,0])
            cylinder(r=.12, h=4);
        }

        translate([0,0,.625+.12])
        rotate([0,90,0]) {
            translate([0,1.5-1.25-.12,0])
            cylinder(r=.12, h=4);
            translate([0,1.5+1.25+.12,0])
            cylinder(r=.12, h=4);
        }
    }
}