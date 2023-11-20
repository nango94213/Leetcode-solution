class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        res = float('inf')
        current = 0
        for right in range(len(nums)):
            current += nums[right]
            
            while current - nums[left] >= target:
                current -= nums[left]
                left += 1
            

            if current >= target:
                res = min(res, right-left+1)

            
        
        return res if res != float('inf') else 0