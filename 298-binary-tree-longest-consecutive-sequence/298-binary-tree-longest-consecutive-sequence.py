# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        max_length = 0
        
        
        def dfs(current, parent, length):
            nonlocal max_length
            if current:
                if parent and (parent.val+1)==current.val:
                    length += 1
                else:
                    length = 1
                
                max_length = max(max_length, length)
                
                dfs(current.left, current, length)
                dfs(current.right, current, length)
        
        dfs(root, None, 0)
        
        return max_length
                
        