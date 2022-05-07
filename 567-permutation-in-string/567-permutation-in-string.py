class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        count1 = Counter(s1)
        
        size = len(s1)
        
        left = 0
        
        count2 = Counter()
        
        for right in range(len(s2)):
            
            count2[s2[right]] += 1
            
            if right + 1 >= size:
                
                if count1 == count2:
                    return True
                
                count2[s2[left]] -= 1
                left += 1
        
        return False
                
                
            
            
        