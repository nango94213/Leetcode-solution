class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        rows = len(maze)
        cols = len(maze[0])
        directions = [(0, -1), (-1, 0), (0, 1), (1, 0)]
        
        seen = set(tuple(start))
        
        def dfs(x, y):
            if [x, y] == destination:
                return True
            
            for d in directions:
                
                newX = x
                newY = y
                
                while 0 <= newX + d[0] < rows and 0 <= newY + d[1] < cols and maze[newX+d[0]][newY+d[1]] == 0:
                    newX += d[0]
                    newY += d[1]
                
                if (newX, newY) not in seen:
                    seen.add((newX, newY))
                    
                    if dfs(newX, newY):
                        return True
            
            return False
        
        return dfs(start[0], start[1])
                