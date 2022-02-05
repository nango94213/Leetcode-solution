import collections
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        indegree = collections.defaultdict(int)
        outgoing = collections.defaultdict(list)
        
        for p in prerequisites:
            indegree[p[0]] += 1
            outgoing[p[1]].append(p[0])
        
        stack = []
        
        for i in range(numCourses):
            if indegree[i] == 0:
                stack.append(i)
        
        res = []
        
        while stack:
            current = stack.pop()
            res.append(current)
            for o in outgoing[current]:
                    indegree[o] -= 1
                    
                    if indegree[o] == 0:
                        stack.append(o)
        
        return res if len(res) == numCourses else []