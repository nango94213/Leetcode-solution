class Solution:
    def amountPainted(self, paint: List[List[int]]) -> List[int]:
        res = []
        track = [0] * 500000
        
        for s, e in paint:
            count = 0
            while s < e:
                if track[s] == 0:
                    track[s] = e
                    count += 1
                    s += 1
                else:
                    t = s
                    s = track[s]
                    track[t] = max(track[t], e)
            res.append(count)
        return res
                