class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        directions = [(0, -1), (-1, 0), (0, 1), (1, 0)]
        
        
        def dfs(x, y, s):
            
            if len(s) == 1:
                return True
            
            board[x][y] = '#'
            
            for d in directions:
                
                i = x + d[0]
                j = y + d[1]
                
                if 0 <= i < rows and 0 <= j < cols and board[i][j] == s[1]:
                    
                    if dfs(i, j, s[1:]):
                        
                        return True
            
            board[x][y] = s[0]
            
            return False
        
        for i in range(rows):
            for j in range(cols):
                
                if board[i][j] == word[0] and dfs(i, j, word):
                    return True
        
        return False
            