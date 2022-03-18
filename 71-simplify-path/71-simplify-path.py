class Solution:
    def simplifyPath(self, path: str) -> str:
        
        res = []
        
        path = path.split('/')
        
        for p in path:
            
            if p == '..':
                if res:
                    res.pop()
            
            elif p != '.' and p != '':
                res.append(p)
        
        return '/' + '/'.join(res)