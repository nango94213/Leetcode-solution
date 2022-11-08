class Solution:
    def amountPainted(self, paint: List[List[int]]) -> List[int]:
        p = [0] * 500000
        res = []
        for s, e in paint:
            count = 0
            
            while s < e:
                if p[s] == 0:
                    count += 1
                    p[s] = e
                    s += 1
                else:
                    t = s
                    s = p[s]
                    p[t] = max(p[t], e)
            res.append(count)
        
        return res