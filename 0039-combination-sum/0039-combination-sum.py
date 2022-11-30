class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        
        def dfs(pool, path, current):
            if current > target:
                return
            
            if current == target:
                res.append(path)
                
            for i in range(len(pool)):
                if i != 0 and pool[i] == pool[i-1]:
                    continue
                dfs(pool[i:], path+[pool[i]], current+pool[i])
        
        dfs(sorted(candidates), [], 0)
        return res
        