difference() {
    union() {
        cube([60, 120, 15]);
        translate([0,0,-10])
            cube([60, 50, 10]);
    }        

    translate([30,35,-11]) {
        cylinder(h=27, r=10);
        translate([0,45,0])
            cylinder(h=27, r=10);
    }
}

translate([0,0,15]) {
    cube([60, 15, 10]);
    translate([0,120-15,0]) {
        cube([15, 15, 20]);
        translate([60-15,0,0])
            cube([15, 15, 20]);
    }
}

