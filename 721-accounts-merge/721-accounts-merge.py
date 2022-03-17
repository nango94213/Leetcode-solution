import collections
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        
        graph = collections.defaultdict(set)
        
        all_emails = set()
        
        name = {}
        
        for account in accounts:

            person = account[0]
            emails = account[1:]
            
            if len(emails) == 1:
                all_emails.add(emails[0])
                
                name[emails[0]] = person
            
            else:
                for i in range(len(emails)):
                    name[emails[i]] = person
                    all_emails.add(emails[i])
                    graph[emails[i]].update(emails[:i]+emails[i+1:])
                    
        
        checked = set()
        res = []
        for e in all_emails:
            if e not in checked:
                checked.add(e)
                
                group = []
                
                q = collections.deque([e])
                
                while q:
                    
                    current = q.popleft()
                    group.append(current)
                    for outgoing in graph[current]:
                        if outgoing not in checked:
                            checked.add(outgoing)
                            q.append(outgoing)
                
     
                res.append([name[e]] + sorted(group))
        
        return res
                    
                    
                
        