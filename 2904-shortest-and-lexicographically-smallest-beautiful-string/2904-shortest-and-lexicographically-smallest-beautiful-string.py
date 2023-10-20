class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        g = k
        res = s
        left = 0
        marker = False
        for right in range(len(s)):
            if s[right] == '1':
                k -= 1
            
            while k == 0:
                marker = True

                if len(res) > right - left + 1:
                        res = s[left:right+1]
                elif len(res) == right - left + 1:
                        res = min(res, s[left:right+1])

                if s[left] == '1':
                    k += 1
                left += 1

        return res if marker else ""
        
        