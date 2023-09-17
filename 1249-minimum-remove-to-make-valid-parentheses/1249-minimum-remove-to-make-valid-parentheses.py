class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        remove = set()
        
        stack = []
        
        for i, v in enumerate(s):
            if v == '(':
                stack.append(i)
            if v == ')':
                if not stack:
                    remove.add(i)
                else:
                    stack.pop()
        remove.update(stack)
        res = ''
        for i in range(len(s)):
            if i not in remove:
                res += s[i]
        
        return res
        