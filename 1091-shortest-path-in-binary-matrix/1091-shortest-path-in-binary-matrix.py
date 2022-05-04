import collections
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        
        q = collections.deque([(0, 0)])
        
        row = len(grid)
        cols = len(grid[0])
        
        target = (row-1, cols-1)
        
        if grid[row-1][cols-1] ==1 or grid[0][0] == 1:
            return -1
        
        seen = set([(0, 0)])
        
        steps = 1
        
        while q:
     
            for _ in range(len(q)):
                
                x, y = q.popleft()
                
                if (x, y) == target:
                    return steps
                
                for d in directions:
                    
                    newx, newy = x + d[0], y + d[1]
                    
                    if 0 <= newx < row and 0 <= newy < cols and grid[newx][newy] == 0 and (newx, newy) not in seen:
                        
                        seen.add((newx, newy))
                        
                        q.append((newx, newy))
            
            
            steps += 1
        
        return -1