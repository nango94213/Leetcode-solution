class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(pool, path):
            
            if len(path) == len(nums):
                res.append(path)
                
            
            for i in range(len(pool)):
                dfs(pool[:i]+pool[i+1:], path+[pool[i]])
        dfs(nums, [])
        return res
        