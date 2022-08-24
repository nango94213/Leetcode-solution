class Solution:
    def maxDepth(self, s: str) -> int:
        
        stack = []
        res = 0
        count = 0
        
        for c in s:
            
            if c == '(':
                
                stack.append(c)
                count += 1
                res = max(res, count)
            
            if c == ')':
                
                stack.pop()
                count -= 1
        
        return res
                
            