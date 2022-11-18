class Solution:
    def maximumSwap(self, num: int) -> int:
        num = list(str(num))
        swap1 = 0
        swap2 = 0
        largest = -1
        
        for i in range(len(num)-1, -1, -1):
            if num[i] < num[largest]:
                swap1 = i
                swap2 = largest
            
            if num[i] > num[largest]:
                largest = i
        
        num[swap1], num[swap2] = num[swap2], num[swap1]
        return int(''.join(num))
        