a = atan((21+5)/(26-5));
h1=17*sin(a);
h2=7*sin(a);

union() {
    difference() {
        cube([26, 39+7+7, 21+5]);

        rotate([0,90-a, 0])
        translate([-30,-1,0])
        cube([30, 39+7+7+2, 50]);
        
        translate([-1, -1, 21])
        cube([28, 12, 6]);

        translate([-1, 31+11, 21])
        cube([28, 12, 6]);
        
        translate([0,7+11, h2])
        cube([27, 17, h1]);
        
    }
    cube([26, 7, 16.7]);
    translate([0,39+7,0])
    cube([26, 7, 16.7]);
}