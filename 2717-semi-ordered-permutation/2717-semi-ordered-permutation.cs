public class Solution {
    public int SemiOrderedPermutation(int[] nums) {
        int n = nums.Length;
        int i = Array.IndexOf(nums, 1);
        int j = Array.IndexOf(nums, n);
        
        if (i < j) {
            return i + (n-j-1);
        } else {
            return i + (n-j-1) - 1;
        }
        
        
        
    }
}