class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        
        nums.sort()
        
        left = 0
        right = len(nums) - 1
        res = -1
        
        while left < right:
            total  = nums[left] + nums[right]
            
            if total < k:
                res = max(res, total)
                left += 1
            else:
                right -= 1
        
        return res