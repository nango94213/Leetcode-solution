"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        
        if not root:
            return root
        
        prev = None
        first = None
        
        def dfs(node):
            nonlocal prev, first
            if node:
                dfs(node.left)
                
                if not prev:
                    first = node
                else:
                    prev.right = node
                    node.left = prev
                
                prev = node
                
                dfs(node.right)
        
        dfs(root)
        first.left = prev
        prev.right = first
        
        return first
        
        