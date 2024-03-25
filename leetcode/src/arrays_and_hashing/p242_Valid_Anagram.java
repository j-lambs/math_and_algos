//Given two strings s and t, return true if t is an anagram of s, and false otherwise.
// Time Complexity: O(n^2)
// Memory Complexity: O(n^2)
package arrays_and_hashing;
import java.util.HashMap;
public class p242_Valid_Anagram {
    public static boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) {
            return false;
        }

        HashMap map1 = makeCharacterHM(s);
        HashMap map2 = makeCharacterHM(t);

        if (map1.equals(map2)) {
            return true;
        }
        return false;
    }
    public static HashMap makeCharacterHM(String str) {
        HashMap<Character, Integer> map = new HashMap<>();
        for (int i = 0; i < str.length(); i++) {
            char k = str.charAt(i);
            if (map.containsKey(k)) {
                map.put(k, map.get(k) + 1);
            } else {
                map.put(k, 1);
            }
        }
        return map;
    }
    public static void main(String[] args) {
        String s = "anagram", t = "nagaram";
        System.out.println(isAnagram(s,t));

        s = "rat"; t = "car";
        System.out.println(isAnagram(s,t));
    }
}
