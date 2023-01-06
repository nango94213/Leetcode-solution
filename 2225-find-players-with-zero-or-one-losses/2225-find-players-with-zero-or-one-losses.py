import collections
class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        indegree = collections.defaultdict(int)
        
        total = set()
        
        for x, y in matches:
            indegree[y] += 1
            total.add(x)
            total.add(y)
        
        a = []
        b = []
        
        for n in total:
            if indegree[n] == 0:
                a.append(n)
            if indegree[n] == 1:
                b.append(n)
        
        return [sorted(a), sorted(b)]