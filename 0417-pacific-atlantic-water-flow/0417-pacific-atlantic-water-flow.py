class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        
        m = len(heights)
        n = len(heights[0])
        
        def dfs(x, y, r):
            r.add((x, y))
            for d in directions:
                newX = x + d[0]
                newY = y + d[1]
                
                if 0 <= newX < m and 0 <= newY < n and heights[newX][newY] >= heights[x][y] and (newX, newY) not in r:
                    
                    dfs(newX, newY, r)
            
            
        
        a = set()
        b = set()
        
        for i in range(m):
            dfs(i, 0, a)
            dfs(i, n-1, b)
        
        for j in range(n):
            dfs(0, j, a)
            dfs(m-1, j, b)
        
        return a.intersection(b)
        
            
        
  