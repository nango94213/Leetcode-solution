import collections
class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        table = collections.defaultdict(list)
        for i, v in enumerate(nums):
            table[v].append(i)
      
        res = [0] * len(nums)
        
        for i in range(len(res)):
            if res[i] != 0 or len(table[nums[i]]) == 1:
                continue
            
            array = table[nums[i]]
            prefix = [0]
            for n in array:
                    prefix.append(prefix[-1]+n)
  
            prefix.append(0)
           
            for i in range(1, len(prefix)-1):
                
                res[array[i-1]] = (i-1) * array[i-1] - prefix[i-1] + prefix[-2]-prefix[i] - (len(array)-i) * array[i-1]
                
        return res
            
 
            
            
        