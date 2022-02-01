class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        res = []
        buffer = ''
        inBlock = False
        
        for line in source:
            i = 0
            while i < len(line):
                if line[i] == '/' and (i+1) < len(line) and  line[i+1] == '/' and not inBlock:
                    i = len(line)
                
                elif line[i] == '/' and (i+1) < len(line) and line[i+1] == '*' and not inBlock:
                    i += 1
                    inBlock = True
                
                elif line[i] == '*' and (i+1) < len(line) and line[i+1] == '/' and inBlock:
                    i += 1
                    inBlock = False
                
                elif not inBlock:
                    buffer += line[i]
                
                i += 1
            
            if buffer and not inBlock:
                res.append(buffer)
                buffer = ''
        
        return res
        