class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        
        def dfs(pool, path):
            res.append(path)
            
            for i in range(len(pool)):
                dfs(pool[i+1:], path+[pool[i]])
        
        dfs(nums, [])
        
        return res
        