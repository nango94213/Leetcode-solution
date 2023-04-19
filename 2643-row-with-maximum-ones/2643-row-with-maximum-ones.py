class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        res = [0, 0]
        
        for i in range(len(mat)):
            count = sum(mat[i])
            if count > res[1]:
                res = [i, count]
        
        return res
        