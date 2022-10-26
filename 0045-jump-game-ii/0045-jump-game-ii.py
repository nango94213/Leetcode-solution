class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        if len(nums) == 1:
            return 0
        
        res = 0
        
        left = 0
        right = 0
        
        while right < len(nums) - 1:
            
            largest = max(i + nums[i] for i in range(left, right+1))
            
            left, right = right + 1, largest
            
            res += 1
        
        return res