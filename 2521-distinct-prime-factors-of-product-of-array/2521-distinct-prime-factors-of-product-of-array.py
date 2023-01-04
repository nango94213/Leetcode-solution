class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        res = set()
        for n in nums:
            for i in range(2, int(n**0.5)+1):
                if n % i == 0:
                    res.add(i)
                    
                    while n % i == 0:
                        n =  n // i
                
                if n == 1:
                    break
            if n > 1:
                res.add(n)

        return len(res)