class Solution:
    def amountPainted(self, paint: List[List[int]]) -> List[int]:
        res = []
        track = [0] * 500000
        
        for s, e in paint:
            count = 0
            while s < e:
                if track[s] == 0:
                    count += 1
                    track[s] = e
                    s += 1
                else:
                    old = s
                    s = track[s]
                    track[old] = max(track[old], e)
            res.append(count)
        return res