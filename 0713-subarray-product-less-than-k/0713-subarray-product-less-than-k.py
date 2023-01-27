class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        
        if k <= 1:
            return 0
        total = 1
        left = 0
        count = 0
        for right in range(len(nums)):
            total *= nums[right]
            
            while total >= k:
                total //= nums[left]
                left += 1
            
            count += right - left + 1
        return count