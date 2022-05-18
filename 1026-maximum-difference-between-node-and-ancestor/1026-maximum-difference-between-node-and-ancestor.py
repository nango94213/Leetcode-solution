# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        
        res = 0
        
        def dfs(node):
            nonlocal res
            if not node:
                return ()
            
            if node and (not node.left) and (not node.right):
                return (node.val, node.val)

            left = dfs(node.left)
            right = dfs(node.right)
            
            current_min = min(left + right)
            current_max = max(left + right)
            
            
            res = max(abs(node.val-current_min), abs(node.val-current_max), res)
            
            return (min(node.val, current_min), max(node.val, current_max))
        
        dfs(root)
        
        return res
            
        