import collections
class Solution:
    def minJumps(self, arr: List[int]) -> int:
        
        dic = collections.defaultdict(list)
        
        for i, v in enumerate(arr):
            dic[v].append(i)

        q = collections.deque([0])
        
        seen = set([0])
        
        jumps = 0
        
        goal = len(arr) - 1
        
        while q:
            print(q)
            for _ in range(len(q)):
                
                current = q.popleft()
                
                if current == goal:
                    return jumps
                
                next_left = current - 1
                next_right = current + 1
                
                sames = dic[arr[current]]

                if (0 <= next_left <= goal) and (next_left not in seen):
                    seen.add(next_left)
                    q.append(next_left)
                
                if (0 <= next_right <= goal) and (next_right not in seen):
                    seen.add(next_right)
                    q.append(next_right)
                
                for same in sames:
                    if same not in seen:
                        seen.add(same)
                        q.append(same)
                del dic[arr[current]]
            
            jumps += 1
        
        
                    
        