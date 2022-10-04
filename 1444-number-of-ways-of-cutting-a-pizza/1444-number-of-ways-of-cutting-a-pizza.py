from functools import lru_cache
class Solution:
    def ways(self, pizza: List[str], K: int) -> int:
        MOD = 10 ** 9 + 7
        n, m = len(pizza), len(pizza[0])
        num_apples = [[0] * (m + 1) for _ in range(n + 1)]
        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                num_apples[i][j] = (j + 1 < m and num_apples[i][j + 1]) + \
                                   (i + 1 < n and num_apples[i + 1][j]) - \
                                   (i + 1 < n and j + 1 < m and num_apples[i + 1][j + 1]) + \
                                   int(pizza[i][j] == 'A')
                
        def is_valid(x0, y0, x1=n-1, y1=m-1):
            '''inclusive'''
            if x0 > x1 or y0 > y1: return False
            num = num_apples[x0][y0] - \
                  num_apples[x1 + 1][y0] - \
                  num_apples[x0][y1 + 1] + \
                  num_apples[x1 + 1][y1 + 1]
            return num > 0
        
        @cache
        def num_ways(x, y, k):
            if not is_valid(x, y): return 0
            if k == 1: return 1
            res = 0
            # cut horizontally
            for j in range(y, m - 1):
                if is_valid(x, y, n - 1, j):
                    res = (res + num_ways(x, j + 1, k - 1)) % MOD
            # cut vertically                    
            for i in range(x, n - 1):
                if is_valid(x, y, i, m - 1):
                    res = (res + num_ways(i + 1, y, k - 1)) % MOD
            return res
        
        return num_ways(0, 0, K)
        