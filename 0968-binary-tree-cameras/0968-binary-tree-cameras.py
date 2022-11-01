# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        
  
        cover = {None}
        res = 0
        def dfs(node, par):
            nonlocal res
            if node:
                
                dfs(node.left, node)
                dfs(node.right, node)
                
                if par is None and node not in cover or node.left not in cover or node.right not in cover:
                    res += 1
                    cover.update([node, node.left, node.right, par])
        
        dfs(root, None)
        return res
                    
        