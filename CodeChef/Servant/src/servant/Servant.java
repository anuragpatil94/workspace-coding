package servant;

import java.util.Scanner;

/**
 *
 * @author Anurag
 */
public class Servant {

    /**
     * FLOW008 Beginner
     *
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        int[] a = new int[1001];
        int i, n;
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        for (i = 0; i < n; i++) {
            a[i] = sc.nextInt();
        }
        for (i = 0; i < n; i++) {
            if (a[i] < 10) {
                System.out.println("What an obedient servant you are!");
            } else {
                System.out.println("-1");
            }
        }
    }

}
