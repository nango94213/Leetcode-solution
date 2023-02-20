class Solution:
    def minMaxDifference(self, num: int) -> int:
        s = list(str(num))
        s1 = list(str(num))
        sub = ''
        sub1 = ''
        for i,c in enumerate(s):
            if not sub:
                if c != '9':
                    sub, s[i] = c, '9'
            if sub:
                if c == sub:
                    s[i] = '9'
                    
            if not sub1:
                sub1, s1[i] = c, '0'
            if sub1:
                if c == sub1:
                    s1[i] = '0'
        
        maxn = int(''.join(s))
        minn = int(''.join(s1))
        
        return maxn - minn
        
        
        