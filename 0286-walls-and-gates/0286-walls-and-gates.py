class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        directions = [(0, -1), (-1, 0), (0, 1), (1, 0)]
        if not rooms:
            return []
        
        q = collections.deque()
        
        m = len(rooms)
        n = len(rooms[0])
        
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    q.append((i, j))
        
        jump = 1
        
        while q:
            for _ in range(len(q)):
                x, y = q.popleft()
                
                for d in directions:
                    i = x + d[0]
                    j = y + d[1]
                    
                    if 0 <= i < m and 0 <= j < n and rooms[i][j] == 2147483647:
                        rooms[i][j] = jump
                        q.append((i, j))
            
            jump += 1
        
        return rooms