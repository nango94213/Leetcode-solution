"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
import collections
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        
        if not root:
            return None
        
        q = collections.deque([root])
        
        while q:
            
            count = 0
            size = len(q)
            for _ in range(size):
                
                current = q.popleft()
                count += 1
                
                if q and count < size:
                    
                    current.next = q[0]
                
                if current.left:
                    q.append(current.left)
                
                if current.right:
                    q.append(current.right)
    
        return root
                