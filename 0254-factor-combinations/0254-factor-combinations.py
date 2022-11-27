class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
        
        factor = []
        for i in range(2, n//2+1):
            if n % i == 0:
                factor.append(i)
        if not factor:
            return []
        res = []
        
        def dfs(pool, path, total):
            if total > n:
                return
            if total == n:
                res.append(path)
            
            for i in range(len(pool)):
                dfs(pool[i:], path+[pool[i]], total*pool[i])
        
        dfs(factor, [], 1)
        
        return res
        