class Solution:
    def longestValidParentheses(self, s: str) -> int:
        
        res = 0
        
        stack = []
        
        for i, v in enumerate(s):
            if v == '(':
                stack.append(i)
            else:
                if stack and s[stack[-1]] == '(':
                    stack.pop()
                    start = -1 if not stack else stack[-1]
                    res = max(res, i - start)
                else:
                    stack.append(i)
        
        return res