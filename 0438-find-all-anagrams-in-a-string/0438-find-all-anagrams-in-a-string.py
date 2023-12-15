class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        countp = Counter(p)
        counts = Counter()
        
        left = 0
        res = []
        n = len(p)
        for right in range(len(s)):
            counts[s[right]] += 1

            if right - left + 1 > n:
                counts[s[left]] -= 1
                if counts[s[left]] == 0:
                    del counts[s[left]]
                
                left += 1
            if counts == countp:
                    res.append(left)
        
        return res