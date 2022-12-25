class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        limits = {c: s.count(c) - k for c in 'abc'}
        if any(x < 0 for x in limits.values()):
            return -1
        left = 0
        count = Counter(s)
        for key in count:
            count[key] -=  k
        
        j = 3
        for right in range(len(s)):
            count[s[right]] -= 1
            
            if count['a'] < 0 or count['b'] < 0 or count['c'] < 0:
                count[s[left]] += 1
                left += 1
                
        return len(s) - (right-left+1)