class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        def ispad(part):
            l, r = 0, len(part) - 1
            while l < r:
                
                if part[l] != part[r]:
                     return False
                
                l += 1
                r -= 1
            return True
    
        def dfs(pool, path):
            if not pool:
                res.append(path)
                return

            for i in range(1, len(pool)+1):
                if ispad(pool[:i]):
                    dfs(pool[i:], path + [pool[:i]])
        
        dfs(s, [])
       
        return res