import heapq
class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        
        res = []
        
        tasks = sorted([(t[0], t[1], i) for i, t in enumerate(tasks)])
        
        heap = []
        
        i = 0
        current = tasks[0][0]
        while len(res) < len(tasks):
            
            while i < len(tasks) and tasks[i][0] <= current:
                heapq.heappush(heap, (tasks[i][1], tasks[i][2]))
                i += 1
            
            
            if heap:
                process, index = heapq.heappop(heap)
            
                res.append(index)
            
                current += process
            elif i < len(tasks):
                current = tasks[i][0]
        
        return res
            