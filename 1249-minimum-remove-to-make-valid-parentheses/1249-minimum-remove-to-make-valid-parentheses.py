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
                else:
                    
                    remove.add(i)
        
        remove.update(stack)
        res = []

        for i, v in enumerate(s):
            
            if i not in remove:
                res.append(v)
        
        return ''.join(res)