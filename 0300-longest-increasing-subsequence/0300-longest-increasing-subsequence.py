import bisect
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        res = []
        for num in nums:
            index = bisect.bisect_left(res, num)
            
            if index == len(res):
                res.append(num)
            else:
                res[index] = num
        
        return len(res)