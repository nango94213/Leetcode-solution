class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        left = 0
        longest = 0
        dic = {}
        
        for right in range(len(s)):
            dic[s[right]] = right
            
            if len(dic) > k:
                left = min(dic.values())
                del dic[s[left]]
                left += 1
            longest = max(longest, right-left+1)
        
        return longest
        