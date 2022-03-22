class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = -float('inf')
        
        current = 0
        
        for n in nums:
            current = n + max(0, current)
            res = max(res, current)
        
        return res
        