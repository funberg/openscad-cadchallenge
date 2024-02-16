
difference() {
    union() {
        cube([62, 100, 20]);
        translate([0, 100-37, 20])
        cube([62, 37, 44-20]);
    }
    
    translate([(62-50)/2, -1, -1])
    cube([50, 102, 6+1]);
        
    translate([31, 100-37-20-20,0])
    hull() {
        cylinder(r=8, h=21);
        translate([0,20, 0])
        cylinder(r=8, h=21);
    }
    
    translate([31, 100-37+20, 0])
    cylinder(d=10,h=45);
    
    translate([31-22, 100-12, 44-20]) {
        cylinder(d=6,h=21);
        translate([44,0,0])
        cylinder(d=6,h=21);
    }
    
    translate([(62-37)/2, 100-37-1, 44-12])
    hull() {
        cube([37, 1, 13]);
        translate([(37-25)/2,37+1, 0])
        cube([25, 1, 13]);
    }
}

