import collections
class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        def check(s):
            stack = 0
            for c in s:
                if c == ')':
                    if not stack:
                        return False
                    else:
                        stack -= 1
                elif c == '(':
                    stack += 1
            return stack == 0
        
        q = collections.deque([s])
        
        seen = set([s])
        
        res = []
        stop = False
        while q:
            for _ in range(len(q)):
                current = q.popleft()
               
                if check(current):
                    stop = True
                    res.append(current)
                
                for i in range(len(current)):
                    tmp = current[:i] + current[i+1:]
                    if tmp not in seen:
                   
                        seen.add(tmp)
                        q.append(tmp)
    
            if stop:
                break
        return res
            