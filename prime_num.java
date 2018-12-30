import java.util.Scanner;
import java.lang.Math;

class prime_num {
	public static void main(String[] args) {
		long start_time = System.currentTimeMillis();
		int count = 0;
		int num, i = 2, j;
		long mid_time1 = System.currentTimeMillis();
		System.out.println("Enter a number: ");
		Scanner sc = new Scanner(System.in);
		num = sc.nextInt();
		long mid_time2 = System.currentTimeMillis();
		System.out.println("The first " + num + " prime numbers are: ");

		while(count < num) {
			for(j = 2; j <= i; j++) {
				if(i % j == 0 && i != j) {
					break;
				}
				else if(i % j == 0  && i == j) {
					System.out.println(i);
					count ++;
				}
			}
			i++;
		}
		long end_time = System.currentTimeMillis();
		long total_time = end_time - start_time - (mid_time2 - mid_time1);
		System.out.println("The total execution time for the program is: ");
		System.out.println((total_time/1000d) + " seconds");
	}
}