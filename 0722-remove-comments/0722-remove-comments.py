class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        res = []
        current = ''
        block = False
        for s in source:
            i = 0
            while i < len(s):
                if s[i] == '/' and i+1 < len(s) and s[i+1] == '/' and not block:
                    i = len(s)
                elif s[i] == '/' and i+1 < len(s) and s[i+1] == '*' and not block:
                    block = True
                    i += 1
                elif s[i] == '*' and i+1 < len(s) and s[i+1] == '/' and block:
                    block = False
                    i += 1
                elif not block:
                    current += s[i]
                i += 1
            
            if current and not block:
                res.append(current)
                current = ''
        return res