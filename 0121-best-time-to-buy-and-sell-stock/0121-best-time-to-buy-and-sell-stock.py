class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prev = float('inf')
        res = 0
        for p in prices:
            if prev < p:
                res = max(res, p - prev)
            else:
                prev = p
        return res
                
                