class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operations = {
        "+": lambda a, b: a + b,
        "-": lambda a, b: a - b,
        "/": lambda a, b: int(a / b),
        "*": lambda a, b: a * b}
        
        stack = []
        
        for token in tokens:
            if token in operations:
                op = operations[token]
                num1 = stack.pop()
                num2 = stack.pop()
                
                stack.append(op(num2, num1))
           
            else:
                stack.append(int(token))
        
        return stack[-1]
                
                