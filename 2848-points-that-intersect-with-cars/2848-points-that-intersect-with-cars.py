class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        
        dic = [0] * 102
        
        for n in nums:
            dic[n[0]] += 1
            dic[n[1]+1] -= 1
        current = 0 
        total = 0
        for i in range(1, len(dic)):
            current += dic[i]
            if current > 0:
                total += 1

      
        return total
        
        