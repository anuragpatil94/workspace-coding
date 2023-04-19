package reversenumber;

import java.util.Scanner;

/**
 *
 * @author Anurag
 */
public class ReverseNumber {

    /**
     * FLOW 007 BEGINNER
     *
     * @param args
     */
    public static void main(String[] args) {
        // TODO code application logic here
        int[] a = new int[1001];
        int i, j, k, temp;
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        for (i = 0; i < n; i++) {
            a[i] = sc.nextInt();
        }
        for (i = 0; i < n; i++) {
            temp = 0;
            while (a[i] != 0) {
                k = a[i] % 10;
                temp = (temp * 10) + k;

                a[i] = a[i] / 10;
            }
            System.out.println(temp);
        }
    }

}
