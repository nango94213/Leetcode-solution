import collections
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dic = collections.defaultdict(list)
        
        for s in strs:
            c = [0] * 26
            for i in s:
                c[ord(i)-ord('a')] += 1
            dic[tuple(c)].append(s)
        
        return dic.values()