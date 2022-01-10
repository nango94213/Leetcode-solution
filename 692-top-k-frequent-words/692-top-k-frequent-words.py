import collections
import heapq
class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        c=collections.Counter(words)
        return heapq.nsmallest(k,c.keys(),key=lambda x:(-c.get(x),x))