/**
 * Learned: 2 arrays, even if they contain the same values, != .equals() each other
 *              - .equals() checks if they have same memory address, not if they have same values
 */

package arrays_and_hashing;

import java.util.*;
import static java.util.Arrays.sort;
public class p49_group_anagrams {
    public static List<List<String>> groupAnagrams(String[] strs) {
        List<List<String>> myList = new ArrayList<>();
        HashMap<String, Integer> map = new HashMap<String, Integer>();    // k = sortedString, v = index in List<List<String>>

        // special case: strs is len 1
        if (strs.length == 1) {
            List<String> temp = new ArrayList<>();
            temp.add(strs[0]);
            myList.add(temp);
            return myList;
        }

        // general case: many strings
        // Can use a HashMaps for each string, where k = char, v = num occurrences of char

        // Here we will sort the Character List of each string
        //
        Integer group_num = -1;
        for (String s: strs) {
            char[] charList = s.toCharArray(); // convert string to character arr
            sort(charList);
            String sortedString = new String(charList);

            // if 's' is not an anagram of a previous word in the list
            //      then add it to HM
            //      add it to new section in
            if (!map.containsKey(sortedString)) {
                ++group_num;    // update the index in the List of Lists containing Strings
                map.put(sortedString, group_num);
                List<String> tempList = new ArrayList<>();
                tempList.add(s);
                myList.add(tempList);
            }
            // 's' is an anagram of another string we've already seen
            else {
                Integer indexGroup = map.get(sortedString);
                (myList.get(indexGroup)).add(s);    // append 's' to same list containing its anagrams
            }
        }

        return myList;
    }


    public static void main(String[] args) {
        String[] strs = {"eat","tea","tan","ate","nat","bat"};
        // Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
//        String[] strs = {"a"};
//        Output: [["a"]]

        List<List<String>> list = groupAnagrams(strs);

        int x = 0;
//        char[] c2 = {'c', 'b'};
//
//        ArrayList<Character> c3 = new ArrayList<>();
//        c3.add('c');
//        c3.add('a');
//        Collections.sort(c3);
//
//        for (Character i: c3) {
//            System.out.println(i);
//        }
    }
}
