$fn=100;

module mount(r1=16, r2=13, s=17) {
    a1 = sqrt(r2*r2-(s/2)*(s/2));
    a2 = sqrt(r1*r1-(s/2)*(s/2));

    rotate([0,0,180])
    difference() {
        circle(r=r1);

        translate([a1-s,0,0]) {
            intersection() {
                translate([-s,-s/2,0])
                square([2*s, s]);
                translate([a2, 0,0])
                circle(r2);
            }
        }
        translate([a1,-s/2,0])
        square(s);

    }
}

module round(r1=16, r2=47, h=11) {
    x=sqrt((r1+r2)^2-(r2+h/2)^2);
    h2=r1*((r2+h/2)/(r1+r2));
    difference() {
        translate([0,-h2,0])
        square([x,2*h2]);
        circle(r=r1);
        translate([x,r2+h/2,0])
        circle(r=r2);
        translate([x,-r2-h/2,0])
        circle(r=r2);
    }
}

rotate([0,0,0]) 
{
    rotate([0,0,17])
    mount(16, 13, 17);
    round(16, 47, 11);  
    
    translate([100,0,0]) {
        rotate([0,0,-163])
        mount(15, 9, 13);
            
        rotate([0,0,180])
        round(15, 23, 11);  
    }
    
    difference() {
        translate([0,-11/2,0])
        square([100,11]);
        circle(r=16);
        translate([100,0,0])
        circle(r=13);
    }
    
}
//#square(17, center=true);
