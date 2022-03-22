class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        min_price = prices[0]
        res = 0
        
        for p in prices:
            res = max(res, p - min_price)
            
            min_price = min(p, min_price)
        
        return res
        