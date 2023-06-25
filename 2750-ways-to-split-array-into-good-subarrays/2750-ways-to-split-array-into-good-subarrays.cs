public class Solution {
    public int NumberOfGoodSubarraySplits(int[] nums) {
        var total = nums.Sum();
        if (total == 0)
            return 0;
        long res = 1;
        int count = 0;
        bool s = false;
        long mod = (long)(Math.Pow(10, 9)+7);
        
        foreach (int n in nums) {
            if (n == 1 && s == false) {
                s = true;
            } else if (n == 0 && s == true) {
                count += 1;
            } else if (n == 1 && s == true) {
                res = (res*(count + 1)) % mod;
                count = 0;
            }
        }
        return (int)res;
        
    }
}