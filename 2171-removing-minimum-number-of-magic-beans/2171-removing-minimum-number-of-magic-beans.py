class Solution:
    def minimumRemoval(self, beans: List[int]) -> int:
       
        beans.sort()
        n = len(beans)
        prefix = []
        
        for b in beans:
            if prefix:
                prefix.append(prefix[-1] + b)
            else:
                prefix.append(b)
      
        res = (prefix[-1] - prefix[0]) - beans[0] * (n-1)
       
        for i in range(n):
            
            res = min(res, prefix[i]+prefix[-1]-prefix[min(i+1, n-1)]-beans[min(i+1, n-1)]*(n-2-i))
           
            
        return res
            