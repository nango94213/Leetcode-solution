import heapq
class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        heap = []
        
        for i in range(len(nums)):
            heapq.heappush(heap, (nums[i][0], i, 0))
        
        right = max([n[0] for n in nums])
        
        res = [-float('inf'), float('inf')]
        
        while heap:
            
            left, index_list, index_number = heapq.heappop(heap)
            
            if (right-left) < (res[1]-res[0]):
                res[0], res[1] = left, right
            
            if index_number == len(nums[index_list]) - 1:
                return res
            
            value = nums[index_list][index_number+1]
            
            right = max(value, right)
            
            heapq.heappush(heap, (value, index_list, index_number+1))
        
        return None