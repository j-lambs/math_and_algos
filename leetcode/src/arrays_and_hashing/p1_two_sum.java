package arrays_and_hashing;

import java.util.HashMap;

public class p1_two_sum {
    public static int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> map = new HashMap<Integer, Integer>(); // k = value in list, v = index in list
        map.put(nums[0], 0);    // put first list k,v pair in map

        for (int i = 1; i < nums.length; i++) {
            int dif = target - nums[i];
            if (map.containsKey(dif)) {
                return new int[]{i, map.get(dif)};
            } else {
                map.put(nums[i], i);
            }

        }
        return new int[]{0, 0};     // error
    }
    public static void main(String[] args) {
//        int[] nums = {2,7,11,15};
//        int target = 9;
//        OUT: [0,1]

        int[] nums = {3,2,4};
        int target = 6;
//        OUT: [1,2]

        for (Integer i: twoSum(nums, target)) {
            System.out.print(i + " ");
        }
    }
}
