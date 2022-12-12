class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        num_set = set(nums)
        res = 0
        
        for n in num_set:
            if n ** 0.5 not in num_set:
                count = 0
                while n in num_set:
                    count += 1
                    n = n ** 2
                res = max(res, count)
        return res if res >= 2 else -1