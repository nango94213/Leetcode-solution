import collections
class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        steps = 0
        target = (len(grid)-1, len(grid[0])-1)
        q = collections.deque([(0, 0, k)])
        seen = set([(0, 0, k)])
        
        m = len(grid)
        n = len(grid[0])
        
        while q:
            for _ in range(len(q)):
                x, y, live = q.popleft()
                
                if (x, y) == target:
                    return steps
                
                for d in directions:
                    newX = x + d[0]
                    newY = y + d[1]
                    
                    if 0 <= newX < m and 0 <= newY < n:
                        
                        if grid[newX][newY] == 0 and (newX, newY, live) not in seen:
                            seen.add((newX, newY, live))
                            q.append((newX, newY, live))
                        
                        if grid[newX][newY] == 1 and live > 0 and (newX, newY, live-1) not in seen:
                            seen.add((newX, newY, live-1))
                            q.append((newX, newY, live-1))
                
            steps += 1
        
        return -1