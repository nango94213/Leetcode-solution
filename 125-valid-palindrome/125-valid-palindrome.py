class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        buffer = []
        
        for c in s:
            if c.isalnum():
                buffer.append(c.lower())
        
        return buffer == buffer[::-1]
        
        