class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        
        
        
        stack = []
        number = 0
        for i in abbr:
            if i.isalpha():
                if number:
                    stack.append(str(number))
                    number = 0
                stack.append(i)
            else:
                if number == 0 and int(i) == 0:
                    return False
                number = number * 10 + int(i)
        if number:
                    stack.append(str(number))
        

        buffer = ''
        
        for s in stack:
            if s.isalpha():
                buffer += s
            else:
                if int(s) > len(word):
                    return False
                buffer += int(s) * '#'
        
        
        index = 0
        
        if len(buffer) != len(word):
            return False
        
        for i in range(len(word)):
            if word[i] != buffer[i] and buffer[i] != '#':
                return False
        
        return True
            
                
            
            
        