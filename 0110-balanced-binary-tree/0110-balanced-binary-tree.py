# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        once = True
        def dfs(node, h):
            nonlocal once
            if not node:
                return h
            
            left = dfs(node.left, h+1)
            right = dfs(node.right, h+1)
            

            if abs(left-right) > 1:
                once = False
                if not once:
                    print(once)
            return max(left, right)
        
        dfs(root, 0)
   
        return once