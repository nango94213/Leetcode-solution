class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        res = []
        
        def dfs(left, right, path):
            
            if left < 0 or right < 0 or left > right:
                return
            
            if left == 0 and right == 0:
                res.append(path)
            
            dfs(left-1, right, path+'(')
            dfs(left, right-1, path+')')
        
        dfs(n, n, '')
        
        return res