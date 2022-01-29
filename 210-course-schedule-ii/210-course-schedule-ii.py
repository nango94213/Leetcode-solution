import collections
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        indegree = collections.defaultdict(int)
        
        for p in prerequisites:
            indegree[p[0]] += 1
        
        stack = []
        
        for i in range(numCourses):
            if indegree[i] == 0:
                stack.append(i)
        
        res = []
        
        while stack:
            current = stack.pop()
            res.append(current)
            for p in prerequisites:
                if p[1] == current:
                    indegree[p[0]] -= 1
                    
                    if indegree[p[0]] == 0:
                        stack.append(p[0])
        
        return res if len(res) == numCourses else []