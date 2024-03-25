import java.util.HashMap;
public class Main {

    public static void main(String[] args) {
        int[] nums = new int[]{2, 7, 11, 15, 1};
        int target = 3;

        HashMap t = new HashMap();
        t.put(nums[0], 0);
        for (int i = 1; i < nums.length; i++) {
            int res = target - nums[i];
            if (t.containsKey(res)) {
                System.out.println(t.get(res) + " " + i);
                break;
            }
            t.put(nums[i], i);
        }
    }
}