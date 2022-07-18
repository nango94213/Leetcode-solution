class Solution:
    def frequencySort(self, s: str) -> str:
        c = Counter(s)
        s = sorted(s, key=lambda x:(c[x], x), reverse=True)
        
        return ''.join(s)
        