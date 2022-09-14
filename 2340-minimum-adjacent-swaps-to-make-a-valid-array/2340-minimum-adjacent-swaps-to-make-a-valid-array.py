class Solution:
    def minimumSwaps(self, nums: List[int]) -> int:
        
        left = min(nums)
        right = max(nums)
        
        r = len(nums) - 1
        l = 0
        for i in range(len(nums)-1, -1, -1):
            if nums[i] == right:
                r = i
                break
        
        for i in range(len(nums)):
            if nums[i] == left:
                l = i
                break
        print(l)
        print(r)
        if l > r:
            return l + len(nums) - 1 - r - 1
        else:
            return l + len(nums) -1 - r
        
                