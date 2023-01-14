class Student {
    // attributes of a student
    String name;
    int age;

    // constructer
    Student(String name, int age) {
        // assigning name and age of the student to class attributes
        this.name = name;
        this.age = age;
        System.out.println("New Student enrolled!");
    }

    // copy constructer
    Student(Student s) {
        this.name = s.name;
        this.age = s.age;
        System.out.println("Student data copied!");
    }

    // methods for the student class
    public void printInfo() {
        System.out.println("\nStudent Details:");
        System.out.println(this.name);
        System.out.println(this.age);
    }
}

public class main {
    public static void main(String args[]) {
        // object initialization
        Student s1 = new Student("aman", 21);
        s1.printInfo();

        Student s2 = new Student(s1);
        s2.printInfo();

        // destructers are already inbuilt in java due to its garbage collector
    }
}