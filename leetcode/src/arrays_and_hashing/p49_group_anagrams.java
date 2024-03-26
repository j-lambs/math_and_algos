package arrays_and_hashing;

import java.util.ArrayList;
import java.util.List;
import static java.util.Arrays.sort;

public class p49_group_anagrams {
    public static List<List<String>> groupAnagrams(String[] strs) {
        List<List<String>> myList = new ArrayList<>();

        // special case: strs is len 1
        if (strs.length == 1) {
            List<String> temp = new ArrayList<>();
            temp.add("\""  + strs[0] + "\"" );
            myList.add(temp);
            System.out.println(myList);
            return myList;
        }

        // general case: many strings
        // Can use a HashMaps for each string, where k = char, v = num occurances of char
        //
        // Here we will sort the Character List of each string
        for (String s: strs) {
            char[] charList = s.toCharArray(); // convert string to character arr
            sort(charList);
            System.out.println(charList);
        }



        return myList;
    }

    public static boolean isAnagram(String s1, String s2) {
        if (s1.length() != s2.length()) {
            return false; }


        return true;
    }


    public static void main(String[] args) {
        String[] strs = {"eat","tea","tan","ate","nat","bat"};
        // Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
//        String[] strs = {"a"};
//        Output: [[""]]

        for (String s: strs) {
            System.out.print(s + " ");
        }
        System.out.println();

        groupAnagrams(strs);

    }
}
