class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        one = 0
        two = 0
        
        while one < len(s) and two < len(t):
            if s[one] == t[two]:
                
                one += 1
                two += 1
            
            else:
                
                two += 1

        return one == len(s) 
        