# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        a = [0, 0]
        b = [0, 0]
        
        def dfs(node, p, d):
            nonlocal a, b
            if node:
                if node.val == x:
                    a = [p, d]
                if node.val == y:
                    b = [p, d]
            
                
                dfs(node.left, node.val, d+1)
                dfs(node.right, node.val, d+1)
        
        dfs(root, -1, 0)
        
        
        return a[0] != b[0] and a[1] == b[1]
        