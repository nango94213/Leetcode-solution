import collections
class Solution:
    def alienOrder(self, words: List[str]) -> str:
        
        all_letter = set()
        
        for w in words:
            all_letter.update(list(w))
        
        indegree = collections.defaultdict(int)
        
        outgoing = collections.defaultdict(set)
        
        for word1, word2 in zip(words, words[1:]):
            for a,b in zip(word1, word2):
                if a != b:
                    if b not in outgoing[a]:
                        outgoing[a].add(b)
                        indegree[b] += 1
                    break
            
            else:
                if len(word2) < len(word1):
                    return ""
        
        q = collections.deque()
        
        for i in all_letter:
            if indegree[i] == 0:
                q.append(i)
        
        res = []

        while q:
            
            current = q.popleft()
            
            res.append(current)
            
            for o in outgoing[current]:
                indegree[o] -= 1
                
                if indegree[o] == 0:
                    
                    q.append(o)
        
        if len(res) < len(all_letter):
            return ""
        
        return ''.join(res)
        