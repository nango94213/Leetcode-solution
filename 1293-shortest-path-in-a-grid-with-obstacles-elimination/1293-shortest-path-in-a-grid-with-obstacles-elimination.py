import collections
class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        rows = len(grid)
        cols = len(grid[0])
        q = collections.deque([(0,0,k)])
        directions = [(0, -1), (-1, 0), (0, 1), (1, 0)]
        seen = set((0,0))
        
        target = (len(grid)-1,len(grid[0])-1)
        
        jump = 0
        
        while q:
            
            for _ in range(len(q)):
                
                x, y, live = q.popleft()
                
                if (x,y) == target:
                    return jump
                
                for d in directions:
                    
                    new_x = x + d[0]
                    new_y = y + d[1]
                    
                    if 0 <= new_x < rows and 0<= new_y < cols:
                        if grid[new_x][new_y] == 1:
                            if live > 0 and (new_x, new_y, live-1) not in seen:
                                seen.add((new_x, new_y, live-1))
                                q.append((new_x, new_y, live-1))
                            else:
                                continue
                        
                        else:
                            if (new_x, new_y, live) not in seen:
                                seen.add((new_x, new_y, live))
                                q.append((new_x, new_y, live))
            
            jump += 1
        
        return -1
                
                
        
        