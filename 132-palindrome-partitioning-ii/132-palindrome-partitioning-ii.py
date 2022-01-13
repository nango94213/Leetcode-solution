class Solution:
    def minCut(self, s: str) -> int:
        
        
        dp = [float('inf')]*len(s)
        dp[0] = 0
        
        for i in range(1, len(s)):
            if s[:i+1] == s[:i+1][::-1]:
                dp[i] = 0
            else:
                for j in range(i):
                    if dp[j] != float('inf') and s[j+1:i+1] == s[j+1:i+1][::-1]:
                        dp[i] = min(dp[i], dp[j] + 1)
        return  dp[-1]
                    
            
        