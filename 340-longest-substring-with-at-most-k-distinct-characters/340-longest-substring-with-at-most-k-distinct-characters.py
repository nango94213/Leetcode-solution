import collections
class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        left = 0
        longest = 0
        dic = collections.OrderedDict()
        
        for right in range(len(s)):
            if s[right] in dic:
                dic.pop(s[right])
            dic[s[right]] = right
            
            if len(dic) > k:
                left = dic.popitem(last=False)[1]
                print(left)
                left += 1
            longest = max(longest, right-left+1)
        
        return longest
        