class Solution:
    def minLength(self, s: str) -> int:
        stack = []
        
        for n in s:
            if stack and (stack[-1] + n == 'AB' or stack[-1] + n == "CD"):
                stack.pop()
            else:
                stack.append(n)
        return len(stack)
        