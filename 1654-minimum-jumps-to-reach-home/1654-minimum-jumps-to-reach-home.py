class Solution:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        limit = 2000 + a + b
        forbidden = set(forbidden)
        
        jump = 0
        
        q = collections.deque([(0, True)])
        seen = set([(0, True)])
        
        while q:
            for _ in range(len(q)):
                p, j = q.popleft()
                
                if p == x:
                    return jump
                
                new = p + a
                if new <= limit and new not in forbidden and (new, True) not in seen:
                        seen.add((new, True))
                        q.append((new, True))
                if not j:
                    continue
                new = p - b
                if new >= 0 and new not in forbidden and (new, False) not in seen:
                        seen.add((new, False))
                        q.append((new, False))
            jump += 1
        return -1