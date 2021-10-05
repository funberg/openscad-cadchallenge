difference() {
    cube([120, 80, 15]);

    translate([30,-1,-1])
    cube([60, 82, 6]);

    translate([15, 15, -1]) {
        for(j=[0:1]) {
            for(i=[0:1]) {
                translate([i*90, j*50,0])
                cylinder(d=10, h=17);
            }
        }   
    }
}

difference() {
    union() {
        translate([120-35,10,15])
        cube([10, 60, 60]);
        
        hull() {
        translate([35,40-5,14])
        cube([120-35, 10, 0.1]);

        translate([120-30-35,40-5,60+15])
        cube([70, 10, 0.001]);
        }
    }
    translate([120-30,10,60+15])
    rotate([-90,0,0])
    translate([0,0,-1])
    cylinder(d=70, h=62);

}

translate([120-30,10,60+15])
rotate([-90,0,0]) {
    difference() {
        cylinder(d=70, h=60);
        translate([0,0,-1])
        cylinder(d=50, h=62);
    }
}


