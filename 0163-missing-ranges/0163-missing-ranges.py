class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        res = []
        
        for a in nums+[upper+1]:
            if a > lower:
                res.append([lower, a-1])
            lower = a + 1
        
        return res
        