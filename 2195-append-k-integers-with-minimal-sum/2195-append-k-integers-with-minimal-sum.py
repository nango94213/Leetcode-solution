class Solution:
    def minimalKSum(self, nums: List[int], k: int) -> int:
        
        total = (k+1)*k // 2
        
        pre = -1
        
        for n in sorted(nums):
            if n > pre:
                if n <= k:
                    k += 1
                    total += k - n
                else:
                    break
  
            pre = n
        return total
        