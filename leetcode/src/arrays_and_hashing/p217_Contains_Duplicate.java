package arrays_and_hashing;

import java.util.HashSet;
public class p217_Contains_Duplicate {
    public static boolean containsDuplicate(int[] nums) {
        HashSet set = new HashSet();
        for (int num : nums) {
            if (set.contains(num)) {
                return true;
            } else {
                set.add(num);
            }
        }
        return false;
    }
    public static void main(String[] args) {
        int[] list = {1, 2, 3, 4};
        int[] list2 = {1, 2, 1};
        System.out.println(containsDuplicate(list));
        System.out.println(containsDuplicate(list2));
    }
}
