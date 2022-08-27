class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        
        stack = [0]
        
        for c in s:
            if c == '(':
                stack.append(0)
                continue
            
            current = stack.pop()
            
            if current != 0:
                stack[-1] += current * 2
                continue
            
            stack[-1] += 1
        
        return stack[-1]
            
            