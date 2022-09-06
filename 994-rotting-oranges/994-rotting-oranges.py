class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        directions = [(0, -1), (-1, 0), (0, 1), (1, 0)]
        
        rows = len(grid)
        cols = len(grid[0])
        
        q = collections.deque()
        
        good = 0
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    q.append((i, j))
                if grid[i][j] == 1:
                    good += 1
        
        minutes = -1
        
        q.append((-1, -1))
        
        while q: 
                x, y = q.popleft()
                
                if x == -1:
                    minutes += 1
                    
                    if q:
                        q.append((-1, -1))
                else:
                    for d in directions:
                        new_x = x + d[0]
                        new_y = y + d[1]
                
                        if 0 <= new_x < rows and 0 <= new_y <cols and grid[new_x][new_y] == 1:
                            grid[new_x][new_y] = 2
                            good -= 1
                            q.append((new_x, new_y))
        return minutes if not good else -1
        