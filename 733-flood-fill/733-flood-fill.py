class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        old = image[sr][sc]
        rows = len(image)
        cols = len(image[0])
        
        seen = set([(sr, sc)])
        
        def dfs(x, y):
            image[x][y] = newColor
            for d in directions:
                
                newx = x + d[0]
                newy = y + d[1]
                
                if 0 <= newx < rows and 0 <= newy < cols and (newx, newy) not in seen and image[newx][newy] == old:
                    seen.add((x, y))
                    dfs(newx, newy)
        
        
        
        dfs(sr, sc)
        
        
        return image