//even nums (2's), ends w 0 (5's), evenly divisible by 30 (3's),
// evenly divisible by 20 -> evenly divisible by 60 (bc has to be divisible by both 20 and 30)
// must also be a multiple of 110 (11*10) --> multiple of 660
//          additionally: 660 % 12 = 0
// must also be a multiple of 130 (13*10) -->  13*660 = 8580

// 145860

// 9699690 = product of all primes < 20

/**
 * This does not require programming at all.
 * Compute the prime factorization of each number from 1 to 20,
 * and multiply the greatest power of each prime together:
 *
 * Given: 2520 is smallest multiple evenly divisible by int {1,2,... 10}
 *
 Find all the prime factors of each given number.
 List all the prime numbers found, as many times as they occur most often for any one given number.
 Multiply the list of prime factors together to find the LCM.


/**
 * looking for smallest num that is evenly divided by ints 1-20
 */
public class p5_smallest_multiple {
    public static void main(String [] args) {
        System.out.println(bruteForceSmallestMultiple());
    }
    public static int bruteForceSmallestMultiple() {
        int magic = 8580;
        int i = magic;
        while (i % 7 != 0 ||
                i % 11 != 0 ||
                i % 12 != 0 ||
                i % 13 != 0 ||
                i % 14 != 0 ||
                i % 15 != 0 ||
                i % 16 != 0 ||
                i % 17 != 0 ||
                i % 18 != 0 ||
                i % 19 != 0) {
            i += magic;
        }
        return i;
    }
}
