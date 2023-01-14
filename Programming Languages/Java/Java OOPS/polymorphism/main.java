/* Compile time polymorphism -> method overloading (same method being used for multiple functionalities) */

class Student {
    String name;
    int age;

    public void printInfo(String name){
        System.out.println(name);
    }

    public void printInfo(int age) {
        System.out.println(age);
    }

    public void printInfo(String name, int age) {
        System.out.println(name);
        System.out.println(age);
    }
}

public class main {
    public static void main(String args[]){
        Student s = new Student();
        s.printInfo("rohan");
        s.printInfo(24);
        s.printInfo("rohan", 24);
    }
}