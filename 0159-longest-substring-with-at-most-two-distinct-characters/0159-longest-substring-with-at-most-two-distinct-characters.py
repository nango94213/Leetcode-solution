class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        
        res = 0
        seen = Counter()
        
        left = 0
        k = 2
        for right in range(len(s)):
            
            if seen[s[right]] == 0:
                k -= 1
            seen[s[right]] += 1
            
            if k < 0:
                seen[s[left]] -= 1
                if seen[s[left]] == 0:
                    k += 1
                left += 1
            
   
        return right - left + 1
        