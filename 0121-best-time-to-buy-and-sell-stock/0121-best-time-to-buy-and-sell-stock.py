class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        currentMax = prices[0]
        res = 0
        for p in prices:
            if p > currentMax:
                res = max(res, p - currentMax)
            
            if p < currentMax:
                currentMax = p
        
        return res