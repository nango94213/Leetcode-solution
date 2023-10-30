class Solution:
    def isPalindrome(self, s: str) -> bool:
        gg = []
        for c in s:
            if c.isalnum():
                gg.append(c)
        left = 0
        right = len(gg) - 1

        while left < right:
            if gg[left].lower() == gg[right].lower():
                left += 1
                right -= 1
            else:
                return False
        
        return True
        