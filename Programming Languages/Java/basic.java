public class Basic {
    public static void basic(String[] args) {
		// primitive data types 
        byte age =  30;
        long viewsCount = 3_123_123_121L;
        float price = 10.99F;
        char c = 'a';
        boolean isEligible = false;
		
		// reference data types
		Date now = new Date(); // creates an object/instance of the Date class
		System.out.println(now); // Thu Oct 20 15:03:17 IST 2022
		
		// String Operations
		String s = "Hello World!";
        System.out.println(s);
		String s = "Hello World!" + "!";
        System.out.println(s);
		System.out.println(s.endsWith("!")); // true
		System.out.println(s.length()); // 13
		System.out.println(s.indexOf("H")); // 0
		System.out.println(s.indexOf("ello")); // 1
		System.out.println(s.indexOf("sky")); // -1
		System.out.println(s.replace("!", "*")); // Hello World** /* Returns a new string object!! Does not edit the old object. */ Strings are immutable
		System.out.println(s.toLowerCase()); // hello world!!
		System.out.println(s.trim()); // remove white spaces from both sides
		String s = "Hello \"World\"!" + "!"; // escape sequences
		String file = "C:\\Windows\\..."; // print dirs by escaping back slashes
		
		// Arrays
		int[] numbers = {1,2,3,4,5};
        System.out.println(Arrays.toString(numbers)); // prints the array as a string
		System.out.println((numbers.length)); // 5
		Arrays.sort(numbers); // sort the array
		
		int[][] matrix = new int[2][3];
        matrix[0][1] = 1;
        System.out.println(Arrays.deepToString(matrix)); // [[0, 1, 0], [0, 0, 0]]
		final float pi = 3.14F; // final is a way to declare a constant in java
		
		double result = (double)10 / (double)3;
        System.out.println(result); // 3.3333333333333335
		
		// Implicit casting -- Happens when there is no chance f
        // byte > short > int > long > float > double
        double x = 1.1;
        double y = x + 2; // this int 2 will be auto caster to double (2.0)
        System.out.println(y);
		
		String x = "1"; // string to integer
        int y = Integer.parseInt(x) + 2;
        System.out.println(y);
		String x = "1.1";
        double y = Double.parseDouble(x) + 2;
        System.out.println(y);
		
		int x = Math.round(5.445F); // 5
        System.out.println(x);
        x = (int)Math.ceil(5.4F); // 6
        System.out.println(x);
        x = (int)Math.floor(5.4F); // 5
        System.out.println(x);
		int result = Math.max(1,2);
		
		int result = (int)Math.round(Math.random() * 100);
        System.out.println(result);
		
		// we cannot create an instantiation of an abstract class
		String result = NumberFormat.getPercentInstance().format(0.1); // method chaining
        System.out.println(result);
		
		// getting input 
		Scanner scanner = new Scanner(System.in);
        System.out.print("Name: ");
        String name = scanner.next(); // scanner.nextInt, nextFloat, nextByte etc..
        System.out.println("You are " + name); // You are maamu
		
		
    }
}