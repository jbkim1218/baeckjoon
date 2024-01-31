import java.util.Scanner;

public class Main {
	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);

		int[] arr = new int[10];
		int count = 0;

		for (int i = 0; i < arr.length; i++) {
			arr[i] = sc.nextInt() % 42;

			boolean check = false;
			for (int j = 0; j < i; j++) {
				if (arr[i] == arr[j]) {
					check = true;
					break;
				} else {
					check = false;
				}
			}

			if (check == false) {
				count++;
			}

		}

		System.out.println(count);
	}
}