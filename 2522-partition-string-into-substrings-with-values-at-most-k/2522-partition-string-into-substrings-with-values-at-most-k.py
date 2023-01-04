class Solution:
    def minimumPartition(self, s: str, k: int) -> int:
        count = 0
        num = 0
        for c in s:
            num = num * 10 + int(c)
            
            if num <= k:
                continue
            else:
                num = int(c)
                count += 1
            
            if num > k:
                return -1
        return count + 1