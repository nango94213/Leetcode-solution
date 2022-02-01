class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        if len(nums) == 1:
            return 0
        
        l = 0
        jump = 1
        r = nums[0]
        
        
        while r < len(nums) - 1:
            jump += 1
            farthest = max(nums[i]+i for i in range(l, r+1))
            
            l, r = r + 1, farthest
        
        return jump
            
        