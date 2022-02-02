import collections
class Solution:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        
        limit = 2000 + a + b
        
        q = deque([(0, True)])
        seen = {(0, True)}
        
        for bad in forbidden:
            seen.add((bad, True))
            seen.add((bad, False))
        
        steps = 0
        
        while q:
            for _ in range(len(q)):
                current, isforward = q.popleft()
                
                if current == x:
                    return steps
                forward, backward = (current+a, True), (current-b, False)
                if (current + a) <=limit and forward not in seen:
                    q.append(forward)
                    seen.add(forward)
                
                if isforward and (current-b) > 0 and backward not in seen:
                    q.append(backward)
                    seen.add(backward)
            steps += 1
        return -1


                
            
                        
                
                
                
                
            