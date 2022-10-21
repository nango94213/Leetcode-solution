class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        
        stack = []
        remove= set()
        
        for i in range(len(s)):
            
            if s[i] == '(':
                stack.append(i)
            
            if s[i] == ')':
                if stack:
                    stack.pop()
                else:
                    remove.add(i)
        
        remove.update(stack)
        
        res = []
        for i in range(len(s)):
            if i not in remove:
                res.append(s[i])
                
        return ''.join(res)
                