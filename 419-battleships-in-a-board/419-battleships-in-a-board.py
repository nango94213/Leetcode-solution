class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        
        
        directions = [(1, 0), (0, 1)]
        
        count = 0
        rows = len(board)
        cols = len(board[0])
        
        def dfs(x, y):

            board[x][y] = '.'
            
            for d in directions:
                
                newx = x + d[0]
                newy = y + d[1]
                
                if 0 <= newx < rows and 0 <= newy < cols and board[newx][newy] == 'X':
                    
                    dfs(newx, newy)
        
        
        
        for i in range(rows):
            for j in range(cols):
                
                if board[i][j] == 'X':
                    count += 1
                    dfs(i, j)
        
        
        return count