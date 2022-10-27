class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        current = 0
        
        for i, v in enumerate(nums):
            if current < i:
                return False
            current = max(current, nums[i]+i)
            
        return True