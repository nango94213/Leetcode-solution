class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        
        res = -1
        low = nums[0]
        
        for i in range(1, len(nums)):
            if nums[i] > low:
                res = max(res, nums[i]-low)
            
            low = min(nums[i], low)
        
        return res
        