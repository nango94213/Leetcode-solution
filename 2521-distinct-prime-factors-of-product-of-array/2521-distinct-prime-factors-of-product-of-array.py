class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
     
        res = set()
        for n in nums:
            c = 2
          
            while n > 1:
                
                if n % c == 0:
                    n = n // c
                    res.add(c)
                else:
                    c = c + 1

        return len(res)