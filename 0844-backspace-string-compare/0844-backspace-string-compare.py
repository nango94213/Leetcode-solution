class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        ss = []
        for c in s:
            if c != '#':
                ss.append(c)
            else:
                if ss:
                    ss.pop()
        tt = []
        for c in t:
            if c != '#':
                tt.append(c)
            else:
                if tt:
                    tt.pop()
        return ss == tt