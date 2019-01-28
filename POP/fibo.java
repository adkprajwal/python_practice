import java.util.Scanner;

class fibo{  
 static long n1 = 0, n2 = 1, n3 = 0;    
 static void printFibonacci(int count){    
    if(count > 0){    
         n3 = n1 + n2;    
         n1 = n2;    
         n2 = n3;    
         System.out.print(" "+n3);   
         printFibonacci(count-1);    
     }    
 }    
 public static void main(String args[]){ 
    long start_time = System.currentTimeMillis();

    //GETTING NUMBER OF TERMS TO GENERATE AS INPUT
    System.out.println("Enter number of terms: ");
    long mid_time1 = System.currentTimeMillis();  
    Scanner sc = new Scanner(System.in);
    int count = sc.nextInt();

    long mid_time2 = System.currentTimeMillis();   
       
    System.out.print(n1+" "+n2);    
    printFibonacci(count-2); 

    long end_time = System.currentTimeMillis(); 
    long total_time = end_time - start_time -(mid_time2 - mid_time1);
    System.out.println();
    System.out.println("Execution time: " + (total_time/1000d) + "Second");
 }  
}  