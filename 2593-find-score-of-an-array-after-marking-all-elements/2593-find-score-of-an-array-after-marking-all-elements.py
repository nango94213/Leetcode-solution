import heapq
class Solution:
    def findScore(self, nums: List[int]) -> int:
        index = set()
        temp = [(v, i) for i, v in enumerate(nums)]
        temp.sort()
        total = 0
      
        for i in range(len(temp)):
            if temp[i][1] in index:
                continue
            total += temp[i][0]
        
            index.update([temp[i][1], temp[i][1]-1, temp[i][1]+1, len(temp)])
            
        return total
        