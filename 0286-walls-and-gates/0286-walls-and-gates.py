import collections
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        if not rooms:
            return 
        directions = [(0, -1), (-1, 0), (0, 1), (1, 0)]
        
        m = len(rooms)
        n = len(rooms[0])
        
        q = collections.deque()
        
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    q.append((i, j))
        
        jump = 0
        
        while q:
            
            for _ in range(len(q)):
                
                current = q.popleft()
                
                for d in directions:
                    i = current[0] + d[0]
                    j = current[1] + d[1]
                    
                    if 0 <= i < m and 0 <= j < n and rooms[i][j] == 2147483647:
                        rooms[i][j] = jump + 1
                        q.append((i, j))
            jump += 1
        
                
        