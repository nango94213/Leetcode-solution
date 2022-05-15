import collections
class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        q = collections.deque([(0, 0, k)])
        seen = set([(0, 0, k)])
        
        rows = len(grid)
        cols = len(grid[0])
        
        target = (rows-1, cols-1)
        
        steps = 0
        
        while q:
            
            for _ in range(len(q)):
                
                x, y, live = q.popleft()
                
                if (x, y) == target:
                    
                    return steps
                
                for d in directions:
                    
                    newx, newy = x + d[0], y + d[1]
                    
                    if 0 <= newx < rows and 0 <= newy < cols:
                        
                        if grid[newx][newy] != 1 and (newx, newy, live) not in seen:
                            q.append((newx, newy, live))
                            seen.add((newx, newy, live))
                        
                        if grid[newx][newy] == 1 and (live-1) >=0 and (newx, newy, live-1) not in seen:
                            q.append((newx, newy, live-1))
                            seen.add((newx, newy, live-1))
            
            steps += 1
        
        return -1