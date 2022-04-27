# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import heapq

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        h = []
        
        def dfs(node):
            
            if node:
          
                
                dfs(node.left)
                h.append(node.val)
                dfs(node.right)
        
        
        dfs(root)

        return h[k-1]
        
        