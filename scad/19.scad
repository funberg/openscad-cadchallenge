$fn=100;

// cheat and 
use <scad-utils/morphology.scad>

module body() {
    r = .5;
    difference() {
        // donut
        circle(r=2.215+r);
        circle(r=2.215-r);
        
        // crop to angles
        rotate([0,0,30])
        translate([0,-3])
        square([3, 6]);

        rotate([0,0,-110])
        translate([0,-3])
        square([3, 6]);
    }
    
    // Endcaps
    rotate([0,0,120])
    translate([2.215,0])
    circle(r=r);
    
    rotate([0,0,120+40])
    translate([2.215,0])
    circle(r=r);
    
    hull() {
        translate([-3.5,0])
        circle(r=.625);
        circle(r=.625);
    }
}

scale([10,10,10]) {
    intersection(){
//        difference() {
//            square(1e5, center=true);
//            body();
//            
//        }
        difference() {
            square(1e5, center=true);
            fillets();
            body();
        
        }
    }
//    difference() {
//        union() {
//            
//            intersection() {
//                fillet(r=1.483)
//                body();
//                translate([-4.5,0])
//                square([3,2]);
//            }
//
//            fillet(r=0.25)
//            body();
//        }
//        union() {
//            r = .125;
//            difference() {
//                // donut
//                circle(r=2.215+r);
//                circle(r=2.215-r);
//                
//                // crop to angles
//                rotate([0,0,30])
//                translate([0,-3])
//                square([3, 6]);
//
//                rotate([0,0,-110])
//                translate([0,-3])
//                square([3, 6]);
//            }
//            
//            // slot end holes
//            rotate([0,0,120])
//            translate([2.215,0])
//            circle(r=r);
//            
//            rotate([0,0,120+40])
//            translate([2.215,0])
//            circle(r=r);
//            
//            // base holes
//            circle(d=.5);
//            translate([-3.5,0])
//            circle(d=.5);
//        }
//    }
}

module fillets() {
    r1=2.215+.5;
    r2=1.483;
    r3=.625;

    h = tri_height(heron_area(r1+r2, r2+r3, 3.5), 3.5);
    a = asin(h/(r1+r2));
    rotate([0,0,-a])
    translate([-(r1+r2),0])
    circle(r=1.483);


    r4=2.215-.5-.25;
    a2 = asin((.625+.25)/r4);
    rotate([0,0,-a2])
    translate([-r4,0])
    circle(r=.25);
}


module circle_arc(r=1, width, start=0, end=360) {
    difference() {
        #circle(r+width/2);
        circle(r-width/2);
    }  
}

function heron_area(a, b, c) = 0.25 * sqrt((a + b + c) * (-a + b + c) * (a - b + c) * (a + b - c));

function tri_height(A, b) = (2*A)/b;
