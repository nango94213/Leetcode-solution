"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        seen = {}
        
        seen[node] = Node(node.val, [])
        
        q = collections.deque([node])
        
        while q:
            current = q.popleft()
            
            for n in current.neighbors:
                if n not in seen:
                    seen[n] = Node(n.val, [])
                    
                    
                    q.append(n)
                seen[current].neighbors.append(seen[n])
        return seen[node]
        