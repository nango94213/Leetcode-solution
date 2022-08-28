class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        minSofar = prices[0]
        res = 0
        
        for p in prices[1:]:
            
            if p < minSofar:
                minSofar = p
                continue
            
            res = max(p-minSofar, res)
        
        return res
        