class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        
        res = []
        
        def dfs(path, pool, total):
            if total > target:
                return
            if total == target:
                res.append(path)
            
            for i in range(len(pool)):
                if i != 0 and pool[i] == pool[i-1]:
                    continue
                
                dfs(path+[pool[i]], pool[i+1:], total+pool[i])
        
        dfs([], candidates, 0)
        
        return res
        