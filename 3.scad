difference() {
    union() {
        cube([50, 88, 18]);

        translate([0,88-38-12,0])
        cube([50,12,56]);

        translate([28,0,0])
        cube([12,88,56]);

        //cube([50,88,56]); // full cube
    }
    hull() 
    {
        rotate([45,0,0])
        translate([-1,0,0])
        cube([1,100,100]);
        rotate([0,-atan(56/50),0])
        translate([0,-1,0])
        cube([100,1,100]);
    }
}