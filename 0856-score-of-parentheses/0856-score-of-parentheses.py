class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [0]
        
        for c in s:
            if c == '(':
                stack.append(0)
            else:
                current = stack.pop()
                
                if current == 0:
                    stack[-1] += 1
                else:
                    stack[-1] += 2*current
        
        return stack[-1]