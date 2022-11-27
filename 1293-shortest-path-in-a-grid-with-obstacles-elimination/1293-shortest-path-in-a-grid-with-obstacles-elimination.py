import collections
class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        q = collections.deque([(0, 0, k)])
        seen = set([(0, 0, k)])
        
        step = 0
        
        m = len(grid)
        n = len(grid[0])
        target = (m-1, n-1)
        
        while q:
            for _ in range(len(q)):
                x, y, a = q.popleft()
                if (x, y) == target:
                    return step
                
                for d in directions:
                    i = x + d[0]
                    j = y + d[1]
                    
                    if 0 <= i < m and 0 <= j < n:
                        if grid[i][j] == 0 and (i, j, a) not in seen:
                            seen.add((i, j, a))
                            q.append((i, j, a))
                        
                        if grid[i][j] == 1 and a > 0 and (i, j, a-1) not in seen:
                            seen.add((i, j, a-1))
                            q.append((i, j, a-1))
            
            step += 1
        
        return -1