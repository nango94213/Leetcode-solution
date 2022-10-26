class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        def check(string):
            stack = []
            
            for c in string:
                if c != '#':
                    stack.append(c)
                    continue
                
                if stack:
                    stack.pop()
            
            return stack
    
        return check(s) == check(t)
        