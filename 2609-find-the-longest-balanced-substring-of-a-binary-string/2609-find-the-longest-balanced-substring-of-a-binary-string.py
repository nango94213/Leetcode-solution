class Solution:
    def findTheLongestBalancedSubstring(self, s: str) -> int:
        
        cluster = [[s[0], 1]]
        current = 0
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                cluster[-1][1] += 1
            else:
                cluster.append([s[i], 1])
        res = 0
        for i in range(1, len(cluster)):
            if cluster[i-1][0] == '0' and cluster[i][0] == '1':
                 res = max(res, min(cluster[i][1], cluster[i-1][1]))
        return res * 2