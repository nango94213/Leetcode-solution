public class Solution {
    public int FindNonMinOrMax(int[] nums) {
        var minN = nums.Min();
        var maxN = nums.Max();
  
        foreach (int n in nums) {
            if (n != minN && n != maxN) {
                return n;
            }
        }
        return -1;
        
    }
}