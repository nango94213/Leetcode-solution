class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        
        prev2 = 0
        prev1 = nums[0]
        
        res = 0
        
        for i in range(1, len(nums)):
            prev1, prev2 = max(prev2+nums[i], prev1), prev1
        
        return prev1