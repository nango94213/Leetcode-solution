import collections
class Solution:
    def canCross(self, stones: List[int]) -> bool:
        if stones[1] != 1:
            return False
        q = collections.deque([(1, 1)])
        seen = set([(1, 1)])
        s = set(stones)
        while q:
        
            current, k = q.popleft()
            if current == stones[-1]:
                return True
            
            if current+k in s and (current+k, k) not in seen:
                seen.add((current+k, k))
                q.append((current+k, k))
            if current+k+1 in s and (current+k+1, k+1) not in seen:
                seen.add((current+k+1, k+1))
                q.append((current+k+1, k+1))            
            if current+k-1 in s and (current+k-1, k-1) not in seen:
                seen.add((current+k-1, k-1))
                q.append((current+k-1, k-1))
        
        return False
            