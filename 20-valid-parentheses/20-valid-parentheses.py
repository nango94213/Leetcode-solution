class Solution:
    def isValid(self, s: str) -> bool:
        
        dic = {'(':')', '{':'}', '[':']'}
        
        stack = []
        
        for i in s:
            if i not in dic:
                if stack and dic[stack[-1]] == i:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        
        return stack == []