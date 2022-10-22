class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        dic = {0: 1}
        
        current = 0
        count = 0
        
        for n in nums:
            
            current += n
            
            if current - k in dic:
                count += dic[current-k]
            
            dic[current] = 1 if current not in dic else dic[current] + 1
        
        return count