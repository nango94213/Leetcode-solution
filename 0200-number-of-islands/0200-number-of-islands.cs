public class Solution {
    int m = 0;
    int n = 0;
    public int NumIslands(char[][] grid) {
        m = grid.Length;
        n = grid[0].Length;
        int res = 0;
        void Dfs(char[][] grid, int x, int y) {
            grid[x][y] = '0';
            Tuple<int, int>[] directions = {Tuple.Create(-1, 0), Tuple.Create(1, 0), Tuple.Create(0, -1), Tuple.Create(0, 1)};
            foreach (var d in directions) {
               var newX = x + d.Item1;
               var newY = y + d.Item2;
               if (0 <= newX && newX < m && 0 <= newY && newY < n && grid[newX][newY] == '1') {
                   Dfs(grid, newX, newY);
               }
            }
        }
    
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == '1') {
                    res ++;
                    Dfs(grid, i, j);
                }
            }
        }
        return res;
    }
}
    
    