class Solution:
    def decodeString(self, s: str) -> str:
        number = []
        string = []
        
        current = ''
        n = 0
        
        for c in s:
            if c.isdigit():
                n = n*10 + int(c)
            
            if c.isalpha():
                current += c
            
            if c == '[':
                number.append(n)
                string.append(current)
                
                current = ''
                n = 0
            
            if c == ']':
                current = string.pop() + number.pop() * current
        
        return current