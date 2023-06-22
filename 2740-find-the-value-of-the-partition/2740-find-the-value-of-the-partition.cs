public class Solution {
    public int FindValueOfPartition(int[] nums) {
        var res = int.MaxValue;
        Array.Sort(nums);
        for (int i = 1; i < nums.Length; i++ ) {
            res = Math.Min(res, nums[i]-nums[i-1]);
        }
        return res;
    }
}