class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        
        current = 0
        
        dic = {0: -1}
        
        for i in range(len(nums)):
            current += nums[i]
            
            if current % k in dic:
                if i - dic[current%k] + 1 > 2:
                    return True
            else:
                dic[current%k] = i
                
        
        return False
        