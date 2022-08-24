class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        
        stack = []
        remove = set()
        
        for i, v in enumerate(s):
            
            if v == '(':
                
                stack.append(i)
            
            if v == ')':
                
                if stack:
                    stack.pop()
                    continue
    
                remove.add(i)
        remove.update(stack)
        res = []
        
        for i in range(len(s)):
            
            if i not in remove:
                res.append(s[i])
        
        return ''.join(res)