class Solution:
    def amountPainted(self, paint: List[List[int]]) -> List[int]:
        
        res = []
        done = [0]  * 500000
        
        for s, e in paint:
            
            count = 0
            
            while s < e:
                if done[s] == 0:
                    count += 1
                    done[s] = e
                    s += 1
                else:
                    tmp = s
                    s = done[s]
                    done[tmp] = max(done[tmp], e)
            
            res.append(count)
        
        return res