public class Solution {
    public int CountBeautifulPairs(int[] nums) {
        int GCD(int a, int b) {
            if (b == 0)
                return a;
            else
                return GCD(b, a%b);
        }
        int res = 0;
        for (int i = 0; i < nums.Length; i++) {
            for (int j = i+1; j < nums.Length; j++) {
                var a = nums[i].ToString()[0];
                var b = nums[j].ToString();
                b = b[b.Length-1].ToString();
                if (GCD(int.Parse(a.ToString()), int.Parse(b)) == 1)
                    res += 1;
            }
                
        }
        return res;
                
        
    }
}