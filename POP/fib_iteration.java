import java.util.Scanner;

class fib_iteration {
	public static void main(String[] args) {
		long start_time = System.currentTimeMillis();
		long a = 0, b = 1;
		System.out.println("Enter the number of terms: ");
		long mid_time1 = System.currentTimeMillis();
		Scanner sc = new Scanner(System.in);
		int num = sc.nextInt();
		long mid_time2 = System.currentTimeMillis();
		System.out.println();
		System.out.println(a);
		System.out.println(b);
		for(int i = 1; i <= (num-2); i++) {
			long c = a + b;
			System.out.println(c);
			a = b;
			b = c;
		}
		long end_time = System.currentTimeMillis();
		long total_time = end_time - start_time - (mid_time2 - mid_time1);
		System.out.println("The total execution time for the program is:" + (total_time/1000d) +  "seconds");
	}
}