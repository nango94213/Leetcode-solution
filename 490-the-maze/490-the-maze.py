class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        rows = len(maze)
        cols = len(maze[0])
        directions = [(0, -1), (-1, 0), (0, 1), (1, 0)]
        seen = set([(start[0], start[1])])
        def dfs(i, j):
            
            if [i, j] == destination:
                return True
            
            for d in directions:
                new_x = i
                new_y = j

                while 0 <= new_x + d[0] < rows and 0 <= new_y + d[1] < cols and maze[new_x+d[0]][new_y+d[1]] != 1:
                    new_x += d[0]
                    new_y += d[1]
                    
                if (new_x, new_y) not in seen:
                    seen.add((new_x, new_y))
                    if dfs(new_x, new_y):
                        return True
   
            return False
        
        return dfs(start[0], start[1])