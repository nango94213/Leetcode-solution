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
            

            size = len(q)
            for i in range(size):
                
                current = q.popleft()

                if i < size - 1:
                    
                    current.next = q[0]
                
                if current.left:
                    q.append(current.left)
                
                if current.right:
                    q.append(current.right)
    
        return root
                