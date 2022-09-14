class Solution:
    def minimumSwaps(self, nums: List[int]) -> int:
        
        left = 0
        right = 0
        
        n = len(nums)
        for i in range(1, n):
            
            if nums[i] >= nums[right]:
                right = i
            
            if nums[i] < nums[left]:
                left = i
        
        return left + n - 1 - right - 1 if left > right else left + n - 1 - right