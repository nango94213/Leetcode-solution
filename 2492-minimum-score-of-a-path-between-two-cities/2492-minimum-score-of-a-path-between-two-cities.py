import collections

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        graph = collections.defaultdict(dict)
        for s, e, d in roads:
            graph[s][e] = d
            graph[e][s] = d
        

        q = collections.deque([1])
        seen = set([1])
        res = float('inf')
        while q:
            current = q.popleft()
            for o in graph[current]:
                if o not in seen:
                    seen.add(o)
                    q.append(o)
                res = min(res, graph[current][o])
             
        return res