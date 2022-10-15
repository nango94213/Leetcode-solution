class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        
        print(chr(3+ord('A')-1))
        
        res = ''
        
        while columnNumber:
            if columnNumber % 26 == 0:
                offset = 26
            else:
                offset = columnNumber % 26
            res = chr(offset+ord('A')-1) + res
            
            if columnNumber % 26 == 0:
                columnNumber = columnNumber // 26 - 1
                continue
            columnNumber = columnNumber // 26
            
  
        return res
        