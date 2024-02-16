$fn=100;
use <scad-utils/morphology.scad>;
w1=2+3/4;
h1=5/16;
d1=2+3/8;

w2=1+1/2;
h2=2+3/4;

h3=7/8;
t1=7/16;
t2=1/2;

scale([10,10,10]) {
    linear_extrude(t1) {
    difference() {
        union() {
            fillet(r=1/8)
            rounding(r=1/8) {
                square([w1, h1]);
                translate([w1/2, 1+1/4,0])
                circle(d=d1);
            }
            // square up base
            square([w1, h1-1/8]);
            
            translate([w1/2-w2/2,0])
            square([w2, h2]);
        }
        
        translate([w1/2,1+1/4])
        circle(d=1);
        
        translate([w1/2, 1+1/4])
        rotate([0,0,45])
        translate([0,-3/16])
        square([2, 3/8]);
        
    }
}
    translate([w1/2, h2, h3+t1])
    rotate([90,0,180]) 
    {
        difference() {
            linear_extrude(t2)
            difference() {
                hull() {
                    circle(r=5/8);
                    translate([-w2/2,-h3-t1])
                    square([w2, t1]);
                }
                circle(d=7/16); 
            }
            eps=0.01;
            translate([0,0,-eps])
            cylinder(d=7/8, h=1/4+eps);
        }
    }
    
}