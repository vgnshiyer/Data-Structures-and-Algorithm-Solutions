import java.text.NumberFormat;
import java.util.Scanner;

public class main {
    /*
    Principal:
    Interest:
    Period (Years):

    M = P * (r * (1 + r)^n)/((1 + r)^n - 1)
     */
    public static String getMortgage(int p, float r, int n){
        double M = p * (r * Math.pow((1 + r), n))/(Math.pow((1 + r),n) - 1);
        return NumberFormat.getCurrencyInstance().format(M);
    }

    public static void main(String[] args) {
        final byte MONTHS_IN_YEAR = 12;
        final byte PERCENT = 100;

        Scanner scanner = new Scanner(System.in);

        int principal;
        while(true) {
            System.out.print("Principal: ");
            principal = scanner.nextInt();
            if(principal < 1000 || principal >100000)
                System.out.println("Enter an amount in the range 1000 to 100000");
            else break;
        }

        float annualInterest;
        while(true){
            System.out.print("Annual Interest: ");
            annualInterest = scanner.nextFloat();
            if(annualInterest < 1 || annualInterest > 30)
                System.out.println("Enter a an interest rate in the range 1 to 30");
            else break;
        }
        float monthlyInterest = annualInterest / MONTHS_IN_YEAR / PERCENT;

        int years;
        while(true) {
            System.out.print("Period (Years): ");
            years = scanner.nextInt();
            if(years < 1 || years > 30)
                System.out.println("Enter a tenure in the range of 1 to 10");
            else break;
        }
        int months = years * MONTHS_IN_YEAR;

        String M = getMortgage(principal, monthlyInterest, months);
        System.out.println(M);
    }
}