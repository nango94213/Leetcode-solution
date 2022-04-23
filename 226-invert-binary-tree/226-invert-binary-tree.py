# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        #q = collections.deque()
        
        #q.append(root)
        
        if not root:
            return None
        
        stack = [root]
        
        while stack:
                
                
                current = stack.pop()
                
                current.left, current.right = current.right, current.left
                
            
                if current.left:
                     stack.append(current.left)
            
                if current.right:
                     stack.append(current.right)
        
        return root
        
        
        
        
        