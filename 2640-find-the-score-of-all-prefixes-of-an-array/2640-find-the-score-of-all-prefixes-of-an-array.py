class Solution:
    def findPrefixScore(self, nums: List[int]) -> List[int]:
        total = 0
        current = 0
        res = []
        for n in nums:
            current = max(n, current)
            total += n + current
            res.append(total)
        return res
        