# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        res = 0
        def dfs(node, p, path):
            nonlocal res
            if node:
                
                if node.val == p + 1:
                    path += 1
                else:
                    path = 1
                res = max(res, path)
                
                dfs(node.left, node.val, path)
                dfs(node.right, node.val, path)
        
        dfs(root, root.val, 1)
        return res
        