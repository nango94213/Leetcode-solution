class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        left = 0
        longest = 0
        dic = collections.defaultdict(int)
        total = 0
        
        for right in range(len(s)):
            
            dic[s[right]] +=  1
            
            while (right-left+1)-max(dic.values()) > k:
                
                dic[s[left]] -= 1
                
                left += 1
                
            longest = max(longest, right-left+1)
            
        
        return longest