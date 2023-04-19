package totalexpenses;

import java.text.DecimalFormat;
import java.util.Scanner;

/**
 *
 * @author Anurag
 */
public class TotalExpenses {

    /**
     * FLOW009 BEGINNER
     *
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        int[] quantity = new int[1001];
        int[] price = new int[1001];
        int n, i;
        double amount;
        DecimalFormat df = new DecimalFormat("#.000000");
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        for (i = 0; i < n; i++) {
            quantity[i] = sc.nextInt();
            price[i] = sc.nextInt();
        }
        for (i = 0; i < n; i++) {
            amount = quantity[i] * price[i];
            if (quantity[i] > 1000) {
                amount = (double) (amount - (0.1 * amount));
                System.out.println(df.format(amount));

            } else {
                System.out.println(df.format(amount));
            }

        }

    }

}
