class Solution:
    def isValid(self, s: str) -> bool:
        
        dic = {'(':')', '{':'}', '[':']'}
        
        stack = []
        
        for i in s:
            if i in dic:
                stack.append(i)
                continue
            
            if not stack or dic[stack[-1]] != i:
                return False
            
            stack.pop()
        
        return len(stack) == 0