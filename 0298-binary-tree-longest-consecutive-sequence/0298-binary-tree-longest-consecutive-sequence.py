# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        res = 0
        
        def dfs(node, current, parent):
            nonlocal res
            if node:
                if node.val == parent+1:
                    current += 1
                else:
                    current = 1
                res = max(res, current)
                dfs(node.left, current, node.val)
                dfs(node.right, current, node.val)
        
        dfs(root, 0, 0)
        return res
        