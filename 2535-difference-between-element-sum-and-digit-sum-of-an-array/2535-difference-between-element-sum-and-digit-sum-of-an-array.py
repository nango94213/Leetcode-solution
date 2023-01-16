class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        part1 = sum(nums)
        
        total = 0
        
        for n in nums:
            while n:
                total += (n%10)
                n = n // 10
        return abs(part1-total)
        