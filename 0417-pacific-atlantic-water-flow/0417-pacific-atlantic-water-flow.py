class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        a = set()
        b = set()
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        m = len(heights)
        n = len(heights[0])
        def dfs(x, y, s):
            s.add((x, y))
            
            for d in directions:
                i = x + d[0]
                j = y + d[1]
                
                if 0 <= i < m and 0 <= j < n and heights[i][j] >= heights[x][y] and (i, j) not in s:
                    dfs(i, j, s)
        
        for i in range(m):
            dfs(i, 0, a)
            dfs(i, n-1, b)
        
        for i in range(n):
            dfs(0, i, a)
            dfs(m-1, i, b)
        
        return a.intersection(b)
        