class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        
        old = nums[:]
        count = 0
        high = -float('inf')
        
        check1 = True
        check2 = True
        
        for i in range(1, len(nums)):
            
            if nums[i] < nums[i-1]:
                count  += 1
                nums[i-1] = nums[i]
                    
            if count > 1 or nums[i] < high:
                print(i)
                check1 = False
                break
            
            
            high = max(high, nums[i-1])
            
        high = -float('inf')
        count = 0
        for i in range(1, len(old)):
            
            if old[i] < old[i-1]:
                count  += 1
                old[i] = old[i-1] 
                    
            if count > 1 or old[i] < high:
                check2 = False
                break
            
            
            high = max(high, old[i])
        return check1 or check2
        