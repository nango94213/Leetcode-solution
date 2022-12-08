class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        dp = [0] * (high+1)
        dp[0] = 1
        for i in range(1, high+1):
            a = 0 if i - zero < 0 else dp[i-zero]
            b = 0 if i - one <  0 else dp[i-one]
            dp[i] = (a + b) % (10**9+7)
        
        return sum(dp[i] for i in range(low, high+1)) % (10**9+7)
        