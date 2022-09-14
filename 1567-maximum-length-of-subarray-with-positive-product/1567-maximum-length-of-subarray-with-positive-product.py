class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        
        negative = 0
        positive = 0
        res = 0
        
        for n in nums:
            
            if n == 0:
                negative = positive = 0
            
            if n < 0:
                positive, negative = negative + 1 if negative else 0, positive + 1
            
            if n > 0:
                positive, negative = positive + 1, negative + 1 if negative else 0
            
            res = max(res, positive)
        
        return res
            
            
            
        