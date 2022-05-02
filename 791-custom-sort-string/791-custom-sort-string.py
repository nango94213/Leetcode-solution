class Solution:
    def customSortString(self, order: str, s: str) -> str:
        
        count = Counter(s)
        
        res = []
        
        for o in order:
            
            if o in s:
                res.append(o*count[o])
                
                count[o] = 0
        
        for c in count:
  
                
                res.append(c*count[c])
        
        return ''.join(res)
        