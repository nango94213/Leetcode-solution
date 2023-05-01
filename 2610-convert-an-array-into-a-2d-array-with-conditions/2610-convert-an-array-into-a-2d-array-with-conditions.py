class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        count = Counter(nums)
        
        k = max(count.values())

        res = [[] for _ in range(k)]
        
        for n in nums:
            if count[n] > 0:
                res[count[n]-1].append(n)
                count[n] -= 1
        return res
            
        
        
        
        
        
        
        
        