class Solution:
    def greatestLetter(self, s: str) -> str:
        s_set = set(list(s))
        candidates = set()
        
        for c in s_set:
            if c.lower() in s_set and c.upper() in s_set:
                candidates.add(c)
        return max(candidates).upper() if candidates else ''
        