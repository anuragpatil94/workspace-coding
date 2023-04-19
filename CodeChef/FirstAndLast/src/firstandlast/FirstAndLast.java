package firstandlast;

import java.util.Scanner;

/**
 *
 * @author Anurag
 */
public class FirstAndLast {

    public static void main(String[] args) {
        try {
            int n, i, sum;
            int[] a = new int[1001];
            Scanner sc = new Scanner(System.in);
            n = sc.nextInt();
            for (i = 0; i < n; i++) {
                a[i] = sc.nextInt();
            }
            for (i = 0; i < n; i++) {
                sum = a[i] % 10;
                while (a[i] != 0) {
                    a[i] = a[i] / 10;
                    if (a[i] < 10) {
                        sum = sum + a[i];
                        System.out.println(sum);
                        break;
                    }
                }
            }
        } catch (Exception e) {

        }
    }
}
