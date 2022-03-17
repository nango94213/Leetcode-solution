import collections
class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        steps = 0
        
        q = collections.deque([(0, 0, k)])
        
        seen = set([(0, 0, k)])
        
        target = (len(grid)-1, len(grid[0])-1)

        while q:
            for _ in range(len(q)):
                
                x, y, live = q.popleft()
                
                if (x, y) == target:
                    return steps
                
                for d in directions:
                    
                    new_x = x + d[0]
                    new_y = y + d[1]
                    
                    if 0 <= new_x < len(grid) and 0 <= new_y < len(grid[0]):
                        
                        if grid[new_x][new_y] != 1 and (new_x, new_y, live) not in seen:
                            seen.add((new_x, new_y, live))
                            q.append((new_x, new_y, live))
                        
                        if grid[new_x][new_y] == 1 and live > 0 and (new_x, new_y, live-1) not in seen:
                            seen.add((new_x, new_y, live-1))
                            q.append((new_x, new_y, live-1))

            
            steps += 1
        return -1
        
                
        
        
        