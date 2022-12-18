class Solution:
    def similarPairs(self, words: List[str]) -> int:
        res = 0
        words = list(map(set, words))
        
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                if words[i] == words[j]:
                    res += 1
        return res