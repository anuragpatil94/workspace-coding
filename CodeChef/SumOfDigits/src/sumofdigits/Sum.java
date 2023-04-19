package sumofdigits;

import java.util.Scanner;

/**
 *
 * @author Anurag
 */
public class Sum {

    /**
     * FLOW006 Beginner
     */
    public static void main(String[] args) {
        // TODO code application logic here
        int[] a = new int[1001];
        int sum = 0, i;
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        for (i = 0; i < n; i++) {
            a[i] = sc.nextInt();
        }
        for (i = 0; i < n; i++) {
            sum = 0;
            while (a[i] != 0) {
                sum = sum + a[i] % 10;
                a[i] = a[i] / 10;
            }
            System.out.println(sum);
        }

    }

}
