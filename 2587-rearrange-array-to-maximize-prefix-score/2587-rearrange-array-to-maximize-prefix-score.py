class Solution:
    def maxScore(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        count = 0
        current = 0
        for n in nums:
            current += n
            if current > 0:
                count += 1
        return count
        