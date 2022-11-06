class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        
        s = list(s)
        
        stack = []
        res = []
        i = 0
        
        while i < len(s):
            
            if stack and s[i] == s[i-1]:
                stack[-1] += 1
                if stack[-1] == k:
                    stack.pop()
                    del s[i-k+1:i+1]
                    i -= k
                    
                    
            else:
                stack.append(1)
            
            i += 1
        
        return ''.join(s)
            
        