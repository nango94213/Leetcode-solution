class Solution:
    def maximumSwap(self, num: int) -> int:
        
        num = list(str(num))
        
        currentMax = len(num) - 1
        first = 0
        second = 0
        
        for i in range(len(num)-1, -1, -1):
            
            if num[i] > num[currentMax]:
                currentMax = i
            elif num[i] < num[currentMax]:
                first = i
                second = currentMax
        
        num[first], num[second] = num[second], num[first]
        
        return int(''.join(num))