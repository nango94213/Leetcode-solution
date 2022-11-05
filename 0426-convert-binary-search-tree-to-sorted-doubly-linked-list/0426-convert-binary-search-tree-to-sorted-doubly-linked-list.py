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
            return None
        first = None
        current = None
        
        def dfs(node):
            nonlocal first, current
            
            if node:
                dfs(node.left)
                
                if current:
                    current.right = node
                    node.left = current
                   
                else:
                    first = node
                
                current = node
                
                dfs(node.right)
        
        dfs(root)
        
        first.left = current
        current.right = first
        
        return first
                
                
                
                
                
        