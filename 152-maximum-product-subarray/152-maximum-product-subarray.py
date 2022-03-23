class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        max_sofar = nums[0]
        min_sofar = nums[0]
        res = nums[0]
        
        for n in nums[1:]:
            min_sofar, max_sofar = min(min_sofar*n, n, max_sofar*n), max(min_sofar*n, n, max_sofar*n)
            
            res = max(res, max_sofar)
        
        return res
        