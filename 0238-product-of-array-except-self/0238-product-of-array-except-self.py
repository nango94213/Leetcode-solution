class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        left = []
        prev = 1
        for n in nums:
            left.append(prev)
            prev *= n
        
        prev = 1
        res = []
        for i in range(len(nums)-1, -1, -1):
            res.append(prev*left[i])
            prev *= nums[i]
        return res[::-1]
        