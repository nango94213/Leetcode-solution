public class Solution {
    public long MaxStrength(int[] nums) {
        long total = 1;
        int c = -10;
        if (nums.Length == 1) {
            return nums[0];
        }
        int count = 0;
        int zero = 0;
        foreach (int n in nums) {
            if (n == 0) {
                zero += 1;    
                continue;
            }
            total *= n;
            if (n < 0 && n > c) {
                c = n;
            }
            if (n < 0) {
                count += 1;
            }
        }
        if (nums.Max() == 0 && count == 1) {
            return 0;
        }
        if (zero == nums.Length) {
            return 0;
        }
        if (total >= 0) {
            return total;
        } else {
            return total / c;
        }
    }
}