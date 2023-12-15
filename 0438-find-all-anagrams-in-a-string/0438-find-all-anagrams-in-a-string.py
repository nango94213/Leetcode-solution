class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        count = Counter(p)
        scount = Counter()
        k = len(p)
        
        left = 0
        res = []
        for right in range(len(s)):
            scount[s[right]] += 1
            if scount == count:
                    res.append(left)
            if right >= k - 1:
                
                
                scount[s[left]] -= 1
                if scount[s[left]] == 0:
                    del scount[s[left]]
                left += 1
        return res