import collections
class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        
        m = len(grid)
        n = len(grid[0])
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        
        q = collections.deque()
        
        def dfs(x, y):
            grid[x][y] = -1
            
            for d in directions:
                i = x + d[0]
                j = y + d[1]
                
                if 0 <= i < m and 0 <= j < n:
                    if grid[i][j] == 1:
                        dfs(i, j)
                    elif grid[i][j] == 0:
                        grid[i][j] = -1
                        q.append((i, j))
        stop = False
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    dfs(i, j)
                    stop = True
                    break
            if stop:
                break
        
        step = 0
        while q:
            for _ in range(len(q)):
                x, y = q.popleft()
                
                if grid[x][y] == 1:
                    return step
                
                for d in directions:
                    i = x + d[0]
                    j = y + d[1]
                    if 0 <= i < m and 0 <= j < n and grid[i][j] in (0, 1):
                        if grid[i][j] == 0:
                            grid[i][j] = -1
                        q.append((i, j))
            step += 1
        return -1
                        
                    
        
        
        