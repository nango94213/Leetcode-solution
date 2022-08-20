class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        
        stack = []
        s = list(s)
        
        i =0
        
        while i < len(s):
            
            if stack and s[i] == s[i-1]:
                stack[-1] += 1
                
                if stack[-1] == k:
                    del s[i-k+1:i+1]
                    i -= k
                    stack.pop()
            
            else:
                stack.append(1)
            i += 1
        
        return ''.join(s)
                    
         