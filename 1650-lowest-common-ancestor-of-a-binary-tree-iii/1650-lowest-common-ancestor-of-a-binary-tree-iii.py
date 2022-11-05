"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        
        parent_p = []
        
        while p:
            parent_p.append(p)
            p = p.parent
        
        while q not in parent_p:
            q = q.parent
        
        return q