class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        res = 0
        for letter in columnTitle:
            current = res * 26 + ord(letter) - ord('A') + 1
            
            res = current
        
        return res