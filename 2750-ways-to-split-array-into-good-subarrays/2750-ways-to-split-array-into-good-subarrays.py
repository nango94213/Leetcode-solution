class Solution:
    def numberOfGoodSubarraySplits(self, nums: List[int]) -> int:
        total = sum(nums)
        if total == 0:
            return 0
        if total == 1:
            return 1
        
        res = 1
        s = False
        count = 0
        for i in range(len(nums)):
            if nums[i] == 1 and s == False:
                s = True
            elif nums[i] == 0 and s == True:
                count += 1
            elif nums[i] == 1 and s == True:
            
                res *= (count+1)
                count = 0
        return res % (10**9+7)