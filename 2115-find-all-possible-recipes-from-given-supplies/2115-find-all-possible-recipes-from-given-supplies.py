import collections
class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        
        indegree = collections.defaultdict(int)
        outgoing = collections.defaultdict(set)
        
        supplies = set(supplies)
        rset = set(recipes)
        info = {}
        
        for r, i in zip(recipes, ingredients):
            info[r] = i
            for j in i:
                if j in rset:
                    indegree[r] += 1
                    outgoing[j].add(r)
        q = collections.deque()
        
        for r in rset:
            if indegree[r] == 0:
                q.append(r)
        
        res = []
        
        while q:
            current = q.popleft()
            if all([i in supplies for i in info[current]]):
                supplies.add(current)
                res.append(current)
                
                for o in outgoing[current]:
                    indegree[o] -= 1
                    if indegree[o] == 0:
                        q.append(o)
        return res
                    
        
        