class Solution:
    def punishmentNumber(self, n: int) -> int:
        
        def dfs(pool, path, target):
            
            if not pool:
                if sum(path) == target:
                    return True
                else:
                    return False
            
            for i in range(len(pool)):
                if dfs(pool[i+1:], path+[int(pool[:i+1])],target):
                    return True
            return False
        
        res = 0
        for i in range(1, n+1):
            if dfs(str(i*i),  [], i):
                res += i*i
        return res
        #123