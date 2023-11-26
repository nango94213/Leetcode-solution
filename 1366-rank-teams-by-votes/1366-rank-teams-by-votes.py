class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        info = collections.defaultdict(lambda: [0 for _ in range(len(votes[0]))])
        
        for v in votes:
            for i in range(len(v)):
                info[v[i]][i] += 1
        
        res = list(votes[0])
        
        res.sort(key=lambda x: (info[x], -ord(x)), reverse=True)
        
        return ''.join(res)