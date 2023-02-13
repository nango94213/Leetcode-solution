import bisect
class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        
        nums.sort()
        ans=0
        for i in range(len(nums)):
            v = nums[i]
            a = bisect_left(nums, lower - v, lo=i+1, hi=len(nums))
            b = bisect_right(nums, upper - v, lo=i+1, hi=len(nums))
            ans += b - a
        return ans
                