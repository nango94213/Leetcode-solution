import collections
class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        outgoing = collections.defaultdict(set)
        indegree = collections.defaultdict(int)
        
        dp = [[0]*26 for _ in range(len(colors))]
        
        for e in edges:
            outgoing[e[0]].add(e[1])
            indegree[e[1]] += 1
        
        q = collections.deque()
        
        for i in range(len(colors)):
            if indegree[i] == 0:
                q.append(i)
        
        res = 0
        count = 0
        while q:
            current = q.popleft()
            count += 1
            index = ord(colors[current]) - ord('a')
            dp[current][index] += 1
            res = max(res, dp[current][index])
            
            for o in outgoing[current]:
                dp[o] = [max(i, j) for i, j in zip(dp[current], dp[o])]
                indegree[o] -= 1
                if indegree[o] == 0:
                    q.append(o)
        
        return res if count == len(colors) else -1