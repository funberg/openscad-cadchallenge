$fn=100;

linear_extrude(12)
difference() {
    union() {
        square([75, 40+12+12]);
        hull(){
            translate([75/2, 64+70-20])
            circle(r=20);
            translate([75/2-40/2,0])
            square(40);
        }
        translate([0,64])
        square([75, 20]);
    }

    translate([75/2, 64+70-20])
    circle(r=6);

    translate([75/2+34/2+5, 27+5])
    circle(r=5);

    translate([75/2-34/2-5, 27+5])
    circle(r=5);
    
    x=sqrt(20^2-(20-35/2)^2);
    translate([35/2-20, 64+x])
    circle(r=20);

    translate([35/2+40+20, 64+x])
    circle(r=20);
}

difference() {
    hull() {
        r=14;
        translate([0,0,12])
        cube([75, 64, 1]);
        
        translate([r,0,52-r])
        rotate([-90,0,0])
        cylinder(r=r, h=64);

        translate([75-r,0,52-r])
        rotate([-90,0,0])
        cylinder(r=r, h=64);
    }
    
    translate([-1,12,11])
    cube([77, 40, 42]);

    hull() {
        r=6;
        
        translate([r+7,-1,52-r-7])
        rotate([-90,0,0])
        cylinder(r=r, h=66);

        translate([75-r-7,-1,52-r-7])
        rotate([-90,0,0])
        cylinder(r=r, h=66);
    }
}