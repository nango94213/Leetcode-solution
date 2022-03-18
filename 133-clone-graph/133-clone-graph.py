"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

import collections

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node
        
        seen = {}
        
        q = collections.deque([node])
        
        seen[node] = Node(node.val, [])
        
        
        while q:
            
            current = q.popleft()
            
            for nei in current.neighbors:
                
                if nei not in seen:
                    
                    q.append(nei)
                    
                    seen[nei] = Node(nei.val, [])
                
                seen[current].neighbors.append(seen[nei])
        
        return seen[node]
        
        
        