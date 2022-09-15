class Solution:
    def findDerangement(self, n: int) -> int:
        
        if n < 2:
            return 0
        
        dp = [0] * n
        dp[1] = 1
        for i in range(2, n):
            dp[i] = i * (dp[i-2] + dp[i-1]) % (10**9+7)

        return dp[-1]
        