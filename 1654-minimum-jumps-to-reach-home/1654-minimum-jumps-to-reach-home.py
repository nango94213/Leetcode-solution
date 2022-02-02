import collections
class Solution:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        
        limit = 2000 + a + b
        
        q = collections.deque([(0, True)])
        seen = set([(0, True)])
        
        for bad in forbidden:
            seen.add((bad, True))
            seen.add((bad, False))
        
        steps = 0
        while q:
            
            for _ in range(len(q)):
                current, is_forward = q.popleft()
                
                if current == x:
                    return steps
                
                next_jump = current + a
                
                if next_jump <= limit and (next_jump, True) not in seen:
                    q.append((next_jump, True))
                    seen.add((next_jump, True))
                
                if is_forward:
                    next_jump = current - b
                    if next_jump > 0 and (next_jump, False) not in seen:
                        q.append((next_jump, False))
                        seen.add((next_jump, False))
            
            steps += 1
        
        return -1
                        
                
                
                
                
            