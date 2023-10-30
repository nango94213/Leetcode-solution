class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        sofar = prices[0]
        
        for i in range(1, len(prices)):
            if prices[i] > sofar:
                res = max(res, prices[i] - sofar)
            if prices[i] < sofar:
                sofar = prices[i]
        
        return res
        