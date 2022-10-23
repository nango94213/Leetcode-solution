import collections
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        indegree = collections.defaultdict(int)
        outgoing = collections.defaultdict(set)
        
        for p in prerequisites:
            indegree[p[0]] += 1
            outgoing[p[1]].add(p[0])
        
        q = collections.deque()
        
        for node in range(numCourses):
            if indegree[node] == 0:
                q.append(node)
        res = []
        
        while q:
            
            current = q.popleft()
            res.append(current)
            
            for o in outgoing[current]:
                indegree[o] -= 1
                
                if indegree[o] == 0:
                    q.append(o)
        
        return res if len(res) == numCourses else []
        
        
        