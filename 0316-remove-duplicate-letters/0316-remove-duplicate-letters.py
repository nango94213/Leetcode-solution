class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        dic = {}
        for i, v in enumerate(s):
            dic[v] = i
        
        seen = set()
        
        res = []
        
        for i, c in enumerate(s):
            if c not in seen:
                while res and res[-1] > c and dic[res[-1]] > i:
                        tmp = res.pop()
                        seen.remove(tmp)
                seen.add(c)
                res.append(c)
        
        return ''.join(res)
        