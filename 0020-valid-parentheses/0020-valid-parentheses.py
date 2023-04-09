class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dic = {')':'(', ']':'[', '}':'{'}
        
        for c in s:
            if c not in dic:
                stack.append(c)
            else:
                if not stack or dic[c] != stack[-1]:
                    return False
                stack.pop()
                
        return stack == []
        