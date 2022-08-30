class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        direction=[(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
        
        copyBoard = deepcopy(board)
        
        m, n = len(board), len(board[0])
        
        
        for i in range(m):
            for j in range(n):
                
                count = 0
                
                for d in direction:
                    
                    x = i + d[0]
                    y = j + d[1]
                    
                    if 0 <= x < m and 0 <= y < n and copyBoard[x][y] == 1:
                        count += 1
      
                if copyBoard[i][j] == 1 and (count < 2 or count >3):
                    board[i][j] = 0
                
                if copyBoard[i][j] == 0 and count == 3:
                    board[i][j] = 1
       
                