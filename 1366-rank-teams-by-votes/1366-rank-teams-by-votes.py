import collections
class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        info = collections.defaultdict(lambda :[0 for _ in range(len(votes[0]))])
        
        for i in range(len(votes)):
            for j, v in enumerate(votes[i]):
                info[v][j] += 1
        

        return ''.join(sorted(info.keys(), key=lambda x: (info[x], -ord(x)), reverse=True))
        