class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(pool, path, total):
            
            if total > target:
                return
            if total == target:
                res.append(path)
            
            for i in range(len(pool)):
                dfs(pool[i:], path+[pool[i]], total+pool[i])
        
        dfs(candidates, [], 0)
        
        return res
        