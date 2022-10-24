class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
            return 0
        
        prev1 = 1
        prev2 = 1
        
        for i in range(1, len(s)):
            current = 0
            
            if s[i] != '0':
                current += prev1
            
            if int(s[i-1:i+1]) >= 10 and int(s[i-1:i+1]) <= 26:
                current += prev2
            
            prev1, prev2 = current, prev1
        
        return prev1
        