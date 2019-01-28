import java.util.Scanner;
import java.util.Random;
import java.util.Arrays;

class Search {
	public void search_m(int[] my_array,int num, int len) {
		//BINARY SEARCH ALGORITHM
		int start = 0;
		int end = len - 1;
		boolean flag = false;

		while(start < end) {
			int mid = ((start + end) / 2);
			if (my_array[mid] < num) {
				start = mid + 1;
			}
			else if (my_array[mid] > num ) {
				end = mid - 1;
			}
			else {
				System.out.println();
				System.out.println("The required number is found at index: " + mid);
				flag = true;
				break;
			}
		}
		if (flag == false) {
				System.out.println();
				System.out.println("The required number is not found");				
		}
	}
}
public class binary_search {
	public static void main(String[] args) {
		long start_time = System.currentTimeMillis();
		Search s = new Search();

		//GENERATING ARRAY OF RANDOM NUMBERS AND PRINTING THE ARRAY
		int[] my_array = new int[1000];
		System.out.println();
		for(int i = 0; i < 1000; i++) {
			Random rand = new Random();
			my_array[i] = rand.nextInt(20000) + 1;
			if(i == 0) {
				System.out.print("[" + my_array[i] + ", ");
			}
			else if(i > 0 && i < 999){
				System.out.print(my_array[i] + ", ");
			}
			else {
				System.out.print(my_array[i]+"]");
				System.out.println();
			}
		}

		//PRINTING SORTED ARRAY
		Arrays.sort(my_array);
		System.out.println();
		System.out.println("The sorted array is: ");
		System.out.println();

		for(int i = 0; i < 1000; i++) {
			if(i == 0) {
				System.out.print("[" + my_array[i] + ", ");
			}
			else if(i > 0 && i < 999){
				System.out.print(my_array[i] + ", ");
			}
			else {
				System.out.print(my_array[i]+"]");
				System.out.println();
			}
		}

		//GETTING INPUT NUMBER TO SEARCH
		System.out.println();
		System.out.println("Enter a number to search: ");
		long mid_time1 = System.currentTimeMillis();
		Scanner sc = new Scanner(System.in);
		int num = sc.nextInt();
		long mid_time2 = System.currentTimeMillis();

		int len = my_array.length;	//GETTING LENGTH OF ARRAY
		s.search_m(my_array, num, len);

		long end_time = System.currentTimeMillis();
		long total_time = end_time - start_time - (mid_time2 - mid_time1);
	}
}

