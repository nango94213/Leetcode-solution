class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        
        res = []
        dic = {}
        for i, v in enumerate(s):
            dic[v] = i
        
        seen = set()
        
        for i, v in enumerate(s):
            if v not in seen:
                while res and res[-1] > v and dic[res[-1]] > i:
                    tmp = res.pop()
                    seen.remove(tmp)
                
                seen.add(v)
                res.append(v)
        
        return ''.join(res)
                    