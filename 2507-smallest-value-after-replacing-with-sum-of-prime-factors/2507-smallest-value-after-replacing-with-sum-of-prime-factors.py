class Solution:
    def smallestValue(self, n: int) -> int:
        def check(num):
            total = 0
            for i in range(2, num+1):
                while num % i == 0:
                    total += i
                    num //= i
            return total
        
        while n != check(n):
            n = check(n)
        return n
        