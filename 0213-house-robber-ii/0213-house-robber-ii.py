class Solution:
    def rob(self, nums: List[int]) -> int:
        
        def house(num):
   
            prev2 = 0
            prev1 = num[0]
            
            for i in range(1, len(num)):
                current = max(prev2+num[i], prev1)
                prev1, prev2 = current, prev1
            
            return prev1
        
        if len(nums) == 1:
            return nums[0]
        return max(house(nums[:-1]), house(nums[1:]))