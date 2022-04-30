class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        
        timestamp = []
        
        for t in trips:
            
            timestamp.append((t[1], t[0]))
            timestamp.append((t[2], -t[0]))
        
        timestamp.sort()
        
        total = 0
        
        for t in timestamp:
            
            total += t[1]
            
            if total > capacity:
                return False
            
        
        return True