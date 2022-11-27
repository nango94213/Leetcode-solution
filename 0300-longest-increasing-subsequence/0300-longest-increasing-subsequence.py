import bisect
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        res = []
        
        for n in nums:
            if res and res[-1] > n:
                index = bisect.bisect_left(res, n)
                res[index] = n
            elif not res or res[-1] < n:
                res.append(n)
        
        return len(res)
        