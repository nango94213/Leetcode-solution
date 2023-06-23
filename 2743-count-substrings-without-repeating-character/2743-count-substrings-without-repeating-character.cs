public class Solution {
    public int NumberOfSpecialSubstrings(string s) {
        Dictionary<char, int> test = new Dictionary<char, int> ();
        int res = 0;
        int left = 0;
        for (int right = 0; right < s.Length; right++) {
            if (test.ContainsKey(s[right])) {
                left = Math.Max(left, test[s[right]]+1);
            }
            res += right - left + 1;
            test[s[right]] = right;
        }
        return res;
    }
}