import collections
class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        
        stones = list(map(tuple, stones))

        s = set(stones)
        dx = collections.defaultdict(set)
        dy = collections.defaultdict(set)
        
        for i,j in s:
            dx[i].add(j)
            dy[j].add(i)
        
        def dfs(i, j):
            for nextY in dx[i]:
                if (i, nextY) in s:
                    s.remove((i, nextY))
                    dfs(i, nextY)
            
            for nextX in dy[j]:
                if (nextX, j) in s:
                    s.remove((nextX, j))
                    dfs(nextX, j)
        
        island = 0
        
        for x, y in stones:
            if (x, y) not in s:
                continue
            island += 1
            dfs(x, y)
        
        return len(stones) - island