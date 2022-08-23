class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        
        wordDict = set(wordDict)
        
        def check(g):
            
            dp = [False] * len(g)
            
            for i in range(len(g)):
                if g[:i+1] in wordDict:
                    dp[i] = True
                    continue
                
                for j in range(i):
                    if g[:j+1] in wordDict:
                        dp[i] = True
                        break
            return dp[-1]
        
        
        res = []
        
        def dfs(pool, path):
            
            if not pool:
                res.append(path[1:])
                return
            
            if not check(pool):
                return
            
            for i in range(len(pool)):
                
                if pool[:i+1] in wordDict:
                    
                    dfs(pool[i+1:], path+" "+pool[:i+1])
        
        dfs(s, "")
        
        return res
                
                