import collections
class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        dic = collections.defaultdict(lambda: [0 for i in range(len(votes[0]))])
        
        for v in votes:
            for i, c in enumerate(v):
                dic[c][i] += 1
     
        return ''.join(sorted(dic.keys(), key=lambda x: (dic[x], - ord(x)), reverse = True))
                