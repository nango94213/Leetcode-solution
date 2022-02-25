class Solution:
    def countPrimes(self, n: int) -> int:
        
        if n < 3:
            return 0
        
        prime = [True] * n
        
        prime[0], prime[1] = False, False
        
        for i in range(2, int(n**0.5)+1):
            if prime[i] == True:
                for j in range(i**2, n, i):
                    prime[j] = False
        
        return sum(prime)
            
        