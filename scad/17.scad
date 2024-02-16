$fn = 100;
difference() {
    union() {
        linear_extrude(10)
        difference() {
            circle(r=73);

            for(i=[0:5]) {
                rotate([0,0,i*60]) {
                    translate([0,38.5])
                    hull() {
                        circle(d=13);
                        translate([0,38.5])
                        square(13, center=true);
                    }
                    rotate([0,0,30])
                    // y distance ?
                    translate([0,73+20])
                    circle(r=32);
                }
            }
        }

        translate([0,0,-2])
        cylinder(d=45, h=10+2+2);
    }

    translate([0,0,-3])
    linear_extrude(10+2+2+2) {
        circle(r=12.7);
        translate([-6.5/2,12.7-2])
        square([6.5, 3.25+2]);
    }

}