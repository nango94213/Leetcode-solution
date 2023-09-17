class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        seen = set([(start[0], start[1])])
        m = len(maze)
        n = len(maze[0])
        def dfs(x, y):
            if [x, y] == destination:
                return True
            
            for d in directions:
                i = x
                j = y
                while 0 <= i + d[0] < m and 0 <= j + d[1] < n and maze[i + d[0]][j + d[1]] != 1:
                    i += d[0]
                    j += d[1]
                
                if (i, j) not in seen:
                    seen.add((i, j))
                    if dfs(i, j):
                        return True
            
            return False
        
        return dfs(start[0], start[1])

            
        