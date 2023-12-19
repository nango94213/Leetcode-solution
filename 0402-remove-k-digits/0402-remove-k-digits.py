class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        
        stack = []
        
        for n in num:
            while stack and stack[-1] > n and k > 0:
                stack.pop()
                k -= 1
                
            if not stack and n == '0':
                continue
            stack.append(n)
        
        for i in range(k):
            if stack:
                stack.pop()
        res = ''.join(stack)
        return res if res != "" else "0"