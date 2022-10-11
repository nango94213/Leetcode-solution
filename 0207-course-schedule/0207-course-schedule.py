import collections
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        n = numCourses
        indegree = collections.defaultdict(int)
        outgoing = collections.defaultdict(set)
        
        for p in prerequisites:
            indegree[p[0]] += 1
            outgoing[p[1]].add(p[0])
        
        q = collections.deque()
        
        for i in range(n):
            if indegree[i] == 0:
                q.append(i)
        
        count = 0
        
        while q:
            current = q.popleft()
            count += 1
            
            for o in outgoing[current]:
                indegree[o] -= 1
                
                if indegree[o] == 0:
                    q.append(o)
        
        return True if count == n else False
            
            