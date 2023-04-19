package findreminder;

import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        try {
            Scanner sc = new Scanner(System.in);
            int n = sc.nextInt();
            int[] c = new int[1001];
            int i, a, b;
            for (i = 0; i < n; i++) {
                a = sc.nextInt();
                b = sc.nextInt();
                c[i] = a % b;
            }
            for (i = 0; i < n; i++) {
                System.out.println(c[i]);
            }
        } catch (Exception e) {

        }
    }

}
