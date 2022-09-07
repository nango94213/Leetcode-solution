import collections
class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        
        q = collections.deque()
        seen = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '*':
                    grid[i][j] = 'X'
                    q.append((i, j))
                    seen.add((i, j))
        
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        step = 0
        
        
        while q:

            for _ in range(len(q)):
                
                x, y = q.popleft()
                
                if grid[x][y] == '#':
                    return step
  
                for d in directions:
                    i, j = x + d[0], y + d[1]
                    
                    if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] != 'X' and (i, j) not in seen:
                        q.append((i, j))
                        seen.add((i, j))
            
            step += 1
        
        
        return -1
        
        
                
        