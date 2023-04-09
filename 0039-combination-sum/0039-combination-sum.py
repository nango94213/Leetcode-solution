class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        res = []      
        def dfs(pool, path, current):
            if current > target:
                return 
            if current == target:
                res.append(path)
            
            for i in range(len(pool)):
     
                dfs(pool[i:], path+[pool[i]], current+pool[i])
        
        dfs(candidates, [], 0)
        
        return res
        