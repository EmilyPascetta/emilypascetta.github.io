import java.util.Scanner;

public class TipCalculator {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Would you like to calculate tip by bill or calculate tip percentage by tip amount?");
        System.out.println("Enter 1 or 2");
        double choice = scanner.nextInt();
        while(choice != 1 && choice != 2){
            System.out.println("Invalid choice, please choose 1 or 2");
             choice = scanner.nextInt();
        }

        if(choice == 1) {
            System.out.print("Enter the bill amount: $");
            double sum = scanner.nextDouble();

            System.out.print("Enter the tip percentage: ");
            double amount = scanner.nextDouble();

            double tipAmount = (amount / 100) * sum;

            double totalAmount = sum + tipAmount;

            System.out.printf("Tip Amount: $%.2f%n", tipAmount);
            System.out.printf("Total Amount (Including Tip): $%.2f%n", totalAmount);
        }
        else{
            System.out.print("Enter the total bill amount: $");
            double totalBill = scanner.nextDouble();

            System.out.print("Enter the tip amount: $");
            double tipAmount = scanner.nextDouble();

            double tipPercentage = (tipAmount / totalBill) * 100;

            System.out.printf("The tip percentage is: %.2f%% %n", tipPercentage);

        }

        scanner.close();
    }
}
