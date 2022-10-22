class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        res = []
        buffer = ''
        inblock = False
        
        for s in source:
            i = 0
            while i < len(s):
                if s[i] == '/' and (i+1) < len(s) and s[i+1] == '/' and not inblock:
                    i = len(s)
                elif s[i] == '/' and (i+1) < len(s) and s[i+1] == '*' and not inblock:
                    inblock = True
                    i += 1
                elif s[i] == '*' and (i+1) < len(s) and s[i+1] == '/' and inblock:
                    inblock = False
                    i += 1
                elif not inblock:
                    buffer += s[i]
                
                i += 1
            
            if buffer and not inblock:
                res.append(buffer)
                buffer = ''
        
        return res
                    
                    
        