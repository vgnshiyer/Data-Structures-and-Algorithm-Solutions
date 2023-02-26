# Object oriented programming

### Class
In object-oriented programming (OOP), a class is a blueprint or template for creating objects that define a set of attributes (data members) and behaviors (methods) that the objects will have.

A class defines the characteristics and behaviors of objects that belong to that class. It describes the data that an object can hold and the operations that can be performed on that data.

For example, a "car" class might have data members such as "make", "model", "year", and "color", and methods such as "start", "stop", "accelerate", and "brake". Objects created from this class would represent individual cars, each with its own set of values for the data members and the ability to perform the methods defined in the class.

Classes are a fundamental concept in OOP, and they allow programmers to create reusable code that can be used to create multiple objects with similar characteristics and behaviors.

### Objects
In object-oriented programming (OOP), an object is an instance of a class that has its own unique set of data (attributes) and behaviors (methods) based on the blueprint defined in the class.

An object is created using the constructor method of its class, which sets the initial values of its attributes. Once an object is created, it can be manipulated by calling its methods, which can modify the object's attributes and perform other actions.

For example, consider the "car" class we mentioned in the previous answer. An object created from this class would represent a specific car, such as a 2018 Honda Civic with a red exterior. The object's data members would hold the values of the car's make, model, year, and color, while its methods could be used to start the engine, accelerate, or brake.

Objects are a key component of OOP, and they allow programmers to create modular and reusable code that can be easily extended and modified. Objects can interact with each other and with other parts of a program, making it possible to build complex systems with many interconnected parts.

Example,
```
public class Car {
    private String make;
    private String model;
    private int year;
    private String color;
    
    public Car(String make, String model, int year, String color) {
        this.make = make;
        this.model = model;
        this.year = year;
        this.color = color;
    }
    
    public void start() {
        System.out.println("Starting the engine.");
    }
    
    public void accelerate() {
        System.out.println("Accelerating.");
    }
    
    public void brake() {
        System.out.println("Applying the brakes.");
    }
}
```
In this example, the Car class is defined using the public class keywords, followed by the name of the class (Car). The class has four private data members (make, model, year, and color), which are accessed and initialized using a constructor method that takes arguments for each data member.

The class also defines three public methods (start, accelerate, and brake) that can be called on objects created from the class. These methods print messages to the console indicating the actions being taken.
```
Car myCar = new Car("Honda", "Civic", 2018, "red");
myCar.start();
myCar.accelerate();
```
In this example, a new object myCar is created from the Car class by calling its constructor method and passing in the arguments for make, model, year, and color. Then, the start and accelerate methods are called on the myCar object, which prints messages to the console indicating that the engine is starting and the car is accelerating.

**What is a constructor?**
In object-oriented programming, a constructor is a special method that is used to initialize the data members of an object when it is created. The constructor has the same name as the class and is typically defined with the def keyword in Python or the public keyword in Java.

When an object is created from a class, the constructor is automatically called to initialize its data members to their default values or the values passed in as arguments.

```
public class Person {
    private String name;
    private int age;
    private String email;
    
    public Person(String name, int age, String email) {
        this.name = name;
        this.age = age;
        this.email = email;
    }
}
```
In this example, the constructor method Person takes three arguments (name, age, and email) and initializes the object's data members with these values using the this keyword.

Some properties of constructors:
1. Name: Constructors have the same name as the class they belong to. This ensures that the constructor is automatically called when an object of the class is created.

2. Access level: Constructors can have different access levels, such as public, private, or protected, which determine whether they can be called from outside the class or only within the class.

3. Parameters: Constructors can take parameters to initialize the object's data members with specific values. This allows for greater flexibility in creating objects with different initial states.

4. Default constructor: If no constructor is defined for a class, a default constructor is automatically created by the compiler. This default constructor initializes the object's data members to their default values.

5. Overloading: Like other methods in a class, constructors can be overloaded to take different combinations of arguments. This allows for multiple constructors to be defined with different initialization logic.

6. Initialization order: Constructors can call other constructors in the same class or in a parent class to perform initialization logic in a specific order. This can be useful when there are dependencies between the object's data members or when initializing inherited data members.

7. Return type: Constructors do not have a return type, as their primary purpose is to initialize the object's data members rather than return a value.

**What is method overloading?**
Method overloading is a feature in object-oriented programming where multiple methods can have the same name but different parameters. In other words, a class can have multiple methods with the same name but different argument lists.

When a method is called, the compiler determines which method to call based on the number and types of arguments passed in. If multiple methods have the same name but different argument lists, the compiler will choose the appropriate method based on the argument types.

```
public class MathOperations {
    public int add(int x, int y) {
        return x + y;
    }
    
    public double add(double x, double y) {
        return x + y;
    }
    
    public int add(int x, int y, int z) {
        return x + y + z;
    }
}
```
In this example, the MathOperations class has three methods called add, each with a different number or type of arguments. The first method takes two int parameters and returns their sum, the second method takes two double parameters and returns their sum, and the third method takes three int parameters and returns their sum.

When we call the add method with different arguments, the compiler will choose the appropriate method based on the types of the arguments. For example:
```
MathOperations math = new MathOperations();
int sum1 = math.add(2, 3);          // calls the first add method
double sum2 = math.add(2.5, 3.5);   // calls the second add method
int sum3 = math.add(2, 3, 4);       // calls the third add method
```

Method overloading allows programmers to define multiple methods with the same name but different argument lists, making code more readable and easier to use. By providing different versions of a method that take different types of arguments, we can make our code more flexible and versatile, allowing it to handle a wider range of inputs.

**What is the this keyword?**
The this keyword is a reference to the current object instance in object-oriented programming. It is used to refer to the current object's members (fields and methods) and to differentiate between local variables and instance variables with the same name.

In Java, the this keyword is commonly used in the following ways:

1. To refer to instance variables: When an instance variable has the same name as a local variable or parameter, the this keyword can be used to refer to the instance variable. For example:
```
public class Person {
    private String name;
    
    public void setName(String name) {
        this.name = name;
    }
}
```

2. To call another constructor in the same class: If a class has multiple constructors, the this keyword can be used to call another constructor from within a constructor. This is known as constructor chaining. For example:
```
public class Person {
    private String name;
    private int age;
    
    public Person(String name) {
        this(name, 0);
    }
    
    public Person(String name, int age) {
        this.name = name;
        this.age = age;
    }
}
```

3. To return the current object: When a method needs to return the current object instance, the this keyword can be used as the return value. This is commonly used in method chaining, where multiple methods are called on the same object instance. For example:
```
public class StringBuilder {
    private String str;
    
    public StringBuilder append(String str) {
        this.str += str;
        return this;
    }
    
    public StringBuilder reverse() {
        this.str = new StringBuilder(this.str).reverse().toString();
        return this;
    }
}
```

### Inheritance
Inheritance is a fundamental concept in object-oriented programming (OOP) where a class can be defined based on an existing class, inheriting all its properties and methods, and extending or modifying them as needed. The existing class is known as the parent or superclass, and the new class is known as the child or subclass.

Inheritance allows us to reuse code and build more complex and specialized classes by building on existing classes. It also enables polymorphism, where a subclass can be treated as its parent class, allowing for greater flexibility and modularity in our code.
```
public class Animal {
    protected String name;
    protected int age;
    
    public Animal(String name, int age) {
        this.name = name;
        this.age = age;
    }
    
    public void speak() {
        System.out.println("I am an animal.");
    }
}

public class Dog extends Animal {
    public Dog(String name, int age) {
        super(name, age);
    }
    
    public void speak() {
        System.out.println("Woof!");
    }
}

public class Cat extends Animal {
    public Cat(String name, int age) {
        super(name, age);
    }
    
    public void speak() {
        System.out.println("Meow!");
    }
}
```
In this example, we have a parent class Animal that has two instance variables name and age, a constructor that sets these variables, and a speak method that prints a message to the console.

We also have two child classes Dog and Cat that extend the Animal class. These subclasses inherit the name and age variables and the speak method from the Animal class, but they also have their own speak methods that override the parent speak method to provide a different behavior for each subclass.

Here's an example of using these classes:
```
public class Main {
    public static void main(String[] args) {
        Animal animal1 = new Animal("Animal", 1);
        animal1.speak(); // prints "I am an animal."
        
        Dog dog1 = new Dog("Fido", 3);
        dog1.speak(); // prints "Woof!"
        
        Cat cat1 = new Cat("Whiskers", 2);
        cat1.speak(); // prints "Meow!"
    }
}
```
In this example, we create an instance of each class and call their speak methods. The Animal object prints the message "I am an animal.", while the Dog object prints "Woof!" and the Cat object prints "Meow!". This demonstrates polymorphism in action, where each object can be treated as its parent class Animal, but the Dog and Cat objects have their own specialized behavior defined in their speak methods.

1. Single inheritance:
In single inheritance, a subclass extends a single parent class. This is the most common type of inheritance. For example:
```
class Animal {
    void move() {
        System.out.println("Animals can move");
    }
}

class Dog extends Animal {
    void bark() {
        System.out.println("Dogs can bark");
    }
}
```
In this example, Dog is a subclass of Animal. It inherits the move() method from Animal, and adds a new bark() method.

2. Multilevel inheritance:
In multilevel inheritance, a subclass is derived from another subclass, which is derived from a parent class. For example:
```
class Animal {
    void move() {
        System.out.println("Animals can move");
    }
}

class Mammal extends Animal {
    void eat() {
        System.out.println("Mammals can eat");
    }
}

class Dog extends Mammal {
    void bark() {
        System.out.println("Dogs can bark");
    }
}
```
In this example, Dog is a subclass of Mammal, which is a subclass of Animal. Dog inherits the move() method from Animal, the eat() method from Mammal, and adds a new bark() method.

3. Hierarchical inheritance:
In hierarchical inheritance, two or more subclasses extend the same parent class. For example:
```
class Animal {
    void move() {
        System.out.println("Animals can move");
    }
}

class Dog extends Animal {
    void bark() {
        System.out.println("Dogs can bark");
    }
}

class Cat extends Animal {
    void meow() {
        System.out.println("Cats can meow");
    }
}
```

In this example, both Dog and Cat are subclasses of Animal. They both inherit the move() method from Animal, but Dog adds a new bark() method, while Cat adds a new meow() method.

4. Multiple inheritance:
Multiple inheritance is not directly supported in Java, but it can be simulated using interfaces. In this approach, a class can implement multiple interfaces, which define a set of methods that the class must implement. For example
```
interface Animal {
    void move();
}

interface Pet {
    void play();
}

class Dog implements Animal, Pet {
    public void move() {
        System.out.println("Dogs can move");
    }

    public void play() {
        System.out.println("Dogs can play");
    }
}
```
In this example, Dog implements both the Animal and Pet interfaces, which define the move() and play() methods, respectively. This allows Dog to have both the behavior of an animal and the behavior of a pet. Note that while this is not true multiple inheritance, it achieves a similar effect.

**What is the super keyword?**
In Java, the super keyword is used to refer to the superclass of a subclass. It can be used in two ways:

1. Call superclass constructor:
When a subclass is instantiated, its constructor automatically calls the constructor of its superclass. If the superclass has a parameterized constructor, the subclass constructor must call it using the super() keyword. For example:
```
class Animal {
    Animal(String name) {
        System.out.println("The animal's name is " + name);
    }
}

class Dog extends Animal {
    Dog(String name) {
        super(name);
        System.out.println("The dog's name is " + name);
    }
}
```
In this example, the Animal class has a parameterized constructor that takes a name argument. The Dog class extends Animal, and its constructor calls the Animal constructor using super(name). This ensures that the name parameter is passed to both the Animal and Dog constructors.

2. Call superclass methods:
A subclass can call methods of its superclass using the super keyword. This is useful when the subclass wants to override a method of the superclass but still use some of the superclass's behavior. For example:
```
class Animal {
    void move() {
        System.out.println("Animals can move");
    }
}

class Dog extends Animal {
    void move() {
        super.move();
        System.out.println("Dogs can run");
    }
}
```
In this example, the Dog class overrides the move() method of Animal, but still calls the move() method of Animal using super.move(). This ensures that the original behavior of move() is preserved, while adding new behavior specific to Dog.

**What is method overriding?**
Method overriding is a feature of object-oriented programming that allows a subclass to provide its own implementation of a method that is already defined in its superclass. The method in the subclass must have the same signature (name, parameters, and return type) as the method in the superclass.

When a method is called on an object of the subclass, the subclass's implementation of the method is executed instead of the superclass's implementation. This allows the subclass to customize the behavior of the inherited method to suit its own specific needs.

Here is an example of method overriding in Java:
```
class Animal {
    void makeSound() {
        System.out.println("The animal makes a sound");
    }
}

class Cat extends Animal {
    void makeSound() {
        System.out.println("Meow");
    }
}
```
In this example, the Animal class defines a makeSound() method that prints a generic message. The Cat class extends Animal and overrides the makeSound() method with its own implementation that prints "Meow".

When the makeSound() method is called on an instance of Cat, the subclass's implementation is executed instead of the superclass's implementation. For example:
```
Animal animal = new Animal();
animal.makeSound(); // Output: The animal makes a sound

Cat cat = new Cat();
cat.makeSound(); // Output: Meow

Animal catAsAnimal = new Cat();
catAsAnimal.makeSound(); // Output: Meow
```
In the last line, we create an instance of Cat and assign it to a variable of type Animal. Even though the variable is of type Animal, the actual object is still an instance of Cat. When we call makeSound() on the variable, the Cat class's implementation is executed because the object's actual type is used to determine which method to call.