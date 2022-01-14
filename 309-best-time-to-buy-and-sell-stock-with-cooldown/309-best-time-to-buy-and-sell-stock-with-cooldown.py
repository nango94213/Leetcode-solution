class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n <= 1:
            return 0
        dp = [[0, 0] for i in range(n+1)]
        dp[1][1] = 0 - prices[0] 
        for i in range(2, n+1):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i-1])    #don't buy or sell
            dp[i][1] = max(dp[i-2][0] - prices[i-1], dp[i-1][1])     # buy on i-th day or don't buy
        return max(dp[-1])