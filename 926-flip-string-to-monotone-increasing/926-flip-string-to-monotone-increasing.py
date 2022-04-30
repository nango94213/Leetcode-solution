class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        
        count0 = s.count('0')
        count1 = 0
        
        res = float('inf')
        
        for number in s:
            
            if number == '0':
                count0 -= 1
            else:
                res = min(res, count0+count1)
                
                count1 += 1

        return min(res, count0+count1)
        