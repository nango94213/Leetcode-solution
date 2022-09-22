import collections
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        
        q = collections.deque([0])
        
        count = 0
        
        seen = set([0])
        
        while q:

            current = q.popleft()
            
      
            count += 1
        
       
            if count == len(rooms):
                return True
            
            for key in rooms[current]:
                
                if key not in seen:
                    seen.add(key)
                    q.append(key)
        
        return False
        