class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        graph = collections.defaultdict(set)
        for r in roads:
            graph[r[0]].add(r[1])
            graph[r[1]].add(r[0])
        res = 0
        
        def dfs(node, prev):
            nonlocal res
            p = 1 if node else 0
            for o in graph[node]:
                if o == prev:
                    continue
                
                p += dfs(o, node)
                
            res += math.ceil(p/seats) if node else 0
            
            return p
        dfs(0, 0)
        return res