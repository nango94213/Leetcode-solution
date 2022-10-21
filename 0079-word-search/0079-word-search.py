class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        m = len(board)
        n = len(board[0])
        directions = [(0, -1), (-1, 0), (0, 1), (1, 0)]
        
        
        def dfs(x, y, s):
            
            if len(s) == 1:
                return True
            
            board[x][y] = '#'
            
            for d in directions:
                
                i, j = x + d[0], y + d[1]
                
                if 0 <= i < m and 0 <= j < n and board[i][j] == s[1]:
                    
                    if dfs(i, j, s[1:]):
                        return True
            
            board[x][y] = s[0]
            
            return False
        
        for i in range(m):
            for j in range(n):
                
                if board[i][j] == word[0] and dfs(i, j, word):
                    return True
        
        return False
            