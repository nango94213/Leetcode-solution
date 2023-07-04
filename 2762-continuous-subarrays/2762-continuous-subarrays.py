class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        left = 0
        res = 0
        dic = {}
        for right in range(len(nums)):
            if nums[right] in dic:
                dic[nums[right]] = right
            else:
                dic[nums[right]] = right
                d = []
                for k in dic:
                    if nums[right] - k > 2:
                        left = max(left, dic[k]+1)
                        d.append(k)
                    elif k - nums[right] > 2:
                        left = max(left, dic[k]+1)
                        d.append(k)
                for k in d:
                    del dic[k]
            
            res += right - left + 1
        
        return res
            
        