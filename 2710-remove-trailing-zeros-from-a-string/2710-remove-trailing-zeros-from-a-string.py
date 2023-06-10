class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        if num[-1] != "0":
            return num
        index = len(num) - 1
      
        for i in range(len(num)-2, -1, -1):
            if num[i] == "0":
                index -= 1
            else:
                break
      
        
        return num[:index]
 
        