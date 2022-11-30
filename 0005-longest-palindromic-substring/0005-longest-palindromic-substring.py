class Solution:
    def longestPalindrome(self, s: str) -> str:
        def helper(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left+1:right]
        res = ''
        for i in range(len(s)):
            res = max(res, helper(i, i), helper(i, i+1), key=len)
        return res
        