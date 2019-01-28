import java.util.Scanner;
import java.util.Random;
import java.util.Arrays;

class Search {
	public void search_m(int[] my_array) {

		//long start_time = System.currentTimeMillis();

		//GETTING INPUT NUMBER TO SEARCH
		System.out.println();
		System.out.println("Enter a number to search: ");
		//long mid_time1 = System.currentTimeMillis();
		Scanner sc = new Scanner(System.in);
		int num = sc.nextInt();
		//long mid_time2 = System.currentTimeMillis();

		int len = my_array.length;	//GETTING LENGTH OF ARRAY


		//LINEAR SEARCH ALGORITHM
		
		boolean flag = false;

		for(int i = 0; i < len; i++) {
			if(my_array[i] != num) {
				i++;
			}
			else if (my_array[i] == num) {
				System.out.println();
				System.out.println("The element is found at index" + i);
				flag = true;
				break;
			}
		}
		if(flag == false) {
			System.out.println();
			System.out.println("The required element is not found");
		}
	}
}
public class linear_search {
	public static void main(String[] args) {
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
		s.search_m(my_array);

		/*long end_time = System.currentTimeMillis();
		long total_time = end_time - start_time - (mid_time2 - mid_time1);*/
	}
}

