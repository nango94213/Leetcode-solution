class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        
        count = Counter(nums)
        degree = max(count.values())
        candidates = {}
        
        for n in count:
            if count[n] == degree:
                candidates[n] = [-1, -1]
        
        res = float('inf')
        
        for i in range(len(nums)):
            
            if nums[i] in candidates and candidates[nums[i]][0] == -1:
                candidates[nums[i]][0] = i
        
        for i in range(len(nums)-1, -1, -1):
            if nums[i] in candidates and candidates[nums[i]][1] == -1:
                candidates[nums[i]][1] = i
        
        for c in candidates.values():
            res = min(res, c[1] - c[0] + 1)
        
        return res
            
            
            