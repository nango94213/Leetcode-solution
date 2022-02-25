import collections
class Solution:
    def canCross(self, stones: List[int]) -> bool:
        if stones[1]!=1:
            return False
            
        
        stack = collections.deque([(1,1)])
        
        seen = set([(1, 1)])
        target = stones[-1]
        stones_set = set(stones)
        while stack:
            for _ in range(len(stack)):
                k, p = stack.popleft()
                if p == target:
                    return True
            
                if (p+k) in stones_set and 0<=k<=target and (k, p+k) not in seen:
                    seen.add((k, p+k))
                    stack.append((k, p+k))
                
                if (p+k+1) in stones_set and 0<=k+1<=target and (k+1, p+k+1) not in seen:
                    seen.add((k+1, p+k+1))
                    stack.append((k+1, p+k+1))
                
                if (p+k-1) in stones_set and 0<=k-1<=target and (k-1, p+k-1) not in seen:
                    seen.add((k-1, p+k-1))
                    stack.append((k-1, p+k-1))
        
        return False
        