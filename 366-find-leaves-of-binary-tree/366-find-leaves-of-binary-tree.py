# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        dic = collections.defaultdict(list)
        
        def dfs(node):
            
            if not node:
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)
            
            current_level = max(left, right) + 1
            
            dic[current_level].append(node.val)
            
            return current_level
        
        dfs(root)
        
        return dic.values()
        
        