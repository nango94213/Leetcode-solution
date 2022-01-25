class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        res = []
        
        def dfs(pool, path):
            
            if not pool:
                res.append(path)
                return
                
            for i in range(len(pool)):
                
                if pool[:i+1] == pool[:i+1][::-1]:
                    dfs(pool[i+1:], path+[pool[:i+1]])
        
        dfs(s, [])
        
        return res