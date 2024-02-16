$fn = 100;
scale([10,10,10]) {
    linear_extrude(.62)
    difference() {
        translate([.5,.5])
        hull() {
            for(j=[0:1]) {
                for(i=[0:1]) {
                    translate([i*(4.5-1), j*(2-1)])
                    circle(r=.5);
                }
            }
        }
        hull() {
            translate([.5,1])
            circle(d=.38);
            translate([0,1])
            square(.38, center=true);
        }

        hull() {
            translate([4.5-.5,1])
            circle(d=.38);
            translate([4.5,1])
            square(.38, center=true);
        }
    }
    
    translate([2.25,0,.62+.75])
    rotate([-90,0,0])
    difference() {
        linear_extrude(.62)
        hull() {
            circle(r=1);
            translate([-1,0])
            square([2, .75]);
        }
        translate([0,0,-0.1])
        cylinder(d=.625, h=.625+.2);

        translate([0,0,-0.1])
        cylinder(d=1.25, h=.12+.1);
    }
}