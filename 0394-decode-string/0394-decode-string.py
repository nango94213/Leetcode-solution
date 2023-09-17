class Solution:
    def decodeString(self, s: str) -> str:
        stackN = []
        stackS = []
        
        current = ''
        number = 0
        
        for c in s:
            if c.isdigit():
                number = number*10 + int(c)
            if c.isalpha():
                current += c
            
            if c == '[':
                stackN.append(number)
                stackS.append(current)
                number = 0
                current = ''
            
            if c == ']':
                current = stackS.pop() + stackN.pop() * current
        
        return current
            
        