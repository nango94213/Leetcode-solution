class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
        
        if n == 1:
            return []
        factors = []
        for i in range(2, n//2 + 1):
            if n % i == 0:
                factors.append(i)
        
        res = []
      
        def dfs(pool, path, current):
           
            if current > n:
                return
            
            if current == n:
                res.append(path)
            
            for i in range(len(pool)):
                dfs(pool[i:], path+[pool[i]], current*pool[i])
        
        dfs(factors, [], 1)
        
        return res
            
            