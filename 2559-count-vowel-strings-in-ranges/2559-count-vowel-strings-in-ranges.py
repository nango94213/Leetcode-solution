class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        prefix = [0]
        vowel = set(['a', 'e', 'i', 'o','u'])
        
        current = 0
        for w in words:
            current += w[0] in vowel and w[-1] in vowel
            prefix.append(current)
        
        res = []
        
        for q in queries:
            res.append(prefix[q[1]+1]-prefix[q[0]])
        
        return res