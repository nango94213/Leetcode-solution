class Solution:
    def minCut(self, s: str) -> int:
        dp = [sys.maxsize] * (len(s)+1)
        dp[0] = 0
        for j in range(1, len(s)+1):
            for i in range(j):
                if dp[i] != sys.maxsize and s[i:j] == s[i:j][::-1]:
                    dp[j] = min(dp[j], dp[i]+1)
        return dp[-1]-1
        