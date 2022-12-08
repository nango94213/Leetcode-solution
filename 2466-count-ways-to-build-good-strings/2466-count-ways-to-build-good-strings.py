class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        dp = Counter()
        dp[0] = 1
        for i in range(1, high+1):
            dp[i] = (dp[i-zero] + dp[i-one]) % (10**9+7)
        
        return sum(dp[i] for i in range(low, high+1)) % (10**9+7)
        