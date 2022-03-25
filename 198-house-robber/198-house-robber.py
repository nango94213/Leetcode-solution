class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        
 
        
        two = nums[0]
        one = max(nums[0], nums[1])
        
        for i in range(2, len(nums)):
            two, one = one, max(two+nums[i], one)
        
        return one
        
        