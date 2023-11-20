class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        res = []
        
        for n in nums+[upper+1]:
            if n > lower:
                res.append([lower, n-1])
            
            
            lower = n + 1
        return res
            