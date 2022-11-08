import bisect
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        
        check = [i[1] for i in envelopes]
        
        res = []
        
        for number in check:
            index = bisect.bisect_left(res, number)
            
            if not res:
                res.append(number)
                continue
            if number > res[-1]:
                res.append(number)
            else:
                res[index] = number
        
        return len(res)
        