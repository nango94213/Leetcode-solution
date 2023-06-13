public class Solution {
    public int MinimizedStringLength(string s) {
        char[] charArray = s.ToCharArray();
        HashSet<char> set = new HashSet<char>(charArray);
        return set.Count;
        
    }
}