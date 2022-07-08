import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {
	
    public static void main(String[] args) {
        int i = 4;
        double d = 4.0;
        String s = "HackerRank ";
		
        Scanner scan = new Scanner(System.in);

        /* Declare second integer, double, and String variables. */
        int integer_2;
        double double_2;
        String str2; 
        /* Read and save an integer, double, and String to your variables.*/
        integer_2 = scan.nextInt();
        double_2 = scan.nextDouble();
        scan.nextLine();
        str2 = scan.nextLine();
        // Note: If you have trouble reading the entire String, please go back and review the Tutorial closely.
        
        /* Print the sum of both integer variables on a new line. */
        System.out.println(i + integer_2);  
        /* Print the sum of the double variables on a new line. */
		System.out.println(d + double_2);  
        /* Concatenate and print the String variables on a new line; 
        	the 's' variable above should be printed first. */
        System.out.println(s.concat(str2));      

        scan.close();
    }
}