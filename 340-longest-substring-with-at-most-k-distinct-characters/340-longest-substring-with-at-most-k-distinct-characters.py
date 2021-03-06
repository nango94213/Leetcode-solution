import collections
class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        left = 0
        longest = 0
        dic = collections.OrderedDict()
        
        for right in range(len(s)):
   
            dic[s[right]] = right
            dic.move_to_end(s[right])
                
      
            
            if len(dic) > k:
                left = dic.popitem(last=False)[1] + 1

            longest = max(longest, right-left+1)
        
        return longest
        