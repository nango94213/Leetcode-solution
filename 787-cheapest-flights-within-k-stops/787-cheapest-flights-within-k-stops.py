class Solution:
    
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        
        # Build the adjacency matrix
        adj_matrix = [[0 for _ in range(n)] for _ in range(n)]
        for s, d, w in flights:
            adj_matrix[s][d] = w
            
        # Shortest distances dictionary
        distances = {}
        distances[(src, 0)] = 0
        
        # BFS Queue
        bfsQ = deque([src])
        
        # Number of stops remaining
        stops = 0
        ans = float("inf")
        
        # Iterate until we exhaust K+1 levels or the queue gets empty
        while bfsQ and stops < K + 1:
            
            # Iterate on current level
            length = len(bfsQ)
            for _ in range(length):
                node = bfsQ.popleft()
                
                # Loop over neighbors of popped node
                for nei in range(n):
                    if adj_matrix[node][nei] > 0:
                        dU = distances.get((node, stops), float("inf"))
                        dV = distances.get((nei, stops + 1), float("inf"))
                        wUV = adj_matrix[node][nei]
                        
                        # No need to update the minimum cost if we have already exhausted our K stops. 
                        if stops == K and nei != dst:
                            continue
                        
                        if dU + wUV < dV:
                            distances[nei, stops + 1] = dU + wUV
                            bfsQ.append(nei)
                            
                            # Shortest distance of the destination from the source
                            if nei == dst:
                                ans = min(ans, dU + wUV)
            stops += 1   
        
        return -1 if ans == float("inf") else ans