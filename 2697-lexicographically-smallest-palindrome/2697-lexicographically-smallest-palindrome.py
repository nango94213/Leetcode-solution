class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        s = list(s)
        n = len(s)
        
        if n % 2 == 0:
            left = n//2 -1
            right = left + 1
        else:
            left = n//2 -1
            right = left + 2
     
        while left >= 0 and right <= n-1:
            if s[left] != s[right]:
                s[right] = s[left] = min(s[right], s[left])
            left -= 1
            right += 1
        return ''.join(s)
        