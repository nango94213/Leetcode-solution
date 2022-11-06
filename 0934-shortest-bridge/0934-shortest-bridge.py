class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        
        m = len(grid)
        n = len(grid[0])
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        

        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    x, y = i, j
                    break
        
        bound = collections.deque()
        
        def dfs(x, y):
            grid[x][y] = -1
            
            for d in directions:
                i = x + d[0]
                j = y + d[1]
                
                if 0 <= i < m and 0 <= j < n:
                    if grid[i][j] == 0:
                        grid[i][j] = -1
                        bound.append((i, j))
                    elif grid[i][j] == 1:
                        dfs(i, j)
        dfs(x, y)
        jump = 0
     
        while bound:
            for _ in range(len(bound)):
                
                current = bound.popleft()
                
                if grid[current[0]][current[1]] == 1:
                    return jump
                
                for d in directions:
                    i = current[0] + d[0]
                    j = current[1] + d[1]
                    
                    if 0 <= i < m and 0 <= j < n and grid[i][j] != -1:
                        if grid[i][j] == 0:
                            grid[i][j] = -1
                        bound.append((i, j))
            jump += 1
        
        return -1