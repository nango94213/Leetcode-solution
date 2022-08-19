class Solution:
    def decodeString(self, s: str) -> str:
        number = []
        string = []
        
        currentNumber = 0
        currentString = ''
        
        for c in s:
            if c.isnumeric():
                currentNumber = currentNumber * 10 + int(c)
            elif c == '[':
                number.append(currentNumber)
                string.append(currentString)
                currentNumber = 0
                currentString = ''
            elif c.isalpha():
                currentString += c
            elif c == ']':
                currentString = string.pop() + number.pop() * currentString
        return currentString
                
            