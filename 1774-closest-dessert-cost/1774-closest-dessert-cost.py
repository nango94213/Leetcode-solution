class Solution:
    def closestCost(self, baseCosts: List[int], toppingCosts: List[int], target: int) -> int:
        res = float('inf')
        
        def dfs(pool, path):
            nonlocal res
         
            if abs(path-target) < abs(res-target):
                res = path
                print(path)
            if abs(path-target) == abs(res-target):
                res = min(res, path)
            if path > target:
                return
            
            for i in range(len(pool)):
                dfs(pool[i+1:], path)
                dfs(pool[i+1:], path+pool[i])
                dfs(pool[i+1:], path+2*pool[i])
        
        for b in baseCosts:
            dfs(toppingCosts, b)
        
        return res
        