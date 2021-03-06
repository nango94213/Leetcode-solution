class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res=[]
        def dfs(pool,path):
            
            if len(path) == k:
                res.append(path)
                return
            
            for i in range(len(pool)):
                if i!=0 and pool[i] == pool[i-1]:
                    continue
                tmp = path + [pool[i]]   
                dfs(pool[i+1:],tmp)
        
        dfs(range(1, n+1),[])
        
        return res