import collections
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        if not rooms:
            return 
        directions = [(0, -1), (-1, 0), (0, 1), (1, 0)]
        
        rows = len(rooms)
        cols = len(rooms[0])
        
        q = collections.deque()
        
        for i in range(rows):
            for j in range(cols):
                if rooms[i][j] == 0:
                    q.append((i, j))
        
        while q:
            x, y = q.popleft()
            
            for d in directions:
                
                new_x = x + d[0]
                new_y = y + d[1]
                
                if new_x < 0 or new_y < 0 or new_x >= rows or new_y >= cols or rooms[new_x][new_y] != 2147483647:
                    continue
                
                rooms[new_x][new_y] = rooms[x][y] + 1
                
                q.append((new_x, new_y))
                
                
        