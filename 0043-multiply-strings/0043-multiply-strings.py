class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        
        def split(number):
            res = []
            
            digit = 1
            
            for i in range(len(number)-1, -1, -1):
                res.append(int(number[i])*digit)
                digit *= 10
            
            return res
        
        one = split(num1)
        two = split(num2)
        
        return str(sum([x*y for x in one for y in two]))
        