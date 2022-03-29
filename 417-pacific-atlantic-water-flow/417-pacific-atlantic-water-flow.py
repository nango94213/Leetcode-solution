class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        
        rows = len(heights)
        cols = len(heights[0])
        
        pacific = set()
        atlantic = set()
        
        def dfs(x, y, s):
            
            if s:
                pacific.add((x,y))
                
                for d in directions:
                    newx = x + d[0]
                    newy = y + d[1]
                    
                    if 0 <= newx < rows and 0 <= newy < cols and heights[newx][newy] >= heights[x][y] and (newx, newy) not in pacific:
                        dfs(newx, newy, s)
            else:
                atlantic.add((x,y))
                
                for d in directions:
                    newx = x + d[0]
                    newy = y + d[1]
                    
                    if 0 <= newx < rows and 0 <= newy < cols and heights[newx][newy] >= heights[x][y] and (newx, newy) not in atlantic:
                        dfs(newx, newy, s)
                
            
        
        
        for i in range(rows):
            
            dfs(i, 0, True)
            
            dfs(i, cols-1, False)
        
        for i in range(cols):
            
            dfs(0, i , True)
            
            dfs(rows-1, i , False)
        return list(pacific.intersection(atlantic))