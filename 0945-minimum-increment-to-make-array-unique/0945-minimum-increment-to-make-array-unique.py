class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        
        nums.sort()
        res = 0
        need = 0
        
        for i in nums:
            res += max(need - i, 0)
            need = max(i + 1, need+1)
        
        return res