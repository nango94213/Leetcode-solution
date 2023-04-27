class Solution:
    def findPrefixScore(self, nums: List[int]) -> List[int]:
        total = 0
        current = 0
 
        for i in range(len(nums)):
            current = max(nums[i], current)
            total += nums[i] + current
            nums[i] = total
        return nums
        