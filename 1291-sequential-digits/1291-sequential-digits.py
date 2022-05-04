class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        
        res = []
        
        def dfs(path):
            
            if low <= path <= high:
                res.append(path)
            
            if path > high:
                return 
            
            if (path%10) == 9:
                return 
            
            new = path * 10 + ((path%10) + 1)
                
            dfs(new)
        
        for start in range(1, 9):
            dfs(start)
        
        
        return sorted(res)
           
        
        