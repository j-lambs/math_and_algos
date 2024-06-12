package arrays_and_hashing;

import java.util.*;

public class p347_top_k_frequent_elts {
    public static void main(String[] args) {
        int[] nums = {1, 1, 1, 2, 2, 3};
        topKFrequent(nums, 2);


    }
    public static int[] topKFrequent(int[] nums, int k) {
        HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();
        Set<Integer> set = new HashSet<Integer>();


        // create hashmap with elts and their frequency in 'nums'
        for(int i : nums) {
            set.add(i);
            map.put(i, (int) map.getOrDefault(i, 0) + 1);
            System.out.print(i + ", ");
            System.out.println(map.get(i));
        }

        PriorityQueue<Integer> pq = new PriorityQueue<Integer>();
        for(Integer i : set) {
            pq.add(map.get(i));
        }

        return new int[0];
    }
}
