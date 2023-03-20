class Solution:
    def maximizeGreatness(self, nums: List[int]) -> int:
        nums.sort()
        pool = deepcopy(nums)
        count = 0
        
        i = j = 0
  
        while j < len(nums):
            if pool[j] > nums[i]:
                j += 1
                i += 1
                count += 1
            else:
                j += 1
        return count
        