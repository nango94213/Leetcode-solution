class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:

        res = []
        
        def dfs(pool, path):

            if len(path) > 4:
                return
            
            if len(path) == 4 and not pool:
                res.append('.'.join(path))
            
            for i in range(len(pool)):
                if pool[:i+1] == '0' or (pool[:i+1][0] != '0' and int(pool[:i+1]) <= 255):
                    dfs(pool[i+1:], path+[pool[:i+1]])
        
        dfs(s, [])
        
        return res
                                 
        