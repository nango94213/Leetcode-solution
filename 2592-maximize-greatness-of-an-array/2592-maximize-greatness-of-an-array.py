class Solution:
    def maximizeGreatness(self, nums: List[int]) -> int:
        nums.sort()

        count = 0
        for n in nums:
            if n > nums[count]:
                count += 1
        
        return count
        