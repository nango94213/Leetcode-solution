class Solution:
    
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        
        def compare(q):
            i = 0
            
            for j, v in enumerate(q):
                
                if i < len(pattern) and pattern[i] == v:
                    i += 1
                elif v.isupper():
                    return False
            return i == len(pattern)
        
        res = []
        
        for q in queries:
            res.append(compare(q))
            
        
        return res
            
        