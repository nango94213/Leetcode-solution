import collections
class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        graph = collections.defaultdict(set)
        
        for a, b in dislikes:
            graph[a].add(b)
            graph[b].add(a)
        
        seen = set()
        two_group = {}
        for i in range(1, n+1):
            if i not in seen:
                stack = collections.deque([(i, True)])
                two_group[i] = True
                while stack:
                    person, group = stack.popleft()    
                    seen.add(person)
                    for child in graph[person]:
                            if child in two_group and (two_group[child] != (not group)):
                                             return False
                            if child not in seen:

                                        
                                        stack.append((child, not group))
                                        two_group[child] = not group
                    
        return True
                
                