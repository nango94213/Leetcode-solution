class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        s = list(s)
     
        for i in range(len(s)//2+1):
            if s[i] != s[-i-1]:
                if s[i] < s[-i-1]:
                    s[-i-1] = s[i]
                else:
                    s[i] = s[-i-1]
        return ''.join(s)
        