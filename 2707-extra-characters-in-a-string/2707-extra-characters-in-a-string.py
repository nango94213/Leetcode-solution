class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        dp = [i+1 for i in range(len(s))]
        
        dictionary = set(dictionary)
        
        for i in range(len(s)):
            if s[:i+1] in dictionary:
                dp[i] = 0
            else:
                for j in range(i):
                    if s[j+1:i+1] in dictionary:
                        dp[i] = min(dp[i], dp[j])
                    dp[i] = min(dp[i], dp[i-1]+1)
      
        return dp[-1]
                
                
        
        