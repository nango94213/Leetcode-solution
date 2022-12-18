class Solution:
    def similarPairs(self, words: List[str]) -> int:
        count = Counter()
        
        for word in words:
            tmp = [0] * 26
            for c in word:
                tmp[ord(c)-ord('a')] = 1
            count[tuple(tmp)] += 1
        res = 0
        print(count)
        for v in count.values():
            if v > 1:
                res += math.factorial(v)//(2*math.factorial(v-2))
        return res