class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        
        res = 0
        seen = Counter()
        
        left = 0
        
        for right in range(len(s)):
            
            seen[s[right]] += 1
            
            while len(seen) > 2:
                seen[s[left]] -= 1
                if seen[s[left]] == 0:
                    del seen[s[left]]
                left += 1
            res = max(res, right - left + 1)
   
        return res
        