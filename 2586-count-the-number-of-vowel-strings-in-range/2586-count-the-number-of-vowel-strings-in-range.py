class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        count = 0
        v = set(['a', 'e', 'i', 'o', 'u'])
        for i in range(left, right+1):
            if words[i][0] in v and words[i][-1] in v:
                count += 1
        return count
        