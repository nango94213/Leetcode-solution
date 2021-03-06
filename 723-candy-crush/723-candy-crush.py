class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        
        m = len(board)
        n = len(board[0])
        
    
        
        while True:
            remove = set()
            
            
            for i in range(m):
                for j in range(n-2):
                
                    if board[i][j] == board[i][j+1] == board[i][j+2] != 0:
                        remove.update([(i, j), (i, j+1), (i, j+2)])
            
            
            for j in range(n):
                for i in range(m-2):
                    
                    if board[i][j] == board[i+1][j] == board[i+2][j] != 0:
                        remove.update([(i, j), (i+1, j), (i+2, j)])
            
            if not remove:
                return board
            
            
            
            for j in range(n):
                falling = 0
                for i in range(m-1, -1, -1):
                    if (i, j) in remove:
                        falling += 1
                    else:
                        board[i+falling][j] = board[i][j]
                        
                for i in range(falling):
                    board[i][j] = 0
            
            