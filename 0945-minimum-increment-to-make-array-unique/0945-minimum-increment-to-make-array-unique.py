class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        
        res = 0
        
        need = 0
        
        for n in nums:
            res += max(need-n, 0)
            need = max(need+1, n+1)
            
        return res
        