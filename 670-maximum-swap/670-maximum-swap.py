class Solution:
    def maximumSwap(self, num: int) -> int:
        
        num = list(str(num))
        
        idx_max_n = len(num) - 1
        swap_left = 0
        swap_right = 0
        
        for i in range(len(num)-1, -1, -1):
            if num[i] > num[idx_max_n]:
                idx_max_n = i
            elif num[i] < num[idx_max_n]:
                swap_left = i
                swap_right = idx_max_n
        
        num[swap_left], num[swap_right] = num[swap_right], num[swap_left]
        
        return int(''.join(num))
        
        