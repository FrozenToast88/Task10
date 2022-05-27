import java.time.LocalDate;
import java.util.Scanner;

public class Poised {

    public static void main(String[] args) {

        Scanner input = new Scanner(System.in); // scanner

        // user input requested
        System.out.println("Enter project number : ");
        int questionP1 = input.nextInt();

        System.out.println("Enter project name : ");
        String questionP2 = input.next();

        System.out.println("What type of building is being designed? exp'house, apartment block or store, ect ");
        String questionP3 = input.next();

        System.out.println("Enter project Address : ");
        String questionP4 = input.next();

        System.out.println("Enter in the ERF number : ");
        int questionP5 = input.nextInt();

        System.out.println("Enter total fee being charged for the project : ");
        double questionP6 = input.nextDouble();

        System.out.println("Enter total amount paid to dat : ");
        double questionP7 = input.nextDouble();

        System.out.println("Enter deadline for the project : Example 'yyyy-mm-dd' ");
        LocalDate questionP8 = (LocalDate.parse(input.next()));



        System.out.println("Enter Architect Name : ");
        String questionA1 = input.next();

        System.out.println("Enter Architect Telephone Number : ");
        int questionA2 = input.nextInt();

        System.out.println("Enter Architect Email Address  : ");
        String questionA3 = input.next();

        System.out.println("Enter Architect physical Address  : ");
        String questionA4 = input.next();



        System.out.println("Enter Contractor Name : ");
        String questionCo1 = input.nextLine();

        System.out.println("Enter Contractor Telephone Number : ");
        int questionCo2 = input.nextInt();

        System.out.println("Enter Contractor Email Address  : ");
        String questionCo3 = input.next();

        System.out.println("Enter Contractor Physical Address  : ");
        String questionCo4 = input.next();




        System.out.println("Enter Client Name : ");
        String questionCl1 = input.next();

        System.out.println("Enter Client Telephone Number : ");
        int questionCl2 = input.nextInt();

        System.out.println("Enter Client Email Address  : ");
        String questionCl3 = input.next();

        System.out.println("Enter Client Physical Address  : ");
        String questionCl4 = input.next();


        //captured project,architect,contractor,client class user data requested
        project Assignment = new project(questionP1 ,questionP2 ,questionP3 ,questionP4 ,questionP5 ,questionP6 ,questionP7 ,questionP8);
        architect Designer = new architect(questionA1 ,questionA2 ,questionA3,questionA4);
        contractor Builder = new contractor(questionCo1 ,questionCo2 ,questionCo3,questionCo4);
        client Customer = new client(questionCl1,questionCl2,questionCl3,questionCl4);

        //All classes data captured displayed
        System.out.println(Assignment);
        System.out.println(Designer);
        System.out.println(Builder);
        System.out.println(Customer);

    }
}

