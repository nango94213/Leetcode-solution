class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        

        
        left = 0
        right = len(people) - 1
        
        people.sort()
        
        count = 0
        
        while left <= right:
            
            if people[left] + people[right] <= limit:
                
                left += 1
             
            right -= 1
            
            count += 1
        
        return count
                
        