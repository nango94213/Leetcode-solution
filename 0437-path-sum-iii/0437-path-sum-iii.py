# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        dic = {0: 1}
        res = 0
        current = 0
        def dfs(node):
            nonlocal res
            nonlocal current
            if node:
                
                current += node.val
               
                if (current - targetSum) in dic:
                    res += dic[current-targetSum]
                
                dic[current] = 1 if current not in dic else dic[current] + 1
                
                dfs(node.left)
                
                
                
                dfs(node.right)
                dic[current] -= 1
                current -= node.val
        
        dfs(root)
     
        return res
                