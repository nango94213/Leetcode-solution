class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        sign = '+'
        num = 0
        
        for i, v in enumerate(s):
            if v.isdigit():
                num = num * 10 + int(v)
            
            if v in '+-/*' or i == len(s) - 1:
                if sign == '+':
                    stack.append(num)
                
                if sign == '-':
                    stack.append(-num)
                
                if sign == '/':
                    stack.append(int(stack.pop()/num))
                
                if sign == '*':
                    stack.append(stack.pop()*num)
                
                num = 0
                sign = v
        
        return sum(stack)
        