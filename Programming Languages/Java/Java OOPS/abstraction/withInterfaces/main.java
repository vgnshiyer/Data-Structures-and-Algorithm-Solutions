interface Animal {
    // any method inside an interface cannot have a definition. it can only have a declaration
    public void walk();
}

interface Bird {
    public void fly();
}

class Horse implements Animal, Bird {
    public void walk(){
        System.out.println("walks on 4 legs");
    }

    public void fly(){
        System.out.println("A horse does not fly u dope!");
    }
}

public class main {
    public static void main(String args[]){
        Horse h = new Horse();
        h.walk();
        h.fly();
    }
}