class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        
        def compare(s):
            j = 0
            for i in range(len(s)):
                if j < len(pattern) and s[i] == pattern[j]:
                    j += 1
                elif s[i].isupper():
                    return False
            
            return j == len(pattern)
        
        res = []
        for q in queries:
            if compare(q):
                res.append(True)
            else:
                res.append(False)
        
        return res