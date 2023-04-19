/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package thesmallestpair;

import java.util.Scanner;

/**
 *
 * @author AnuragPC
 */
public class TheSmallestPair {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        int t, n, i, j;
        int temp;
        int sum[] = new int[100000];
        int a[] = new int[100000];
        Scanner sc = new Scanner(System.in);
        t = sc.nextInt();
        for (i = 0; i < t; i++) {
            n = sc.nextInt();

            for (j = 0; j < n; j++) {
                a[j] = sc.nextInt();
            }
            temp = a[0] + a[1];

            for (int k = 0; k < n; k++) {

                for (int l = k + 1; l < n; l++) {
                    if (temp > (a[k] + a[l])) {
                        temp = a[k] + a[l];
                    }

                }

            }
            sum[i] = temp;

        }
        for (i = 0; i < t; i++) {
            System.out.println(sum[i]);
        }

    }
}
