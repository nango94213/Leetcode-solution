# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        def dfs(sub_inorder):
            if sub_inorder:
                current_val = preorder.pop(0)
                index = sub_inorder.index(current_val)
                root = TreeNode(current_val)
            
                root.left = dfs(sub_inorder[:index])
                root.right = dfs(sub_inorder[index+1:])
            
                return root
        
        return dfs(inorder)