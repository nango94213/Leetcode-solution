import heapq
class Solution:
    def findScore(self, nums: List[int]) -> int:
        index = set()
        temp = [(v, i) for i, v in enumerate(nums)]
        heapq.heapify(temp)
        total = 0
      
        while temp:
            current = heapq.heappop(temp)
            if current[1] not in index:
                total += current[0]
                index.add(current[1])
                index.add(max(0, current[1]-1))
                index.add(min(len(nums)-1, current[1]+1))
        return total
        