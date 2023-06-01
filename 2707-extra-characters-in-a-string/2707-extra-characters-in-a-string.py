class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        dp = [0] * len(s)
        
        dictionary = set(dictionary)
        
        for i in range(len(s)):
            if s[:i+1] in dictionary:
                dp[i] = 0
            else:
                dp[i] = dp[i-1]+1 if i != 0 else 1
                for j in range(i):
                    if s[j+1:i+1] in dictionary:
                        dp[i] = min(dp[i], dp[j])
                    
      
        return dp[-1]
                
                
        
        