class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(pool, path):
            res.append(path)
            
            for i in range(len(pool)):
                if i != 0 and pool[i] == pool[i-1]:
                    continue
                
                dfs(pool[i+1:], path+[pool[i]])
        
        dfs(sorted(nums), [])
        return res
        