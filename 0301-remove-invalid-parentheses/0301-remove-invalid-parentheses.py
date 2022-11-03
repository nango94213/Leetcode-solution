import collections
class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        def valid(string):
            stack = 0
            
            for c in string:
                if c == ')':
                    if not stack:
                        return False
                    stack -= 1
                elif c == '(':
                    stack += 1
            
            return stack == 0
        q = collections.deque([s])
        
        seen = set([s])
        
        steps = 0
        stop = False
        res = []
        while q:
            for _ in range(len(q)):
                current = q.popleft()
                
                if valid(current):
                    res.append(current)
                    stop = True
                
                for i in range(len(current)):
                    child = current[:i] + current[i+1:]
                    if child not in seen:
                        seen.add(child)
                        q.append(child)
            if stop:
                return res
        return res
        
        
        