package addnumbers;

import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        try {
            int a, b;
            int[] c = new int[1001];
            Scanner sc = new Scanner(System.in);
            int n = sc.nextInt();
            for (int i = 0; i < n; i++) {
                a = sc.nextInt();
                b = sc.nextInt();
                c[i] = a + b;
            }
            for (int i = 0; i < n; i++) {
                System.out.println(c[i]);
            }
        } catch (Exception e) {

        }
    }
}
