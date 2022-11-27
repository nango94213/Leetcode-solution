class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        dic = {0: -1}
        current = 0
        
        for i, v in enumerate(nums):
            current += v
            if current%k in dic and i - dic[current%k] >= 2:
                return True
            
            if current%k not in dic:
                dic[current%k] = i
        
        return False