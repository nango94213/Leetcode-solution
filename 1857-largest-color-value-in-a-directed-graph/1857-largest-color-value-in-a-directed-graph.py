import collections
class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        
        indegree = collections.defaultdict(int)
        outgoing = collections.defaultdict(set)
        
        for e in edges:
            indegree[e[1]] += 1
            outgoing[e[0]].add(e[1])
        
        dp = [[0]*26 for _ in range(len(colors))]
        
        processed = 0
        
        q = collections.deque()
        
        for i in range(len(colors)):
            if indegree[i] == 0:
                q.append(i)
        res = 0
        while q:
            current = q.popleft()
            processed += 1
            index = ord(colors[current]) - ord('a')
            
            dp[current][index] += 1
            
            res = max(res, dp[current][index])
            
            for o in outgoing[current]:
                indegree[o] -= 1
                
                dp[o] = [max(a, b) for a, b in zip(dp[current], dp[o])]
                
                if indegree[o] == 0:
                    q.append(o)
        
        return res if processed == len(colors) else -1
        