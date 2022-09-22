import collections
class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        
        if k == 0:
            return 1.0
        direction=offsets = [(1, 2), (2, 1), (2, -1), (1, -2),(-1, -2), (-2, -1), (-2, 1), (-1, 2)]
        q= {(row, column): 1}  
        steps = 0
        while q and steps < k:
            nextQ = collections.defaultdict(int)
            for key, value in q.items():
                i, j = key
                count = value
                
                
                for d in direction:
                    next_x=i+d[0]
                    next_y=j+d[1]
                
                    if 0 <= next_x < n and 0 <= next_y < n:
                        nextQ[(next_x, next_y)] += count
            
            q = nextQ
            steps+=1
  
        return sum(q.values()) / (8**k)