class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        direction=[(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
        row_n=len(board)
        col_n=len(board[0])
        
        def dfs(x, y):
            
            count = 0
            
            for d in direction:
                i = x + d[0]
                j = y + d[1]
                
                if 0 <= i < row_n and 0 <= j < col_n and board[i][j] == 'M':
                    count += 1
      
            if count:
                board[x][y] = str(count)
                return
            
            board[x][y] = 'B'
            
            for d in direction:
                i = x + d[0]
                j = y + d[1]
                
                if 0 <= i < row_n and 0 <= j < col_n and board[i][j] == 'E': 
                    dfs(i, j)
                
        
        if board[click[0]][click[1]] == 'M':
            board[click[0]][click[1]] = 'X'
            return board
        
        if board[click[0]][click[1]] == 'E':
            dfs(click[0], click[1])
        return board