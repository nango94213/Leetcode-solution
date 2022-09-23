class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        
        dp = [0] * len(prices)
        
        dp[0] = 1
        
        for i in range(1, len(prices)):
            
            if prices[i] == prices[i-1] - 1:
                dp[i] = dp[i-1] + 1
                continue
            
            dp[i] = 1
       
        return sum(dp)