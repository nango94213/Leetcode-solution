class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        directions = [(0, -1), (-1, 0), (0, 1), (1, 0)]
        
        def dfs(i, j, s):
            
            if len(s) == 1:
                return True
            
            board[i][j] = '#'
            for d in directions:
                new_x = i + d[0]
                new_y = j + d[1]

                if 0 <= new_x < rows and 0 <= new_y < cols and board[new_x][new_y] == s[1]:
                    if dfs(new_x, new_y, s[1:]):
                        return True
            board[i][j] = s[0]
            
            return False
        
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0]:
                    if dfs(i, j, word):
                        return True
        
        return False