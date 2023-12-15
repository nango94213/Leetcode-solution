class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        prev = 0
        res = -float('inf')
        for n in nums:
            current = max(n, n + prev)
            res = max(res, current)
            prev = current
        
        return res
        