class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        
        pointer1 = pointer2 = 0
        
        slots1.sort()
        
        slots2.sort()
        
        
        while pointer1 < len(slots1) and pointer2 < len(slots2):
            
            left = max(slots1[pointer1][0], slots2[pointer2][0])
            right = min(slots1[pointer1][1], slots2[pointer2][1])
            
            if right - left >= duration:
                
                return [left, left+duration]
            
            if slots1[pointer1][1] < slots2[pointer2][1]:
                pointer1 += 1
            else:
                pointer2 += 1
            
        
        return []