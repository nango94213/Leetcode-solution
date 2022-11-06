import collections
class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        
        rset = set(recipes)
        sset = set(supplies)
        
        indegree = collections.defaultdict(int)
        outgoing = collections.defaultdict(set)
        info = {}
        for i in range(len(recipes)):
            info[recipes[i]] = ingredients[i]
            
            for child in ingredients[i]:
                if child in rset:
                    indegree[recipes[i]] += 1
                    outgoing[child].add(recipes[i])
        
        q = collections.deque()
        
        for r in recipes:
            if indegree[r] == 0:
                q.append(r)
        
        res = []
        
        while q:
            current = q.popleft()
            if all(i in sset for i in info[current]):
                res.append(current)
                sset.add(current)
                
                for o in outgoing[current]:
                    indegree[o] -= 1
                    if indegree[o] == 0:
                        q.append(o)
        return res