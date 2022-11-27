import bisect
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        
      
        res = []
        
        for e in [i[1] for i in envelopes]:
            index = bisect.bisect_left(res, e)
            
            if index == len(res):
                res.append(e)
            else:
                res[index] = e
        
        return len(res)