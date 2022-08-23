class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        
        wordDict = set(wordDict)
        
        
        
        
        res = []
        
        def dfs(pool, path):
            
            if not pool:
                res.append(path[1:])
            
            for i in range(len(pool)):
                
                if pool[:i+1] in wordDict:
                    
                    dfs(pool[i+1:], path+" "+pool[:i+1])
        
        dfs(s, "")
        
        return res
                
                