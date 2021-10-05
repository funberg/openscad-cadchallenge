$fn=100;
rotate([-90,0,0])
scale([10,10,10]){

difference(){
    union(){
        difference() {

            cylinder(d=2.1875, h=.3125);
                
            rotate_extrude(angle=360)
            rotate([0, 0,90])
            difference() {
                square([.125, 2.1875/2]);
                translate([.125,2.1875/2-.156])
                rotate([0,0,atan(.125/.156)])
                square([2, 3]);
            }
        }

        translate([0,0,.3125])
        cylinder(h=.75-.3125, d=2.0625);
    }
    
    cylinder(d=.25, h=.75+0.1);
    cylinder(d=.4375, h=.3125);

    translate([0,-.50,.75-.50]) {
        cylinder(h=0.05, r1=0, r2=0.164/2);
        translate([0,0,0.05])
        cylinder(h=.50, d=0.164);
    }    
}



}