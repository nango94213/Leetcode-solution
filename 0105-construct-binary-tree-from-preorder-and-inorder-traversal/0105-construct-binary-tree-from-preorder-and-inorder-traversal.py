# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        info = {}
        for i, v in enumerate(inorder):
            info[v] = i
        
        def dfs(s):
            if s and preorder:
                
                current = preorder.pop(0)
                index = info[current] - info[s[0]]
                root = TreeNode(current)
                root.left = dfs(s[:index])
                root.right = dfs(s[index+1:])
                
                return root
        
        return dfs(inorder)
        