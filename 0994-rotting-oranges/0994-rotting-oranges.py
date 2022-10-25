class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions = [(0, -1), (-1, 0), (0, 1), (1, 0)]
        
        m = len(grid)
        n = len(grid[0])
        
        q = collections.deque()
        
        good = 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append((i, j))
                if grid[i][j] == 1:
                    good += 1
        
        if good == 0:
            return 0
        res = 0
        
        while q:
            for _ in range(len(q)):
                current = q.popleft()
                
                for d in directions:
                    i = current[0] + d[0]
                    j = current[1] + d[1]
                    
                    if 0 <= i < m and 0 <= j < n and grid[i][j] == 1:
                        good -= 1
                        grid[i][j] = 2
                        q.append((i, j))
            
            res += 1
       
        return res - 1 if not good else -1
        