import collections

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        graph = collections.defaultdict(set)
        for s, e, d in roads:
            graph[s].add(e)
            graph[e].add(s)
        

        q = collections.deque([1])
        seen = set([1])
        while q:
            current = q.popleft()
            for o in graph[current]:
                if o not in seen:
                    seen.add(o)
                    q.append(o)
        
        res = float('inf')
        for s, e, d in roads:
            if s in seen and e in seen:
                res = min(res, d)
        return res