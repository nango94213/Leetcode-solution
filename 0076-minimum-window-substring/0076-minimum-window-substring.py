class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count = Counter(t)
        res = ''
        k = len(t)
        left = 0
        for i in range(len(s)):
            if s[i] in count:
                count[s[i]] -= 1
                if count[s[i]] >= 0:
                    k -= 1
            
            while k == 0:
                if not res or len(res) > i - left + 1:
                    res = s[left:i+1]
                
                if s[left] in count:
                    count[s[left]] += 1
                    if count[s[left]] > 0:
                        k += 1
                left += 1
        return res
        