class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        row = 0
        best = 0
        
        for i in range(len(mat)):
            count = sum(mat[i])
            if count > best:
                row = i
                best = count
        
        return [row, best]
        