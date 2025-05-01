import java.util.*;

class HouseRobber {
    public static void main(String[] args) {
        System.out.println("Hello World!");
        // int[] houses = {9,2,2,8,10,8,5,17,15,3,17,19,3,2,8};
        int[] houses = {9,2,2,8,10,8,5};
        for (int house : houses) {
            System.out.print(house + " ");
        }
        System.out.println();
        System.out.println("Max Profit: " + rob(houses));

        System.out.println();
        System.out.println("Max Profit: " + robSkip2(houses));
    }

    public static int rob(int[] nums) {
        int firstHouseValue = 0;
        int secondHouseValue = 0;

        for (int i : nums) {
            int tempMax = Math.max(i + firstHouseValue, secondHouseValue);
            firstHouseValue = secondHouseValue;
            secondHouseValue = tempMax;
            System.out.println("Cur Total Profit: " + secondHouseValue);
        }
        System.out.println();
        return secondHouseValue;
    }

    public static int robSkip2(int[] nums) {
        int firstHouseValue = 0;
        int secondHouseValue = 0;
        int thirdHouseValue = 0;

        for (int i = 0; i < nums.length; i++) {
            int tempMax = max3(nums[i] + firstHouseValue, nums[i + 1] + secondHouseValue, thirdHouseValue);
            int temp = secondHouseValue;
            firstHouseValue = secondHouseValue;
            secondHouseValue = thirdHouseValue;
            thirdHouseValue = tempMax;

        }
        return 0;
    }

    public static int max3(int a, int b, int c) {
        int maxAB = Math.max(a, b);
        int maxBC = Math.max(b, c);
        int maxAC = Math.max(a, c);

        if (maxAB == maxAC)
            return a;
        else if (maxAB == maxBC)
            return b;
        else
            return c;
    }
}
