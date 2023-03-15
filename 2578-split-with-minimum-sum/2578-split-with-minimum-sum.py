class Solution:
    def splitNum(self, num: int) -> int:
        nums = []
        
        while num:
            nums.append(num%10)
            num //= 10
        nums.sort()
        
        res = 0
        digit = 1
        print(nums)
        for i in range(len(nums)-1, 0, -2):

            res += nums[i]*digit + nums[i-1]*digit
            digit *= 10
        return res if  len(nums) % 2 == 0 else res + nums[0] * digit
            