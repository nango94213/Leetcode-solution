class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        count = Counter()
        
        left = 0
        for right in range(len(s)):
            if count[s[right]] == 0:
                k -= 1
            count[s[right]] += 1
            if k < 0:
                count[s[left]] -= 1
                if count[s[left]] == 0:
                    k += 1
                
                left += 1
        
        return right - left + 1
                
        