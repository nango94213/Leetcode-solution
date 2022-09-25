class Solution(object):
    def nextGreaterElement(self, n):
        """
        :type n: int
        :rtype: int
        """
            
        n=list(str(n))
        for i in range(len(n)-2,-1,-1):
            if n[i]<n[i+1]:
              
                for j in range(len(n)-1, i, -1):
             
                    if n[j] > n[i]:
  
                        n[i], n[j] = n[j], n[i]
                    
                        left = i + 1
                        right = len(n) - 1
                    
                        while left < right:
                            n[left], n[right] = n[right], n[left]
                            left += 1
                            right -= 1
                    
                        res=int(''.join(n))
                        return res if res<=2**31-1 else -1
        return -1
        
        
        