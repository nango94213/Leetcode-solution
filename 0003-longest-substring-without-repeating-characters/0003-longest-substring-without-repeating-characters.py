class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {}
        
        left = 0
        
        res = 0
        
        for right in range(len(s)):
            
            if s[right] in dic:
                left = max(left, dic[s[right]]+1)
            
            dic[s[right]] = right
            
            res = max(res, right-left+1)
        return res
        