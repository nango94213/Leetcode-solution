class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        dic = {}
        left = 0
        res = 0
        for i in  range(len(s)):
            
            if s[i] in dic:
                left = max(left, dic[s[i]]+1)
            
            res = max(res, i-left+1)
            
            dic[s[i]] = i
        
        return res