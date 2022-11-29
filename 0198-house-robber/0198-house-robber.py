class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prev2 = 0
        prev1 = nums[0]
        
        for i in range(1, len(nums)):
            current = max(nums[i]+prev2, prev1)
            prev1, prev2 = current, prev1
        
        return prev1
        