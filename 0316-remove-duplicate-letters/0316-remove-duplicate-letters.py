class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        
        res = []
        dic = {}
        for i, v in enumerate(s):
            dic[v] = i
            
        seen = set()
        
        for i, v in enumerate(s):
            if v not in seen:
                
                while res and res[-1] > v and i < dic[res[-1]]:
                    letter = res.pop()
                    seen.remove(letter)
                    
                res.append(v)
                seen.add(v)
        
        return ''.join(res)