class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        
        if 0 not in nums:
            return len(set(nums))
        else:
            return len(set(nums)) - 1
        