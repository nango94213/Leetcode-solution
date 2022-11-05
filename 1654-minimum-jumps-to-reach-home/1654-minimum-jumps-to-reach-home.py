import collections
class Solution:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        
        limit = 2000 + a + b
        
        q = collections.deque([(0, True)])
        
        forbidden = set(forbidden)
        
        seen = set([(0, True)])
        
        jump = 0
        
        while q:
            
            for _ in range(len(q)):
                
                current, d = q.popleft()
                
                if current == x:
                    return jump
                
                if current + a <= limit and (current+a, True) not in seen and current+a not in forbidden:
                    q.append((current+a, True))
                    seen.add((current+a, True))
                
                if d:
                    if current - b >= 0 and (current-b, False) not in seen and current-b not in forbidden:
                        q.append((current-b, False))
                        seen.add((current-b, False))
            
            jump += 1
        
        return -1
                
                
                
                
            