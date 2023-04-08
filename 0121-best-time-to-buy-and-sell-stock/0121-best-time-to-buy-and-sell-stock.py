class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_sofar = float('inf')
        res = 0
        
        for p in prices:
            res = max(p-min_sofar, res)
            
            min_sofar = min(p, min_sofar)
        
        return res
        