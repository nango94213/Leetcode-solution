class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        if len(nums) == 1:
            return 0
        
        jump = 1
        
        left = 0
        right = nums[0]
        farthest = 0
        
        while right < len(nums) - 1:
            farthest = max(i+nums[i] for i in range(left, right+1))
            
            jump += 1
            
            left, right = right + 1, farthest
        
        return jump
        