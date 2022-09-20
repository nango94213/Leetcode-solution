import bisect
class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        
        A = [i for i, v in enumerate(s) if v == '|']
        
        res = []
        
        for q in queries:
            i = bisect.bisect_left(A, q[0])
            j = bisect.bisect_right(A, q[1]) - 1
            
            ans = A[j] - A[i] - (j - i) if i < j else 0
            res.append(ans)
        
        return res