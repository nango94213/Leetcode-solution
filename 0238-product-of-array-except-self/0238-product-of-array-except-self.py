class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        prev = []
        
        current = 1
        
        for n in nums:
            prev.append(current)
            current *= n
        current = 1
        for i in range(len(nums)-1, -1, -1):
            prev[i] = prev[i] * current
            current *= nums[i]
        return prev