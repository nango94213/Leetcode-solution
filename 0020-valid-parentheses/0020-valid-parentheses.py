class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dic = {')':'(', ']':'[', '}':'{'}
        
        for c in s:
            if c in dic:
                if not stack or stack[-1] != dic[c]:
                    return False
                stack.pop()
            else:
                stack.append(c)
        
        return True if not stack else False
        