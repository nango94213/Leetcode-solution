class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        if not digits:
            return []
        
        m = {"2":"abc", '3':"def", '4':"ghi", '5':"jkl", '6':"mno", '7':"pqrs", '8':"tuv", '9':"wxyz"}
        
        res = []
        
        def dfs(pool, path):
            
            if len(path) == len(digits):
                res.append(path)
                return
            
            for c in m[digits[pool]]:
                
                dfs(pool+1, path+c)
        
        dfs(0, '')
        return res
        