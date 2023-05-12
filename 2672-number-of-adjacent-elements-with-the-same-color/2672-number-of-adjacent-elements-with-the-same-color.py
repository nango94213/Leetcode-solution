class Solution:
    def colorTheArray(self, n: int, queries: List[List[int]]) -> List[int]:
        current = 0
        state = [0] * n
        res = []
        for q in queries:
            if q[0] < n - 1:
                if state[q[0]] == state[q[0]+1] and state[q[0]] != 0:
                    current -= 1
                if q[1] == state[q[0]+1]:
                    current += 1
            if q[0] > 0:
                if state[q[0]] == state[q[0]-1] and state[q[0]] != 0:
                    current -= 1
                if q[1] == state[q[0]-1]:
                    current += 1
                    
            
            state[q[0]] = q[1]
    
            res.append(current)
        return res
        