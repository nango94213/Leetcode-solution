public class Solution {
    public bool IsFascinating(int n) {
        int[] count = new int[9];
        
        var merge = n.ToString() + (2 * n).ToString() + (3 * n).ToString();
        
        foreach (char c in merge) {
            if (c == '0') {
                return false;
            }
            count[int.Parse(c.ToString())-1] += 1;
        }

        return string.Join(", ", count) == "1, 1, 1, 1, 1, 1, 1, 1, 1";
        
    }
}