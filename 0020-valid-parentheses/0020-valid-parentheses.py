class Solution:
    def isValid(self, s: str) -> bool:
        
        dic = {'(':')', '{':'}', '[':']'}
        
        stack = []
        
        for c in s:
            if c in dic:
                stack.append(c)
                continue
            
            if not stack or stack and dic[stack[-1]] != c:
                return False
            else:
                stack.pop()
        
        return stack == []