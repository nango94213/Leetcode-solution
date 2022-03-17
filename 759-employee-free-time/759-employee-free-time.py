"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""
class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':

        h = heapq.merge(*schedule, key=lambda x: x.start)
        h = list(h)
        res = []
        current = h[0]
        
        b = current.end
        for i in h[1:]:
            if b < i.start:
                res.append(Interval(b, i.start))
                b = i.end
            else:
                b = max(b, i.end)
        
        return res
            
            

            

        
            