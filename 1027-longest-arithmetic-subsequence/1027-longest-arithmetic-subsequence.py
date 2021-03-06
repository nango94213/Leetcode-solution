import collections
class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        
        dic = collections.defaultdict(lambda: 1)
        
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                
                dic[(j, nums[j]-nums[i])] = dic[(i, nums[j]-nums[i])] + 1
        
        
        return max(dic.values())
        