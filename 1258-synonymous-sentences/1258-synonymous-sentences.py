import collections
class Solution:
    def generateSentences(self, synonyms: List[List[str]], text: str) -> List[str]:
        
        res = set()
        
        dic = collections.defaultdict(set)
        
        for k, v in synonyms:
            dic[k].add(v)
            dic[v].add(k)
        
        q = collections.deque([text])
        
        while q:
            
            current = q.popleft()
            
            res.add(current)
            
            splitCurrent = current.split(' ')
            
            for i, v in enumerate(splitCurrent):
                
                for nextW in dic[v]:
                    
                    merge = ' '.join(splitCurrent[:i] + [nextW] + splitCurrent[i+1:])
                    
                    if merge not in res:
                        res.add(merge)
                        q.append(merge)
        
        return sorted(list(res))
        