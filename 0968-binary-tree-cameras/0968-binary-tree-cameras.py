# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        count = 0
        seen = set([])
        
        def dfs(node, p):
            
            if node:
                nonlocal count
                dfs(node.left, node)
                dfs(node.right, node)
                
                if node.left and node.left not in seen or node.right and node.right not in seen:
                    count += 1
                    seen.update([node, node.left, node.right, p])
        
        dfs(root, None)
        
        if root not in seen:
            count += 1
        
        return count
                
                
            
        