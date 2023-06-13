public class Solution {
    public int LongestSemiRepetitiveSubstring(string s) {
        int left = 0;
        int p = 0;
        for (int right = 0; right < s.Length; right ++) {
            if (right != 0 && s[right] == s[right-1]) {
                p += 1;
            }
            
            if (p > 1) {
                if (s[left] == s[left+1]) {
                    p -= 1;
                }
                left += 1;
            }
        }
        return s.Length - left;
        
    }
}