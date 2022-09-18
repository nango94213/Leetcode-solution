class Solution:
    def minSwaps(self, data: List[int]) -> int:
        total = sum(data)
        
        if not total:
            return 0
        
        left = 0
        
        res = float('inf')
        
        count = 0
        
        for right in range(len(data)):
            if data[right] == 0:
                count += 1
            
            if right >= total - 1:
                res = min(res, count)
                
                if data[left] == 0:
                    count -= 1
                
                left += 1
        
        return res
            
            