import collections
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = collections.deque()
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        m = len(grid)
        n = len(grid[0])
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append((i, j))
                if grid[i][j] == 1:
                    count += 1
                    

        time = -1
        
        while q:
            for _ in range(len(q)):
                current = q.popleft()
                
                for d in directions:
                    x = current[0] + d[0]
                    y = current[1] + d[1]
                    
                    if 0 <= x < m and 0 <= y < n and grid[x][y] == 1:
                        grid[x][y] = 2
                        count -= 1
                        q.append((x, y))
            
            time += 1

        return max(time, 0) if count == 0 else -1