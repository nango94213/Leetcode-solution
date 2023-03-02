class Solution:
    def leftRigthDifference(self, nums: List[int]) -> List[int]:
        res = []
        left = 0 
        right = sum(nums)
        for i in range(len(nums)):
            right -= nums[i]
            res.append(abs(left-right))
            left += nums[i]
        
        return res
            