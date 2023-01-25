class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        a = set([max(col) for col in zip(*matrix)])
        b = set([min(row) for row in matrix])
        
        return a.intersection(b)