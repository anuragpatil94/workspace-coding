package smallestnumbersofnotes;

import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        try {
            Scanner sc = new Scanner(System.in);
            int T = sc.nextInt();
            int a[] = new int[1001];
            int b[] = {100, 50, 10, 5, 2, 1};
            int i, temp;
            for (i = 1; i <= T; i++) {
                a[i] = sc.nextInt();
            }
            for (i = 1; i <= T; i++) {
                temp = a[i];
                int N = 0;
                for (int j = 0; j < b.length; j++) {
                    if (temp >= b[j]) {
                        N = N + temp / b[j];
                        temp = temp % b[j];
                    }
                }
                System.out.println(N);
            }
        } catch (Exception e) {

        }
    }
}
