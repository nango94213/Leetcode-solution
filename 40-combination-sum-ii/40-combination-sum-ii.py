class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res=[]
        
        def dfs(pool,path,current):
            
            if current<0:
                return
            
            if current==0:
                res.append(path)
                return
            
            for i in range(len(pool)):
                if i==0 or pool[i-1]!=pool[i]:
                     dfs(pool[i+1:],path+[pool[i]],current-pool[i])
        
        dfs(sorted(candidates),[],target)
        
        return res