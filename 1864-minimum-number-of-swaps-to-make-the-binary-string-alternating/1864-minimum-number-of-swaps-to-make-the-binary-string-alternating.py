class Solution:
    def minSwaps(self, s: str) -> int:
        
        count = Counter(s)
        
        if abs(count['1']-count['0']) > 1:
            return -1
        
        count0 = 0
        count1 = 0
        
        for i in range(0, len(s), 2):
            if s[i] != '0':
                count0 += 1
            if s[i] != '1':
                count1 += 1
        
        if count['1'] == count['0']:
            return min(count0, count1)
        
        if count['1'] > count['0']:
            return count1
        else:
            return count0