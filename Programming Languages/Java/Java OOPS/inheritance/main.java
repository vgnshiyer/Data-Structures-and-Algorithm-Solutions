class Shape {
    String color;

    public void area() {
        System.out.println("prints area");
    }
}

// class Triangle inherited properties/attributes from parent class shape
class Triangle extends Shape {
    // class Triangle automatically has a property called color

    public void area(int l, int h) {
        System.out.println(0.5*l*h);
    }
}

class EquilateralTriangle extends Triangle {
    public void area(int l, int h) {
        System.out.println(0.5*l*h);
    }
}

class Circle extends Shape {
    public void area(int r) {
        System.out.println((3.14)*r*r);
    }
}

public class main {
    public static void main(String args[]) {
        Triangle t1 = new Triangle();
        t1.color = "red";
    }
}