class Solution:
    def minimumRemoval(self, beans: List[int]) -> int:
       
        beans.sort()
        n = len(beans)
        total = sum(beans)
        best = beans[0] * n
        for i in range(n-1):
            best = max(best, beans[i+1]*(n-i-1))
        
        return total - best
            