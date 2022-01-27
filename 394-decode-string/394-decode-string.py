class Solution:
    def decodeString(self, s: str) -> str:
        
        stack_number = []
        stack_string = []
        
        current_number = 0
        current_string = ''
        
        for i in s:
            
            if i.isnumeric():
                
                current_number = current_number * 10 + int(i)
            
            elif i == '[':
                
                stack_number.append(current_number)
                stack_string.append(current_string)
                
                current_number = 0
                current_string = ''
            
            elif i == ']':
                
                current_string = stack_string.pop() + stack_number.pop() * current_string
            
            else:
                current_string += i
                
        
        return current_string
                
                
        