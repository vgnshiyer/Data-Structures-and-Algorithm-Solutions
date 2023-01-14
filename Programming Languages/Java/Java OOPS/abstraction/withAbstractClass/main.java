abstract class Animal {
    // an abstract method does not have a definition, it can only be declared
    abstract void walk();
}

class Horse extends Animal {
    public void walk(){
        System.out.println("walks on 4 legs.");
    }
}

class Chicken extends Animal {
    public void walk(){
        System.out.println("walks on 2 legs.");
    }
}

public class main {
    public static void main(String args[]){
        Horse h = new Horse();
        h.walk();
        Chicken c = new Chicken();
        c.walk();
    }
}