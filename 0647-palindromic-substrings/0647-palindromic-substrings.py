class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        def helper(x, y):
            nonlocal res
            while x >= 0 and y <= len(s) - 1 and s[x] == s[y]:
                x -= 1
                y += 1
                res += 1
        
        for i in range(len(s)):
            helper(i, i)
            helper(i, i+1)
        
        return res
        