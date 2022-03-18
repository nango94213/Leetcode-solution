import collections
class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        
        
        q = collections.deque([start])
        
        seen = set([start])
        
        while q:
            
            current = q.popleft()
            
            if arr[current] == 0:
                return True
            
            next_right = current + arr[current]
            
            next_left = current - arr[current]
            
            if next_right < len(arr) and next_right not in seen:
                seen.add(next_right)
                q.append(next_right)
            
            
            if next_left >= 0 and next_left not in seen:
                seen.add(next_left)
                q.append(next_left)
        
        return False
            
            
            
        