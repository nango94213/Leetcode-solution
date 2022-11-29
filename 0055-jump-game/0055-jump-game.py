class Solution:
    def canJump(self, nums: List[int]) -> bool:
        far = 0
        
        for i, v  in enumerate(nums):
            if far < i:
                return False
            far = max(far, i+v)
        return True
        