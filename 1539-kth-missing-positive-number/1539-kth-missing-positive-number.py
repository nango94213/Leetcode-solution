class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        
        numbers = 0
        
        current = 1
        index = 0
        
        while numbers < k:
            
            if index < len(arr) and current == arr[index]:
                index += 1
            else:
                numbers += 1
            
            current += 1
        
        return current - 1
                
            
        