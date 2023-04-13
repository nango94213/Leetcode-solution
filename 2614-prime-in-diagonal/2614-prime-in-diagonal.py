class Solution:
    def diagonalPrime(self, nums: List[List[int]]) -> int:
        '''def is_prime(n):
            if n <= 1:
                return False
            if n <= 3:
                return True
            if n % 2 == 0 or n % 3 == 0:
                return False

            i = 5
            while i * i <= n:
                if n % i == 0 or n % (i + 2) == 0:
                        return False
                i += 6

            return True'''
        def is_prime(n):
            if n <= 1:
                return False
            for i in range(2, int(n**0.5)+1):
                if n % i == 0:
                    return False
            return True
        res = 0
        n = len(nums) - 1
        for i in range(len(nums)):
            if is_prime(nums[i][i]):
                res = max(res, nums[i][i])
            if is_prime(nums[n-i][i]):
                res = max(res, nums[n-i][i])
        return res
